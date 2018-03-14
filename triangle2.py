

import math
from graphics import *

def square(x):
    return x * x

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX())
                     + square(p2.getY() - p1.getY()))
    return dist

def main():
    win = GraphWin("Vault Of Glass",500,500)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    win.setBackground("#7f7f7f")
    message = Text(Point(5, 0.5), "Click on nine points")
    message.draw(win)

    # Get and draw nine vertices of triangle
    p1 = Point(5, 8.66)
    p1.draw(win)
    p2 = Point(0, 0)
    p2.draw(win)
    p3 = Point(10, 0)
    p3.draw(win)
    p4 = Point(5, 6.5)
    p4.draw(win)
    p5 = Point(1.25, 0)
    p5.draw(win)
    p6 = Point(8.75, 0)
    p6.draw(win)
    p7 = Point(5, 4.33)
    p7.draw(win)
    p8 = Point(2.5, 0)
    p8.draw(win)
    p9 = Point(7.5, 0)
    p9.draw(win)
    p10 = Point(5, 2.16)
    p10.draw(win)
    p11 = Point(3.75, 0)
    p11.draw(win)
    p12 = Point(6.25, 0)
    p12.draw(win)

    # Use Polygon object to draw the triangles
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("#ADD8E6")
    triangle.setOutline("black")
    triangle.draw(win)
    triangle = Polygon(p4,p5,p6)
    triangle.setFill("#ADD8E6")
    triangle.setOutline("black")
    triangle.draw(win)
    triangle = Polygon(p7,p8,p9)
    triangle.setFill("#ADD8E6")
    triangle.setOutline("black")
    triangle.draw(win)
    triangle = Polygon(p10,p11,p12)
    triangle.setFill("#7f7f7f")
    triangle.setOutline("black")
    triangle.draw(win)

    # Calculate the perimeter of the triangle
    perim = distance(p1,p2) + distance(p2,p3) + distance(p3,p1)
    perim = distance(p4,p5) + distance(p5,p6) + distance(p4,p6)
    perim = distance(p7,p8) + distance(p8,p9) + distance(p7,p9)
    message.setText("The perimeter is: %0.2f" % perim)

    win.mainloop()
    win.master.destroy()
    win.__autoflush()

main()
