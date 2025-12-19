from turtle import Screen
from Food import Food
from Snake import Snake
import time
from scoreboard import Scoreboard
screen =Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Snake Game")
screen.tracer(0)


Snake = Snake()
Food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(Snake.up,"Up")
screen.onkey(Snake.down,"Down")
screen.onkey(Snake.left,"Left")
screen.onkey(Snake.right,"Right")

screen.listen()

game_is_on = True
while game_is_on:
     screen.update()
     time.sleep(0.1)
     Snake.move()


     if Snake.head.distance(Food)  < 15:
         Food.refresh()
         Snake.extend()
         scoreboard.increase_score()

     #for game over asingment
     if abs(Snake.head.xcor()) > 280 or abs(Snake.head.ycor()) > 280:
        game_is_on = False
        scoreboard.game_over()

     #eating its own tail
     for segment in Snake.segments[1:]:
        if Snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()