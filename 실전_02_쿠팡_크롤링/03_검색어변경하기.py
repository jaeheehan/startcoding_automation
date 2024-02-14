import requests
from bs4 import BeautifulSoup
import pyautogui
import openpyxl

keyword = pyautogui.prompt("검색어를 입력하세요 >>>")

wb = openpyxl.Workbook('coupang_result.xlsx')
ws = wb.create_sheet(keyword)
ws.append(['순위', '브랜드명', '상품명', '가격', '상품페이지링크'])

rank=1;
done = False
for page in range(1, 5):
    if done == True:
        break
    print(page, "번째 페이지 입니다.")
    main_url = f"https://www.coupang.com/np/search?q={keyword}&page={page}"

    response = requests.get(main_url, headers={'User-Agent': 'Mozilla/5.0',"Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"})
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    links = soup.select("a.search-product-link")
    for link in links:
        # 광고상품 제거
        if len(link.select("span.ad-badge-text")) > 0:
            print('광고 상품입니다.')
        else:
            sub_url = "https://www.coupang.com/" + link.attrs['href']
            response = requests.get(sub_url,  headers={'User-Agent': 'Mozilla/5.0',"Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"})
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            # 브랜드명
            try:
                brand_name = soup.select_one('a.prod-brand-name').text
            except:
                brand_name = ""

            # 상품명
            product_name = soup.select_one('h2.prod-buy-header__title').text

            # 가격
            try:
                product_price = soup.select_one('span.total-price > strong').text
            except:
                product_price = "0"

            print(rank, brand_name.strip(), product_name.strip(), product_price.strip())
            ws.append([rank, brand_name.strip(), product_name.strip(), product_price.strip(), sub_url])
            rank = rank + 1
            if rank > 100:
                done = True
                break

wb.save('coupang_result.xlsx')