import requests
from bs4 import BeautifulSoup
import pprint
import re

res = requests.get('http://www.traststroy.ru/services')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select(".left_menu_block a")

def get_data(href):

    print(href.replace('/', ''))
    
    res = requests.get('http://www.traststroy.ru' + href)
    html = BeautifulSoup(res.text, 'html.parser')
    print(html.title.string)
    
    # meta data
    for tags in html.find_all('meta'):
        name = tags.get('name')
        if (name == 'description' or name == 'Keywords'):
            print(tags.get('content'))

    # h1
    h1 = html.select("h1")[0]
    print(h1)

    # text
    text = html.select(".content_block")
    print(text)

    print(' ')

for idx, item in enumerate(links):
    # title = item.getText()
    href = item.get('href', None)

    get_data(href)


# links = block.find_all("a")

# print(block)


# title = soup.title.string

# print(title)