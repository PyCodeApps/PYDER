import pyttsx3
import webbrowser
print("© Copyright 2022 Ifeanyi Onuama. All rights reserved")
def speak(audio):
	
	engine = pyttsx3.init()
	# getter method(gets the current value
	# of engine property)
	voices = engine.getProperty('voices')
	
	# setter method .[0]=male voice and
	# [1]=female voice in set Property.
	engine.setProperty('voice', voices[1].id)
	
	# Method for the speaking of the assistant
	engine.say(audio)
	
	# Blocks while processing all the currently
	# queued commands
	engine.runAndWait()
speak("There is a newer version of this application: would you like to open?")
open = input("(yes/no): ")
if open == 'yes':
    webbrowser.open("www.github.com/pycodeapps/pyder-2.0")
    speak("run program again to continue")
    exit()
else:
    speak("Welcome to Pieder 1.0, what would you like to do?")
todo = input("Game(1)\nYoutube(2)\nGoogle(3)\nGoodbye(4):\n")


def snake():
        import time
        import turtle
        import random

        delay = 0.1
        score = 0
        high_score = 0



        # Creating a window screen
        wn = turtle.Screen()
        wn.title("Ifeanyi PYDER Snake Game")
        wn.bgcolor("black")
        # the width and height can be put as user's choice
        wn.setup(width=600, height=600)
        wn.tracer(0)

# head of the snake
        head = turtle.Turtle()
        head.shape("square")
        head.color("white")
        head.penup()
        head.goto(0, 0)
        head.direction = "Stop"

# food in the game
        food = turtle.Turtle()
        colors = random.choice(['red', 'green', 'black'])
        shapes = random.choice(['square', 'triangle', 'circle'])
        food.speed(0)
        food.shape(shapes)
        food.color(colors)
        food.penup()
        food.goto(0, 100)

        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 250)
        pen.write("Score : 0 High Score : 0", align="center",
		font=("candara", 24, "bold"))



# assigning key directions
        def group():
                if head.direction != "down":
                        head.direction = "up"


        def godown():
                if head.direction != "up":
                        head.direction = "down"


        def goleft():
                if head.direction != "right":
                        head.direction = "left"


        def goright():
                if head.direction != "left":
                        head.direction = "right"


        def move():
                if head.direction == "up":
                        y = head.ycor()
                        head.sety(y+20)
                if head.direction == "down":
                        y = head.ycor()
                        head.sety(y-20)
                if head.direction == "left":
                        x = head.xcor()
                        head.setx(x-20)
                if head.direction == "right":
                        x = head.xcor()
                        head.setx(x+20)


		
        wn.listen()
        wn.onkeypress(group, "w")
        wn.onkeypress(godown, "s")
        wn.onkeypress(goleft, "a")
        wn.onkeypress(goright, "d")

        segments = []



        # Main Gameplay
        while True:
                wn.update()
                if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
                        time.sleep(1)
                        head.goto(0, 0)
                        head.direction = "Stop"
                        colors = random.choice(['red', 'blue', 'green'])
                        shapes = random.choice(['square', 'circle'])
                        for segment in segments:
                                segment.goto(1000, 1000)
                        segments.clear()
                        score = 0
                        delay = 0.1
                        pen.clear()
                        pen.write("Score : {} High Score : {} ".format(
                                score, high_score), align="center", font=("candara", 24, "bold"))
                if head.distance(food) < 20:
                        x = random.randint(-270, 270)
                        y = random.randint(-270, 270)
                        food.goto(x, y)

                        # Adding segment
                        new_segment = turtle.Turtle()
                        new_segment.speed(0)
                        new_segment.shape("square")
                        new_segment.color("orange") # tail colour
                        new_segment.penup()
                        segments.append(new_segment)
                        delay -= 0.001
                        score += 10
                        if score > high_score:
                                high_score = score
                        pen.clear()
                        pen.write("Score : {} High Score : {} ".format(
                                score, high_score), align="center", font=("candara", 24, "bold"))
                # Checking for head collisions with body segments
                for index in range(len(segments)-1, 0, -1):
                        x = segments[index-1].xcor()
                        y = segments[index-1].ycor()
                        segments[index].goto(x, y)
                if len(segments) > 0:
                        x = head.xcor()
                        y = head.ycor()
                        segments[0].goto(x, y)
                move()
                for segment in segments:
                        if segment.distance(head) < 20:
                                time.sleep(1)
                                head.goto(0, 0)
                                head.direction = "stop"
                                colors = random.choice(['red', 'blue', 'green'])
                                shapes = random.choice(['square', 'circle'])
                                for segment in segments:
                                        segment.goto(1000, 1000)
                                segment.clear()

                                score = 0
                                delay = 0.1
                                pen.clear()
                                pen.write("Score : {} High Score : {} ".format(
                                        score, high_score), align="center", font=("candara", 24, "bold"))
                time.sleep(delay)

        wn.mainloop()
              

    
def goodbye():
    speak("bye bye")

def google():
    import pywhatkit as kt
    query = input("Search here: ")
    kt.search(query)

def youtube():
    webbrowser.opne("www.youtube.com")

if todo == '1':
    snake()

if todo == '3':
    google()

if todo == '4':
    goodbye()

if todo == '2':
    youtube()
