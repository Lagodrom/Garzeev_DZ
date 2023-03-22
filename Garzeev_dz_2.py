import numpy as np
import pygame
import  random
matrix_len=10-1
robot_cor=[0,0]
exit_cor=[0,0]
target_list=[]
mask = []

def airlocks_definition (airlocks_count,mask):
    #Todone:функция для генерации воздушных шлюзов на карте
    """
    заносит на карту стартовую позицию робота и позицию выхода с корабля
    variant - переменная, содержащая в себе указание какой вариант генерации воздушного шлюза задействовать
    :param mask: матрица - карта корабля (местности)
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
            while (mask[x][0]!=0):
                x = random.randint(0, matrix_len)
            if (i==0):
                mask[x][0]=1
                robot_cor=[x,0]
            else:
                mask[x][0]=4
                exit_cor=[x,0]
        elif (variant==2):
            y=random.randint(0,matrix_len)
            while (mask[0][y]!=0):
                y = random.randint(0, matrix_len)
            if (i==0):
                mask[0][y]=1
                robot_cor = [0,y]
            else:
                mask[0][y]=4
                exit_cor = [0,y]
        elif (variant==3):
            x=random.randint(0,matrix_len)
            while (mask[x][matrix_len]!=0):
                x = random.randint(0, matrix_len)
            if (i==0):
                mask[x][matrix_len]=1
                robot_cor = [x,matrix_len]
            else:
                mask[x][matrix_len]=4
                exit_cor = [x,matrix_len]
        elif (variant==4):
            y=random.randint(0,matrix_len)
            while (mask[matrix_len][y]!=0):
                y = random.randint(0, matrix_len)
            if (i==0):
                mask[matrix_len][y]=1
                robot_cor = [matrix_len,y]
            else:
                mask[matrix_len][y]=4
                exit_cor = [matrix_len,y]

def say_object(x,y):
    global mask
    global matrix_len
    # 1 - робот.
    # 2 - стена.
    # 3 - объекты     за     которыми     едет     робот
    # 4 - зона     эвакуцию
    result = ""
    if x > matrix_len-1 or x < 0:
        result = "край вселенной"
    elif y > matrix_len-1 or y < 0:
        result = "край вселенной"
    elif mask[x,y] == 0:
        result = "Пусто"
    elif mask[x,y] == 2:
        result = "Стена"
    elif mask[x,y] == 3:
        result = "Добыча"
    elif mask[x,y] == 4:
        result = "Выход"
    else:
        result = "НЛО!!"

    return result
def what_i_see(coords):
    global matrix_len
    global mask
    # print(coords) # [0, 9] y,x
    for x in range(-1,2):
        for y in range(-1,2):
            # по сторонам света
            # С-З | C   | C-В
            # З   |робот| В
            # Ю-З | Ю   | Ю-В
            if x==0 and y==0: print("это я тут в центре стою")
            if x==-1 and y==-1:
                print("Ю-З вижу:",say_object(coords[1]+x,coords[0]+y))
            if x==0 and y==-1:
                print("Ю вижу:",say_object(coords[1]+x,coords[0]+y))
            if x==1 and y==-1:
                print("Ю-В вижу:",say_object(coords[1]+x,coords[0]+y))
            if x==-1 and y==0:
                print("З вижу:",say_object(coords[1]+x,coords[0]+y))
            if x==1 and y==0:
                print("В вижу:",say_object(coords[1]+x,coords[0]+y))
            if x==-1 and y==1:
                print("С-З вижу:",say_object(coords[1]+x,coords[0]+y))
            if x==0 and y==1:
                print("С вижу:",say_object(coords[1]+x,coords[0]+y))
            if x==1 and y==1:
                print("С-В вижу:",say_object(coords[1]+x,coords[0]+y))

    return
def goal_definition (goal_count,mask):
    global matrix_len
    global target_list
    for i in range (goal_count):
            x = random.randint(0,matrix_len)
            y = random.randint(0, matrix_len)
            while (mask[x][y]!=0):
                x = random.randint(0, matrix_len)
                y = random.randint(0, matrix_len)
            mask[x][y]=3
            target_list.append([x,y])
def wall_generation (wall_count,mask):
    global matrix_len
    for i in range(wall_count):
        x = random.randint(0, matrix_len)
        y = random.randint(0, matrix_len)
        while (mask[x][y] != 0):
            x = random.randint(0, matrix_len)
            y = random.randint(0, matrix_len)
        mask[x][y] = 2
def robot_move (mask):
    global robot_cor
    global target_list
    global exit_cor
    target_list.append(exit_cor)
    move=[]
    for goal_cor in target_list:
        while (robot_cor!=goal_cor):
#код для одного перемещения робота из сектора в сектор
            what_i_see(robot_cor)
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
                otklonenie = -1
                # if ()
                if (vector_move[0]+otklonenie>1 or vector_move[0]+otklonenie<-1):
                    otklonenie=-1
                move = [int((robot_cor[0] + vector_move[0]+otklonenie)), int((robot_cor[1] + vector_move[1]))]
            elif (otklonenie_chance==10):
                otklonenie = 1
                if (vector_move[0]+otklonenie>1 or vector_move[0]+otklonenie<-1):
                    otklonenie= -1
                move = [int((robot_cor[0] + vector_move[0]+ otklonenie)), int((robot_cor[1] + vector_move[1]))]
            mask[robot_cor[0]][robot_cor[1]]=0
            mask[move[0]][move[1]]=1
            robot_cor=[move[0],move[1]]
            print(mask)
        #print(mask)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
#создание карты корабля
if __name__ == '__main__':

    mask = np.zeros((matrix_len, matrix_len))
    # for i in range (25):
    #     x= random.randint(0,9)
    #     y= random.randint(0,9)
    #     mask[x][y]=2
    airlocks_definition(2, mask)
    goal_definition(2, mask)
    #wall_generation(20,mask)
    print(mask)
    robot_move(mask)
