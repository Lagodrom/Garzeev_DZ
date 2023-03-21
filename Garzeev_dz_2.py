import numpy as np
import pygame
import  random
#создание карты корабля
map, mask = np.zeros((10,10)), np.zeros((10,10))
for i in range (25):
    x= random.randint(0,9)
    y= random.randint(0,9)
    mask[x][y]=1
print(mask)