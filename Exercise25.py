#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://duythanhcse.wordpress.com
#Facebook for solving coding problem: https://www.facebook.com/groups/communityuni

#Description:
    #These codes I improved from Exercise24.
    #Improved the rock-scissors - paper
    #1.create class GameGUI
    #2.Update GUI for turtle
    #   2.1. All the results are drawn on the GUI
    #   2.2. Load image rock, scissors, paper for Computer and human
    #3. Show the result for each playing
import turtle
from random import randint
class GameUI:
    #list to store image for Machine
    arrImageMachine = ["data_exercise25/paper_machine.gif",
                       "data_exercise25/scissor_machine.gif",
                       "data_exercise25/rock_machine.gif"]
    # list to store image for Human
    arrImageHuman = ["data_exercise25/paper_human.gif",
                     "data_exercise25/scissor_human.gif",
                     "data_exercise25/rock_human.gif"]

    # turtle_machine: draw image for machine
    turtle_machine = None
    # turtle_human: draw image for human
    turtle_human = None
    # turtle_machine_label: draw label image for machine
    turtle_machine_label = None
    # turtle_human_label: draw label image for human
    turtle_human_label = None
    # turtle_result: draw result between human and machine
    turtle_result = None
    def __init__(self):
       self.turtle_machine = turtle.Turtle()
       self.turtle_human = turtle.Turtle()
       self.turtle_machine_label = turtle.Turtle()
       self.turtle_human_label = turtle.Turtle()
       self.turtle_result = turtle.Turtle()

       turtle.title("Rock Paper Scissors Game")
       #Set the size of the screen
       turtle.setup(800, 600)
       self.registerImage(self.arrImageMachine)
       self.registerImage(self.arrImageHuman)

    # Register image to be #turtle shape
    def registerImage(self,arrImage):
       for img in arrImage:
           turtle.addshape(img)

    #this function converts number to label of rock, paper, scissors
    def getLabel(self,num):
        if num ==0:
            return "[paper]"
        if num ==1 :
            return "[scissor]"
        else:
            return "[rock]"
    #this function use to show Welcome and help gamer
    def welcome(self,):
        msg="""
        Welcome to Rock paper Scissors Game!
        Please press [r] or [p] or [s]
        r ->rock
        p ->paper
        s ->scissor
        """
        self.turtle_result.reset()
        self.turtle_result.penup()
        style = ('batang', 20, 'italic')
        self.turtle_result.setposition(0,100)
        self.turtle_result.color('blue')
        self.turtle_result.write(msg, move=False, font=style,  align="center")
        self.turtle_result.hideturtle()

    #this function use to draw label
    def drawLabel(self,turleItem,msg,x,y,color,style,align):
        turleItem.reset()
        turleItem.penup()
        turleItem.setposition(x, y)
        turleItem.color(color)
        turleItem.write(msg, move=False, font=style, align=align)
        turleItem.hideturtle()
    #this function use to:
    #show human and computer result
    def show_result(self,myno,cno):
        self.turtle_machine.penup()
        self.turtle_machine.goto(100, 0)
        self.turtle_machine.shape(self.arrImageMachine[cno])
        self.turtle_human.penup()
        self.turtle_human.goto(-200,0)
        self.turtle_human.shape(self.arrImageHuman[myno])
        # Calculating the Win
        result=myno-cno
        msg=""
        if result ==2:
            # I rock, look at the computer
            result =-1
        elif result ==-2:
            # I see, the computer rocks. I win
            result=1
        if result ==0:
            msg="A draw with a computer. Do it again"
        elif result <0: #result =-1
            #You lost
            msg="You lost!"
        else: #result =1
            msg = "You won!"
        msgHuman="Your choice "+self.getLabel(myno)
        msgMachine="Computer selects "+self.getLabel(cno)
        style = ('batang', 15, 'italic')
        self.drawLabel(self.turtle_human_label,msgHuman,-200, -150,'red',style,"center")
        self.drawLabel(self.turtle_machine_label, msgMachine, 100, -150, 'red', style, "center")
        style = ('batang', 20, 'italic')
        self.drawLabel(self.turtle_result, msg,0,200, 'blue', style, "center")
    #this function is shown paper
    def paper(self):
        cno=randint(0,2)
        myno=0
        #Your choice is [paper]
        self.show_result(myno, cno)

    # this function is shown scissors
    def scissor(self):
        cno=randint(0,2)
        myno=1
        #Your choice is [scissors].
        self.show_result(myno,cno)

    # this function is shown rock
    def rock(self):
        cno=randint(0,2)
        myno=2
        #Your choice is [rock]
        self.show_result(myno,cno)

    # this function is listening the event
    def eventListener(self):
        #I make rocks
        turtle.onkeypress(self.rock, 'r')
        turtle.onkeypress(self.rock, 'R')

        #I make sissor
        turtle.onkeypress(self.scissor,'s')
        turtle.onkeypress(self.scissor,'S')

        #I make paper
        turtle.onkeypress(self.paper,'p')
        turtle.onkeypress(self.paper,'P')

        turtle.listen()
    def showGameUI(self):
        self.welcome()
        self.eventListener()
        turtle.mainloop()
#create game object
game=GameUI()
#call showGameUI method to start a game
game.showGameUI()