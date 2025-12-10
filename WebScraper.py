import sys
sys.stdout.reconfigure(encoding='utf-8')

from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get('https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States#Presidents', headers=headers).text
soup = BeautifulSoup(response, 'lxml')
# for line in soup.find_all('tbody')[2]:
#      table_heads = line.th.get_text(strip=True)
#      print(table_heads)

for items in soup.find_all("th", class_="navbox-group"):
    texts = items.get_text(strip=True)
    print(texts)