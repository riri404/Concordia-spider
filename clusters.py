import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
import json
import os
from sklearn.metrics.pairwise import cosine_similarity


class TextCluster:
    def __init__(self, file_name, num_clusters, sentiment_analyzer):
        self.file_name = file_name
        self.num_clusters = num_clusters
        self.sentiment_analyzer = sentiment_analyzer
        self.data = None
        self.documents = None
        self.vectorizer = TfidfVectorizer(max_df=0.5, min_df=2, stop_words='english')
        self.model = None

    def load_data(self):
        """Load JSON data and store it in the 'data' attribute"""
        with open(self.file_name, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
        self.documents = [doc['page_text'] for doc in self.data]

    def cluster_data(self):
        """Perform clustering and add cluster labels to data"""
        X = self.vectorizer.fit_transform(self.documents)
        X_normalized = normalize(X)

        # Perform clustering using KMeans
        self.model = KMeans(n_clusters=self.num_clusters, init='k-means++', max_iter=100, n_init=1, random_state=42)
        self.model.fit(X_normalized)

        # Add cluster labels to each document in the data
        for idx, label in enumerate(self.model.labels_):
            self.data[idx]['cluster'] = label  # Add the 'cluster' label to each document

    def get_cluster_info(self):
        """Generate cluster information, including top terms and average sentiment"""
        order_centroids = self.model.cluster_centers_.argsort()[:, ::-1]
        terms = self.vectorizer.get_feature_names_out()
        cluster_info = {}
        for i in range(self.num_clusters):
            top_terms = [terms[ind] for ind in order_centroids[i, :20]]  # Top 20 terms for each cluster
            cluster_info[i] = {"top_terms": top_terms, "average_sentiment": self.calculate_cluster_sentiment(i)}
        return cluster_info

    def calculate_cluster_sentiment(self, cluster_index):
        """Calculate the average sentiment score for the given cluster"""
        document_sentiments = [self.sentiment_analyzer.get_sentiment(doc) for doc in self.documents]
        cluster_documents = [i for i, label in enumerate(self.model.labels_) if label == cluster_index]

        # Calculate cosine similarity between document vectors and cluster centers
        similarity_matrix = cosine_similarity(self.vectorizer.transform(self.documents), self.model.cluster_centers_)

        weighted_sentiments = []
        for docID in cluster_documents:
            weight = similarity_matrix[docID, cluster_index]  # Similarity of the document to the cluster center
            sentiment = document_sentiments[docID]  # Sentiment score of the document
            weighted_sentiments.append(weight * sentiment)  # Weighted sentiment

        if weighted_sentiments:
            return np.mean(weighted_sentiments)  # Return the mean weighted sentiment
        return 0


# Set LOKY_MAX_CPU_COUNT to the number of CPU cores to use
os.environ["LOKY_MAX_CPU_COUNT"] = "4"
