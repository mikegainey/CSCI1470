import turtle

sides = input("Input number of sides: ")
sides = int(sides)

wn = turtle.Screen()
wn.bgcolor("cadet blue")
wn.title("7-sided n-gon")

geowiz = turtle.Turtle()

geowiz.color("brown")
geowiz.pensize(5)

for i in range(sides):
    geowiz.forward(150)
    geowiz.left(360/sides)

wn.mainloop()
