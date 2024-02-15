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
import os
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
print(ssl.OPENSSL_VERSION)

if not os.path.exists('고양이'):
    os.mkdir('고양이')

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
browser.get("https://www.google.com/search?sca_esv=c53b42b634ca65da&rlz=1C5CHFA_enKR1005KR1008&sxsrf=ACQVn0_9x0c7EtMH8BvzUpDNehx5UECTlw:1707959495621&q=%EA%B3%A0%EC%96%91%EC%9D%B4&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiPwJv4lKyEAxW8n68BHQvgANQQ0pQJegQIEBAB&biw=1685&bih=845&dpr=1")

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

# 썸네일 이미지 태그 추출
imgs = browser.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")

i = 1
for i, img in enumerate(imgs, 1):
    # 이미지를 클릭해서 큰사이즈를 찾아요
    img.click()
    time.sleep(1)

    # 큰 이미지 주소 추출
    target = browser.find_element(By.CSS_SELECTOR, ".sFlh5c.pT0Scc")
    img_src = target.get_attribute('src')

    # 이미지 다운로드
    # 크롤이 하다보면 HTTP Error 403: Forbidden 에러가 납니다.
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    try:
        urllib.request.urlretrieve(img_src, f"고양이/{i}.jpg")
    except:
        print('error')
