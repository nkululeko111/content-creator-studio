import os
import json
from api.scrapers.topic_fetcher import fetch_topics
from slugify import slugify  # pip install python-slugify

BASE_DIR = "data/articles"

def save_article(category, title):
    safe_category = slugify(category)
    category_dir = os.path.join(BASE_DIR, safe_category)
    os.makedirs(category_dir, exist_ok=True)

    filename = slugify(title) + ".json"
    filepath = os.path.join(category_dir, filename)

    article_data = {
        "title": title,
        "category": category,
        "script": None,
        "images": [],
        "video": None,
        "status": "pending"
    }

    with open(filepath, "w") as f:
        json.dump(article_data, f, indent=2)

    print(f"✅ Saved: {filepath}")

def generate_articles_for_category(category):
    topics = fetch_topics(category)
    for title in topics:
        save_article(category, title)

if __name__ == "__main__":
    categories = [
        "News and Gossip",
        "Conspiracies",
        "Life Hacks",
        "Sports",
        "Technology",
        "Kids Education (Animations k-12)",
        "Untold Stories",
        "Folktales Worldwide",
        "Music",
    ]

    for category in categories:
        generate_articles_for_category(category)
