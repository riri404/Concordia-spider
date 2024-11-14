# Concordia Spider 
## Description
The concordia_spider.py script is a web scraping tool built using [Scrapy](https://docs.scrapy.org/en/latest/index.html), designed to extract and analyze text data from web pages on the Concordia University website (concordia.ca). It collects text content, performs sentiment analysis, and clusters the pages based on their content. Additionally, the script includes two supporting modules, sentiment.py, and clusters.py, which provide sentiment analysis and text clustering functionality, respectively. The main script, main.py, demonstrates how to use these modules to analyze and cluster the scraped data.

## Sentiment Analysis Insights

Based on the sentiment analysis graphs and cluster data, here are actionable insights that can help improve user engagement and satisfaction across various content areas. These insights aim to highlight unexpected findings and reveal potential areas for improvement.


### 1. Sentiment Score Distribution per Cluster

![cluster distribution](https://github.com/riri404/Concordia-spider/blob/master/charts/Figure_1-CS.png)

#### Insight
- Most clusters have average sentiment scores between 20 and 40, with only a few exceeding 50. This suggests that the sentiment across clusters is generally moderate rather than highly positive.

#### Unexpected Finding
- Very few clusters fall below a sentiment score of 20 or above 50. This may imply limited highly engaging or inspiring content but is positive in that there are no extremely negative clusters.

#### Actionable Takeaway
- Focus on clusters with extreme sentiments (both high and low). For example:
  - **Cluster 11 (COVID protocols)** has the lowest sentiment score at 0.82, likely indicating frustration or negativity.
  - **Cluster 9 (volunteer/immigration support)** has a high sentiment of 66, suggesting it resonates well with users.

#### Recommendation
- **Low-Sentiment Clusters**: For clusters with lower sentiment (e.g., COVID-related content), consider making the language more supportive and positive.
- **High-Sentiment Clusters**: For clusters with high sentiment, investigate the aspects users find appealing and explore expanding similar content.

---

### 2. Cluster Composition

![cluster distribution](https://github.com/riri404/Concordia-spider/blob/master/charts/Figure_2-CS.png)

#### Insight
- **Cluster 3** has the highest number of pages, followed by clusters 6, 10, and 12. Larger clusters likely represent broader topics or high-priority areas on the site, while smaller clusters (e.g., clusters 5, 13, and 19) may represent niche or specialized content.

#### Unexpected Finding
- Cluster 9, with a high sentiment score, has a moderate number of pages, suggesting users respond well to this content even though it isn't a primary focus.
- Cluster 11 has a very low sentiment, but the small number of pages suggests its impact might be limited; however, it could still affect user perception.

#### Actionable Takeaway
- **Reassess Content Priorities**: Expand content in high-sentiment clusters like Cluster 9 if these topics align with user interests. For highly populated but lower-sentiment clusters, like Cluster 3, restructure content to improve clarity and engagement.

#### Recommendation
- **Consolidate Large Clusters**: Ensure that clusters with high page counts and moderate sentiment are up-to-date and engaging.
- **Expand Niche High-Sentiment Clusters**: Explore if smaller clusters with high sentiment could be expanded to serve user needs better.

---

### 3. Average Sentiment Score per Cluster

![cluster distribution](https://github.com/riri404/Concordia-spider/blob/master/charts/Figure_3-CS.png)

#### Insight
- Clusters show a broad range of sentiment scores, from very low (Cluster 11 at 0.82) to high (Cluster 9 at 66.46). Higher-sentiment clusters generally involve community and support topics (e.g., Cluster 9), while lower-sentiment scores often align with procedural or financial content (e.g., Clusters 5 and 11).

#### Unexpected Finding
- Practical or service-related topics, like financial information (Clusters 5 and 12), show low to moderate sentiment. This may indicate user frustration with these topics.

#### Actionable Takeaway
- **Enhance Support for Low-Sentiment Clusters**: Simplify language, add FAQs, or improve navigation for content related to finances or protocols to reduce user frustration.

#### Recommendation
- **User-Friendly Additions**: Consider adding step-by-step guides, interactive tools, or support chat options for complex topics. Ensure high-sentiment content is easy to find.

---

### Additional Observations Based on Specific Clusters

Here are further observations based on cluster themes and sentiment scores:

- **Cluster 1 (Graduation, Careers, Achievements)**
  - **Sentiment Score**: 51.23
  - **Insight**: This cluster has positive sentiment, suggesting users appreciate career and achievement content.
  - **Recommendation**: Showcase alumni stories, career outcomes, or student achievements more prominently.

- **Cluster 5 (Financial Services)**
  - **Sentiment Score**: 17.00
  - **Insight**: Users find financial content frustrating, as reflected by the low sentiment.
  - **Recommendation**: Simplify financial information, provide budgeting tips, and consider support options.

- **Cluster 11 (COVID-19 Protocols)**
  - **Sentiment Score**: 0.82
  - **Insight**: Extremely low sentiment likely reflects frustration with COVID-19 restrictions.
  - **Recommendation**: Reframe content to focus on well-being, and provide updates about eased restrictions or wellness support.

- **Cluster 9 (Volunteering and Immigration Support)**
  - **Sentiment Score**: 66.46
  - **Insight**: Highest sentiment score, indicating strong user engagement.
  - **Recommendation**: Add more volunteer and immigration support resources, potentially expanding partnerships for additional engagement opportunities.

- **Cluster 15 (Lifelong Learning and Support)**
  - **Sentiment Score**: 30.67
  - **Insight**: Moderate sentiment; users may find value but see room for improvement.
  - **Recommendation**: Add resources for professional development and highlight alumni success stories.

## Summary

To maximize the value of these insights:

1. **Expand High-Sentiment Areas**: Prioritize expansion in high-sentiment clusters like volunteering (Cluster 9) to further engage users.
2. **Improve Low-Sentiment Topics**: Address clusters with lower sentiment scores, such as financial information (Cluster 5) and COVID protocols (Cluster 11), to enhance clarity and support.
3. **Reevaluate Content Prioritization**: Audit large clusters with moderate sentiment for relevance and potential restructuring to improve user experience.

By addressing these areas, the company can better align content with user interests, improve engagement, and address potential friction points in the user journey.

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
```pip install scrapy beautifulsoup4 afinn langdetect nltk scikit-learn numpy```
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
