import requests
import os
from serpapi import GoogleSearch

def fetch_bing_images(query, count=5):
    """Fetch images using Bing Image Search (free API)."""
    # Use Bing Image Search API (free tier)
    url = "https://api.bing.microsoft.com/v7.0/images/search"
    headers = {"Ocp-Apim-Subscription-Key": "YOUR_BING_API_KEY"}
    params = {"q": query, "count": count}
    response = requests.get(url, headers=headers, params=params)
    return [img["contentUrl"] for img in response.json().get("value", [])]

def download_images(urls, folder="images"):
    """Download images to local folder."""
    os.makedirs(folder, exist_ok=True)
    for i, url in enumerate(urls):
        try:
            response = requests.get(url)
            with open(f"{folder}/image_{i}.jpg", "wb") as f:
                f.write(response.content)
        except:
            print(f"Failed to download {url}")

if __name__ == "__main__":
    query = "Kenny Kunene latest news"
    image_urls = fetch_bing_images(query)
    download_images(image_urls)
    print(f"✅ Downloaded {len(image_urls)} images for '{query}'")


import requests
import os

# def fetch_images(query, count=5, folder="images"):
#     url = "https://api.pexels.com/v1/search"
#     headers = {"Authorization": "YOUR_PEXELS_API_KEY"}
#     params = {"query": query, "per_page": count}
#     response = requests.get(url, headers=headers, params=params)
#     urls = [photo["src"]["medium"] for photo in response.json()["photos"]]
    
#     os.makedirs(folder, exist_ok=True)
#     for i, url in enumerate(urls):
#         with open(f"{folder}/{query.replace(' ', '_')}_{i}.jpg", "wb") as f:
#             f.write(requests.get(url).content)

# if __name__ == "__main__":
#     fetch_images("Beyoncé politician Cape Town")

# Note:

# Get free API key at Pexels.

# Fallback: Use serpapi or Bing Images if Pexels lacks images.






# import requests
# import os

# UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")
# SEARCH_TERM = "Kenny Kunene politician"  # dynamically replace with your topic

# def get_unsplash_images(query, count=5):
#     url = "https://api.unsplash.com/search/photos"
#     headers = {
#         "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
#     }
#     params = {
#         "query": query,
#         "per_page": count,
#         "orientation": "landscape"
#     }
#     response = requests.get(url, headers=headers, params=params)
#     data = response.json()
#     image_urls = [result['urls']['regular'] for result in data['results']]
#     return image_urls

# if __name__ == "__main__":
#     images = get_unsplash_images(SEARCH_TERM, count=5)
#     for idx, url in enumerate(images):
#         print(f"Image {idx+1}: {url}")
#         # Optional: download images
#         img_data = requests.get(url).content
#         with open(f"images/image_{idx+1}.jpg", "wb") as f:
#             f.write(img_data)