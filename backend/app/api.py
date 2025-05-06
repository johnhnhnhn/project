from flask import Blueprint, jsonify
from .services.scraper import scrape_bbc
from .services.sentiment import analyze_sentiment
from .trend_analysis import analyze_trends

# Create the API blueprint
api_bp = Blueprint('api', __name__)

@api_bp.route('/articles', methods=['GET'])
def get_articles():
    articles = scrape_bbc()  # Scrape articles using the scraper function
    sentiments = [analyze_sentiment(article['title']) for article in articles]
    trends = analyze_trends(articles)
    
    # Combine the articles, sentiments, and trends into one response
    response = {
        'articles': articles,
        'sentiments': sentiments,
        'trends': trends
    }
    
    return jsonify(response)  # Return the data as JSON
