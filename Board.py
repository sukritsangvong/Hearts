######################################################################
#
# sample1.py
#
# Started in Pascal by Jeff Ondich on 1/25/95
# Ported to C++, Java, and Python
# Last modified 11 October 2017 by DLN
#
# Part (B):
#
#   1. Run this program, and read all the functions to see what they
#   do.  Try changing the parameters passed to sayHello(),
#   sayHelloAgain(), sayHelloAgain(), and drawSomeCircles().  How do
#   the parameters affect the picture?
#
#   2. Where is the origin (0,0) in the coordinate system of GraphWin?
#   Are larger y values higher or lower on the screen?  Are larger x
#   values further right or further left on the screen?  How can you
#   tell?
#
######################################################################

from graphics import *


def lineTo(window, startPoint, endPoint, color):
    '''Draws a line of the specified color from the Point
       startPoint to the Point endPoint.  Returns the
       endPoint.  Note that since this function does not
       save the Line object it creates, there is no way
       to later un-draw the Line.'''
    line = Line(startPoint, endPoint)
    line.setOutline(color)
    line.draw(window)
    return endPoint

def sayHello(window, startX, startY):
    lineColor = color_rgb(255, 255, 255)
    pen = Point(startX, startY)
    pen = lineTo(window, pen, Point(pen.x + 60, pen.y - 80), lineColor)
    pen = lineTo(window, pen, Point(pen.x - 10, pen.y - 20), lineColor)
    pen = lineTo(window, pen, Point(pen.x, pen.y + 100), lineColor)
    pen = lineTo(window, pen, Point(pen.x + 10, pen.y - 30), lineColor)
    pen = lineTo(window, pen, Point(pen.x + 10, pen.y), lineColor)
    pen = lineTo(window, pen, Point(pen.x + 10, pen.y + 30), lineColor)
    pen = lineTo(window, pen, Point(pen.x + 15, pen.y), lineColor)
    pen = lineTo(window, pen, Point(pen.x + 10, pen.y - 30), lineColor)
    pen = lineTo(window, pen, Point(pen.x + 5, pen.y + 20), lineColor)
    pen = Point(pen.x - 10, pen.y - 40)
    pen = lineTo(window, pen, Point(pen.x, pen.y - 2), lineColor)

def sayHelloAgain(window, x, y):
    textColor = color_rgb(255, 0, 0)
    text = Text(Point(x, y), 'HeyHey')
    text.setTextColor(textColor)
    text.setSize(30)
    text.draw(window)

def drawSomeCircles(window, y):
    circleColor = color_rgb(0, 0, 255)
    circle = Oval(Point(0,0), Point(200, 500))
    circle.setOutline(circleColor)
    circle.draw(window)

    circle = Circle(Point(350, y), 50)
    circle.setFill(circleColor)
    circle.draw(window)


# All the functions are defined.  Now start doing stuff.

# Open the window
windowWidth = 600
windowHeight  = 500
window = GraphWin('Graphics demo', windowWidth, windowHeight)
backgroundColor = color_rgb(0, 0, 0)
window.setBackground(backgroundColor)

# Draw some things
drawSomeCircles(window, 100)
sayHello(window, 100, windowHeight - 100)
sayHelloAgain(window, windowWidth - 250, windowHeight - 100)

# Wait for user input.
s = input('Hit Enter to quit')
