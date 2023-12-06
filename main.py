from sentiment import SentimentAnalyzer
from clusters import TextCluster

def main():
    # Initialize the SentimentAnalyzer
    sentiment_analyzer = SentimentAnalyzer()

    # Specify the file containing data and the number of clusters
    file_name = './COMP479-Project4/scraped.json'
    num_clusters = 3

    # Create a TextCluster instance
    text_cluster = TextCluster(file_name, num_clusters, sentiment_analyzer)

    # Load data and perform clustering
    text_cluster.load_data()
    text_cluster.cluster_data()

    # Retrieve and print cluster information
    cluster_info = text_cluster.get_cluster_info()
    # Save cluster information to a text file
    with open('./COMP479-Project4/cluster_3.txt', 'w') as file:
        file.write("Cluster Information:\n")
        for cluster_id, info in cluster_info.items():
            file.write(f"Cluster {cluster_id}:\n")
            file.write(f"  Top Terms: {info['top_terms']}\n")
            file.write(f"  Average Sentiment: {info['average_sentiment']}\n\n")

    num_clusters = 6

    # Create a TextCluster instance
    text_cluster = TextCluster(file_name, num_clusters, sentiment_analyzer)

    # Load data and perform clustering
    text_cluster.load_data()
    text_cluster.cluster_data()

    # Retrieve and print cluster information
    cluster_info = text_cluster.get_cluster_info()
    # Save cluster information to a text file
    with open('./COMP479-Project4/cluster_6.txt', 'w') as file:
        file.write("Cluster Information:\n")
        for cluster_id, info in cluster_info.items():
            file.write(f"Cluster {cluster_id}:\n")
            file.write(f"  Top Terms: {info['top_terms']}\n")
            file.write(f"  Average Sentiment: {info['average_sentiment']}\n\n")


if __name__ == "__main__":
    main()



