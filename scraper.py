import requests
import re
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def extract_country(text):
    countries = ["USA", "US", "United States", "UK", "United Kingdom", "Canada", "Australia", 
                 "Germany", "Netherlands", "Turkey", "China", "Japan", "Italy", "France", 
                 "Sweden", "Switzerland", "Norway", "UAE", "Saudi Arabia", "Pakistan", "India"]
    text = text.upper()
    for c in countries:
        if c.upper() in text:
            if c in ["US", "USA", "UNITED STATES"]:
                return "USA"
            if c in ["UK", "UNITED KINGDOM"]:
                return "UK"
            return c
    return "Other"

def extract_degree(text):
    text = text.lower()
    if "phd" in text or "doctorate" in text or "doctoral" in text:
        return "PhD"
    if "master" in text or "msc" in text or "ma " in text or "mba" in text:
        return "Master"
    if "bachelor" in text or "bs " in text or "undergraduate" in text or "bachelor's" in text:
        return "Bachelor"
    return "Other"

def scrape_brightscholarship():
    scholarships = []
    try:
        url = "https://brightscholarship.com"
        response = requests.get(url, headers=HEADERS, timeout=20)
        soup = BeautifulSoup(response.text, "html.parser")

        # Fix: article -> div.post
        posts = soup.find_all("div", class_=lambda x: x and any(s in x for s in ['post', 'entry', 'card']))

        for post in posts:
            title_tag = post.find(["h2", "h3", "a"])
            if not title_tag:
                continue

            link_tag = title_tag.find("a") if title_tag.name != "a" else title_tag
            if not link_tag:
                continue

            title = link_tag.get_text(strip=True)
            source_url = link_tag.get("https://opportunitiescorners.com/](https://opportunitiescorners.com", "")

            if len(title) < 10:
                continue

            scholarships.append({
                "title": title,
                "country": extract_country(title),
                "degree_level": extract_degree(title),
                "deadline": "",
                "funding_type": "",
                "source_url": source_url
            })

    except Exception as e:
        print("Bright Scholarship Error:", e)

    return scholarships

def scrape_opportunitiescorners():
    scholarships = []
    try:
        # Fix: Sahi URL daala
        url = "https://opportunitiescorners.com"
        response = requests.get(url, headers=HEADERS, timeout=20)
        soup = BeautifulSoup(response.text, "html.parser")

        # Fix: article -> div.post
        posts = soup.find_all("div", class_=lambda x: x and 'post' in x)

        for post in posts:
            title_tag = post.find(["h2", "h3", "a"])
            if not title_tag:
                continue

            link_tag = title_tag.find("a") if title_tag.name != "a" else title_tag
            if not link_tag:
                continue

            title = link_tag.get_text(strip=True)
            source_url = link_tag.get("href", "")

            if len(title) < 10:
                continue

            scholarships.append({
                "title": title,
                "country": extract_country(title),
                "degree_level": extract_degree(title),
                "deadline": "Unknown",
                "funding_type": "Unknown",
                "source_url": source_url
            })

    except Exception as e:
        print("Opportunities Corners Error:", e)

    return scholarships

def scrape_all():
    all_data = []
    all_data.extend(scrape_brightscholarship())
    all_data.extend(scrape_opportunitiescorners())
    return all_data