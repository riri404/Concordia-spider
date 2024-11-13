import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
import json
import os

# Load the data
fileName = 'scraper/test1.json'
with open(fileName, 'r', encoding='utf-8') as file:
    data = json.load(file)
documents = [doc['page_text'] for doc in data]

# Set LOKY_MAX_CPU_COUNT to the number of CPU cores you want to use
os.environ["LOKY_MAX_CPU_COUNT"] = "4"  # Replace 4 with the number of cores you wish to use

# text Preprocessing
# and feature extraction using vectorizer
vectorizer = TfidfVectorizer(max_df=0.5, min_df=2, stop_words='english')
X = vectorizer.fit_transform(documents)

# Normalize the feature vectors
X_normalized = normalize(X)

# Clustering with k=3 for comparison
true_k = 3
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1, random_state=42)
model.fit(X_normalized)

print(f"\n--- K-Means (k={true_k}) ---\n")
print(f"Number of elements assigned to each cluster (KMEANS {true_k}): {np.bincount(model.labels_)}\n")
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names_out()
for i in range(true_k):
    print(f"Cluster {i}: ", end='')
    for ind in order_centroids[i, :10]:  # top 10 words for each cluster
        print(f'{terms[ind]}', end=' ')
    print('\n')

# Clustering with k=6 for comparison
true_k = 6
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1, random_state=42)
model.fit(X_normalized)

print(f"\n--- K-Means (k={true_k}) ---\n")
print(f"Number of elements assigned to each cluster (KMEANS {true_k}): {np.bincount(model.labels_)}\n")
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
for i in range(true_k):
    print(f"Cluster {i}: ", end='')
    for ind in order_centroids[i, :10]:  # top 10 words for each cluster
        print(f'{terms[ind]}', end=' ')
    print('\n')