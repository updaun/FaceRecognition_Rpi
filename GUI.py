from tkinter import *
import tkinter.font

from dir_make import make
from face_shot import shot
from train_model import train
from face_lock import lock
from file_remove import remove


def getTextInput():
    result = textExample.get(1.0, END+"-1c")
    # print(result)
    return result


root = Tk()
root.geometry("480x640")
root.title("스마트 도어 시스템")

#font=tkinter.font.Font(family="돋움", size=20, slant="italic")
font = tkinter.font.Font(size=15)
font1 = tkinter.font.Font(size=11)


btn1 = Button(root, text="체험자 폴더 생성", width=25,
              height=2, font=font, command=make)
btn2 = Button(root, text="데이터 촬영", width=25, height=2, font=font, command=shot)
btn3 = Button(root, text="인공지능 학습", width=25,
              height=2, font=font, command=train)
btn4 = Button(root, text="스마트 도어 작동", width=25,
              height=2, font=font, command=lock)
btn5 = Button(root, text="이미지 삭제", width=25,
              height=2, font=font, command=remove)


label1 = Label(root, text='- 체험자의 이름을 영어로 입력하세요.',
               anchor="sw", width=40, height=2, font=font1)

label2 = Label(root, text='- 스페이스 바를 눌러 사진을 촬영하세요.(종료 - ESC)',
               anchor="sw", width=40, height=2, font=font1)

label3 = Label(root, text='- 사진 개수에 따라 학습 시간이 다릅니다.',
               anchor="sw", width=40, height=2, font=font1)

label4 = Label(root, text='- 학습된 스마트 도어가 작동합니다.(종료 - ESC)',
               anchor="sw", width=40, height=2, font=font1)

label5 = Label(root, text='- 체험을 종료하고, 사진을 삭제합니다.',
               anchor="sw", width=40, height=2, font=font1)

ci = Label(root, text='(주)한국공학기술연구원', anchor="s",
           width=40, height=3, font=font)


label1.pack()

textExample = Text(root, width=26, height=1, font=font)
textExample.pack()

btn1.pack()

label2.pack()

btn2.pack()

label3.pack()

btn3.pack()

label4.pack()

btn4.pack()

label5.pack()

btn5.pack()

ci.pack()

root.mainloop()
