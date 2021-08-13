'''
The credits function is used to create an autoscrolling credits environment.
To contributors:
Steps to add your name in these credits:
1. Create a function named after you, following the other functions as a template.
2. In any area where you contributed, underneath a current contributors name, insert "linecount(1)" and beneath that, your function.
'''
from terminal import clear # importing the required function
from time import sleep # importing the required function

def linecount(num): # defining the linecount function: printing line breaks for a set number of times
    count = 0 # defining count
    while count != num: # while the count is not equal to the specified number
        print("\n") # prints a line break
        sleep(0.2) # wait fro 0.2 seconds
        count = count + 1 # add one to count

def liam(): # defining the liam function, to print liam's name
    print("Liam") # prints my name
    sleep(0.2) # wait for 0.2 seconds

def jaden(): # defining the jaden function, to print jaden's name
    print("Jaden") # prints out jaden
    sleep(0.2) # wait for 0.2 seconds

def credit(): # prints out the credits with autoscroll
    clear() # prints out the credits with autoscroll
    print("The Backrooms - Credits") # prints out the credits with autoscroll
    sleep(0.2) # prints out the credits with autoscroll
    linecount(3) # prints out the credits with autoscroll
    print("Game Planning") # prints out the credits with autoscroll
    sleep(0.2) # prints out the credits with autoscroll
    linecount(3) # prints out the credits with autoscroll
    liam() # prints out the credits with autoscroll
    linecount(1) # prints out the credits with autoscroll
    jaden() # prints out the credits with autoscroll
    linecount(3) # prints out the credits with autoscroll
    print('Story Writing') # prints out the credits with autoscroll
    sleep(0.2) # prints out the credits with autoscroll
    linecount(3) # prints out the credits with autoscroll
    jaden() # prints out the credits with autoscroll
    linecount(1) # prints out the credits with autoscroll
    liam() # prints out the credits with autoscroll
    linecount(3) # prints out the credits with autoscroll
    print("Puzzle Design") # prints out the credits with autoscroll
    sleep(0.2) # prints out the credits with autoscroll
    linecount(3) # prints out the credits with autoscroll
    liam() # prints out the credits with autoscroll
    linecount(3) # prints out the credits with autoscroll
    print("Game Engine") # prints out the credits with autoscroll
    sleep(0.2) # prints out the credits with autoscroll
    linecount(3) # prints out the credits with autoscroll
    jaden() # prints out the credits with autoscroll
    linecount(3) # prints out the credits with autoscroll
    print('Dialogue Authoring') # prints out the credits with autoscroll
    sleep(0.2) # prints out the credits with autoscroll
    linecount(3) # prints out the credits with autoscroll
    jaden() # prints out the credits with autoscroll
    linecount(1) # prints out the credits with autoscroll
    liam() # prints out the credits with autoscroll
    linecount(3) # prints out the credits with autoscroll
    print("Character Design") # prints out the credits with autoscroll
    sleep(0.2) # prints out the credits with autoscroll
    linecount(3) # prints out the credits with autoscroll
    liam() # prints out the credits with autoscroll
    linecount(3) # prints out the credits with autoscroll
    print("Special Thanks") # prints out the credits with autoscroll
    sleep(0.2) # prints out the credits with autoscroll
    linecount(1) # prints out the credits with autoscroll
    print("asciiart.eu") # prints out the credits with autoscroll
    sleep(0.2) # prints out the credits with autoscroll
    linecount(1) # prints out the credits with autoscroll
    print('An anonymous 4chan user') # prints out the credits with autoscroll
    sleep(0.2) # prints out the credits with autoscroll
    linecount(1) # prints out the credits with autoscroll
    print("And YOU for playing this game!") # prints out the credits with autoscroll
    sleep(0.2) # prints out the credits with autoscroll