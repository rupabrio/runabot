import pyautogui
from random import randint
from time import sleep

#mover cursor

def main(new_x, new_y, rango_x, rango_y):
    x = randint(new_x, new_x + rango_x)
    y = randint(new_y, new_y + rango_y)
    sleep(1)
    return pyautogui.moveTo(x, y, 0)

if __name__ == "__main__":
    for i in range(10):
        main(100, 200, 400, 600)
