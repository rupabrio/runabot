import cv2
import pyautogui
import numpy as np
from random import randint
from time import sleep

irons = [
	{'ref' : './vision/iron4.png', 'coords' : (0, 0, 2000, 2000)},
	{'ref' : './vision/iron5.png', 'coords' : (0, 0, 2000, 2000)}
	]



def look_at(ref, coords, tolerance=0.69):
	#Load up assets
	pyautogui.screenshot('./vision/snap.png', region=coords)
	snap = cv2.imread('./vision/snap.png')
	reference = cv2.imread(ref)
	match = cv2.matchTemplate(snap, reference, cv2.TM_CCOEFF_NORMED)
	#Location
	loc = np.where(match > tolerance)
	if len(loc[0]) > 0 :		
		return (loc[1][0], loc[0][0])

def mine_rock(coords):
	pyautogui.moveTo(coords[0] + 40, coords[1] + 40, 0)
	pyautogui.click()
	print('found')
	sleep(randint(8, 10))

while True:
	for iron in irons:
		rock = look_at(iron['ref'], iron['coords'])
		if not rock:
			print('Not found')
			continue
		mine_rock(rock)


