import sys, os, combatfunctions as combat
room1condition = False
room1condition1 = False
room2condition = False
room3condition = False
roomstate = [1, 1]
help = open("help.txt", "r")

platform = sys.platform
print(platform)
if platform == "linux" or platform == "linux2" or platform == "darwin":
    clearcmd = "clear"
elif platform == "win32" or platform == "win64":
    clearcmd = "cls"

def clear():
    os.system(clearcmd)

def clrprint(text):
    os.system(clearcmd)
    print(text)



def roomstatechange(x):
    global roomstate
    roomstate = x

def command(query):
    ask = input(query)
    if ask == "help": #help command
        clrprint(help.read())
    elif ask == "map": # command to look at the map
        room = open("./roommaps/room" + str(roomstate[0]) + "-" + str(roomstate[1]) + ".txt", "r")
        clrprint(room.read())
        room.close()
    elif ask.startswith("take"): #command to pick up items
        global room1condition, room1condition1, room2condition, room3condition
        if roomstate[0] == 1: #handlers for individual rooms: eg room1
            if ask.endswith("blunt knife") and room1condition == False:
                clrprint("Took the blunt knife.")
                combat.bagadd("blunt knife")
                room1condition = True
            if ask.endswith("cube") and room1condition1 == False:
                clrprint("Took the cube.")
                combat.bagadd("mysterious cube")
                room1condition1 = True
        if roomstate[0] == 2: #same but for room2
            if ask.endswith("key") and room2condition == False:
                clrprint("Took the key.")
                combat.bagadd("key")
                room2condition = True
        if roomstate[0] == 3: #same but for room3
            if ask.endswith("kitchen knife") and room3condition == False:
                clrprint("Took the kitchen knife.")
                combat.bagadd("kitchen knife")
                room3condition = True
    elif ask == "what" or ask == "look":
        meta = open("./roommaps/meta.txt", "r")
        for i in meta:
            if i.startswith("room" + str(roomstate[0])) and room1condition == False:
                clrprint(i[7:-1])
    elif ask == "bag":
        combat.weapons()
    command("> ")

def start():
    dialogue = open("./dialogue.txt", "r")
    clrprint(dialogue.readline())
    clrprint(dialogue.readline())
    command("> ")