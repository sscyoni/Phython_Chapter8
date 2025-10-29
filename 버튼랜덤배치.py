from tkinter import*
from random import ramdint
def place_random_buttons() :

  for button in buttons :
    x = radint(50,400)
    y= randint(50,250)
    width = randint(50,100)
    height=randint(20,50)
    button.place(x=x,y=y,width=width,height=height)

root = Tk()
root.geometry("500x300")

buttons = []
colors - ["red","green","blue","yellow"]


#버튼 생성 및 리스트에 추가
for colors in colors :
  button = Button(rrot,text = color,bg=color,fg = "white")
  buttons.append(button)

place _random_buttons()

#새로고침 버튼 생성 및 place 배치
refresh_button = Button(root,text ="새로고침",command = place_random_buttons)
refresh_button.place(x=150,y=250)

root.mainloop()
