# topic_fetcher.py

import feedparser

CATEGORY_FEEDS = {
    "News and Gossip": "https://news.google.com/rss/search?q=celebrity+OR+politician+OR+trending&hl=en-ZA&gl=ZA&ceid=ZA:en",
    "Conspiracies": "https://www.reddit.com/r/conspiracy/.rss",
    "Life Hacks": "https://www.reddit.com/r/LifeProTips/.rss",
    "Sports": "https://news.google.com/rss/search?q=sports&hl=en-ZA&gl=ZA&ceid=ZA:en",
    "Technology": "https://news.google.com/rss/search?q=technology&hl=en-ZA&gl=ZA&ceid=ZA:en",
    "Kids Education (Animations k-12)": "https://www.reddit.com/r/AskScience/.rss",
    "Untold Stories": "https://www.reddit.com/r/nosleep/.rss",
    "Folktales Worldwide": "https://www.reddit.com/r/folktales/.rss",
    "Music": "https://news.google.com/rss/search?q=music&hl=en-ZA&gl=ZA&ceid=ZA:en",
}

def fetch_topics(category):
    feed_url = CATEGORY_FEEDS.get(category)
    if not feed_url:
        return []

    feed = feedparser.parse(feed_url)
    topics = [entry.title for entry in feed.entries[:3]]
    return topics

# Example usage
if __name__ == "__main__":
    category = "News and Gossip"
    topics = fetch_topics(category)
    print(f"Top trending topics for {category}:\n")
    for i, topic in enumerate(topics, 1):
        print(f"{i}. {topic}")




# # api/scrapers/topic_fetcher.py

# import feedparser
# import random

# # Define sources for each playlist
# CATEGORY_FEEDS = {
#     "News & Gossip": [
#         "https://news.google.com/rss/search?q=celebrity+OR+politician+OR+trending&hl=en",
#         "https://www.reddit.com/r/popular/.rss",
#         "https://www.tiktok.com/tag/trending"  # Tiktok API is limited; maybe scrape or skip
#     ],
#     "Conspiracies": [
#         "https://www.reddit.com/r/conspiracy/.rss",
#         "https://www.bbc.com/news/topics/cjgn7gy0g0vt/conspiracy-theories"
#     ],
#     "Life Hacks": [
#         "https://www.reddit.com/r/LifeProTips/.rss",
#         "https://www.wikiwand.com/en/List_of_life_hacks"
#     ],
#     "Sports": [
#         "https://news.google.com/rss/search?q=sports&hl=en",
#         "https://www.reddit.com/r/sports/.rss"
#     ],
#     "Technology": [
#         "https://news.google.com/rss/search?q=technology&hl=en",
#         "https://www.reddit.com/r/technology/.rss"
#     ],
#     "Kids Education": [
#         "https://www.reddit.com/r/AskScience/.rss",
#         "https://en.wikipedia.org/wiki/Special:Random"
#     ],
#     "Untold Stories": [
#         "https://www.reddit.com/r/nosleep/.rss",
#         "https://www.bbc.com/news/angles/untold-stories"
#     ],
#     "Folktales": [
#         # Could be manual or curated sources
#         "https://www.africanfolktales.com/feed"  # hypothetical
#     ],
#     "Music": [
#         "https://www.billboard.com/feed/",
#         "https://www.reddit.com/r/listentothis/.rss"
#     ]
# }

# def get_random_source(feed_list):
#     return random.choice(feed_list)

# def fetch_topics(category):
#     sources = CATEGORY_FEEDS.get(category)
#     if not sources:
#         return []

#     source_url = get_random_source(sources)
#     # For Reddit RSS
#     if "reddit" in source_url:
#         feed = feedparser.parse(source_url)
#         return [entry.title for entry in feed.entries[:3]]
#     # For Google News RSS
#     elif "google" in source_url:
#         feed = feedparser.parse(source_url)
#         return [entry.title for entry in feed.entries[:3]]
#     # For other sources, you can add parsing logic
#     # Or for Wikipedia, fetch a random article
#     elif "wikipedia" in source_url:
#         # implement API call or return a static or random topic
#         return ["Random Wikipedia article"]
#     # Add other parsers as needed
#     else:
#         return []

# # For TikTok or social media, scraping might be needed, but for now, skip due to complexity.

# # Usage example
# if __name__ == "__main__":
#     for cat in CATEGORY_FEEDS:
#         print(f"\nCategory: {cat}")
#         print(fetch_topics(cat))