import turtle as trtl 
t = trtl.Turtle()
size = 25
def circle():
	t.penup()
	t.forward(size)

def drawing_circle(size):
	t.circle()
	t.penup()
	t.forward(size)

t.penup()
t.setposition(0,0)

drawing_circle(size)
for i in range(4):
	size = size + 25
	t.forward(size)
	drawing_circle(size)