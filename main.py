import turtle
from turtle import Screen, Turtle
from math import pi, sin, cos

myTurtle = turtle.Turtle()

  
while True:
  choice = input("\n1. Draw Concentric Squares\n2. Draw Concentric Circles\n3. Draw an Octagon \n4. Draw a Poppy \n5. Exit\nYour answer: ").lower()
  myTurtle.clear()
        
  if choice == "draw concenteric squares" or choice == "1":
    turtle.clear()
    myTurtle.speed(6)
    size = 10

    def drawConcSquares(size):
        count = 1
        while (count <= 4):
            myTurtle.forward(size)
            myTurtle.left(90)
            count = count + 1

    while (size <= 200):
        drawConcSquares(size)
        myTurtle.penup()
        myTurtle.forward(13)
        myTurtle.right(90)
        myTurtle.forward(5)
        myTurtle.right(90)
        myTurtle.forward(18)
        myTurtle.right(180)
        myTurtle.pendown()
        size = size + 10
          
      
  if choice == "draw concentric circles" or choice == "2":
    turtle.clear()
    myTurtle.speed(6)
      
    def drawConcCircles(size, dx): # size is the radius and dx is the amount
        for i in range(dx):
            myTurtle.circle(size*i)
            print (size*i)
            myTurtle.up()
            myTurtle.sety((size*i)*(-1))
            myTurtle.down()
            
    drawConcCircles(10,5)#drawConcCircles(10,11) 

    
  if choice == "draw an octagon" or choice == "3":
    turtle.clear()
    myTurtle.speed(2)
      
    def drawOctogon(size):
        count = 1
        while count <= 8:
            myTurtle.forward(size)
            myTurtle.left(45)
            count = count + 1
        
    drawOctogon(50)
  
    
  if choice == "draw a poppy" or choice == "4":
    turtle.clear()
    myTurtle.speed(4)
      
    def drawPoppy(turtle, k):
        origin_x, origin_y = turtle.position()
        theta = 0.0

        turtle.begin_fill()

        while theta < 2.0 * pi:
            x = 2 * k * (1 - cos(theta)) * cos(theta)
            y = 2 * k * (1 - cos(theta)) * sin(theta)

            turtle.goto(origin_x + x, origin_y + y)
            theta += 0.1

        turtle.end_fill()

    screen = Screen()

    yertle = Turtle(visible=False)
    yertle.speed('fastest') 
    yertle.color('red')

    for sign in [-1, 1]:
        yertle.penup()
        yertle.setx(sign * 100)
        yertle.pendown()

        drawPoppy(yertle, sign * 30)

    yertle.penup()
    yertle.home()
    yertle.dot(80, 'black')
    screen.mainloop()
      
    
  if choice == "exit" or choice == "5":
    print("You have chose to quit this program.")
    quit()
