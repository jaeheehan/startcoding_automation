import requests
from bs4 import BeautifulSoup
import time

response = requests.get(
    "https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC")
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
        # 만약 연예뉴스 라면
        if "entertain" in response.url:
            title = soup.select_one(".end_tit")
            content = soup.select_one("#articeBody")
        else:
            title = soup.select_one("#title_area")
            content = soup.select_one("#dic_area")

        print("=============== 링크 ===============\n", url)
        print("=============== 제목 ===============\n", title.text.strip())
        print("=============== 본문 ===============\n", content.text.strip())
        time.sleep(0.3)
