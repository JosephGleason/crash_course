#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    """Fetch posts and print their titles"""
    fetched = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    if fetched.status_code == 200:
        print("Status Code: 200")
        
        data = fetched.json()
        for i in data:
            print(f"{i['title']}")

def fetch_and_save_posts():
    fetched = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    if fetched.status_code == 200:
        print("Status Code: 200")
        
        data = fetched.json()
        with open("posts.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            for post in data:
                writer.writerow({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                })
