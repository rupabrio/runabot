import cv2
import pyautogui
import numpy

barra_test = {'img' : './data/barra_test.png', 'reg' : (0, 0, 50, 40)}

def matchear_imagen(reg, imagen):
    pyautogui.screenshot('./data/captura.png', region=reg)
    pantalla = cv2.imread('./data/captura.png')
    plantilla = cv2.imread(imagen)
    res = cv2.matchTemplate(pantalla, plantilla, cv2.TM_CCOEFF_NORMED)
    tolerancia = .80
    loc = numpy.where(res >= tolerancia)
    if len(loc[0]) > 0 :
        print('la barra esta arriba')
        return True
    print('la barra esta en otro lado')
    return False

matchear_imagen(barra_test['reg'], barra_test['img'])
