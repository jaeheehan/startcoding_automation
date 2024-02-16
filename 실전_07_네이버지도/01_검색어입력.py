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

