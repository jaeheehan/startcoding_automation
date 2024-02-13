import requests
from bs4 import BeautifulSoup

main_url = "https://www.coupang.com/np/search?q=%EA%B2%8C%EC%9D%B4%EB%B0%8D%20%EB%A7%88%EC%9A%B0%EC%8A%A4"

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
        product_price = soup.select_one('span.total-price > strong').text

        print(brand_name.strip(), product_name.strip(), product_price.strip())
