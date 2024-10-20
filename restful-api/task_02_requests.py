#!/usr/bin/python3
"""
Module with the functions to print and save data with the get method
"""


import requests
import csv


def fetch_and_print_posts():
    """
    Print the post
    """

    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """
    Save the post
    """

    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        posts_data = [{'id': post['id'], 'title': post['title'],
                      'body': post['body']} for post in posts]
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_data)
        print("Posts saved to posts.csv")
    else:
        print("Failed to fetch posts.")
