import requests
from bs4 import BeautifulSoup

url = 'https://mangadex.org/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup)