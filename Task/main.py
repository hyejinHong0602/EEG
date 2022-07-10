import datetime
import time

# current = datetime.datetime.now()
# print(current)

from tkinter import *

window = Tk()

window.geometry("1080x720")
window.resizable(True, True)

Label1 = Label(window, text="x", font=("G마켓 산스 TTF Bold", 44))
Label1.pack(pady=250)


def start():
    current = datetime.datetime.now()
    print(current, 'start')
    Label1.config(text="Start", font=("G마켓 산스 TTF Bold", 44), bg='green')


def red():
    current = datetime.datetime.now()
    print(current, 'red')
    # print('red')
    Label1.config(text="Redddd", font=("G마켓 산스 TTF Bold", 60), fg='red', bg='red')


def green():
    current = datetime.datetime.now()
    print(current, 'green')
    # print('green')
    Label1.config(text="green을 떠올리세요.", font=("G마켓 산스 TTF Bold", 44), fg='green', bg='green')

def blue():
    current = datetime.datetime.now()
    print(current, 'blue')
    # print('blue')
    Label1.config(text="Blue를 떠올리세요.", font=("G마켓 산스 TTF Bold", 44), fg='blue')

def rest():
    current = datetime.datetime.now()
    print(current, 'rest')
    # print('rest 5s')
    Label1.config(text=" ", font=("G마켓 산스 TTF Bold", 44))


def end():
    current = datetime.datetime.now()
    print(current,' end')
    Label1.config(text="End.", font=("G마켓 산스 TTF Bold", 44), fg='black')

sec = 1000

#----------------
window.after(0, start) # start
window.after(sec, rest) # start 1초 뒤 부터 30초간 rest

for i in range(0, 5):
    window.after(sec + 30 * sec + 1 * 1000 * i + 5 * 1000 * i, red) # 1은 화면 띄워주는 시간, 5는 rest 시간
    window.after(sec + 30 * sec + 1 * 1000 * (i+1) + 5 * 1000 * i, rest)
# ----------------------------------------------- #

for i in range(5, 10):
    window.after(sec + 30 * sec * 2 + 1 * 1000 * i + 5 * 1000 * i, green) # 1은 화면 띄워주는 시간, 5는 rest 시간
    window.after(sec + 30 * sec * 2 + 1 * 1000 * (i+1) + 5 * 1000 * i, rest)

# ----------------------------------------------- #
for i in range(10, 15):
    window.after(sec + 30 * sec * 3 + 1 * 1000 * i + 5 * 1000 * i, blue) # 1은 화면 띄워주는 시간, 5는 rest 시간
    window.after(sec + 30 * sec * 3 + 1 * 1000 * (i+1) + 5 * 1000 * i, rest)

# ----------------------------------------------- #
window.after(sec + 30 * sec * 3 + 1 * 1000 * 15 + 5 * 1000 * 15, end)



#----------------
# window.after(0, start) # start
# window.after(1000, rest) # start 1초 뒤 부터 30초간 rest
#
# window.after(1000+30*1000, red) # 30초뒤 red보여주기
# window.after(1000+30*1000 + 1*1000, rest)
# window.after(1000+30*1000 + 1*1000 + 5*1000, red)
# window.after(1000+30*1000 + 1*1000*2 + 5*1000, rest)
# window.after(1000+30*1000 + 1*1000*2 + 5*1000*2, red)
# window.after(1000+30*1000 + 1*1000*3 + 5*1000*2, rest)
# window.after(1000+30*1000 + 1*1000*3 + 5*1000*3, red)
# window.after(1000+30*1000 + 1*1000*4 + 5*1000*3, rest)
# window.after(1000+30*1000 + 1*1000*4 + 5*1000*4, red)
# window.after(1000+30*1000 + 1*1000*5 + 5*1000*4, rest)
# # ----------------------------------------------- #
# window.after(1000+30*1000 + 1*1000*5 + 5*1000*5, green)
# window.after(1000+30*1000 + 1*1000*6 + 5*1000*5, rest)
# window.after(1000+30*1000 + 1*1000*6 + 5*1000*6, green)
# window.after(1000+30*1000 + 1*1000*7 + 5*1000*6, rest)
# window.after(1000+30*1000 + 1*1000*7 + 5*1000*7, green)
# window.after(1000+30*1000 + 1*1000*8 + 5*1000*7, rest)
# window.after(1000+30*1000 + 1*1000*8 + 5*1000*8, green)
# window.after(1000+30*1000 + 1*1000*9 + 5*1000*8, rest)
# window.after(1000+30*1000 + 1*1000*9 + 5*1000*9, green)
# window.after(1000+30*1000 + 1*1000*10 + 5*1000*9, rest)
# # ----------------------------------------------- #
# window.after(1000+30*1000 + 1*1000*10 + 5*1000*10, blue)
# window.after(1000+30*1000 + 1*1000*11 + 5*1000*10, rest)
# window.after(1000+30*1000 + 1*1000*11 + 5*1000*11, blue)
# window.after(1000+30*1000 + 1*1000*12 + 5*1000*11, rest)
# window.after(1000+30*1000 + 1*1000*12 + 5*1000*12, blue)
# window.after(1000+30*1000 + 1*1000*13 + 5*1000*12, rest)
# window.after(1000+30*1000 + 1*1000*13 + 5*1000*13, blue)
# window.after(1000+30*1000 + 1*1000*14 + 5*1000*13, rest)
# window.after(1000+30*1000 + 1*1000*14 + 5*1000*14, blue)
# window.after(1000+30*1000 + 1*1000*15 + 5*1000*14, rest)
# # ----------------------------------------------- #
# window.after(1000+30*1000 + 1*1000*15 + 5*1000*15, end)

window.mainloop()
