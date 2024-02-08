from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

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

# 검색창을 클릭
search = browser.find_element(By.CLASS_NAME, "_searchInput_search_text_3CUDs")
search.click()


