from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip
import csv

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
browser.get("https://www.naver.com")
browser.implicitly_wait(10) # 로딩이 끝날 때까지 10초까지는 기다려줌

# 쇼핑 메뉴 클릭
browser.find_element(By.CSS_SELECTOR, "#shortcutArea > ul > li:nth-child(4)").click()
time.sleep(2)

# 현재 탭 저장
p = browser.current_window_handle

# 열려있는 탭 조회
chwd = browser.window_handles

# 새로운 탭으로 이동
for w in chwd:
    if (w != p):
        browser.switch_to.window(w)

# 검색창을 클릭
search = browser.find_element(By.CSS_SELECTOR, "input._searchInput_search_text_3CUDs")
search.click()

# 검색어를 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    # 맨 아래로 스크롤 내린다.
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")
    if before_h == after_h:
        break
    before_h = after_h

# 파일 생성
f = open(r"data.csv", 'w', encoding='utf-8', newline='')
writer = csv.writer(f)

# 상품 정보 div
items = browser.find_elements(By.CSS_SELECTOR, ".basicList_list_basis__uNBZx > div > div > div > div > div:nth-child(2)")

for item in items:
    # print(item.get_attribute("innerHTML"))
    name = item.find_element(By.CSS_SELECTOR, "div[class*=title] > a").text
    try:
        price = item.find_element(By.CSS_SELECTOR, ".price").text
    except:
        price = "판매중단"
    link = item.find_element(By.CSS_SELECTOR, "div[class*=title] > a").get_attribute("href")
    print(name, price, link)
    writer.writerow([name, price, link])

# 파일 닫기
f.close()