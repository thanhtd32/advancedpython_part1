#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://tranduythanh.com


from turtle import * # Turtle module
from random import randint #Random number related module
from time import  sleep #Time training module

numbers=[] #List to store random numbers

qno=int(textinput("","How many numbers do you want to remember?"))

if qno>1 :
    setup(300,200)

for i in range(qno):
    # Clear the screen and set the turtle's position to (0,0)
    reset()
    #hide the shape of the turtle
    ht()
    # Pick up the pen to stop drawing
    pu()
    #turtle 위치의 이동
    goto(-30,0)

    numbers.append(randint(1,99))
    write(numbers[i],font=("",32))
    # 2 second pause
    sleep(2)
#Close the turtle screen
bye() 
Success=True
for i in range(qno):#Compare 5 numbers
    unumber=int(input(str(i+1)+' digit>>'))
    if unumber != numbers[i] :
        #If not, treat incorrect answer
        print(numbers,"It's wrong answer")
        #The answer is not the same, so it is treated as a failure
        Success = False
        break
    if i == qno - 1: #If everything is correct, the answer is correct
       print(numbers,"That's the right answer.")
