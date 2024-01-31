import pyautogui
import time

# 1. 화면 크기 출력
# print(pyautogui.size())

# 2. 마우스 위치 출력
# time.sleep(2)
# print(pyautogui.position())

# 3. 마우스 이동
# pyautogui.moveTo(1047, 372, 2)

# 4. 마우스 클릭
# pyautogui.click()
# pyautogui.click(button='right')
# pyautogui.doubleClick()
# pyautogui.click(clicks=3, interval=1)

# 5. 마우스 드래그
# 1299,173 -> 1166, 183
pyautogui.moveTo(1299,173, 2)
pyautogui.dragTo(1166,183, 2, button='left')