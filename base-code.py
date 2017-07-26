from tkinter import *
import tkinter.messagebox
tk=Tk()
tk.title("Tic-Tac-Toe")
import sys
a=[['1','2','3'],['4','5','6'],['7','8','9']]
def printM():
    for i in range(3):
        for j in range(3):
            sys.stdout.write(a[i][j])
            sys.stdout.flush()
        print()
def playerMove(p,i,j):
    if (p==1):
        a[i][j]='*'
    elif (p==2):
        a[i][j]='0'
def tictac():
    print ("welcome to tic-tac-toe game\ngiven the matrix:")
    printM()
    n=4
    while n>0 :
        print ("player 1 input your position")
        x=int(input("input a number"))
        i=(x-1)//3
        j=(x-1)%3
        playerMove(1,i,j)
        printM()
        print("player 2 input your position")
        x = int(input("input a number"))
        (int)
        i = (x - 1) // 3
        j = (x - 1) % 3
        playerMove(2, i, j)
        printM()
tictac()
