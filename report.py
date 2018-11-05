import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('data.txt', sep='\t')

num = df["n"]
color_num = df["Yn"]
df_color = pd.DataFrame({'blue_count': [],'red_count': []})

blue_num = 0
blue_list = []
red_num = 0
red_list = []
list_blue_red = []
for c in color_num:
    if c  == 1:
        blue_num += 1
    elif c == 0:
        red_num += 1
    blue_list.append(blue_num)
    red_list.append(red_num)
    list_blue_red.append([blue_num, red_num])

#問題１
pos_a = [] #Posterior P(X = A|Y)
pos_b = [] #Posterior P(X = B|Y)
for i, lbr in enumerate(list_blue_red):
    n_blue = lbr[0]
    n_red = lbr[1]
    square_3n = 3**(i +1) #3のn乗
    square_2nb = 2**(i+1+n_blue) #2の(n+b)乗
    pay = (square_3n) / (square_3n + square_2nb)
    pby = 1- pay
#     pos_b = (square_2nb) /(square_3n + square_2nb)
    pos_a.append(pay)
    pos_b.append(pby)

num = range(1,10001)

#問題１ n = 1-100
x1 = num
y1 = pos_a
x2 = num
y2 = pos_b
plt.scatter(x1, y1, c='orange', label = "P(X=A|Y)")
plt.scatter(x2, y2, c='green', label = "P(X=B|Y)")
plt.xlim([0, 100])
plt.ylim([0, 1])
plt.legend(loc="right")
plt.show()

#問題1 n = 1-10000
x1 = num
y1 = pos_a
x2 = num
y2 = pos_b
plt.scatter(x1, y1, c='orange', label = "P(X=A|Y)")
plt.scatter(x2, y2, c='green', label = "P(X=B|Y)")
plt.xlim([0, 10000])
plt.ylim([0, 1])
plt.legend(loc="right")
plt.show()

#問題１施行数え上げ
x01 = num
y01 = blue_list
x02 = num
y02 = red_list
plt.plot(x01, y01, c='blue', label = "blue_count")
plt.plot(x02, y02, c='red', label = "red_count")
plt.xlim([0, 10000])
plt.ylim([0, 5500])
plt.legend(loc="right")
plt.show()

#問題2
pos_a2 = [] #Posterior P(X = A|Y)
pos_b2 = [] #Posterior P(X = B|Y)
for i, lbr in enumerate(list_blue_red):
    n_blue = lbr[0]
    n_red = lbr[1]
    square_3n2 = 3**(i+3) #3の(n+2)乗
    square_2nb = 2**(i+1+n_blue) #2の(n+b)乗
    pay2 = (square_3n2) / (square_3n2 + square_2nb)
    pby2 = 1- pay2
    pos_a2.append(pay2)
    pos_b2.append(pby2)

#問題2 n = 1-100
x21 = num
y21 = pos_a2
x22 = num
y22 = pos_b2
plt.scatter(x21, y21, c='orange', label = "P(X=A|Y)")
plt.scatter(x22, y22, c='green', label = "P(X=B|Y)")
plt.xlim([0, 100])
plt.ylim([0, 1])
plt.legend(loc="right")
plt.show()

#問題2 n = 1-10000
x21 = num
y21 = pos_a2
x22 = num
y22 = pos_b2
plt.scatter(x21, y21, c='orange', label = "P(X=A|Y)")
plt.scatter(x22, y22, c='green', label = "P(X=B|Y)")
plt.xlim([0, 10000])
plt.ylim([0, 1])
plt.legend(loc="right")
plt.show()

#問題3
pos_a3 = [] #Posterior P(X = A|Y)
pos_b3 = [] #Posterior P(X = B|Y)
for i, lbr in enumerate(list_blue_red):
    n_blue = lbr[0]
    n_red = lbr[1]
    square_3n = 3**(i +1) #3のn乗
    square_2nb = 2**(i+1+n_blue) #2の(n+b)乗
    square_9_2nb = 9*square_2nb #9×2の(n+b)乗
    pay3 =  square_9_2nb / (square_3n + square_9_2nb)
    pby3 = 1- pay3
    pos_a3.append(pay3)
    pos_b3.append(pby3)

#問題3 n = 1-100
x31 = num
y31 = pos_a3
x32 = num
y32 = pos_b3
plt.scatter(x31, y31, c='orange', label = "P(X=A|Y)")
plt.scatter(x32, y32, c='green', label = "P(X=B|Y)")
plt.xlim([0, 100])
plt.ylim([0, 1])
plt.legend(loc="right")
plt.show()

#問題3 n = 1-10000
x31 = num
y31 = pos_a3
x32 = num
y32 = pos_b3
plt.scatter(x31, y31, c='orange', label = "P(X=A|Y)")
plt.scatter(x32, y32, c='green', label = "P(X=B|Y)")
plt.xlim([0, 10000])
plt.ylim([0, 1])
plt.legend(loc="right")
plt.show()