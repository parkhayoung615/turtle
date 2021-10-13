import turtle
t=turtle.Turtle()

ts = turtle.getscreen()
ts.bgcolor("#FFDDFF");

def circle():
    t.fillcolor('sky blue')
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    
    t.fillcolor('magenta')
    t.begin_fill()
    t.circle(70)
    t.end_fill()
    
    t.fillcolor('blue')
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    
    t.left(90)
    
    
circle()
circle()
circle()
circle()