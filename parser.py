import requests
from bs4 import BeautifulSoup

URL = 'https://dou.ua/forums/topic/33000/'
HEADERS = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}


def get_html(url, params=None):
   r = requests.get(url, headers=HEADERS, params=params)
   return r


def get_soup(html):
   soup = BeautifulSoup(html, 'html.parser')
   content = soup.find_all('div', class_='b-comment level-0')

   comments = []
   for comment in content:
      comments.append({
         'name': comment.find('a', class_='avatar').get_text().replace('\n' and '\t', '').replace('\n' and '\t', ''),
         'pic': comment.find('img', class_='g-avatar').get('scr'),
         'text': comment.find('div', class_='comment_text b-typo').get_text().replace('\xa0' and '\n', ' '),
      })
   print(comments)


def parce():
   html = get_html(URL)
   if html.status_code == 200:
      get_soup(html.text)
   else:
      print('Something wrong!')
   

parce()