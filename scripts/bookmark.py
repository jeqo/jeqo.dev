#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urlparse
import re
from pathlib import Path
import sys


def sanitize_title(title):
    title = re.sub(r'[^\w\s-]', '', title.lower())
    return re.sub(r'[-\s]+', '-', title).strip('-')


def extract_metadata(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        metadata = {'url': url}

        # Extract title
        title_meta = soup.find('meta', {'property': 'og:title'})
        title_tag = soup.find('title')
        metadata['title'] = (title_meta.get('content') if title_meta else 
                           title_tag.text if title_tag else 
                           urlparse(url).path.split('/')[-1]).strip()

        # Extract author
        author_meta = (soup.find('meta', {'property': 'article:author'}) or 
                      soup.find('meta', {'name': 'author'}))
        metadata['author'] = author_meta.get('content') if author_meta else None

        # Extract date
        date_meta = (soup.find('meta', {'property': 'article:published_time'}) or 
                    soup.find('meta', {'name': 'publication_date'}))
        metadata['date'] = date_meta.get('content') if date_meta else None

        return metadata
    except Exception as e:
        print(f"Error extracting metadata: {e}")
        return {'url': url, 'title': urlparse(url).path.split('/')[-1]}


def generate_bookmark(url, base_path='./contents/links'):
    today = datetime.now()
    metadata = extract_metadata(url)

    dir_path = Path(base_path) / str(today.year) / f"{today.month:02d}"
    dir_path.mkdir(parents=True, exist_ok=True)

    file_name = f"{sanitize_title(metadata['title'])}.smd"
    file_path = dir_path / file_name

    entry = f"""---
.title = "{metadata['title']}",
.date = @date("{today.strftime('%Y-%m-%dT%H:%M:%S')}"),
.author = "jeqo",
.layout = "bookmark.shtml",
.tags = [
],
.draft = true,
---

## URL: [{metadata['url'].replace('https://', '')}]({metadata['url']})
* Author: {metadata.get('author', 'N/A')}
* Publication Date: {metadata.get('date', 'N/A')}

### Quotes

### Notes
"""

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(entry)

    return file_path


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./bookmark.py URL")
        sys.exit(1)

    url = sys.argv[1]
    file_path = generate_bookmark(url)
    print(f"Bookmark entry generated at: {file_path}")
