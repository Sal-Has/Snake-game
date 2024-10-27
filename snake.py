from turtle import Turtle,Screen

UP = 90
DOWN=270
LEFT=180
RIGHT= 0
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:



    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]


    def create_snake(self):
        for position in POSITIONS:
            self.add_turtle(position)


    def add_turtle(self,position):
        # add a new segement
        new_turtle = Turtle()
        new_turtle.color("white")
        new_turtle.shape("square")
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtles.append(new_turtle)
    def extend(self):
        self.add_turtle(self.turtles[-1].position())

    def reset(self):
        for seg in self.turtles:
            seg.goto(1000,1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]
    def move(self):
        for turtle in range(len(self.turtles)-1,0,-1):
            new_x =self.turtles[turtle-1].xcor()
            new_y =self.turtles[turtle-1].ycor()
            self.turtles[turtle].goto(new_x,new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.seth(UP)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)


