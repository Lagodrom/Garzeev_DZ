import numpy as np
import pygame
import  random
def airlocks_definition (mask):
    #функция для генерации воздушных шлюзов на карте
    """
    заносит на карту стартовую позицию робота и позицию выхода с корабля
    variant - переменная, содержащая в себе указание какой вариант генерации воздушного шлюза задействовать
    :param mask: матрица - карта корабля (местности)
    :return: отрисовывает на карте местоположение робота (1) и местоположение выхода с корабля (4)
    """
    for i in range (2):
        variant = random.randint(1, 4)  # определение на каком из краев карты будет находуться шлюз
        # 1- левый край карты; 2 - верхний край карты; 3 - правый край карты; 4 - нижний край карты
        if (variant==1):
            x=random.randint(0,9)
            if (i==1):
                mask[x][0]=1
            else:
                mask[x][0]=4
        elif (variant==2):
            y=random.randint(0,9)
            if (i==1):
                mask[0][y]="1"
            else:
                mask[0][y]="4"
        elif (variant==3):
            x=random.randint(0,9)
            if (i==1):
                mask[x][9]="1"
            else:
                mask[x][9]="4"
        elif (variant==4):
            y=random.randint(0,9)
            if (i==1):
                mask[9][y]="1"
            else:
                mask[9][y]="4"

#создание карты корабля
if __name__ == '__main__':
    map, mask = np.zeros((10,10)), np.zeros((10,10))
    # for i in range (25):
    #     x= random.randint(0,9)
    #     y= random.randint(0,9)
    #     mask[x][y]=2
    airlocks_definition(mask)
    print(mask)
