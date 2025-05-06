from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # Positive: >0, Negative: <0, Neutral: 0
    return sentiment

def analyze_news_sentiments(news_headlines):
    sentiments = {}
    for source, headlines in news_headlines.items():
        sentiments[source] = [analyze_sentiment(headline) for headline in headlines]
    return sentiments
