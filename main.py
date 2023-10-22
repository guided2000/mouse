import pyautogui as p
import random
import time

counter =0
for i in range(100):
    x=random.randint(900,1500)
    y=random.randint(400,800)
    p.moveTo(x,y)
    counter+=1
    time.sleep(1)
    print(counter)