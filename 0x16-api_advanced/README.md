
0x16. API Advanced
Project Overview
This project involves writing Python scripts to interact with the Reddit API, focusing on advanced API usage. The tasks cover a range of skills, including querying API endpoints, handling pagination, parsing JSON responses, making recursive API calls, and sorting data. The Reddit API serves as a practical platform for honing these skills.

Background Context
Questions related to APIs are common in interviews, ranging from simple endpoint queries to complex tasks involving recursion and data manipulation. The project emphasizes the importance of API usage, especially with the vast capabilities offered by platforms like Reddit. Becoming proficient in API calls can prove beneficial in technical interviews and personal projects.

Resources
Reddit API Documentation
Query String
Learning Objectives
By the end of this project, you should be able to explain without external assistance:

General
How to read API documentation to find the desired endpoints.
How to use an API with pagination.
How to parse JSON results from an API.
How to make a recursive API call.
How to sort a dictionary by value.

Requirements
General
Allowed editors: vi, vim, emacs
Interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
Files should end with a new line
The first line of all files should be exactly #!/usr/bin/python3
Libraries must be organized in alphabetical order
A README.md file, at the root of the project folder, is mandatory
Code should follow the PEP 8 style
All files must be executable
Code length will be tested using wc
Modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
The Requests module must be used for sending HTTP requests to the Reddit API
Tasks
0. How many subs?
Write a function that queries the Reddit API and returns the number of subscribers for a given subreddit. If the subreddit is invalid, the function should return 0.

python

def number_of_subscribers(subreddit)

$ python3 0-main.py programming
756024
$ python3 0-main.py this_is_a_fake_subreddit
0
1. Top Ten
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

python
Copy code
def top_ten(subreddit)

...
2. Recurse it!
Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit
None
3. Count it! (Advanced)
