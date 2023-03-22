from typing import List, Any

import numpy as np
import pygame
import  random
matrix_len=10-1
robot_cor=[0,0]
exit_cor=[0,0]
target_list=[]
mask=[]
def airlocks_definition (airlocks_count,map):
    #Todone:функция для генерации воздушных шлюзов на карте
    """
    заносит на карту стартовую позицию робота и позицию выхода с корабля
    variant - переменная, содержащая в себе указание какой вариант генерации воздушного шлюза задействовать
    :param map: матрица - карта корабля (местности)
    :return: отрисовывает на карте местоположение робота (1) и местоположение выхода с корабля (4)
    """
    global matrix_len
    global robot_cor
    global exit_cor
    for i in range (airlocks_count):
        variant = random.randint(1, 4)  # определение на каком из краев карты будет находуться шлюз
        # 1- левый край карты; 2 - верхний край карты; 3 - правый край карты; 4 - нижний край карты
        if (variant==1):
            x=random.randint(0,matrix_len)
            while (map[x][0]!=0):
                x = random.randint(0, matrix_len)
            if (i==0):
                map[x][0]=1
                robot_cor=[x,0]
            else:
                map[x][0]=4
                exit_cor=[x,0]
        elif (variant==2):
            y=random.randint(0,matrix_len)
            while (map[0][y]!=0):
                y = random.randint(0, matrix_len)
            if (i==0):
                map[0][y]=1
                robot_cor = [0,y]
            else:
                map[0][y]=4
                exit_cor = [0,y]
        elif (variant==3):
            x=random.randint(0,matrix_len)
            while (map[x][matrix_len]!=0):
                x = random.randint(0, matrix_len)
            if (i==0):
                map[x][matrix_len]=1
                robot_cor = [x,matrix_len]
            else:
                map[x][matrix_len]=4
                exit_cor = [x,matrix_len]
        elif (variant==4):
            y=random.randint(0,matrix_len)
            while (map[matrix_len][y]!=0):
                y = random.randint(0, matrix_len)
            if (i==0):
                map[matrix_len][y]=1
                robot_cor = [matrix_len,y]
            else:
                map[matrix_len][y]=4
                exit_cor = [matrix_len,y]

def goal_definition (goal_count,map):
    global matrix_len
    global target_list
    for i in range (goal_count):
            x = random.randint(0,matrix_len)
            y = random.randint(0, matrix_len)
            while (map[x][y]!=0):
                x = random.randint(0, matrix_len)
                y = random.randint(0, matrix_len)
            map[x][y]=3
            target_list.append([x,y])
def wall_generation (wall_count,map):
    global matrix_len
    for i in range(wall_count):
        x = random.randint(0, matrix_len)
        y = random.randint(0, matrix_len)
        while (map[x][y] != 0):
            x = random.randint(0, matrix_len)
            y = random.randint(0, matrix_len)
        map[x][y] = 2
def say_object(x,y,map):
    global matrix_len
    # 1 - робот.
    # 2 - стена.
    # 3 - объекты     за     которыми     едет     робот
    # 4 - зона     эвакуцию
    result = ""
    if x > matrix_len or x < 0:
        result = "край вселенной"
    elif y > matrix_len or y < 0:
        result = "край вселенной"
    elif map[x,y] == 0:
        result = "Пусто"
    elif map[x,y] == 2:
        result = "Стена"
    elif map[x,y] == 3:
        result = "Добыча"
    elif map[x,y] == 4:
        result = "Выход"
    else:
        result = "НЛО!!"

    return result
def what_i_see(cor,map):
    global matrix_len
    global mask
    x=robot_cor[0]
    y=robot_cor[1]

    print(x,y)
    print("в комнате со мной вижу:",say_object(x, y, mask))
    print("З вижу:",say_object(x-1, y, map))
    print("С-З вижу:",say_object(x-1, y+1, map))
    print("С вижу:",say_object(x, y+1, map))
    print("С-В вижу:",say_object(x+1, y+1, map))
    print("В вижу:",say_object(x+1, y, map))
    print("Ю-В вижу:",say_object(x+1, y-1, map))
    print("Ю вижу:", say_object(x, y - 1, map))
    print("Ю-З вижу:", say_object(x - 1, y - 1, map))
    # for x in range (-1,2):
    #     for y in range (-1,2):
    #         if x == -1 and y == -1:
    #             print("Ю-З вижу:", say_object(x, y, map))
    #         if x == 0 and y == -1:
    #             print("Ю вижу:", say_object(x, y, map))
    #         if x == 1 and y == -1:
    #             print("Ю-В вижу:", say_object(x, y, map))
    #         if x == -1 and y == 0:
    #             print("З вижу:", say_object(x, y, map))
    #         if x == 1 and y == 0:
    #             print("В вижу:", say_object(x, y, map))
    #         if x == -1 and y == 1:
    #             print("С-З вижу:", say_object(x, y, map))
    #         if x == 0 and y == 1:
    #             print("С вижу:", say_object(x, y, map))
    #         if x == 1 and y == 1:
    #             print("С-В вижу:", say_object(x, y, map))
    # for x in range(-1,2):
    #     for y in range(-1,2):
    #         # по сторонам света
    #         # С-З | C   | C-В
    #         # З   |робот| В
    #         # Ю-З | Ю   | Ю-В
    #         if x==0 and y==0: print("это я тут в центре стою")
    #         if x==-1 and y==-1:
    #             print("Ю-З вижу:",say_object(x,y,map))
    #         if x==0 and y==-1:
    #             print("Ю вижу:",say_object(x,y,map))
    #         if x==1 and y==-1:
    #             print("Ю-В вижу:",say_object(x,y,map))
    #         if x==-1 and y==0:
    #             print("З вижу:",say_object(x,y,map))
    #         if x==1 and y==0:
    #             print("В вижу:",say_object(x,y,map))
    #         if x==-1 and y==1:
    #             print("С-З вижу:",say_object(x,y,map))
    #         if x==0 and y==1:
    #             print("С вижу:",say_object(x,y,map))
    #         if x==1 and y==1:
    #             print("С-В вижу:",say_object(x,y,map))

    return
def robot_move (map):
    global robot_cor
    global target_list
    global exit_cor
    global mask
    target_list.append(exit_cor)
    move=[]
    for goal_cor in target_list:
        while (robot_cor!=goal_cor):
            what_i_see(robot_cor,map)
#код для одного перемещения робота из сектора в сектор
            vector_move=[goal_cor[0]-robot_cor[0],goal_cor[1]-robot_cor[1]]
            if (vector_move[0]!=0):
                vector_move[0]=vector_move[0]/(abs(vector_move[0]))
            if (vector_move[1]!=0):
                vector_move[1] = vector_move[1] / (abs(vector_move[1]))
            #вероятность отклонения движения у робота
            otklonenie_chance= random.randint(1,10)
            if (otklonenie_chance!=9 and otklonenie_chance!=10):
                move=[int((robot_cor[0]+vector_move[0])),int((robot_cor[1]+vector_move[1]))]
            elif (otklonenie_chance==9): #отклонение по x координте
                print("попал камушек под колесо. Отклонение влево")
                otklonenie = 1
                if (vector_move[0]==1 and vector_move[1]==1): #отклонение влево при движение [1,1]
                    move = [int((robot_cor[0] + vector_move[0])), int((robot_cor[1] + vector_move[1]-otklonenie))]
                elif (vector_move[0]==1 and vector_move[1]==-1): #отклонение влево при движение [1,-1]
                    move = [int((robot_cor[0] + vector_move[0]-otklonenie)), int((robot_cor[1] + vector_move[1]))]
                elif (vector_move[0]==-1 and vector_move[1]==1): #отклонение влево при движение [-1,1]
                    move = [int((robot_cor[0] + vector_move[0]+otklonenie)), int((robot_cor[1] + vector_move[1]))]
                elif (vector_move[0]==-1 and vector_move[1]==-1): #отклонение влево при движение [-1,-1]
                    move = [int((robot_cor[0] + vector_move[0])), int((robot_cor[1] + vector_move[1]+otklonenie))]
                elif (vector_move[0]==1 and vector_move[1]==0): #отклонение влево при движение [1,0]
                    move = [int((robot_cor[0] + vector_move[0]-otklonenie)), int((robot_cor[1] + vector_move[1]))]
                elif (vector_move[0]==-1 and vector_move[1]==0): #отклонение влево при движение [-1,0]
                    move = [int((robot_cor[0] + vector_move[0]+otklonenie)), int((robot_cor[1] + vector_move[1]))]
                elif (vector_move[0]==0 and vector_move[1]==1): #отклонение влево при движение [0,1]
                    move = [int((robot_cor[0] + vector_move[0])), int((robot_cor[1] + vector_move[1]-otklonenie))]
                elif (vector_move[0]==0 and vector_move[1]==-1): #отклонение влево при движение [0,-1]
                    move = [int((robot_cor[0] + vector_move[0])), int((robot_cor[1] + vector_move[1]+otklonenie))]
            elif (otklonenie_chance==10):
                print("попал камушек под колесо. Отклонение вправо")
                otklonenie = 1
                if (vector_move[0] == 1 and vector_move[1] == 1):  # отклонение вправо при движение [1,1]
                    move = [int((robot_cor[0] + vector_move[0]-otklonenie)), int((robot_cor[1] + vector_move[1]))]
                elif (vector_move[0] == 1 and vector_move[1] == -1):  # отклонение вправо при движение [1,-1]
                    move = [int((robot_cor[0] + vector_move[0])), int((robot_cor[1] + vector_move[1]-otklonenie))]
                elif (vector_move[0] == -1 and vector_move[1] == 1):  # отклонение вправо при движение [-1,1]
                    move = [int((robot_cor[0] + vector_move[0])), int((robot_cor[1] + vector_move[1])+otklonenie)]
                elif (vector_move[0] == -1 and vector_move[1] == -1):  # отклонение вправо при движение [-1,-1]
                    move = [int((robot_cor[0] + vector_move[0]-otklonenie)), int((robot_cor[1] + vector_move[1]))]
                elif (vector_move[0] == 1 and vector_move[1] == 0):  # отклонение вправо при движение [1,0]
                    move = [int((robot_cor[0] + vector_move[0]+otklonenie)), int((robot_cor[1] + vector_move[1]))]
                elif (vector_move[0] == -1 and vector_move[1] == 0):  # отклонение вправо при движение [-1,0]
                    move = [int((robot_cor[0] + vector_move[0]-otklonenie)), int((robot_cor[1] + vector_move[1]))]
                elif (vector_move[0] == 0 and vector_move[1] == 1):  # отклонение вправо при движение [0,1]
                    move = [int((robot_cor[0] + vector_move[0])), int((robot_cor[1] + vector_move[1]+otklonenie))]
                elif (vector_move[0] == 0 and vector_move[1] == -1):  # отклонение вправо при движение [0,-1]
                    move = [int((robot_cor[0] + vector_move[0])),int((robot_cor[1] + vector_move[1]-otklonenie))]
            map[robot_cor[0]][robot_cor[1]]=0
            map[move[0]][move[1]]=1
            robot_cor=[move[0],move[1]]
            print(map)
        #print(map)
    what_i_see(robot_cor, map)
def no_wall_nearby(x,y,map):
    global matrix_len
    result = True
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if (x+dx)>=0 and (x+dx)<=matrix_len:
                if (y+dy)>=0 and (y+dy)<=matrix_len:
                    if map[x+dx,y+dy] >0:
                        result = False
                        print("wall conflict ",x,y,"vs",x+dx,y+dy)
                else:
                    result = False
            else:
                result = False
    if result: print ("no conflict:",x,y)
    return result

def wall_placement():
    global matrix_len
    for i in range (int((matrix_len ** 2)/3)):
        x= random.randint(0,matrix_len)
        y= random.randint(0,matrix_len)
        if no_wall_nearby(x,y,map):
            map[x][y]=2
    return
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
#создание карты корабля
if __name__ == '__main__':
    map = np.zeros((10,10))

    # for i in range (25):
    #     x= random.randint(0,9)
    #     y= random.randint(0,9)
    #     map[x][y]=2
    airlocks_definition(2,map)
    goal_definition(2,map)
    wall_placement()
    #wall_generation(20,map)
    mask=map
    print(map)
    robot_move(map)
    print(mask)
