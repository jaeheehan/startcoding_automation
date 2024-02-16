from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
browser.implicitly_wait(5) # 웹페이지가 로딩 될때까지 5초는 기다림
browser.maximize_window()
browser.get("https://map.naver.com/p?c=15.00,0,0,0,dh")

# 검색창 입력
search = browser.find_element(By.CSS_SELECTOR, "input.input_search")
search.click()
time.sleep(1)
search.send_keys("강남역 맛집")
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(2)

# 본문 (iframe 안으로 들어가기)
iframe = browser.find_element(By.CSS_SELECTOR,"#searchIframe")
browser.switch_to.frame(iframe)

# iframe 안쪽 한번 클릭하기
browser.find_element(By.CSS_SELECTOR, "#_pcmap_list_scroll_container").click()

# 로딩된 데이터 개수 확인
lis = browser.find_elements(By.CSS_SELECTOR, "li.UEzoS")
before_len = len(lis)

while True:
    # 맨 아내로 스크롤 내린다.
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1.5)

    # 스크롤 후 로딩된 데이터 개수 확인  별점이 있는 것만
    lis = browser.find_elements(By.CSS_SELECTOR, "li:has(span.orXYY)")
    after_len = len(lis)

    # 로딩된 데이터 개수가 같다면 반복 멈춤
    if before_len == after_len:
        break
    before_len = after_len

for li in lis:
    # 가게명
    name = li.find_element(By.CSS_SELECTOR, "span.TYaxT")
    print(name.text)

# 가게 이름 10개 가져오기
# names = browser.find_elements(By.CSS_SELECTOR, "span.TYaxT")
# for name in names:
#     print(name.text)
#
# time.sleep(2)

# iframe 밖으로 나오기
browser.switch_to.default_content()



