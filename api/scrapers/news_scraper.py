import feedparser
import praw
from newspaper import Article

# Reddit API setup (free)
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="script:content-studio:v1.0"
)

def scrape_google_news(query="celebrity OR politician", max_results=5):
    """Fetch trending news from Google News RSS."""
    url = f"https://news.google.com/rss/search?q={query}&hl=en-ZA&gl=ZA&ceid=ZA:en"
    feed = feedparser.parse(url)
    return [{"title": entry.title, "url": entry.link} for entry in feed.entries[:max_results]]

def scrape_reddit_posts(subreddit="entertainment", limit=5):
    """Scrape Reddit for trending gossip."""
    posts = []
    for post in reddit.subreddit(subreddit).hot(limit=limit):
        posts.append({"title": post.title, "url": f"https://reddit.com{post.permalink}"})
    return posts

def scrape_tiktok_trends(hashtag="celebritynews"):
    """Placeholder for TikTok scraping (manual for now)."""
    # TODO: Use TikTok API or selenium if needed
    return [{"title": "Trending TikTok gossip (manual)", "url": ""}]

if __name__ == "__main__":
    news = scrape_google_news()
    reddit_posts = scrape_reddit_posts()
    tiktok_trends = scrape_tiktok_trends()
    
    all_topics = news + reddit_posts + tiktok_trends
    print(f"📰 Trending News & Gossip ({len(all_topics)} topics):")
    for i, topic in enumerate(all_topics, 1):
        print(f"{i}. {topic['title']} ({topic['url']})")