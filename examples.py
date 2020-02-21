import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body)
# print(soup.find_all('div'))
# print(soup.find_all('title'))
# print(soup.find('a'))
# print(soup.find(id="22380364"))
# print(soup.select(".storylink")[0])

#
links = soup.select(".storylink")
votes = soup.select(".score")

votes.get()