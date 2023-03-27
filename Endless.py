import platform as pt
import time
import os
from colorama import Fore,Style
ops=pt.system()
try:
    import pyautogui as py
except:
    if ops=="Android":
        print("This Code Doesn't Work On Android")
        exit()

def lolan():
    print("\n"+Fore.RED+name)
    print("\n"+Fore.BLUE+note)
    print(Style.RESET_ALL)

def send_mass():
    message=input("Enter The Message You Want To Send : ")
    try:
        number=int(input("How Many Times You Want To Send The Message : "))
    except ValueError:
        if ops=="Windows":
            os.system("cls")
        else:
            os.system("clear")
        lolan()
        print("Enter A Valid Number\n")
        return
    if number<1:
        if ops=="Windows":
            os.system("cls")
        else:
            os.system("clear")
        lolan()
        print("\nEnter A Valid Number Of Times To Send The Message\n")
        return
    print("Open The Chat You Want Send This Message In Any Platform In 20 Seconds")
    t=1
    while t<=20:
        print(t,end="\r")
        time.sleep(1)
        t+=1
    i=0
    while i<number:
        py.write(message)
        py.press("enter")
        i+=1
    if ops=="Windows":
        os.system("cls")
    else:
        os.system("clear")
    lolan()

name="""░█▀▀▀ ░█▄─░█ ░█▀▀▄ ░█─── ░█▀▀▀ ░█▀▀▀█ ░█▀▀▀█ 
░█▀▀▀ ░█░█░█ ░█─░█ ░█─── ░█▀▀▀ ─▀▀▀▄▄ ─▀▀▀▄▄ 
░█▄▄▄ ░█──▀█ ░█▄▄▀ ░█▄▄█ ░█▄▄▄ ░█▄▄▄█ ░█▄▄▄█

                                        BY : lolxn__"""
note="Note : I Won't Be Responsible For Any Damage Caused By The Script, Use At Your Own Risk"
if ops=="Windows":
    os.system("cls")
else:
    os.system("clear")
lolan()
while 1:
    print("1. Send Mass Message\n2. Exit")
    choice=input("Enter Your Choice : ")
    if choice=='1':
        if ops=="Windows":
            os.system("cls")
        else:
            os.system("clear")
        lolan()
        send_mass()
    elif choice=='2':
        if ops=="Windows":
            os.system("cls")
        else:
            os.system("clear")
        break
    else:
        if ops=="Windows":
            os.system("cls")
        else:
            os.system("clear")
        lolan()
        print("Invalid Choice\n")