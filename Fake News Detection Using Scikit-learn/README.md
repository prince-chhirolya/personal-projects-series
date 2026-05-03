# Diabetes Prediction Using Keras

<p>In this project, I use two different data sources of news and combine them as a dataset. After that, we will use the scikit-learn library to create a classifier that will be used to determine if a piece of news is fake.</p>

## Technologies Used
<p style='font-weight: bold'>
Python | Scikit-learn | Kaggle News Dataset | NLP 
</p>

## Key Learnings
* Create a data frame using data pulled from the News API. 
* Select the features from the textual data.
* Create a classifier to classify the textual data.

## Project Description

Social media has made fake news spread faster than ever, creating an urgent need for automated fake news detection systems. Machine learning classification can identify patterns in text that distinguish deliberately false information from legitimate journalism, making it essential for content moderation platforms and fact-checking services. This project demonstrates how natural language processing and text classification tackle real-world misinformation challenges.

In this project, I build a fake news classifier using Python and scikit-learn that analyzes news articles and predicts their authenticity. I work with two datasets: a Kaggle news dataset containing labeled real and fake articles, and a custom dataset I create by fetching live news from the News API. After combining these datasets, I implement feature extraction using TfidfVectorizer to convert text into numerical representations. I apply a passive-aggressive classifier, an online machine learning algorithm that aggressively updates when predictions are wrong but remains passive when correct, making it ideal for text classification tasks.

I split the data into training and testing sets, train the classifier on labeled examples, and evaluate performance using accuracy metrics and confusion matrices. By the end, you'll have a working fake news detection system demonstrating scikit-learn classification, text feature engineering, TF-IDF vectorization, model evaluation, and API data collection applicable to any NLP classification problem like spam detection or sentiment analysis.