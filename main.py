from sentiment import SentimentAnalyzer
from clusters import TextCluster

# Initialize Sentiment Analyzer
sentiment_analyzer = SentimentAnalyzer()

# Initialize Text Cluster with file name, number of clusters, and sentiment analyzer
text_cluster = TextCluster(file_name='./quotetutorial/test1.json', num_clusters=6, sentiment_analyzer=sentiment_analyzer)

# Load data and perform clustering
text_cluster.load_data()
text_cluster.cluster_data()

# Get cluster information with average sentiment scores
cluster_info = text_cluster.get_cluster_info()

def print_cluster_info(cluster_info):
    for cluster_id, info in cluster_info.items():
        top_terms = ', '.join(info['top_terms'])
        average_sentiment = info['average_sentiment']
        terms_length = len(info['top_terms'])
        print(f"Cluster {cluster_id}: {top_terms}, Length: {terms_length}")
        print(f"Average Sentiment Score for Cluster {cluster_id}: {average_sentiment}\n")


print_cluster_info(cluster_info)
