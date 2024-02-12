import requests
from bs4 import BeautifulSoup
import time
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요")
response = requests.get(
    f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={keyword}")
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
        elif "sports" in response.url:
            title = soup.select_one("h4.title")
            content = soup.select_one("#newsEndContents")
            # 본문 내용안에 불필요한 div 삭제
            divs = content.select("div")
            for div in divs:
                div.decompose()
            paragraphs = content.select("p")
            for p in paragraphs:
                p.decompose()
        else:
            title = soup.select_one("#title_area")
            content = soup.select_one("#dic_area")

        print("=============== 링크 ===============\n", url)
        print("=============== 제목 ===============\n", title.text.strip())
        print("=============== 본문 ===============\n", content.text.strip())
        time.sleep(0.3)
