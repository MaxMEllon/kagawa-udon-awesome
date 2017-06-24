import requests
import json
from bs4 import BeautifulSoup as bs

base_url = 'https://tabelog.com/udon/kagawa/rank/'

def main():
    for i in map(lambda i: i + 1, range(5)):
        res = requests.get(base_url + str(i) + '/')
        content = res.content
        soup = bs(content, 'html.parser')
        shops = soup.select('div#main-contents > ul > li > div > h3 > strong > a')
        links = list(map(lambda s: { 'link': s['href'] }, shops))
        with open('list.json', 'w', encoding='utf-8') as fp:
            json.dump({ 'all': links  }, fp)
        [print('| [' + shop.text + '](' + shop['href'] + ') | | | | | | | | |') for shop in shops]

if __name__ == '__main__':
    main()
