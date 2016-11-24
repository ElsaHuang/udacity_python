import turtle

def draw_square():
	brad=turtle.Turtle()
	brad.shape("turtle")
	brad.color("white")
	brad.speed(0)

	for i in range(1,5):
		brad.forward(100)
		brad.right(90)

	


def draw_circle(): 
	angie=turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.speed(0)

	angie.circle(100)	

def draw_triangle():
	dada=turtle.Turtle()
	dada.shape("circle")
	dada.color("green")
	dada.speed(0)

	dada.forward(-100)
	dada.right(-240)
	dada.forward(-100)
	dada.right(120)
	dada.forward(-100)

def draw_leaf():
	# leaf=turtle.Turtle()
	# leaf.color("yellow")
	# leaf.speed(0)	

	base=turtle.pos()
	turtle.circle(100,75)
	turtle.goto(base)
	turtle.circle(-100,75)
	turtle.goto(base)
	
def draw_flower:
	

def draw():
	window = turtle.Screen()
	window.bgcolor('red')
	draw_square()
	draw_circle()
	draw_triangle()
	for i in range(1,14):
		turtle.left(27)
		draw_leaf()
	window.exitonclick()
	

draw()

