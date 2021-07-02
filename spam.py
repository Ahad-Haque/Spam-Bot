import pyautogui, time
# initializing time
time.sleep(4)

# open the text file and read it
x = open("gg.txt", 'r')

# reading a line and sending it from gg.txt
for alp in x:
    pyautogui.typewrite(alp)
    pyautogui.press("enter")
    # ll
