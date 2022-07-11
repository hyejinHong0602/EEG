import datetime
import time

# current = datetime.datetime.now()
# print(current)

from tkinter import *

window = Tk()

window.geometry("1080x720")
window.resizable(True, True)
# window.attributes('-fullscreen',True) # 전체 화면
window.configure(background='white')

Label1 = Label(window, text="x", font=("G마켓 산스 TTF Bold", 44))
Label2 = Label(window, text="x", font=("G마켓 산스 TTF Bold", 44))

current = str(datetime.datetime.now())
current = current.replace(':','.')
f = open('stimulus_log/' + current + '.txt', 'w')

def start():
    current = datetime.datetime.now()
    f.write(str(current)+ ' start\n')
    print(current, 'start')
    Label1.config(text="aaa", font=("G마켓 산스 TTF Bold", 104), fg='white', bg='white')
    Label1.pack(pady=90)
    Label2.config(text="Start", font=("G마켓 산스 TTF Bold", 70), bg='white')
    Label2.pack()

def red():
    current = datetime.datetime.now()
    print(current, 'red')
    f.write(str(current) + ' red')
    # print('red')
    # Label1.config(text="Redddd", font=("G마켓 산스 TTF Bold", 60), fg='red', bg='red')

    Label1.config(text="aaa", font=("G마켓 산스 TTF Bold", 170), fg='red', bg='red')
    Label1.pack(pady=120)
    Label2.config(text="Red", font=("G마켓 산스 TTF Bold", 60), fg='red', bg='white')
    Label2.pack()

def green():
    current = datetime.datetime.now()
    print(current, 'green')
    f.write(str(current) + ' green')
    # print('green')
    # Label1.config(text="green을 떠올리세요.", font=("G마켓 산스 TTF Bold", 44), fg='green', bg='green')
    Label1.config(text="aaa", font=("G마켓 산스 TTF Bold", 170), fg='green', bg='green')
    Label1.pack(pady=120)
    Label2.config(text="Green", font=("G마켓 산스 TTF Bold", 60), fg='green', bg='white')
    Label2.pack()

def blue():
    current = datetime.datetime.now()
    print(current, 'blue')
    f.write(str(current) + ' blue')
    # print('blue')
    # Label1.config(text="Blue를 떠올리세요.", font=("G마켓 산스 TTF Bold", 44), fg='blue')
    Label1.config(text="aaa", font=("G마켓 산스 TTF Bold", 170), fg='blue', bg='blue')
    Label1.pack(pady=120)
    Label2.config(text="Blue", font=("G마켓 산스 TTF Bold", 60), fg='blue', bg='white')
    Label2.pack()

def rest():
    current = datetime.datetime.now()
    print(current, 'rest')
    f.write(str(current) + ' rest')
    # print('rest 5s')
    # Label1.config(text=" ", font=("G마켓 산스 TTF Bold", 44), bg='white')
    Label1.config(text=" ", font=("G마켓 산스 TTF Bold", 0), bg='white')
    Label1.pack(pady=50)
    Label2.config(text=" ", font=("G마켓 산스 TTF Bold", 0), bg='white')
    Label2.pack()



def end():
    current = datetime.datetime.now()
    print(current,' end')
    f.write(str(current) + ' end')
    # Label1.config(text="End.", font=("G마켓 산스 TTF Bold", 44), fg='black')
    Label1.config(text="aaa", font=("G마켓 산스 TTF Bold", 104), fg='white', bg='white')
    Label1.pack(pady=90)
    Label2.config(text="END.", font=("G마켓 산스 TTF Bold", 70), fg='black', bg='white')
    Label2.pack()

sec = 1000
init_rest = 30 # start와 red, blue, green 즉, 각 block 사이 rest time
stimulus_interval = 5 # 자극 제시 텀. red 다음 red 보여주는 사이 간격
#----------------

window.after(0, start) # start
window.after(sec, rest) # start 1초 뒤 부터 30초간 rest

for i in range(0, 5):
    window.after(sec + init_rest * sec + 1 * 1000 * i + stimulus_interval * 1000 * i, red) # 1은 화면 띄워주는 시간, 5는 rest 시간
    window.after(sec + init_rest * sec + 1 * 1000 * (i+1) + stimulus_interval * 1000 * i, rest)
# ----------------------------------------------- #

for i in range(5, 10):
    window.after(sec + init_rest * sec * 2 + 1 * 1000 * i + stimulus_interval * 1000 * i, green) # 1은 화면 띄워주는 시간, 5는 rest 시간
    window.after(sec + init_rest * sec * 2 + 1 * 1000 * (i+1) + stimulus_interval * 1000 * i, rest)

# ----------------------------------------------- #
for i in range(10, 15):
    window.after(sec + init_rest * sec * 3 + 1 * 1000 * i + stimulus_interval * 1000 * i, blue) # 1은 화면 띄워주는 시간, 5는 rest 시간
    window.after(sec + init_rest * sec * 3 + 1 * 1000 * (i+1) + stimulus_interval * 1000 * i, rest)

# ----------------------------------------------- #
window.after(sec + init_rest * sec * 3 + 1 * 1000 * 15 + stimulus_interval * 1000 * 15, end)

window.mainloop()
