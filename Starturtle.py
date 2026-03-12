# A built-in graphics module used to draw shapes and patterns using a virtual pen 
# (turtle) that moves with commands like forward(), backward(), left(), and right().


#draw square  using Turtle Programming 

import turtle 

# skk = turtle.Turtle() 
# turtle.bgcolor("Pink")
# for i in range(1): 
# 	skk.forward(100) 
# 	# skk.backward(200)
# 	# skk.right(90) 
	
# turtle.done() 

#  draw star 
# star = turtle.Turtle() 

# star.right(75) 
# star.forward(100) 

# for i in range(4): 
# 	star.left(145) 
# 	star.forward(100) 	
# turtle.done() 

# Hexagons
 
# Hexagon = turtle.Turtle() 
# num_sides = 6
# side_length = 80
# angle = 360/ num_sides 

# for i in range(num_sides): 
# 	Hexagon.forward(side_length) 
# 	Hexagon.right(angle) 
	
# turtle.done() 

# parallelogram 
# t = turtle.Turtle() 
# t.speed(4) 
# for i in range(2): 
# 	t.forward(100) 
# 	t.left(60) 
# 	t.forward(50) 
# 	t.left(120) 
# turtle.done() 


# # Circle :
# screen = turtle.Screen() 
# screen.bgcolor("green") 
# pen = turtle.Turtle() 
# pen.speed(4) 
# pen.fillcolor("red") 
# pen.begin_fill() 
# pen.circle(70) 
# pen.end_fill() 
# pen.hideturtle() 
# turtle.done() 

# Spiral Square Outside In and Inside Out 
  #Inside_Out 

# wn = turtle.Screen() 
# wn.bgcolor("light green") 
# skk = turtle.Turtle() 
# skk.color("blue") 

# def sqrfunc(size): 

# 	for i in range(4): 
# 		skk.fd(size) 
# 		skk.left(90) 
# 		size = size + 5

# sqrfunc(6) 
# sqrfunc(26) 
# sqrfunc(46) 
# sqrfunc(66) 
# sqrfunc(86) 
# sqrfunc(106) 
# sqrfunc(126) 
# sqrfunc(146) 
# turtle.done()

# 
# Python program to draw 
# Spiral Helix Pattern 
# using Turtle Programming 

# loadWindow = turtle.Screen() 
# turtle.speed(0) 

# for i in range(100): 
# 	turtle.circle(5*i) 
# 	turtle.circle(-5*i) 
# 	turtle.left(i) 

# turtle.exitonclick() 



# Rainbow benzene 

# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
# t = turtle.Pen() 
# t.speed(10)
# turtle.bgcolor('black') 
# for x in range(360): 
#     t.pencolor(colors[x%6]) 
#     t.width(x//100 + 1) 
#     t.forward(x) 
#     t.left(90) 

# turtle.done(')'


# t = turtle.Turtle();;
# t.penup()
# t.goto(-200, 200)  # move to top-left corner
# t.pendown()
# t.circle(50)
# turtle.done()


# +x -> moves right
# -x -> moves left
# +y -> moves up
# -y -> moves down

# goto(-200, 200) → top-left
# goto(200, 200) → top-right
# goto(-200, -200) → bottom-left
# goto(200, -200) → bottom-right
