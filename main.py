import math
import random
from tkinter import *

# имя файла
from PIL import ImageTk

name = "houses.txt"

# Загрузка исходных данных из файла
X = list()
XS = list()  # символьные значения
f = open(name, "r")

for s in f:
    s = s.strip()
    SS = s.split(",")
    X.append(SS)
    XS.append(s)

f.close()

# массивы для хранения коэффициентов для нормировки
As = list()
Bs = list()

# нормировка исходных данных
for i in range(len(X[0])):
    M = float(X[0][i])
    m = float(X[0][i])
    for j in range(len(X)):
        X[j][i] = float(X[j][i])
        if abs(X[j][i]) > M:
            M = abs(X[j][i])
        else:
            if abs(X[j][i]) < m:
                m = abs(X[j][i])
    # коэффициенты нормирования
    a = 1 / (M - m)
    b = -m / (M - m)
    # сохранить коэффициенты
    As.append(a)
    Bs.append(b)
    # нормировать
    for j in range(len(X)):
        X[j][i] = a * X[j][i] + b

W = list()  # создать массив для весов
K = 4  # количество классов
M = len(X)  # количество исходных данных
N = len(X[0])  # размерность векторов


# получить случайное значение для инициализирования весов
def get_w():
    z = random.random() * (2.0 / math.sqrt(M))
    return 0.5 - (1 / math.sqrt(M)) + z


# инициализировать веса
for i in range(K):
    W.append(list())
    for j in range(N):
        W[i].append(get_w() * 0.5)

la = 0.5  # коэффициент обучения
dla = 0.05  # уменьшение коэффициента обучения


# расстояние между векторами
def rho(w, x):
    r = 0
    for i in range(len(w)):
        r = r + (w[i] - x[i]) * (w[i] - x[i])

    r = math.sqrt(r)
    return r


# поиск ближайшего вектора
def FindNear(W, x):
    wm = W[0]
    r = rho(wm, x)
    i = 0
    i_n = i
    for w in W:
        if rho(w, x) < r:
            r = rho(w, x)
            wm = w
            i_n = i
        i = i + 1
    return (wm, i_n)


# начать процесс обучения
while la >= 0:
    for k in range(100):  # повторять 100 раз обучение
        for x in X:
            wm = FindNear(W, x)[0]
            for i in range(len(wm)):
                wm[i] = wm[i] + la * (x[i] - wm[i])  # корректировка весов
    la = la - dla  # уменьшение коэффициента обучения

WX = list()  # массив для денормированных весов

# денормировать веса
for i in range(K):
    WX.append(list())
    for j in range(N):
        WX[i].append((W[i][j] - Bs[j]) / As[j])

for wx in WX:
    print(wx)

# печать первых компонент весов
for wx in WX:
    print(wx[0])

Data = list()  # создать классы

for i in range(len(W)):
    Data.append(list())

# отнести исходные данные к своему классу
DS = list()
i = 0
for x in X:
    i_n = FindNear(W, x)[1]
    Data[i_n].append(x)
    DS.append([i_n, XS[i]])
    i = i + 1

# напечатать количество элементов в классах
i = 0
class_n = list()
for d in Data:
    print("Класс " + str(i) + " состоит из " + str(len(d)) + " элементов")
    class_n.append(len(d))
    i = i + 1

# распечатать по классам
f = list()
for i in range(K):
    f.append(open(str(i) + name, "w"))
for ds in DS:
    f[ds[0]].write(ds[1])
    f[ds[0]].write("\n")
for i in range(K):
    f[i].close()


def minmax():
    minmax_array = list()
    for _ in range(7):
        minmax_array.append(list())
    areas = list()
    for _ in range(7):
        areas.append(list())
    with open('0' + name) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {},{}".format(cnt, line.strip().split(',')[0], line.strip().split(',')[1]))
            index = int(line.strip().split(',')[1]) - 1
            print('index: ', index)
            areas[index].append(line.strip().split(',')[0])
            line = fp.readline()
            cnt += 1
    with open('1' + name) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {},{}".format(cnt, line.strip().split(',')[0], line.strip().split(',')[1]))
            index = int(line.strip().split(',')[1]) - 1
            print('index: ', index)
            areas[index].append(line.strip().split(',')[0])
            line = fp.readline()
            cnt += 1
    with open('2' + name) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {},{}".format(cnt, line.strip().split(',')[0], line.strip().split(',')[1]))
            index = int(line.strip().split(',')[1]) - 1
            print('index: ', index)
            areas[index].append(line.strip().split(',')[0])
            line = fp.readline()
            cnt += 1
    with open('3' + name) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {},{}".format(cnt, line.strip().split(',')[0], line.strip().split(',')[1]))
            index = int(line.strip().split(',')[1]) - 1
            print('index: ', index)
            areas[index].append(line.strip().split(',')[0])
            line = fp.readline()
            cnt += 1
    count = 0
    for area in areas:
        minmax_array[count].append(min(area))
        minmax_array[count].append(max(area))
        count = count + 1
    print(minmax_array)
    return minmax_array


def result():
    if var.get() == 0:
        terr = minmax()[0]
        answer = str(terr[0]) + ' - ' + str(terr[1])
        l1.config(text=answer)
    elif var.get() == 1:
        terr = minmax()[1]
        answer = str(terr[0]) + ' - ' + str(terr[1])
        l1.config(text=answer)
    elif var.get() == 2:
        terr = minmax()[2]
        answer = str(terr[0]) + ' - ' + str(terr[1])
        l1.config(text=answer)
    elif var.get() == 3:
        terr = minmax()[3]
        answer = str(terr[0]) + ' - ' + str(terr[1])
        l1.config(text=answer)
    elif var.get() == 4:
        terr = minmax()[4]
        answer = str(terr[0]) + ' - ' + str(terr[1])
        l1.config(text=answer)
    elif var.get() == 5:
        terr = minmax()[5]
        answer = str(terr[0]) + ' - ' + str(terr[1])
        l1.config(text=answer)
    elif var.get() == 6:
        terr = minmax()[6]
        answer = str(terr[0]) + ' - ' + str(terr[1])
        l1.config(text=answer)
    print("\nСтоимость жилья: ", answer, '\n')


window = Tk()
window.title("Хисамов Искандер №3")
window.geometry("300x250+800+400")
var = IntVar()
var.set(0)
r1 = Radiobutton(text='Вахитовский', variable=var, value=0)
r1.pack(side=TOP)
r2 = Radiobutton(text='Ново-Савиновский', variable=var, value=1)
r2.pack(side=TOP)
r3 = Radiobutton(text='Советский', variable=var, value=2)
r3.pack(side=TOP)
r4 = Radiobutton(text='Московский', variable=var, value=3)
r4.pack(side=TOP)
r5 = Radiobutton(text='Приволжский', variable=var, value=4)
r5.pack(side=TOP)
r6 = Radiobutton(text='Авиастроительный', variable=var, value=5)
r6.pack(side=TOP)
r7 = Radiobutton(text='Кировский', variable=var, value=6)
r7.pack(side=TOP)
b1 = Button(text='Узнать стоимость недвижости', command=result)
b1.pack()
l1 = Label(text="0")
l1.pack(side=BOTTOM, pady=15)
window.mainloop()
