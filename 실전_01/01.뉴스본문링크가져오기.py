import requests
from bs4 import BeautifulSoup
import time

response = requests.get(
    "https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
articles = soup.select("div.info_group")
for article in articles:
    links = article.select("a.info")
    if len(links) >= 2:
        url = links[1].attrs["href"]
        print(url)
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        contents = soup.select_one("#dic_area")
        print(contents.text)
        time.sleep(0.3)
