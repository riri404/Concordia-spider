import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
import json
import os


class TextCluster:
    def __init__(self, file_name, num_clusters, sentiment_analyzer):
        self.file_name = file_name
        self.num_clusters = num_clusters
        self.sentiment_analyzer = sentiment_analyzer
        self.data = None
        self.documents = None
        self.sentiment_scores = None
        self.vectorizer = TfidfVectorizer(max_df=0.5, min_df=2, stop_words='english')
        self.model = None

        # Load the data
    #fileName = './quotetutorial/test1.json'
    def load_data(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
        self.documents = [doc['page_text'] for doc in self.data]
        self.sentiment_scores = [self.sentiment_analyzer.get_sentiment(doc) for doc in self.documents]

    # Set LOKY_MAX_CPU_COUNT to the number of CPU cores you want to use
    os.environ["LOKY_MAX_CPU_COUNT"] = "4"  # Replace 4 with the number of cores you wish to use


    def cluster_data(self):
        X = self.vectorizer.fit_transform(self.documents)
        X_normalized = normalize(X)
        self.model = KMeans(n_clusters=self.num_clusters, init='k-means++', max_iter=100, n_init=1, random_state=42)
        self.model.fit(X_normalized)

    def get_cluster_info(self):
        order_centroids = self.model.cluster_centers_.argsort()[:, ::-1]
        terms = self.vectorizer.get_feature_names_out()
        cluster_info = {}
        for i in range(self.num_clusters):
            top_terms = [terms[ind] for ind in order_centroids[i, :10]]
            cluster_info[i] = {"top_terms": top_terms, "average_sentiment": self.calculate_cluster_sentiment(i)}
        return cluster_info

    def calculate_cluster_sentiment(self, cluster_index):
        cluster_sentiments = [self.sentiment_scores[i] for i, label in enumerate(self.model.labels_) if label == cluster_index]
        if cluster_sentiments:
            return np.mean(cluster_sentiments)
        return 0


    # Calculate average sentiment for each cluster
    # cluster_sentiments = {i: [] for i in range(true_k)}
    # for i, label in enumerate(model.labels_):
    #     cluster_sentiments[label].append(sentiment_scores[i])
    #
    # average_cluster_sentiments = {cluster: np.mean(scores) if scores else 0 for cluster, scores in
    #                               cluster_sentiments.items()}
    #
    # print(f"\n--- K-Means (k={true_k}) ---\n")
    # print(f"Number of elements assigned to each cluster (KMEANS {true_k}): {np.bincount(model.labels_)}\n")
    # print("Top terms per cluster:")
    # order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    # terms = vectorizer.get_feature_names_out()
    # for i in range(true_k):
    #     print(f"Cluster {i}: ", end='')
    #     for ind in order_centroids[i, :10]:  # top 10 words for each cluster
    #         print(f'{terms[ind]}', end=' ')
    #     print()
    #     print("Cluster Sentiments:", cluster_sentiments)
    #     print(f"Average Sentiment Score for Cluster {i}: {average_cluster_sentiments[i]}")
    #     print('\n')