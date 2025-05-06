# app/trend_analysis.py

from collections import Counter
from datetime import datetime

def analyze_trends(articles):
    # Example: Count the frequency of words in titles
    words = []
    for article in articles:
        words.extend(article['title'].split())
    return Counter(words).most_common(10)  # Top 10 words
