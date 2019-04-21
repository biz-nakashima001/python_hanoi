import numpy as np
import time

count =0
# n:ハノイの数
# n:移動元
# n:移動先
# n:経由地
def hanoi(n, x, y, z):
    if(n == 0):
        # 何もしない
        print("")
    else:
        # 2^n - 1 経由地へ移動(再帰呼び出し)
        hanoi(n-1, x,z,y)
        # 移動と出力
        printout(x,y)
        # 2^n - 1 経由地から移動先へ(再帰呼び出し)
        hanoi(n-1, z,y,x)

# 移動と出力
def printout(x,y):
    global count # 手数
    global a, b, c 
    global n #  ハノイの数
    global sleep
    count = count + 1

    if(x == 'a'):
       remove = a[-1]
       a = np.delete(a,-1)
       
    elif(x == 'b'):
       remove = b[-1]
       b = np.delete(b,-1)
       
    else:
       remove = c[-1]
       c = np.delete(c,-1)

    if(y == 'a'):
        a = np.append(a, remove)
    elif(y == 'b'):
        b = np.append(b, remove)
    else:
        c = np.append(c, remove)
    
    time.sleep(sleep)
    print(count,"手目: ", x,"->",y)
    print("----------------------------------------------")
    print("a:",a)
    print("b:",b)
    print("c:",c)



if __name__ == '__main__':
    n = int(input("hanoiの数＜: "))
    # ハノイの初期化
    a = np.arange(n, 0, -1)
    b = np.array([])
    c = np.array([])

    print("予想手数:", "２^n -1 -> ", pow(2, n)-1)
    sleep = int(input("スリープ(秒)＜: "))
    print("----------------------------------------------")
    print(a)
    print(b)
    print(c)
    time.sleep(sleep)

    hanoi(n, 'a','b','c')