from collections import Counter
import re

def predict_trend(headlines):
    # Merge all headlines into one text
    text = ' '.join(headlines)
    # Tokenize and count word frequency
    words = re.findall(r'\w+', text.lower())
    word_counts = Counter(words)
    # Return the top 5 frequent words
    return word_counts.most_common(5)

def analyze_news_trends(news_headlines):
    trends = {}
    for source, headlines in news_headlines.items():
        trends[source] = predict_trend(headlines)
    return trends
