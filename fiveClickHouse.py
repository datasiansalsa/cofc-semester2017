#fiveClickHouse.py
#Josh Boquiren
#16 October 2017
#A graphic based program that allows the user to click on 5 points to display
#   a 2D house: 2 clicks for the corners of the house, 1 click for the door,
#   1 click for the window, and a last click for the roof.

from graphics import *
def main():

    win = GraphWin("fiveClickHouse", 800, 500)
    intro = Text(Point(200, 13), "Click on 5 points to draw a house in this order:").draw(win)
    
    #2 points for house frame corners
    intro.setText("Click two points for corners (top left to bottom right) for the frame of the house.")
    #If points are made in any other sequence other than top left to bottom right, the calculations of the
    #   next points will be thrown off. Objects will still be drawn, but not correctly.
    p1 = win.getMouse()
    p2 = win.getMouse()
    length1 = ((p2.getX() - p1.getX()))
    width1 = ((p2.getY() - p1.getY()))     
    frame = Rectangle(p1, p2)
    frame.setFill("grey")
    frame.draw(win)

    #1 point for the door
    intro.setText("Click one point in the rectangle for the door.")
    p3 = win.getMouse()
    width2 = width1/5
    xVal1 = p3.getX()
    yVal2 = p3.getY()
    point1 = Point((xVal1 - (width2)), p3.getY())
    point2 = Point((xVal1+width2),p2.getY())
    door = Rectangle(point1,point2)
    door.setFill("brown")
    door.draw(win)
    
    #1 point for the window
    intro.setText("Click one point in the rectangle for the window.")
    p4 = win.getMouse()
    width3 = width2/2
    xVal3 = p4.getX()
    yVal4 = p4.getY()
    point3 = Point(xVal3-width3, yVal4-width3)
    point4 = Point(xVal3+width3, yVal4+width3)       
    window = Rectangle(point3, point4)
    window.setFill("white")
    window.draw(win)
    
    #1 point for the peak of the roof
    intro.setText("Click one point above the rectangle for the peak of the roof.")
    p5 = win.getMouse()
    point6 = Point((p2.getX()), p1.getY()) #understood point not gotten by mouse click
    roof = Polygon(p1,p5,point6)
    roof.setFill("brown")
    roof.draw(win)

    #Closing
    intro.setText("Click again to quit")
    closeClick = win.getMouse()
    win.close()
    
#End main
