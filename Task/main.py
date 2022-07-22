import datetime
import time

# current = datetime.datetime.now()
# print(current)

from tkinter import *

window = Tk()

window.geometry("1080x720")
window.resizable(True, True)
window.attributes('-fullscreen',True) # 전체 화면
window.configure(background='white')

Label1 = Label(window, text="x", font=("HY견고딕", 44))
Label2 = Label(window, text="x", font=("HY견고딕", 44))

current = str(datetime.datetime.now())
current = current.replace(':','.')
f = open('stimulus_log/' + current + '.txt', 'w')

def start():
    current = datetime.datetime.now()
    f.write(str(current)+ ' start\n')
    print(current, 'start')
    Label1.config(text="aaa", font=("HY견고딕", 104), fg='white', bg='white')
    Label1.pack(pady=90)
    Label2.config(text="Start", font=("HY견고딕", 70), bg='white')
    Label2.pack()

def red():
    current = datetime.datetime.now()
    print(current, 'red')
    f.write(str(current) + ' red\n')
    # print('red')
    # Label1.config(text="Redddd", font=("G마켓 산스 TTF Bold", 60), fg='red', bg='red')
    window.configure(background='white')
    Label1.config(text="aaa", font=("HY견고딕", 104), fg='white', bg='white')
    Label1.pack(pady=120)
    Label2.config(text="Blue", font=("HY견고딕", 70), fg='blue', bg='white')
    Label2.pack()

def green():
    current = datetime.datetime.now()
    print(current, 'green')
    f.write(str(current) + ' green\n')
    # print('green')
    # Label1.config(text="green을 떠올리세요.", font=("G마켓 산스 TTF Bold", 44), fg='green', bg='green')
    window.configure(background='white')
    Label1.config(text="aaa", font=("HY견고딕", 104), fg='white', bg='white')
    Label1.pack(pady=120)
    Label2.config(text="Cyan", font=("HY견고딕", 70), fg='cyan', bg='white')
    Label2.pack()

# def green(): # 1 컬러랑 글씨 같이 있는거
#     current = datetime.datetime.now()
#     print(current, 'green')
#     f.write(str(current) + ' green\n')
#     # print('green')
#     # Label1.config(text="green을 떠올리세요.", font=("G마켓 산스 TTF Bold", 44), fg='green', bg='green')
#     Label1.config(text="aaa", font=("HY견고딕", 170), fg='green', bg='green')
#     Label1.pack(pady=120)
#     Label2.config(text="Green", font=("HY견고딕", 60), fg='green', bg='white')
#     Label2.pack()

def blue():
    current = datetime.datetime.now()
    print(current, 'blue')
    f.write(str(current) + ' blue\n')
    # print('blue')
    # Label1.config(text="Blue를 떠올리세요.", font=("G마켓 산스 TTF Bold", 44), fg='blue')
    window.configure(background='white')
    Label1.config(text="aaa", font=("HY견고딕", 104), fg='white', bg='white')
    Label1.pack(pady=120)
    Label2.config(text="Orange", font=("HY견고딕", 70), fg='orange', bg='white')
    Label2.pack()

# def attention():
#     current = datetime.datetime.now()
#     print(current, 'rest')
#     f.write(str(current) + ' rest\n')
#     # print('rest 5s')
#     # Label1.config(text=" ", font=("G마켓 산스 TTF Bold", 44), bg='white')
#     window.configure(background='white')
#     Label1.config(text=" ", font=("HY견고딕", 0), bg='white')
#     Label1.pack(pady=50)
#     Label2.config(text=" ", font=("HY견고딕", 0), bg='white')
#     Label2.pack()
def attention():
    current = datetime.datetime.now()
    print(current, 'attention')
    f.write(str(current) + ' attention\n')
    # print('rest 5s')
    # Label1.config(text=" ", font=("G마켓 산스 TTF Bold", 44), bg='white')
    window.configure(background='white')
    Label1.config(text=" ", font=("HY견고딕", 0), bg='white')
    Label1.pack(pady=50)
    Label2.config(text=" ", font=("HY견고딕", 0), bg='white')
    Label2.pack()

def rest():
    current = datetime.datetime.now()
    print(current, 'rest')
    f.write(str(current) + ' rest\n')
    # print('rest 5s')
    # Label1.config(text=" ", font=("G마켓 산스 TTF Bold", 44), bg='white')
    window.configure(background='black')
    Label1.config(text=" ", font=("HY견고딕", 0), bg='black')
    Label1.pack(pady=50)
    Label2.config(text=" ", font=("HY견고딕", 0), bg='black')
    Label2.pack()


def end():
    current = datetime.datetime.now()
    print(current,' end')
    f.write(str(current) + ' end\n')
    # Label1.config(text="End.", font=("G마켓 산스 TTF Bold", 44), fg='black')
    Label1.config(text="aaa", font=("HY견고딕", 104), fg='white', bg='white')
    Label1.pack(pady=90)
    Label2.config(text="END.", font=("HY견고딕", 70), fg='black', bg='white')
    Label2.pack()
    f.close()
    window.destroy()

sec = 1000
# init_rest = 30 # start와 red, blue, green 즉, 각 block 사이 rest time
# stimulus_interval = 10 # 자극 제시 텀. red 다음 red 보여주는 사이 간격
# on_time = 2
init_rest = 30
stimulus_time = 1
attention_time = 5
interval_rest = 5
#----------------

window.after(0, start) # start
window.after(sec, rest) # start 1초 뒤 부터 30초간 rest

for i in range(0, 5):
    window.after(stimulus_time * 1000 + init_rest * 1000 + stimulus_time * 1000 * i + attention_time * 1000 * i + interval_rest * 1000 * i, red) # 1은 화면 띄워주는 시간, 5는 rest 시간
    window.after(stimulus_time * 1000 + init_rest * 1000 + stimulus_time * 1000 * (i + 1) + attention_time * 1000 * i + interval_rest * 1000 * i, attention)
    window.after(stimulus_time * 1000 + init_rest * 1000 + stimulus_time * 1000 * (i + 1) + attention_time * 1000 * (i + 1) + interval_rest * 1000 * i, rest)
# ----------------------------------------------- #

for i in range(5, 10):
    window.after(stimulus_time * 1000 + init_rest * 1000 * 2 + stimulus_time * 1000 * i + attention_time * 1000 * i + interval_rest * 1000 * i, green)  # 1은 화면 띄워주는 시간, 5는 rest 시간
    window.after(stimulus_time * 1000 + init_rest * 1000 * 2 + stimulus_time * 1000 * (i + 1) + attention_time * 1000 * i + interval_rest * 1000 * i, attention)
    window.after(stimulus_time * 1000 + init_rest * 1000 * 2 + stimulus_time * 1000 * (i + 1) + attention_time * 1000 * (i + 1) + interval_rest * 1000 * i, rest)
    # window.after(sec + init_rest * sec * 2 + 1 * 1000 * i + stimulus_interval * 1000 * i, green) # 1은 화면 띄워주는 시간, 5는 rest 시간
    # window.after(sec + init_rest * sec * 2 + 1 * 1000 * (i+1) + stimulus_interval * 1000 * i, rest)

# # ----------------------------------------------- #
for i in range(10, 15):
    window.after(stimulus_time * 1000 + init_rest * 1000 * 3 + stimulus_time * 1000 * i + attention_time * 1000 * i + interval_rest * 1000 * i, blue)  # 1은 화면 띄워주는 시간, 5는 rest 시간
    window.after(stimulus_time * 1000 + init_rest * 1000 * 3 + stimulus_time * 1000 * (i + 1) + attention_time * 1000 * i + interval_rest * 1000 * i, attention)
    window.after(stimulus_time * 1000 + init_rest * 1000 * 3 + stimulus_time * 1000 * (i + 1) + attention_time * 1000 * (i + 1) + interval_rest * 1000 * i, rest)

# # ----------------------------------------------- #
window.after(stimulus_time * 1000 + init_rest * 1000 * 3 + stimulus_time * 1000 * 15 + attention_time * 1000 * 15 + interval_rest * 1000 * 15, end)

window.mainloop()
