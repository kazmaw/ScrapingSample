import requests
from bs4 import BeautifulSoup

url = "target url";
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')
p = soup.find_all(id="first")
print(soup)