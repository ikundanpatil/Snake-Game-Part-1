from turtle import Turtle   # Importing Turtle class from turtle module

tim = Turtle()
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]   # Constant data (used by the class)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:                     # 🔹 OOP: Class (Blueprint for Snake object)

    def __init__(self):          # 🔹 OOP: Constructor (special method that runs when object is created)
        self.segments = []       # 🔹 OOP: Instance Variable / Attribute
        self.create_snake()      # 🔹 OOP: Calling a method inside the class
        self.head = self.segments[0]
    
    def create_snake(self):      # 🔹 OOP: Method (Function inside a class)
        for i in STARTING_POSITIONS:
            tim = Turtle("square")   # 🔹 OOP: Creating an object from Turtle class
            tim.color("white")
            tim.penup()
            tim.goto(i)
            self.segments.append(tim)  # 🔹 Using object list as attribute

    def move(self):              # 🔹 OOP: Method that defines behavior of Snake object

        # Move each segment to the position of the segment in front of it
        for seg_num in range(len(self.segments) - 1,0,-1):
            x = self.segments[seg_num - 1].xcor()   # Using object method
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x,y)        # Object interacting with another object
        
        self.head.forward(MOVE_DISTANCE)     # Head moves forward
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP) 

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN) 
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT) 
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) 
        