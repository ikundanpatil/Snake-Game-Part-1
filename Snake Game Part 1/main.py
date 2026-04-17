from turtle import Screen
from snake import Snake
import time

display = Screen()
display.setup(width=600,height=600)
display.bgcolor("black")
display.title("My Snake Game")
display.tracer(0)

snake = Snake()

display.listen()  
display.onkey(snake.up, "Up")
display.onkey(snake.down, "Down")
display.onkey(snake.left, "Left")
display.onkey(snake.right, "Right")


is_game_on = True
while is_game_on:
    display.update()
    time.sleep(0.1)

    snake.move()
     
display.exitonclick()
