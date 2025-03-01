from crewai_tools import tool
import requests
import os

@tool
def serper_tool(query: str) -> str:
    """Search for trending topics using Google."""
    api_key = os.getenv("SERPER_API_KEY")
    url = "https://serper.dev/api/search"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(url, json={"q": query}, headers=headers)
    return response.json()["organic"][0:5]

@tool
def social_media_tool(post: str, platform: str) -> str:
    """Post content to a social media platform (Twitter, LinkedIn, Instagram)."""
    api_keys = {
        "twitter": os.getenv("TWITTER_API_KEY"),
        "linkedin": os.getenv("LINKEDIN_API_KEY"),
        "instagram": os.getenv("INSTAGRAM_API_KEY"),
    }
    url = f"https://api.{platform}.com/post"
    headers = {"Authorization": f"Bearer {api_keys[platform]}"}
    response = requests.post(url, json={"content": post}, headers=headers)
    return f"Post successful on {platform}: {response.json().get('link', 'N/A')}"
