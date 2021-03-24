from bs4 import BeautifulSoup as bs


f = open('index.html', 'r')
html = f.read()
soup = bs(html, 'lxml')