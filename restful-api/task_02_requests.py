#!/usr/bin/python3

import requests
import csv

# Function to fetch and print posts
def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Print the status code
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        # Parse the data into JSON
        posts = response.json()
        
        # Iterate and print titles of all posts
        for post in posts:
            print(f"Title: {post['title']}")
    else:
        print("Failed to fetch posts")

# Function to fetch and save posts to a CSV file
def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if response.status_code == 200:
        # Parse the data into JSON
        posts = response.json()
        
        # Structure data into a list of dictionaries with id, title, and body
        data_to_save = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        # Writing the data to CSV
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data_to_save)
        
        print("Posts saved to posts.csv")
    else:
        print("Failed to fetch posts")

# Call the functions
fetch_and_print_posts()
fetch_and_save_posts()
