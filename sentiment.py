from afinn import Afinn
import re
import nltk
from nltk.corpus.reader import documents
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SentimentAnalyzer:
    def __init__(self):
        self.afinn = Afinn()
        self.km = None
        self.tfidf_matrix = None

    @staticmethod
    def clean_text(text):
        text = re.sub(r'\s+', ' ', text)
        return text

    @staticmethod
    def tokenize_text(text):
        return nltk.word_tokenize(text)

    def get_sentiment(self, text):
        cleaned_text = self.clean_text(text)
        return self.afinn.score(cleaned_text)

    def process_documents(self, documents, n_clusters=3):
        vectorizer = TfidfVectorizer()
        self.tfidf_matrix = vectorizer.fit_transform(documents)
        self.km = KMeans(n_clusters=n_clusters)
        self.km.fit(self.tfidf_matrix)

    def derive_cluster_sentiments(self):
        document_sentiments = [self.get_sentiment(doc) for doc in documents]
        cluster_docs_sentiments = self.map_docs_to_clusters(document_sentiments)

        similarity_matrix = cosine_similarity(self.tfidf_matrix, self.km.cluster_centers_)
        cluster_sentiments = self.calculate_weighted_sentiments(similarity_matrix, cluster_docs_sentiments)

        return cluster_sentiments

    def map_docs_to_clusters(self, document_sentiments):
        clusters = self.km.labels_
        cluster_mapping = {}
        for i, cluster_label in enumerate(clusters):
            if cluster_label not in cluster_mapping:
                cluster_mapping[cluster_label] = []
            cluster_mapping[cluster_label].append((i, document_sentiments[i]))
        return cluster_mapping

    def calculate_weighted_sentiments(self, similarity_matrix, cluster_docs_sentiments):
        weighted_cluster_sentiments = {}
        for cluster, doc_sentiments in cluster_docs_sentiments.items():
            weighted_sentiments = weighted_cluster_sentiments.get(cluster, [])
            for docID, sentiment in doc_sentiments:
                weight = similarity_matrix[docID, cluster]
                weighted_sentiments.append((weight, sentiment))
            weighted_cluster_sentiments[cluster] = weighted_sentiments

        cluster_sentiments = {}
        for cluster, weighted_sentiments in weighted_cluster_sentiments.items():
            cluster_sentiments[cluster] = sum(weight * sentiment for weight, sentiment in weighted_sentiments)

        return cluster_sentiments
