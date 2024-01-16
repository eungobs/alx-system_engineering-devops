#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)

        if response.status_code == 200:
            data = response.json().get('data')
            return data.get('subscribers', 0)
        elif response.status_code == 404:
            return 0  # Subreddit not found
        else:
            return 0  # Other error

    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0
