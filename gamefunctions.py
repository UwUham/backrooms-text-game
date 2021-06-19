import sys, os
roomnum = 1
roomstate = [0, 0, 0, 0]
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
    os.system(clear)

def roomstatechange(x):
    global roomstate
    roomstate = x

def command(query):
    ask = input(query)
    if ask == "help":
        clrprint(help.read())
    elif ask == "look" or ask == "room":
        room = open("./rooms/room" + str(roomnum) + "/room" + str(roomstate[0]) + str(roomstate[1]) + '_' + str(roomstate[2]) + str(roomstate[3]) + ".txt", "r")
        clrprint(room.read())
        room.close()
    elif ask == "what":
        meta = open("./rooms/room" + str(roomnum) + "/meta.txt", "r")
        for line in meta:
            if "room" + str(roomstate[0]) + str(roomstate[1]) + '_' + str(roomstate[2]) + str(roomstate[3]) in line:
                clrprint(line[len(line.split()[0]):-1])
        meta.close()
    elif ask == "u" or ask == "up" or ask == "n" or ask == "forward":
        if roomnum == 1:
            if (roomstate[0] == 3 and roomstate[4] == 0) or (roomstate[0] == 7):
                clrprint("You can't move there.")
            else:
                roomstate[1] = roomstate[1] + 1
                roomstate[3] = 0
    command("> ")