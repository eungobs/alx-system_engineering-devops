#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        
        if response.status_code == 200:
            data = response.json()
            subscribers_count = data['data']['subscribers']
            return subscribers_count
        else:
            return 0

    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 script.py subreddit")
        sys.exit(1)

    subreddit_name = sys.argv[1]
    subscribers_count = number_of_subscribers(subreddit_name)
    
    print(subscribers_count)
