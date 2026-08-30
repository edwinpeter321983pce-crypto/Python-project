import turtle
window = turtle.Turtle()
window.fillcolor("blue")
window.begin_fill()

window.left(180)
for ii in range(8):
        window.forward(100)
        window.right(45)
window.end_fill()
turtle.done()