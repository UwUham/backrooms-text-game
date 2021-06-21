import sys, os, combatfunctions as combat
global room1condition
room1condition = False
roomstate = [1, 1]
platform = sys.platform
help = open("help.txt", "r")
print(platform)


if platform == "linux" or platform == "linux2" or platform == "darwin":
    clearcmd = "clear"
elif platform == "win32" or platform == "win64":
    clearcmd = "cls"

def clrprint(text):
    os.system(clearcmd)
    print(text)

def roomnumchange(x):
    global roomnum
    roomnum = x

def clear():
    os.system(clearcmd)

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
    elif ask.startswith("take"):
        global room1condition
        if roomstate[0] == 1:
            if ask.endswith("blunt knife") and room1condition == False:
                clrprint("Took the blunt knife.")
                combat.bagadd("blunt knife")
                room1condition = True
    elif ask == "what" or ask == "look":
        meta = open("./roommaps/meta.txt", "r")
        for i in meta:
            if i.startswith("room" + roomstate[0]) and room1condition == False:
                print(i[6:])
    command("> ")