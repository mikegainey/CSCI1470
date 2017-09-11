import turtle

colors = ["blue", "red", "purple", "green"]

sides = input("Input number of sides: ")
sides = int(sides)

wn = turtle.Screen()
wn.bgcolor("cornsilk")
wn.title("n-sided n-gon")

geowiz = turtle.Turtle()

geowiz.pensize(5)

offset = 90
for j in range(int(360 / offset)):

    for i in range(sides):
        pencolor = colors[i % 4]
        geowiz.color(pencolor)
        geowiz.forward(100)
        geowiz.left(360/sides)

    geowiz.left(offset)
    
wn.mainloop()
