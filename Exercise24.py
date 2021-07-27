#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://duythanhcse.wordpress.com
#Facebook for solving coding problem: https://www.facebook.com/groups/communityuni

import turtle
import turtle as t
from turtle import *

from random import randint
s=["data_exercise24/paper_machine.gif",
   "data_exercise24/scissor_machine.gif",
   "data_exercise24/rock_machine.gif"]
#Set the size of the screen
t.setup(300,300)
for img in s:
    #Register image to be #turtle shape
    t.addshape(img)
print("If you want to play rock paper scissors, press s for scissors, r for rock, and p for jaws.")
def show_result(myno,cno):
    t.shape(s[cno])
    # Calculating the Win
    result=myno-cno
    msg=""
    if result ==2:
        # I rock, look at the computer, I'm Jim
        result =-1
    elif result ==-2:
        # I see, the computer rocks. I win
        result=1
    if result ==0:
        print("A draw with a computer. Do it again.")
        msg="A draw with a computer. Do it again."
    elif result <0: #result =-1
        print("You lost")
        msg="You lost"
    else: #result =1
        #You won
        print("You won")
        msg = "You won"
    turtle.write(msg, False, align="center")
def rock():
    cno=randint(0,2)
    myno=2
    print("Your choice is [rock]",end='')
    show_result(myno,cno)
def scissor():
    cno=randint(0,2)
    myno=1
    print("Your choice is [scissors].",end='')
    show_result(myno,cno)
def paper():
    cno=randint(0,2)
    myno=0
    print("Your choice is [paper]",end='')
    show_result(myno, cno)
#I make rocks
t.onkeypress(rock, 'r')
#I make sissor
t.onkeypress(scissor,'s')
#I make paper
t.onkeypress(paper,'p')
t.listen()
t.mainloop()
