import pyautogui
import pyperclip

# 1. 키보드 입력 (문자)
# pyautogui.write('startcoding', interval=0.25)

# 2. 키보드 입력 (키)
# pyautogui.press('enter')
# pyautogui.press('up')

# 3. 키보드 입력 (여러개 동시에)
# pyautogui.hotkey('command', 'c')

# 4. 한글 입력 방법
pyperclip.copy('한글입력잘되나?')
pyautogui.keyDown('command')
pyautogui.press('v')
pyautogui.keyUp('command')



