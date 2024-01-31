from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pyperclip
import pyautogui

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
driver.maximize_window()

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
pyperclip.copy("jaehee23")
pyautogui.keyDown('command')
pyautogui.press('v')
pyautogui.keyUp('command')
time.sleep(2)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy("")
pyautogui.keyDown('command')
pyautogui.press('v')
pyautogui.keyUp('command')
time.sleep(2)
# 로그인 버튼
driver.find_element(By.CSS_SELECTOR, "#log\.login").click()