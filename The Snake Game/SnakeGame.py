from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

# Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title('Snake Game')
screen.tracer(0)

# Creating a snake and food
snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up" )
screen.onkey(snake.down, "Down" )
screen.onkey(snake.left, "Left" )
screen.onkey(snake.right, "Right" )

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # check for collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
        score.update_score()
        # print(score.score)
    
    # check collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # detect collision with its tail
    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10 :
            game_is_on = False
            score.game_over()


screen.exitonclick()