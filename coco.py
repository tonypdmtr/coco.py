import sys

# Check Python version number (Python v3+ required)
if sys.version_info[0] < 3:
    print("ERROR: 'pmode' Module requires Python v3.0 or higher")
    exit() # kill script
else:
    # Import the Tkinter & Turtle Graphics Modules
    import tkinter
    import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.screensize()
screen.setup(width = 1.0, height = 1.0)

# Create a Multi-Dimensional Array Which Will Represent Our On-Screen Grid
pixel = []
# Y Position Represents a Row in Our Multi-Dimensional Array
for y in range(30):
    newRow = []
    pixel.append(newRow)
    # X Position Represents a Single Space in an Individual Row in Our Multi-Dimensional Array
    for x in range(30):
        newTurtle = turtle.Turtle(visible=False)
        newRow.append(newTurtle)

# yCoordinate = 290
for y in range(30):
    # Set yCoordinate
    yCoordinate = [290,270,250,230,210,190,170,150,130,110,90,70,50,30,10,
                   -10,-30,-50,-70,-90,-110,-130,-150,-170,-190,-210,-230,
                   -250,-270,-290][y]
    # Set xCoordinate
    for x in range(30):
        xCoordinate = [-290,-270,-250,-230,-210,-190,-170,-150,-130,-110,
                       -90,-70,-50,-30,-10,10,30,50,70,90,110,130,150,170,
                       190,210,230,250,270,290][x]
        pixel[x][y].speed(0)
        pixel[x][y].penup()
        pixel[x][y].goto(xCoordinate, yCoordinate)
        pixel[x][y].shape("square")
        pixel[x][y].color("green")
        pixel[x][y].showturtle()

def set(x, y, c):
    global pixel
    pixel[x][y].color(c)

# Define placeholder Function (placeholder function used in place of main game logic in quick-start guide)
placeholder_x = -440
placeholder_y = 0
cycle = 0
ghost = turtle.Turtle(visible=False)
ghost.speed(0)
ghost.penup()
ghost.goto(placeholder_x, placeholder_y)
ghost.shape("square")
ghost.color("black") # set color to black to make ghost invisible
ghost.showturtle()

def busywork():
    global placeholder_x
    global placeholder_y
    global cycle
    global ghost

    placeholder_x = [-500,-480,-460,-440][cycle]
    ghost.goto(placeholder_x, placeholder_y)
    cycle = (cycle + 1) % 4
