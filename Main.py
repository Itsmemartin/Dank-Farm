#Itsmemartin
import pyautogu
import time

time.sleep(5)

default_cl = 2

clickx,clicky = x,y
#enter your coords above

def write(string, cooldown):
    pyautogui.write(string)
    pyautogui.press('enter')
    time.sleep(cooldown)


def basic_cmd():

    write('This is a auto farm bot, use at your own risk as its against Dankmemers rules', default_cl)
    time.sleep(5)

    write('pls fish', default_cl)
    time.sleep(5)

    write('pls hunt', default_cl)
    time.sleep(5)

    write('pls dig', default_cl)
    time.sleep(5)

    write('pls beg', default_cl)
    time.sleep(5)

    write('pls pm', default_cl)
    pyautogui.click(clickx,clicky)
    time.sleep(5)

    write('pls search', default_cl)
    pyautogui.click(clickx,clicky)
    time.sleep(5)

    write('pls hl', default_cl)
    pyautogui.click(clickx,clicky)
    time.sleep(5)

    write('pls crime', default_cl)
    pyautogui.click(clickx, clicky)
    time.sleep(5)

    write('pls dep max', default_cl)

while True:
    basic_cmd()
    time.sleep(5)
