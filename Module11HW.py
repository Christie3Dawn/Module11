
import pandas as pd

# Assignment 1: Import an Excel file
df = pd.read_excel(r'C:\Users\Chris\Desktop\Python\COVID19_03242020_ByCounty.xlsx')
print(df)


# Assignment 2: Web Scraping
# Taken from https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
# "How to Web Scrape with Python in 4 Minutes: A Beginner's Guide for Webscraping in Python
# By: Julia Kho  Date: Sept 26, 2018

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the url to the website and access the site with the requests library
url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)

# Parse the html with BeautifulSoup. This creates a "nicer, nested BeautifulSoup data structure."
soup = BeautifulSoup(response.text, "html.parser")
# Finds all <a> tags which mark hyperlinks
soup.findAll('a')

# Modified code from original to find actual first line
for tag in soup.findAll('a'):
    if tag.has_attr('href'):
        link = tag['href']
        if link[0:4] == 'data':
            break

# Extracts the link (should be the first link)
# one_a_tag = soup.findAll('a')[38]
# link = one_a_tag['href']


# Saves the first text file to our variable link
# urllib.request library is used to download this file path to our computer
# Two parameters of request.urlretrieve: file url and the filename
download_url = 'http://web.mta.info/developers/'+ link
urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])

time.sleep(1)

# Modified original code to view in Python in usable format
with open('./turnstile_210327.txt','r') as file:
    lines = file.readlines()

import pandas as pd
df = pd.read_csv('./turnstile_210327.txt')

df.head()

# Pauses our code so we are not spamming the website with requests.
# Helps to avoid getting flagged as a spammer.
#time.sleep(1)


