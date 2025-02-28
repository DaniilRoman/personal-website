import os
import re
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Define the directory where blog posts are stored
BLOG_DIR = "../content/blog"
OUTPUT_FILE = "../data/link_previews.json"

# Regex pattern to match the linkpreview shortcode
LINKPREVIEW_PATTERN = re.compile(r'{{<\s*linkpreview\s+text=".*?"\s+url="(.*?)"\s*>}}')

# Extract all URLs from blog posts
def extract_urls():
    urls = set()
    
    for root, _, files in os.walk(BLOG_DIR):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    matches = LINKPREVIEW_PATTERN.findall(content)
                    urls.update(matches)

    return list(urls)

def __round_desc(origin_desc: str) -> str:
    if len(origin_desc) > 150:
        return origin_desc[:150] + "..."
    return origin_desc

# Fetch Open Graph metadata from a given URL
def fetch_metadata(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        meta_description = soup.find("meta", attrs={"name": "description"})
        desc = soup.find("meta", property="og:description")["content"] if soup.find("meta", property="og:description") else (meta_description["content"] if meta_description else "")
        image = soup.find("meta", property="og:image")["content"] if soup.find("meta", property="og:image") else ""
        
        if image and not image.startswith("http"):
            parsed_url = urlparse(url)
            origin_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
            image = urljoin(origin_url, image)
        
        metadata = {
            "url": url,
            "title": soup.find("meta", property="og:title")["content"] if soup.find("meta", property="og:title") else soup.title.string if soup.title else "",
            "description": __round_desc(desc),
            "image": image,
        }
        
        return metadata
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return {"url": url, "title": "Unknown", "description": "", "image": ""}

# Save metadata to Hugo's data directory
def save_metadata(metadata):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

def main():
    urls = extract_urls()
    print(f"Found {len(urls)} URLs in blog posts.")

    metadata = {url: fetch_metadata(url) for url in urls}

    save_metadata(metadata)
    print(f"Saved metadata to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
