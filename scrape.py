import requests
from bs4 import BeautifulSoup as bs

base_url = 'https://tabelog.com/udon/kagawa/rank/'

def main():
    for i in map(lambda i: i + 1, range(5)):
        res = requests.get(base_url + str(i) + '/')
        content = res.content
        soup = bs(content, 'html.parser')
        shops = soup.select('div#main-contents > ul > li > div > h3 > strong > a')
        [print('|' + shop.text + '| | | | | | | | | | [リンク](' + shop['href'] + ')|') for shop in shops]

if __name__ == '__main__':
    main()
