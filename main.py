import pandas as pd
from sentiment import SentimentAnalyzer
from clusters import TextCluster
import visualizations

def main():
    # Initialize the SentimentAnalyzer
    print("Initializing SentimentAnalyzer...")
    sentiment_analyzer = SentimentAnalyzer()

    # Specify the file containing data and the number of clusters
    file_name = 'C:/Users/Admin/PycharmProjects/Concordia-spider-2/scraped.json'

    # First clustering with 3 clusters
    num_clusters = 10
    print("Creating TextCluster with 3 clusters...")
    text_cluster = TextCluster(file_name, num_clusters, sentiment_analyzer)

    # Load data and perform clustering
    text_cluster.load_data()
    text_cluster.cluster_data()

    # Retrieve cluster information
    cluster_info = text_cluster.get_cluster_info()
    # Save cluster information to a text file
    with open('C:/Users/Admin/PycharmProjects/Concordia-spider-2/cluster_3.txt', 'w') as file:
        file.write("Cluster Information:\n")
        for cluster_id, info in cluster_info.items():
            file.write(f"Cluster {cluster_id}:\n")
            file.write(f"  Top Terms: {info['top_terms']}\n")
            file.write(f"  Average Sentiment: {info['average_sentiment']}\n\n")

    # Second clustering with 6 clusters
    num_clusters = 20
    print("Creating TextCluster with 6 clusters...")
    text_cluster = TextCluster(file_name, num_clusters, sentiment_analyzer)

    # Load data and perform clustering
    text_cluster.load_data()
    text_cluster.cluster_data()

    # Retrieve cluster information
    cluster_info = text_cluster.get_cluster_info()
    # Save cluster information to a text file
    with open('C:/Users/Admin/PycharmProjects/Concordia-spider-2/cluster_6.txt', 'w') as file:
        file.write("Cluster Information:\n")
        for cluster_id, info in cluster_info.items():
            file.write(f"Cluster {cluster_id}:\n")
            file.write(f"  Top Terms: {info['top_terms']}\n")
            file.write(f"  Average Sentiment: {info['average_sentiment']}\n\n")

    # Convert data to pandas DataFrame
    df = pd.DataFrame(text_cluster.data)  # Make sure data is in a DataFrame format

    # Run all visualizations on the scraped data
    print("Running visualizations...")
    visualizations.run_all_visualizations(df, cluster_info)  # Pass both DataFrame and cluster_info

if __name__ == "__main__":
    main()
