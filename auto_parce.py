import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/uk/newauto/marka-hyundai/'
HEADERS = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}


def get_html(url, params=None):
   r = requests.get(url, headers=HEADERS, params=params)
   return r


def get_soup(html):
   soup = BeautifulSoup(html, 'html.parser')
   content = soup.find_all('div', class_='proposition')

   cars = []
   for car in content:
      cars.append({
         'name': car.find('h3', class_='proposition_name').get_text().strip(),
         'price': car.find('span', class_='green bold size22').get_text().strip(),
         'volume': car.find('div', class_='proposition_information').get_text().strip(),
      })
   print(cars)


def parce():
   html = get_html(URL)
   if html.status_code == 200:
      get_soup(html.text)
   else:
      print('Something wrong!')
   

parce()