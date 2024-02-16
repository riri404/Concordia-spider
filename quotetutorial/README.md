# COMP479-Project4
Experiment with web crawling, scrape and index a set of web documents. Cluster the documents using k-means. Use the AFINN sentiment analysis script to assign a sentiment score to each cluster.

## To Run:
1. make sure you have the following libraries downloaded: BeautifulSoup, Sci-kit, and Scrapy (mainly)
2. In order to start the spider go to the terminal and run ```scrapy crawl concordia -a max
_files=10 -o test1.json``` this will also save your output in a json file
3. In order to start clustering, we follow what is done in the link below [1], then we can determine from the code the value for k
4. Hit Run and in the output window you will see the different clusters and the top 10 terms in every cluster








[1] https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#sphx-glr-auto-examples-text-plot-documentclustering-py
