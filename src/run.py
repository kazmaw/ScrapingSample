import requests
from bs4 import BeautifulSoup

url = "https://ja.wikipedia.org/wiki/%E3%82%A6%E3%82%A7%E3%83%96%E3%82%B9%E3%82%AF%E3%83%AC%E3%82%A4%E3%83%94%E3%83%B3%E3%82%B0";
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')
p = soup.find_all(id="first")
print(soup)