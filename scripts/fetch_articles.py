import requests
import json

dev_to_username = 'daniilroman'
medium_username = 'daniil_roman'

dev_to_url = f'https://dev.to/api/articles?username={dev_to_username}'
medium_url = f'https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@{medium_username}'

excluded_urls = [
    'https://dev.to/daniilroman/would-your-grandma-use-a-voice-chat-bot-hca',
    'https://medium.com/@daniil_roman/designing-an-application-with-redis-as-a-data-store-what-why-d02e685ee2b8'
]

def is_excluded(url):
    return any(url.startswith(excluded_url) for excluded_url in excluded_urls)

def fetch_dev_to_articles():
    response = requests.get(dev_to_url)
    articles = response.json()
    filtered_articles = [article for article in articles if not is_excluded(article['url'])]
    return filtered_articles

def fetch_medium_articles():
    response = requests.get(medium_url)
    articles = response.json()['items']
    filtered_articles = [article for article in articles if not is_excluded(article['link'])]
    return filtered_articles

def save_to_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    medium_articles = fetch_medium_articles()
    dev_to_articles = fetch_dev_to_articles()

    save_to_json('../static/prev_articles.json', medium_articles+dev_to_articles)

if __name__ == '__main__':
    main()