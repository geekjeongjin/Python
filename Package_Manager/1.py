import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.instagram.com/', params=None)
soup = BeautifulSoup(r.text, 'html.parser')
print('Title: '+soup.title.string)
articles = soup.findAll('div', {'class': 'em'})
print('Article: '+articles[0].text)

print("===========================")

r = requests.get('https://www.twitter.com/')
soup = BeautifulSoup(r.text, 'html.parser')
print('Title: '+soup.title.string)
articles = soup.findAll('div', {'class': 'strong'})
print('Article: '+articles[0].text)
