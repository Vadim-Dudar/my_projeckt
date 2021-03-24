import requests
from bs4 import BeautifulSoup as bs
import json


class Parce():

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }

    def __init__(self ,URL, params=None):
        self.url = URL
        self.params = params 

    def html(self, params=None, HEADERS=HEADERS):
        r = requests.get(self.url, headers=HEADERS, params=params)
        return r

    def content(html):
        soup = bs(html, 'html.parser')
        content = soup.find_all('div', class_='b-comment level-0')

        comments = []
        for comment in content:
            comments.append({
                'name': comment.find('a', class_='avatar').get_text().strip(),
                'text': comment.find('div', class_='comment_text b-typo').get_text().strip(),
                'photo': comment.find('img', class_='g-avatar').get('scr').strip(),
                'time': comment.find('a', class_='comment-link').get_text().strip(),
            })
        print(comments)
        return(comments)

    def do_json():
        pass

    def parce(self):
        html = html(self.url)
        if html.status_code == 200:
            content = content(html.text)
            print(content)
        else:
            print('Something wrong🤷‍♂️')


dou = Parce('https://dou.ua/forums/topic/33060/')
dou.content(dou.html().text)