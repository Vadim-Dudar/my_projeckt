import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/uk/newauto/marka-volkswagen/'
HEADERS = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}


def get_html(url, params=None):
   r = requests.get(url, headers=HEADERS, params=params)
   return r


def get_pages_count(html):
   soup = BeautifulSoup(html, 'html.parser')
   counter = soup.find_all('span', class_='h1ForDefaultSearch')
   print(soup.find_all('span', class_='h1ForDefaultSearch'))
   print(soup.item)
   if len(counter) >= 2:
      return int(counter[-1].get_text().replace(' ', ''))
   else:
      return 1


def do():
   html = get_html(URL)
   h = html.text
   get_pages_count(html.text)
   f = open('txt.txt', 'w')
   f.write(str(h))
   f.close()


do()