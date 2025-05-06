import requests
from bs4 import BeautifulSoup

def scrape_bbc_news():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    for headline in soup.find_all('h3', class_='gs-c-promo-heading__title'):
        headlines.append(headline.text.strip())
    return headlines

def scrape_other_sources(url, headline_tag, class_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    for headline in soup.find_all(headline_tag, class_=class_name):
        headlines.append(headline.text.strip())
    return headlines

# Example of scraping multiple sources
def get_news_from_sources():
    bbc_headlines = scrape_bbc_news()
    cnn_headlines = scrape_other_sources("https://edition.cnn.com", 'h3', 'cd__headline')
    return {
        "BBC": bbc_headlines,
        "CNN": cnn_headlines
    }
