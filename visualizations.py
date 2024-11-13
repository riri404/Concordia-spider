import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


def load_data(json_file):
    """Load JSON data from a specified file and convert it to a DataFrame."""
    with open(json_file, encoding='utf-8') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    print("Loaded DataFrame columns:", df.columns)  # Print column names for debugging
    return df


def plot_sentiment_distribution(cluster_info):
    """Plot a histogram of average sentiment across clusters."""
    # Extract average sentiment from cluster info
    avg_sentiment = [info['average_sentiment'] for info in cluster_info.values()]

    plt.figure(figsize=(10, 6))
    sns.histplot(avg_sentiment, kde=True, color='skyblue')  # Now using average sentiment
    plt.title('Sentiment Score Distribution per Cluster')
    plt.xlabel('Average Sentiment')
    plt.ylabel('Frequency')
    plt.show()


def plot_cluster_composition(df):
    """Plot the composition of clusters (number of pages per cluster)."""
    if 'cluster' not in df.columns:
        raise ValueError("'cluster' column is missing from the DataFrame.")

    cluster_counts = df['cluster'].value_counts()

    plt.figure(figsize=(10, 6))
    cluster_counts.plot(kind='bar', color='salmon')
    plt.title('Cluster Composition')
    plt.xlabel('Cluster')
    plt.ylabel('Number of Pages')
    plt.xticks(rotation=0)
    plt.show()


def plot_average_sentiment_per_cluster(cluster_info):
    """Plot the average sentiment score for each cluster."""
    # Extract cluster IDs and their average sentiment values
    cluster_ids = list(cluster_info.keys())
    avg_sentiment = [info['average_sentiment'] for info in cluster_info.values()]

    plt.figure(figsize=(10, 6))
    plt.bar(cluster_ids, avg_sentiment, color='lightgreen')
    plt.title('Average Sentiment Score per Cluster')
    plt.xlabel('Cluster')
    plt.ylabel('Average Sentiment Score')
    plt.xticks(rotation=0)
    plt.show()


def generate_wordclouds_per_cluster(df):
    """Generate and display a word cloud for each cluster."""
    for cluster_num in df['cluster'].unique():
        cluster_text = ' '.join(df[df['cluster'] == cluster_num]['text'])

        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(cluster_text)

        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Word Cloud for Cluster {cluster_num}')
        plt.show()


def run_all_visualizations(df, cluster_info):
    """Run all visualizations on the given DataFrame and cluster information."""
    # Plot sentiment distribution
    plot_sentiment_distribution(cluster_info)

    # Plot cluster composition
    plot_cluster_composition(df)

    # Plot average sentiment per cluster
    plot_average_sentiment_per_cluster(cluster_info)

    # Generate word clouds for each cluster
    generate_wordclouds_per_cluster(df)
