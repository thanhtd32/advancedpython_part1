#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://tranduythanh.com

from  tkinter import *
window=Tk()
window.title("Take the quiz")
window.geometry("400x650+10+10")
#question label
qlabel=Label(window,width=100,text="")
qlabel.pack()
#image label
ilabel=Label(window)
ilabel.pack()
#Write the correct answer and press [Enter].
Label(window,text="Write the correct answer and press [Enter].").pack()
#Correct/Incorrect result label
rlabel=Label(window)
rlabel.pack()
file=open("data_exercise30/problem.txt","r",encoding="utf8")
p=file.readlines()
file.close()
i=-1
answer=""

def checkanswer(event):
    global  answer, e
    if answer ==e.get() :
        rlabel.config(text="Correct answer.")
    else:
        rlabel.config(text="Wrong answer.")
#User answer input window
e=Entry(window,width=50)
e.bind("<Return>",checkanswer)
e.pack()
def getQuestion():
    global i,answer, e
    i +=1
    # Repeat because there are 4 problems
    if i >=4 : i =0
    e.delete(0,len(e.get()))
    rlabel.config(text="")
    aQuestion =p[i].strip()
    Q=aQuestion.split(":")
    #Q[0]: - the problem
    #Q[1]: - Answer
    #Q[2]:  - image file
    qlabel.config(text=Q[0])
    answer=Q[1]
    img=PhotoImage(file=Q[2])
    ilabel.config(image=img)
    ilabel.image=img
Button(window,text="next problem",command=getQuestion).pack()
getQuestion()
window.mainloop()

