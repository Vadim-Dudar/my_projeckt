import requests
from bs4 import BeautifulSoup as bs
import json


class Parce():

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }

    def __init__(self ,url ,params=None ,act='o'):
        """
        :type url: str
        :type params: str
        :param act: 'o' it's a public site, 'l' it's local .html file
        :type act: str
        """
        self.url = url
        self.params = params 
        self.act = act

    def html(self, url, params=None, headers=HEADERS):
        """
        get response
        """
        r = requests.get(url, headers=headers, params=params)
        return r

    def content(self, html):
        """
        get commetns from page
        """
        soup = bs(html, 'html.parser')
        content = soup.find_all('div', class_='b-comment level-0')

        comments = []
        for comment in content:
            comments.append({
                'name': comment.find('a', class_='avatar').get_text().strip(),
                'text': comment.find('div', class_='comment_text b-typo').get_text().strip(),
                'photo': comment.find('img', class_='g-avatar').get('scr'),
                'time': comment.find('a', class_='comment-link').get_text().strip(),
            })
        return(comments)

    def json(self, content):
        """
        write all files to .json file
        """
        with open('sample.json', 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False)

    def parce(self, act='o'):
        if act == 'o':
            html = self.html(self.url)
            if html.status_code == 200:
                content = self.content(html.text)
                self.json(content)
            else:
                print('Something wrong🤷‍♂️')
        elif act == 'l':
            f = open(self.url)
            content = self.content(f)
            self.json(content)


dou = Parce('index.html')
dou.parce('l')