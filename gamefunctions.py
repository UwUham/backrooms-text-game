import random, sys, os, time, combatfunctions as combat #importing various dependencies: general usage
from terminal import arch_start #importing various dependencies: specifics for the Computer puzzle
from credits import credit #importing various dependencies: the credits at the end

room1condition = False  # defining variables for various places in the code including room text and puzzle completion status
room1condition1 = False # defining variables for various places in the code including room text and puzzle completion status
room2entity = True # defining variables for various places in the code including room text and puzzle completion status
room2condition = False # defining variables for various places in the code including room text and puzzle completion status
room3condition = False # defining variables for various places in the code including room text and puzzle completion status
room6condition = False # defining variables for various places in the code including room text and puzzle completion status
room8condition = False # defining variables for various places in the code including room text and puzzle completion status
FirstTime1 = True  # defining variables for various places in the code including room text and puzzle completion status
FirstTime2 = True  # defining variables for various places in the code including room text and puzzle completion status
FirstTime3 = True  # defining variables for various places in the code including room text and puzzle completion status
FirstTime4 = True  # defining variables for various places in the code including room text and puzzle completion status
FirstTime5 = True  # defining variables for various places in the code including room text and puzzle completion status
FirstTime6 = True  # defining variables for various places in the code including room text and puzzle completion status
FirstTime7 = True  # defining variables for various places in the code including room text and puzzle completion status
FirstTime8 = True  # defining variables for various places in the code including room text and puzzle completion status
PuzzleCleared = False  # defining variables for various places in the code including room text and puzzle completion status
DoorUnlocked = False   # defining variables for various places in the code including room text and puzzle completion status
VaultOpen = False  # defining variables for various places in the code including room text and puzzle completion status
Computer = False   # defining variables for various places in the code including room text and puzzle completion status
lobbyfight = False # defining variables for various places in the code including room text and puzzle completion status
switch = True  # defining variables for various places in the code including room text and puzzle completion status
roomstate = [1, 1] # defining variables for various places in the code including room text and puzzle completion status
pg13 = ""  # defining variables for various places in the code including room text and puzzle completion status

room1items = [] # defining lists that represent dropped items in all the rooms
room2items = [] # defining lists that represent dropped items in all the rooms
room3items = [] # defining lists that represent dropped items in all the rooms
room4items = [] # defining lists that represent dropped items in all the rooms
room5items = [] # defining lists that represent dropped items in all the rooms
room6items = [] # defining lists that represent dropped items in all the rooms
room7items = [] # defining lists that represent dropped items in all the rooms
room8items = [] # defining lists that represent dropped items in all the rooms
room9items = [] # defining lists that represent dropped items in all the rooms

names = ["Olivia", "Noah", "Emma", "Amelia", "Oliver", "Ava", "Elijah", "Sophia", "Lucas", "Charlotte", "Mason", "Isabella", "Levi", "Mia", "Asher", "Luna", "James", "Harper", "Mateo", "Evelyn", "Aiden", "Gianna", "Benjamin", "Aria", "Logan", "Ella", "Leo", "Ellie", "Wyatt"] # a list of possible names for enemy entities

platform = sys.platform # defining the command to clear the screen dependent on the end user's operating system.
if platform == "linux" or platform == "linux2" or platform == "darwin": # defining the command to clear the screen dependent on the end user's operating system.
    clearcmd = "clear" # defining the command to clear the screen dependent on the end user's operating system.
elif platform == "win32": # defining the command to clear the screen dependent on the end user's operating system.
    clearcmd = "cls" # defining the command to clear the screen dependent on the end user's operating system.

def clear(): # assigning the clear command to a function
    os.system(clearcmd) # assigning the clear command to a function

def itemappend(name): # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
    if roomstate[0] == 1: # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
        room1items.append(name) # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
    elif roomstate[0] == 2: # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
        room2items.append(name) # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
    elif roomstate[0] == 3: # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
        room3items.append(name) # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
    elif roomstate[0] == 4: # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
        room4items.append(name) # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
    elif roomstate[0] == 5: # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
        room5items.append(name) # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
    elif roomstate[0] == 6: # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
        room6items.append(name) # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
    elif roomstate[0] == 7: # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
        room7items.append(name) # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
    elif roomstate[0] == 8: # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
        room8items.append(name) # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
    elif roomstate[0] == 9: # creating a drop system based on the current room: this function is made more to communicate with another file than anything.
        room9items.append(name) # creating a drop system based on the current room: this function is made more to communicate with another file than anything.

def clrprint(text): # assigning the clear command to another funtion that I will use frequently: clearing the screen and immediately printing something.
    os.system(clearcmd) # assigning the clear command to another funtion that I will use frequently: clearing the screen and immediately printing something.
    print(text) # assigning the clear command to another funtion that I will use frequently: clearing the screen and immediately printing something.

def command(query): # this is where all the magic happens. It contains almost every command used in the game and controls everything.
    global FirstTime8, room1items, room2items, room3items, room4items, room5items, room6items, room7items, room8items, room9items, room1condition, switch, room1condition1, room2condition, room2entity, room3condition, room8condition, room6condition, FirstTime1, FirstTime2, FirstTime3, FirstTime4, FirstTime5, FirstTime6, FirstTime7, PuzzleCleared, DoorUnlocked, VaultOpen, lobbyfight, Computer # i'm not sure if something like "global *" would have worked at all but now that it's been written there's not much point in changing it.
    ask = input(query).lower() # this turns the written command into a variable.
    if ask == "help": # help command: displays a message with all available commands.
        help = open("help.txt", "r") # open a file containing all the commands
        clrprint(help.read()) # print the contents of the file
        help.close() # close the file
        input("Press ENTER to continue.") # wait for user input before continuing: this is better than waiting a set amount of time because the user can leave the game on and come back later without missing anything.
    elif ask == "map": # command to look at the map
        room = open("./roommaps/room" + str(roomstate[1]) + "-" + str(roomstate[0]) + ".txt", "r") # choose and open a file specific to your current room and visited rooms
        clrprint(room.read()) # print the contents of the map file
        room.close() # close the file
        input("Press ENTER to continue.") # wait for user input
    elif ask.startswith("take"): # command to pick up items. this is a very inefficient method of doing this but it works and that is enough for me.
        if roomstate[0] == 1: # check what room the user is in
            if ask[5:] in room1items: # check if the contents of end of the message have been dropped on the floor
                combat.bagadd(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                clrprint("Took the " + ask[5:] + ".") # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                room1items.remove(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                switch = True # tell the code that we took the item off the floor and it does not need to search the room for the item
        elif roomstate[0] == 2: # check what room the user is in
            if ask[5:] in room2items: # check if the contents of end of the message have been dropped on the floor
                combat.bagadd(ask[5:])  # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                clrprint("Took the " + ask[5:] + ".") # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                room2items.remove(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                switch = True  # tell the code that we took the item off the floor and it does not need to search the room for the item
        elif roomstate[0] == 3: # check what room the user is in
            if ask[5:] in room3items: # check if the contents of end of the message have been dropped on the floor
                combat.bagadd(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                clrprint("Took the " + ask[5:] + ".") # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                room3items.remove(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                switch = True  # tell the code that we took the item off the floor and it does not need to search the room for the item
        elif roomstate[0] == 4: # check what room the user is in
            if ask[5:] in room4items: # check if the contents of end of the message have been dropped on the floor
                combat.bagadd(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                clrprint("Took the " + ask[5:] + ".") # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                room4items.remove(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                switch = True # tell the code that we took the item off the floor and it does not need to search the room for the item
        elif roomstate[0] == 5: # check what room the user is in
            if ask[5:] in room5items: # check if the contents of end of the message have been dropped on the floor
                combat.bagadd(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                clrprint("Took the " + ask[5:] + ".") # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                room5items.remove(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                switch = True  # tell the code that we took the item off the floor and it does not need to search the room for the item
        elif roomstate[0] == 6: # check what room the user is in 
            if ask[5:] in room6items: # check if the contents of end of the message have been dropped on the floor
                combat.bagadd(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                clrprint("Took the " + ask[5:] + ".") # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                room6items.remove(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                switch = True  # tell the code that we took the item off the floor and it does not need to search the room for the item
        elif roomstate[0] == 7: # check what room the user is in
            if ask[5:] in room7items: # check if the contents of end of the message have been dropped on the floor
                combat.bagadd(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                clrprint("Took the " + ask[5:] + ".") # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                room7items.remove(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                switch = True  # tell the code that we took the item off the floor and it does not need to search the room for the item
        elif roomstate[0] == 8: # check what room the user is in
            if ask[5:] in room8items: # check if the contents of end of the message have been dropped on the floor
                combat.bagadd(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                clrprint("Took the " + ask[5:] + ".") # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                room8items.remove(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                switch = True  # tell the code that we took the item off the floor and it does not need to search the room for the item
        elif roomstate[0] == 9: # check what room the user is in
            if ask[5:] in room2items: # check if the contents of end of the message have been dropped on the floor
                combat.bagadd(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                clrprint("Took the " + ask[5:] + ".") # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                room2items.remove(ask[5:]) # put the dropped item in the bag, take it off the floor, and tell the user that the above things have been done.
                switch = True # tell the code that we took the item off the floor and it does not need to search the room for the item
        if switch == False: # check if the code did not tell itself not to search the room
            if roomstate[0] == 1: # checking if the user is in the correct room to take an item
                if ask.endswith("blunt knife") and room1condition == False: # check if the specified item is in the room and it has not already been picked up
                    clrprint("Took the blunt knife.") # take the item, and tell the code that the item has already been picked up.
                    combat.bagadd("blunt knife") # take the item, and tell the code that the item has already been picked up.
                    room1condition = True # take the item, and tell the code that the item has already been picked up.
                if ask.endswith("cube") and room1condition1 == False: # check if the specified item is in the room and it has not already been picked up
                    clrprint("Took the cube.") # take the item, and tell the code that the item has already been picked up.
                    combat.bagadd("mysterious cube") # take the item, and tell the code that the item has already been picked up.
                    room1condition1 = True # take the item, and tell the code that the item has already been picked up.
            elif roomstate[0] == 2: # checking if the user is in the correct room to take an item
                if ask.endswith("key") and room2condition == False: # check if the specified item is in the room and it has not already been picked up
                    clrprint("Took the key.") # take the item, and tell the code that the item has already been picked up.
                    combat.bagadd("key") # take the item, and tell the code that the item has already been picked up.
                    room2condition = True # take the item, and tell the code that the item has already been picked up.
            elif roomstate[0] == 3: # checking if the user is in the correct room to take an item
                if ask.endswith("kitchen knife") and room3condition == False: # check if the specified item is in the room and it has not already been picked up
                    clrprint("Took the kitchen knife.") # take the item, and tell the code that the item has already been picked up.
                    combat.bagadd("kitchen knife") # take the item, and tell the code that the item has already been picked up.
                    room3condition = True # take the item, and tell the code that the item has already been picked up.
            elif roomstate[0] == 8: # checking if the user is in the correct room to take an item
                if ask.endswith("scalpel") and room8condition == False: # check if the specified item is in the room and it has not already been picked up
                    clrprint("Took the scalpel.") # take the item, and tell the code that the item has already been picked up.
                    combat.bagadd("scalpel") # take the item, and tell the code that the item has already been picked up.
                    room8condition = True # take the item, and tell the code that the item has already been picked up.
            elif roomstate[0] == 6: # checking if the user is in the correct room to take an item
                if ask.endswith("usb") and room6condition == False and Computer == True: # check if the specified item is in the room and it has not already been picked up and the puzzle relevant has been completed (also this is for a secret item that there is no hint for in the game.)
                    clrprint("You found a 2GB USB drive plugged into the pc. It looks like this is what was holding the distribution of Backrooms Linux that you used earlier. Maybe you can weaponise this to make somethitng a little bit easier later...") # take the item, and tell the code that the item has already been picked up.
                    combat.bagadd("usb") # take the item, and tell the code that the item has already been picked up.
                    room6condition = True # take the item, and tell the code that the item has already been picked up.
            else: # check if the item is not in the room and has not been dropped
                clrprint("That item is not here!") # tell the user that the item is not available
        switch = False # reset the drop system so that the code can be told again
        input("Press ENTER to continue.") # wait for user input
    elif ask == "what" or ask == "look": #  command to call a descriptive analysis of the room you are in
        meta = open("./roommaps/meta.txt", "r") # open a file containing all the metadata for rooms.
        for i in meta: # cycle through every line in the file
            if i.startswith("room" + str(roomstate[0])): # until you find one that corresponds to the correct room
                clrprint(i[7:-1])
        meta.close()
        input("Press ENTER to continue.") # wait for user input
        if roomstate[0] == 4 and lobbyfight == False: # start of first fight, ensuring that the fight has not been completed already
            combat.combat(random.choice(names), "entity tentacle", 40) # randomising the name and starting the combat sequence, including the statistics for the entity weapon
            lobbyfight = True # changes the variable so that the fight is not repeated if the player enters the lobby with the same roomstate
        elif lobbyfight == True and roomstate[0] == 4: # starts the sequence of events that happens after you finish the fight, and if you re-enter the room without changing the roomstate. 
            clrprint("The entity fades in front of you, as though simply looking at you killed them.") # prints out the text explaining that you have beaten the entity and then clears it afterwards
            input("Press ENTER to continue.") # wait for user input
    elif ask == "bag": # runs the sequence that starts when the player inputs the bag command
        combat.weapons() # calls the weapon function from the combat file
    elif ask == "bedroom": # moves the player into the bedroom
        if roomstate[0] == 2: # checks to see if the room has been entered before
            roomstate[0] = 1 # moves the player back into room one
            clrprint("Bedroom") # prints the text and then clears it afterwards
            input("Press ENTER to continue.") # wait for user input
    elif ask == "corridor": # moves the player into the corridor
        if roomstate[0] == 1 or roomstate[0] == 3: # checks to see if the player is in either of the rooms that can access the lobby (the rooms right next to the lobby)
            roomstate[0] = 2 # moves the player back into the second room which is the corridor
            if FirstTime1 == True: # checks to see if this is the first time that the plyer has entered the room, and if that is the case then starts sequence
                roomstate[1] = roomstate[0] # increases the count of how many rooms the player has discovered
                FirstTime1 = False # changes the variable so that if the player enters the room again, the text is not displayed again
                dialogue = open("./dialogue.txt", "r") # opens the file that contains dialouge
                print(dialogue.readline()) # cycles through each line of the text file to the correct line
                print(dialogue.readline()) # cycles through each line of the text file to the correct line
                clrprint(dialogue.readline()) # cycles through each line of the text file to the correct line
                input("Press ENTER to continue.") # wait for user input
                print(dialogue.readline()) # cycles through each line of text file to the correct line
                clrprint(dialogue.readline()) # prints the correct line of text and then clears it
                dialogue.close() # closes the files that contains dialouge
            else: # if the player is not here for their first time, then this starts the sequence below
                clrprint("Corridor") # prints corridor and then clears the text
            input("Press ENTER to continue.") # wait for user input
        else: # if the player is not in either roomstate 1 or 3, then this starts the sequence below
            clrprint("You can't get there from here.") # prints the text and then clears it
            input("Press ENTER to continue.") # wait for user input
    elif ask == "lobby": # moves the player into the lobby
        if room2entity == True: # checks to see if the entity in room 2 exists, if it does then starts the sequence below
            combat.combat(random.choice(names), "entity fist", 50) # randomsing the name and starting the combat sequence including the statistics for the entity weapon
            room2entity = False # changes the variable to false so that you don' fight the same enemy again
        if roomstate[0] == 2 or roomstate[0] == 4: # checks to see if the player is in either of the rooms that can access the lobby (the rooms right next to the lobby)
            roomstate[0] = 3 # moves the player into room 3
            if FirstTime2 == True: # checks to see if this is the players first time going into the room, if it is, then this starts the sequence below
                roomstate[1] = roomstate[0] # increases the count of how many rooms the player has discovered
                FirstTime2 = False # changes the variable to false so that if the player enters the room again, the text is not displayed again
                dialogue = open("./dialogue.txt", "r") # open the dialogue file
                print(dialogue.readline()) # cycling through to the correct line
                print(dialogue.readline()) # cycling through to the correct line
                print(dialogue.readline()) # cycling through to the correct line
                print(dialogue.readline()) # cycling through to the correct line
                print(dialogue.readline()) # cycling through to the correct line
                print(dialogue.readline()) # cycling through to the correct line
                clrprint(dialogue.readline()) # cycling through to the correct line
                input("Press ENTER to continue.") # wait for user input
                print(dialogue.readline()) # cycle through to the correct line
                clrprint(dialogue.readline()) # clear and print the correct line.
                dialogue.close()
            else:
                clrprint("Lobby")
            input("Press ENTER to continue.")
        else:
            clrprint("You can't get there from here.")
            input("Press ENTER to continue.")
    elif ask == "living room":
        if roomstate[0] == 3 or roomstate[0] == 5 or roomstate[0] == 6 or roomstate[0] == 7 or roomstate[0] == 8:
            if DoorUnlocked == True:
                roomstate[0] = 4
                if FirstTime3 == True:
                    roomstate[1] = roomstate[0]
                    FirstTime3 = False
                    dialogue = open("./dialogue.txt", "r")
                    print(dialogue.readline())
                    print(dialogue.readline())
                    print(dialogue.readline())
                    print(dialogue.readline())
                    print(dialogue.readline())
                    print(dialogue.readline())
                    print(dialogue.readline())
                    print(dialogue.readline())
                    print(dialogue.readline())
                    clrprint(dialogue.readline())
                    input("Press ENTER to continue.")
                    print(dialogue.readline())
                    clrprint(dialogue.readline())
                    dialogue.close()
                else:
                    clrprint("Living Room")
                input("Press ENTER to continue.")
            else:
                clrprint("The door is locked, you can't advance yet.")
                input("Press ENTER to continue.")
        else:
            clrprint("You can't get there from here.")
            input("Press ENTER to continue.")
    elif ask == "storage room":
        if roomstate[0] == 4 and lobbyfight == True:
            roomstate[0] = 5
            if FirstTime4 == True:
                roomstate[1] = roomstate[0]
                FirstTime4 = False
                dialogue = open("./dialogue.txt", "r")
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                clrprint(dialogue.readline())
                input("Press ENTER to continue.")
                print(dialogue.readline())
                clrprint(dialogue.readline())
                dialogue.close()
            else:
                clrprint("Storage Room")
            input("Press ENTER to continue.")
        elif lobbyfight == False:
            clrprint("You should probably look around first before you advance.")
            input("Press ENTER to continue.")

        else:
            clrprint("You can't get there from here.")
            input("Press ENTER to continue.")
    elif ask == "office":
        if roomstate[0] == 4 and VaultOpen == True:
            roomstate[0] = 6
            if FirstTime5 == True:
                roomstate[1] = roomstate[0]
                FirstTime5 = False
                dialogue = open("./dialogue.txt", "r")
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                clrprint(dialogue.readline())
                input("Press ENTER to continue.")
                print(dialogue.readline())
                clrprint(dialogue.readline())
                dialogue.close()
            else:
                clrprint("Office")
            input("Press ENTER to continue.")
    elif ask == "hallway":
        print(FirstTime6)
        if roomstate[0] == 4 and Computer == True:
            roomstate[0] = 7
            if FirstTime6 == True:
                roomstate[1] = roomstate[0]
                FirstTime6 = False
                dialogue = open("./dialogue.txt", "r")
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                clrprint(dialogue.readline())
                input("Press ENTER to continue.")
                print(dialogue.readline())
                clrprint(dialogue.readline())
                dialogue.close()
            else:
                clrprint("Hallway")
        elif Computer == False:
            clrprint("The door is locked, you need a keycard to advance.")
            input("Press ENTER to continue.")
    elif ask == "infirmary":
        if roomstate[0] == 7:
            roomstate[0] = 8
            if FirstTime7 == True:
                roomstate[1] = roomstate[0]
                FirstTime7 = False
                dialogue = open("./dialogue.txt", "r")
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                clrprint(dialogue.readline())
                input("Press ENTER to continue.")
                print(dialogue.readline())
                clrprint(dialogue.readline())
                dialogue.close()
            else:
                clrprint("Infirmary")
            input("Press ENTER to continue.")
    elif ask == "demise":
        if roomstate[0] == 8:
            roomstate[0] = 9
            if FirstTime8 == True:
                roomstate[1] = roomstate[0]
                FirstTime8 = False
                dialogue = open("./dialogue.txt", "r")
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                print(dialogue.readline())
                clrprint(dialogue.readline())
                input("Press ENTER to continue.")
                print(dialogue.readline())
                clrprint(dialogue.readline())
                dialogue.close()
            input("Press ENTER to continue.")
            '''LIAM FIGHT'''
            combat.combat("Liam", "baby hand", 10)
            clrprint("After defeating LIAM, he retreats back around the corner... and the next thing you know you are met with THE SYSTEM, an extremely powerful entity who appears to have ten faces scattered in various places aroud the body. Where the head is, you see LIAM's head. Prepare for your final battle.")
            input("Press ENTER to continue.")
            combat.system()
            #finally, the endings
            gameended = False
            if pg13 == True:
                clrprint("The SYSTEM lies in defeat infront of you. A black door fades into existence in front of you, and you know this is your chance to escape. However, having exterminated the entites and finishing THE SYSTEM, the backrooms are a much safer place and you are unsure on whether or not you want to leave.")
                while gameended == False:
                    ending = input("Leave the backrooms? (yes/no) ")
                    if ending == "yes":
                        gameended = True
                        clrprint("You take the door in front of you, radiating a white glow as you exit to finally earn your freedom. You regain conscience in your bedroom, strangely enough exactly where you left, even though days had passed. There are times when you don't feel alone, like fragments of your past remain to haunt you, though with enough time you will be able to let them go. You know that they don't want to leave, but they have no reason to remain either. Your friends? No, they're just memories now. You have to let them go.")
                        input("The end (press ENTER to continue).")
                    elif ending == "no":
                        gameended = True
                        clrprint("The door disintegrates in front of you and you feel at peace, knowing that this was the correct decision. Despite all you've been through, your mission was not to leave the backrooms, but to make them a safer place for you… and the friends you lost a long time ago. You can still feel them near you, and with enough time and assurance that they're safe, they will surely come back. ASHLEY, XEN, HOPE, JAKE, and many others. Your best friends for many years, will be one with you again soon.")
                        input("The end (press ENTER to continue).")
                    else:
                        clrprint("Please select yes or no.")
            elif pg13 == False:
                clrprint("The SYSTEM lies dead infront of you. Your old, blunt knife fades into existence infront of your hand, emitting an ominous black glow, and you know what you must do to escape. However, having exterminated the entites and finishing THE SYSTEM, the backrooms are a much safer place and you are unsure on whether or not you want to leave.")
                while gameended == False:
                    ending = input("Leave the backrooms? (yes/no) ")
                    if ending == "yes":
                        gameended = True
                        clrprint("You ready your blunt knife, with you since day one, and point it towards yourself. Is this really what you have to do to leave? It'll be worth it in the end. Three… Two… It's been done. I suppose I'm not you anymore, but finally one with myself having been presented with the opportunity for freedom. I snap back into reality. The backrooms, my headspace, were always too hostile to fully immerse myself into. I suppose there's a reason for that. I look around, and my room is completely white. It was honestly more vibrant back in the backrooms despite you only having the ability to perceive what you wanted to. I kind of miss that already. I should probably look around and see how everyone's doing. Why is my door locked? What is this mailbox shaped slit in my door for? Oh god. This isn't my life. I don't want to be here, imprisoned in my own home. I want to go back. Take me back right now. Please. Oh no, they're coming. I remember now. Not again.")
                        input("The end (press ENTER to continue).")
                    elif ending == "no":
                        gameended = True
                        clrprint("The knife disintegrates in your hand and you feel at peace, knowing that this was the correct decision. Despite all you've been through, your mission was not to leave the backrooms, but to make them a safer place for you… and the friends you lost a long time ago. You can still feel them near you, and with enough time and assurance that they're safe, they will surely come back. ASHLEY, XEN, HOPE, JAKE, and many others. Your best friends for many years, will be one with you again soon.")
                        input("The end (press ENTER to continue).")
                    else:
                        clrprint("Please select yes or no.")
            '''credits go here'''
            credit()
            time.sleep(1)
            sys.exit()

                    
            
        elif PuzzleCleared == False:
            clrprint("The door is locked.")
    elif ask == "puzzle":
        PuzzleCleared == False
        if roomstate[0] == 3 and DoorUnlocked == False:
            clrprint("Puzzle Section: Lobby")
        elif roomstate[0] == 5 and VaultOpen == False:
            clrprint("Puzzle Section: Storage Room")
        elif roomstate[0] == 6 and Computer == False:
            clrprint("Puzzle Section: Office")
        else:
            PuzzleCleared = True
            clrprint("There's no puzzle to complete here!")
            input("Press ENTER to continue.")
        while PuzzleCleared == False:
            puzzle_ask = input("> ")
            if puzzle_ask == "help":
                clrprint('''inspect - recieve a description on the puzzle.
                exit - step away from the puzzle and come back later.
                hint - gives you a hint if one is available.''')
                input()
            elif puzzle_ask == "exit":
                clrprint("You step away from the puzzle and return to exploration.")
                input("Press ENTER to continue.")
                break
            elif roomstate[0] == 3:
                if "mind" in puzzle_ask.lower():
                    cleartext = open('./roommaps/puzzles.txt', "r")
                    print(cleartext.readline())
                    clrprint(cleartext.readline())
                    PuzzleCleared = True
                    DoorUnlocked = True
                elif puzzle_ask == "inspect":
                    clrprint("You are presented with a cube, and although it looks completely smooth at first, if you squint your eyes you can just make out a faint enscription: \"WHAT STATE CAN YOU LEAVE OR ENTER WITHOUT CHANGING YOUR ADDRESS?\"")
                elif puzzle_ask == "hint":
                    clrprint("You rack your *mind* but in your current state you can't think of anything.")
            elif roomstate[0] == 5:
                if puzzle_ask == "inspect":
                    clrprint("You see a vault with a digital keypad and a 4-length lcd screen and can safely assume that inputting a 4 digit code will unlock the vault.")
                    combat.PlayerIsHoldingKitchenKnifeForJoesBirthdayIn1982("You see a cutting board, and think back to the kitchen knife you saw earlier. Maybe you need it here?")
                elif "1982" in puzzle_ask:
                    cleartext = open('./roommaps/puzzles.txt', "r")
                    print(cleartext.readline())
                    print(cleartext.readline())
                    print(cleartext.readline())
                    clrprint(cleartext.readline())
                    PuzzleCleared = True
                    VaultOpen = True
                elif puzzle_ask == "hint":
                    clrprint("The Kitchen Knife shall cut a path through the dark puzzle...")
            elif roomstate[0] == 6:
                if puzzle_ask == "inspect":
                    clrprint("In the office there is a singular computer, and although it is rather old you feel a strange amount of power coming out of it. On the desk there is a sticky note, and handwritten on it in black marker it says \"Install the 'neofetch' package and run it.\" You feel like this is your final challenge before your first and only chnce of escape.")
                    input("Press ENTER to continue.")
                    choice = input("Ready to turn on the computer? (yes/no) ")
                    if choice.lower() == 'yes':
                        clear()
                        arch_start()
                        input("Press ENTER to continue.")
                        clrprint("Seeing the screen flash to life fills you with determination. Back in the living room, you hear a door fly open.")
                        input("Press ENTER to continue.")
                        Computer = True
                        break
                    elif puzzle_ask == "hint":
                        clrprint("You should inspect the computer in closer detail...")
            else:
                clrprint("That's not the answer.")
            input("Press ENTER to continue.")
            clear()
        PuzzleCleared = False

    elif ask == "sleep":
        if roomstate[0] == 1 or roomstate[0] == 8:
            combat.heal()
        else:
            clrprint("There's no bed to sleep on here!")
            input("Press ENTER to continue.")

    elif ask.startswith("drop"):
        combat.drop(ask[5:])
    
    else:
        clrprint("Unknown action. Try \"help\".")
        input("Press ENTER to continue.")


    clear()
    command("> ")

def start():
    global pg13
    clrprint('''DISCLAIMER
    This game contains themes not suitable for immature audiences.''')
    loop = 0
    while loop == 0:
        pg13 = input("Enter PG13 mode? (yes/no) ").lower()
        if pg13 == "yes":
            pg13 = True
            loop = 1
        elif pg13 == "no":
            pg13 = False
            loop = 1
        else:
            clrprint("Please select an option.")
        
    dialogue = open("./dialogue.txt", "r")
    clrprint(dialogue.readline())
    clrprint(dialogue.readline())
    dialogue.close()
    command("\033[0;37;40m > ")
