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
pyperclip.copy("sprspre")
pyautogui.keyDown('command')
pyautogui.press('v')
pyautogui.keyUp('command')
time.sleep(2)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy("!Naver12#")
pyautogui.keyDown('command')
pyautogui.press('v')
pyautogui.keyUp('command')
time.sleep(2)
# 로그인 버튼
driver.find_element(By.CSS_SELECTOR, "#log\\.login").click()

# 메일함으로 이동
driver.get("https://mail.naver.com/v2/folders/0/all")
time.sleep(2)

# 메일 쓰기 버튼 클릭
driver.find_element(By.CSS_SELECTOR, "#root > div > nav > div > div.lnb_header > div.lnb_task > a.item.button_write").click()
time.sleep(2)

# 받는 사람
driver.find_element(By.CSS_SELECTOR, "#recipient_input_element").send_keys("sprspre@naver.com")
time.sleep(2)

# 제목
driver.find_element(By.CSS_SELECTOR, "#subject_title").send_keys("파이썬으로 자동화된 메일")
time.sleep(2)

# 본문 (iframe 안으로 들어가기)
iframe = driver.find_element(By.CSS_SELECTOR,"#content > div.contents_area > div > div.editor_area > div > div.editor_body > iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.CSS_SELECTOR, "body > div > div.workseditor-content").send_keys("본문내용")
time.sleep(2)

# iframe 밖으로 나오기
driver.switch_to.default_content()

# 보내기 버튼
driver.find_element(By.CSS_SELECTOR, "#content > div.mail_toolbar.type_write > div:nth-child(1) > div > button.button_write_task").click()


# 종료
time.sleep(5)
driver.close()