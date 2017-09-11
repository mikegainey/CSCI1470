import turtle

colors = ["blue", "red", "purple", "green"]

sides = input("Input number of sides: ")
sides = int(sides)

wn = turtle.Screen()
wn.bgcolor("cornsilk")
wn.title("n-sided n-gon")

geowiz = turtle.Turtle()

geowiz.color("blue")
geowiz.pensize(5)

for i in range(sides):
    geowiz.forward(100)
    geowiz.left(360/sides)

wn.mainloop()
