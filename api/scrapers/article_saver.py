# api/scrapers/article_saver.py

import os
import json
from slugify import slugify

def save_article(article_data, category="general"):
    """
    Saves article data as a JSON file under data/articles/{category}/{slug}.json
    """
    title = article_data.get("title", "untitled")
    slug = slugify(title)[:60]  # Limit filename length
    category_dir = os.path.join("data", "articles", category)
    os.makedirs(category_dir, exist_ok=True)

    filepath = os.path.join(category_dir, f"{slug}.json")

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(article_data, f, indent=2, ensure_ascii=False)

    return filepath

# Example usage
if __name__ == "__main__":
    from article_fetcher import fetch_article_details

    test_url = "https://www.iol.co.za/news/politics/kenny-kunene-says-politics-has-taught-him-discipline-34b7a61a-06b4-47e0-b0fa-7f29cf1b3a79"
    article = fetch_article_details(test_url)
    path = save_article(article, category="politics")
    print(f"Article saved at: {path}")
