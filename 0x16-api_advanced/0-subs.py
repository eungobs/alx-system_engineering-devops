#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit."""
    user_agent = 'Mozilla/5.0'
    headers = {'User-Agent': user_agent}

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        subscribers_count = data.get('subscribers', 0)
        return subscribers_count

    return 0  # Return 0 for any issues, including invalid subreddit or server errors

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 script.py subreddit")
        sys.exit(1)

    subreddit_name = sys.argv[1]
    subscribers_count = number_of_subscribers(subreddit_name)
    
    print(subscribers_count)
