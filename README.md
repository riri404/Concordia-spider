# Concordia Spider 
## Description
The concordia_spider.py script is a web scraping tool built using [Scrapy](https://docs.scrapy.org/en/latest/index.html), designed to extract and analyze text data from web pages on the Concordia University website (concordia.ca). It collects text content, performs sentiment analysis, and clusters the pages based on their content. Additionally, the script includes two supporting modules, sentiment.py, and clusters.py, which provide sentiment analysis and text clustering functionality, respectively. The main script, main.py, demonstrates how to use these modules to analyze and cluster the scraped data.

## Prerequisites
Before running the code, make sure you have the following Python libraries installed:

[Scrapy](https://docs.scrapy.org/en/latest/index.html) (version 2.11.0)

[BeautifulSoup](https://pypi.org/project/beautifulsoup4/) (version 4.12.2)

[Afinn](https://pypi.org/project/afinn/) (version 0.1)

[NLTK](https://pypi.org/project/nltk/) (version 3.8.1)

[Langdetect](https://pypi.org/project/langdetect/) (version 1.0.9)

[Scikit-learn](https://scikit-learn.org/stable/modules/clustering.html) (version 1.3.2)

[Numpy](https://numpy.org/doc/stable/) (1.26)

You can install these libraries using pip if you haven't already:

Copy code
```pip install scrapy beautifulsoup4 afinn-langdetect nltk scikit-learn numpy```
## Usage
### Scraping Data

The main script, concordia_spider.py, is responsible for scraping data from the Concordia University website.
You can adjust the maximum number of files to be downloaded by modifying the max_files parameter in the ConcordiaSpider class constructor.

### Sentiment Analysis

The sentiment.py module contains the SentimentAnalyzer class, which performs sentiment analysis on text data.
It uses the AFINN lexicon for sentiment scoring and can also cluster documents based on sentiment.

### Text Clustering

The clusters.py module includes the TextCluster class, which clusters text documents using K-Means clustering.
It also calculates the average sentiment for each cluster using the sentiment analyzer. I am currently trying to create a meaningful GUI.

### Running the Main Script

main.py demonstrates how to use the SentimentAnalyzer and TextCluster classes to analyze and cluster data from the Concordia University website.
It loads data from a JSON file (in this case, scraped.json), performs clustering with different cluster counts, and saves cluster information to text files (cluster_3.txt and cluster_6.txt).
To run the main script, execute the following command:


## Folder Structure

concordia_spider.py: The main web scraping script.

sentiment.py: Module for sentiment analysis and clustering of documents.

clusters.py: Module for text clustering using K-Means.

main.py: The main script demonstrating the usage of the other modules.

COMP479-Project4: A directory for saving scraped data and cluster information.

## Important Notes

The code in the concordia_spider.py script is designed to work specifically with the Concordia University website. Make sure to adapt it for different websites if needed.
Data is scraped to a JSON file (scraped.json) in the COMP479-Project4 directory. You may need to create this directory manually.
The code may require adjustments or additional error handling for different websites or data sources.
