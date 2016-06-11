##################################################################
# FILE: HelloTurtle.py
# WRITER: Idan Refaeli, idan0610, 305681132
# EXERCISE: intro2cs ex1 2014-2015
# DESCRIPTION:
# A program that draws some simple geometric shapes on the screen
# and prints "Hello Turtle!", using Turtle graphics.
##################################################################
import turtle

# title for the display window
turtle.title("Fun with Turtle Graphics and Python")
turtle.up()				#Lift the pen up, no drawing
turtle.goto(-100, -100)	#Move turtle to the absolute position (-100,-100)
turtle.down()			#Pen is down, drawing now

# Draw a red square:
turtle.color("red")		#Change the color to red
turtle.goto(-100,100)	#Move turtle to the absolute position (-100,100)
turtle.goto(100,100)	#Move turtle to the absolute position (100,100)
turtle.goto(100,-100)	#Move turtle to the absolute position (100,-100)
turtle.goto(-100,-100)	#Move turtle to the absolute position (-100,-100)
turtle.up()				#Lift the pen up, no drawing

# Draw an orange circle:
turtle.color("orange")	#Change the color to orange
turtle.goto(0,-100)		#Move turtle to the absolute position (0,-100)
turtle.down()			#Pen is down, drawing now
turtle.circle(100)		#Draw a circle with radius = 100
turtle.up()				#Lift the pen up, no drawing

# Draw a bigger blue square:
turtle.color("blue")	#Change the color to blue
turtle.goto(0,200)		#Move turtle to the absolute position (0,200)
turtle.down()			#Pen is down, drawing now
turtle.goto(200,0)		#Move turtle to the absolute position (200,0)
turtle.goto(0,-200)		#Move turtle to the absolute position (0,-200)
turtle.goto(-200,0)		#Move turtle to the absolute position (-200,0)
turtle.goto(0,200)		#Move turtle to the absolute position (0,200)
turtle.up()				#Lift the pen up, no drawing

# Prints "Hello Turtle!" in green on the screen:
turtle.color("green")	#Change the color to green
turtle.goto(-70,-5)		#Move turtle to the absolute position (-70,-5)
turtle.down()			#Pen is down, drawing now
turtle.write("Hello Turtle!", font=("Arial", 20, "normal")) #Prints the text
                                                            #to screen
turtle.up()				#Lift the pen up, no drawing

turtle.done()			#We've finished with Turtle
