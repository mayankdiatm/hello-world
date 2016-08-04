#!/usr/bin/env python
import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(200)
        some_turtle.right(90)

def draw_art():
    window =turtle.Screen()
    window.bgcolor("black")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
#    draw_square(brad)
    for i in range(1,74):
        draw_square(brad)
        brad.right(5)
    
   # angie = turtle.Turtle()
   # angie.shape("arrow")
   # angie.color("blue")
   # angie.circle(200)
  

    window.exitonclick()





draw_art()
