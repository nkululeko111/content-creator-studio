import feedparser
import praw
from newspaper import Article

# Reddit API (free)
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="content-studio"
)

def fetch_trends():
    trends = {
        "News & Gossip": fetch_google_news("celebrity OR politician"),
        "Conspiracies": fetch_reddit("conspiracy"),
        "Life Hacks": fetch_reddit("LifeProTips"),
        "Sports": fetch_google_news("sports"),
        "Tech": fetch_google_news("technology"),
        "Kids Education": fetch_k12_topics(),
        "Untold Stories": fetch_reddit("nosleep"),
        "Folktales": fetch_folktales(),
        "Music": fetch_google_news("music")
    }
    return trends

def fetch_google_news(query):
    url = f"https://news.google.com/rss/search?q={query}"
    feed = feedparser.parse(url)
    return [entry.title for entry in feed.entries[:1]][0]  # Top 1 trend

def fetch_reddit(subreddit):
    posts = list(reddit.subreddit(subreddit).hot(limit=1))
    return posts[0].title if posts else "No trending topic found"

def fetch_k12_topics():
    topics = ["Why is the sky blue?", "How do plants grow?", "What is gravity?"]
    return random.choice(topics)

def fetch_folktales():
    tales = ["The Lion and the Hare", "Anansi the Spider"]
    return random.choice(tales)

if __name__ == "__main__":
    trends = fetch_trends()
    for playlist, topic in trends.items():
        print(f"🎬 {playlist}: {topic}")