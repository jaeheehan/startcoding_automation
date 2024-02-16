import requests
from bs4 import BeautifulSoup
import pyautogui

lastpage = pyautogui.prompt("몇 페이지까지 크롤링할까요? (1페이지 = 50개)")

finalPage = int(lastpage)
for i in range(1, finalPage + 1):
    # HTTP 302 방식
    url = f"https://finance.naver.com/sise/field_submit.naver?menu=market_sum&returnUrl=http://finance.naver.com/sise/sise_market_sum.naver?&page={i}&fieldIds=market_sum&fieldIds=per&fieldIds=roe&fieldIds=listed_stock_cnt&fieldIds=pbr&fieldIds=reserve_ratio"

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    trs = soup.select("table.type_2 > tbody > tr[onmouseover=\"mouseOver(this)\"]")

    for tr in trs:
        # nth-child 사용하는 방법
        name = tr.select_one('td:nth-child(2)').text
        per = tr.select_one('td:nth-child(7)').text
        roe = tr.select_one('td:nth-child(8)').text
        pbr = tr.select_one('td:nth-child(9)').text
        reserve_ratio = tr.select_one('td:nth-child(10)').text

        # 데이터 전처리
        # 'N/A' 값이 아닐 경우 에만
        if per != 'N/A' and roe != 'N/A' and pbr != 'N/A' and reserve_ratio != 'N/A':
            per = float(per.replace(',', ''))
            roe = float(roe.replace(',', ''))
            pbr = float(pbr.replace(',', ''))
            reserve_ratio = float(reserve_ratio.replace(',', ''))
            print(name, per, roe, pbr, reserve_ratio)
