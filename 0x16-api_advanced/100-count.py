#!/usr/bin/python3
"""queries the Reddit API, parses the title of all hot articles, and prints a
sorted count of given keywords(case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""
import requests
import requests

def count_words(subreddit, word_list, after=None, results=None):
    """Recursively count the occurrences of keywords in hot articles of a subreddit."""
    if results is None:
        results = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title'].lower()

                # Count occurrences of keywords in the title
                for word in word_list:
                    if word.lower() in title:
                        results[word] = results.get(word, 0) + 1

            # Recursively call the function with the next set of results
            after = data['data']['after']
            if after:
                count_words(subreddit, word_list, after, results)

    except requests.RequestException as e:
        print(f"Error: {e}")

    # Print the results in descending order by count, then alphabetically
    sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
    for keyword, count in sorted_results:
        print(f"{keyword}: {count}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 script.py subreddit [keyword1 keyword2 ...]")
        sys.exit(1)

    subreddit_name = sys.argv[1]
    keywords = sys.argv[2:]

    count_words(subreddit_name, keywords)
