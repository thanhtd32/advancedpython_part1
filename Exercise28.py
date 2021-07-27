#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://duythanhcse.wordpress.com
#Facebook for solving coding problem: https://www.facebook.com/groups/communityuni
from tkinter import  *
window =Tk()

window.title("Create a calculator")
e=Entry(window,width=40,bg="black",fg="white",bd=5)
e.grid(row=0,column=0,columnspan=5)
buttons=[
    '0', '1', '2', '+', '%',
    '3', '4', '5', '-', '//',
    '6', '7', '8', '*', "**",
    '9', '.', '=', '/', 'C']
row = 1
col =0
for char in buttons:
    def click(key = char):
        if key == '=':
            result=eval(e.get())
            s=str(result)
            e.delete(0,END)
            e.insert(0,s)
        elif key =='C':
            e.delete(0,END)
        else:
            e.insert(END,key)
    b=Button(window, text=char, width=7, height=3, command=click)
    b.grid(row=row,column=col)
    col +=1
    if col >4:
        row +=1
        col=0
window.mainloop()