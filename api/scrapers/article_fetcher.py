# api/scrapers/article_fetcher.py

import newspaper

def fetch_article_details(url):
    """
    Fetch article title, summary and full text from a URL using newspaper3k
    """
    article = newspaper.Article(url)
    article.download()
    article.parse()
    
    # Try extracting a summary
    article.nlp()
    
    return {
        "title": article.title,
        "summary": article.summary,
        "text": article.text,
        "top_image": article.top_image
    }

# Example usage
if __name__ == "__main__":
    url = "https://www.iol.co.za/news/politics/kenny-kunene-says-politics-has-taught-him-discipline-34b7a61a-06b4-47e0-b0fa-7f29cf1b3a79"
    details = fetch_article_details(url)
    for key, value in details.items():
        print(f"{key.upper()}:\n{value}\n")
