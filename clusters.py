from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
import json
import os

# Load the data
fileName = './quotetutorial/test1.json'
with open(fileName, 'r', encoding='utf-8') as file:
    data = json.load(file)
documents = [doc['page_text'] for doc in data]

# Set LOKY_MAX_CPU_COUNT to the number of CPU cores you want to use
os.environ["LOKY_MAX_CPU_COUNT"] = "4"  # Replace 4 with the number of cores you wish to use

# text Preprocessing
# and feature extraction using vectorizer
vectorizer = TfidfVectorizer(max_df=0.5, min_df=2, stop_words='english')
X = vectorizer.fit_transform(documents)

# normalize the feature vectors
X_normalized = normalize(X)

# Clustering
true_k = 3  # Adjust this based on the pdf to compare k=3 and k=6
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X_normalized)

# Print the top terms per cluster
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names_out()
for i in range(true_k):
    print(f"Cluster {i}:")
    for ind in order_centroids[i, :10]: # adjust the number of terms
        print(f' {terms[ind]}')
    print()
