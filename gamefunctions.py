import random, sys, os, combatfunctions as combat
from terminal import arch_start
room1condition = False
room1condition1 = False
room2entity = True
room2condition = False
room3condition = False
FirstTime1 = True
FirstTime2 = True
FirstTime3 = True
FirstTime4 = True
FirstTime5 = True
FirstTime6 = True
FirstTime7 = True
PuzzleCleared = False
DoorUnlocked = False
VaultOpen = False
Computer = False
lobbyfight = False
roomstate = [1, 1]
help = open("help.txt", "r")

names = ["Olivia", "Noah",
"Emma",
"Amelia", "Oliver",
"Ava", "Elijah",
"Sophia", "Lucas",
"Charlotte", "Mason",
"Isabella", "Levi",
"Mia", "Asher",
"Luna", "James",
"Harper", "Mateo",
"Evelyn", "Aiden",
"Gianna", "Benjamin",
"Aria", "Logan",
"Ella", "Leo",
"Ellie", "Wyatt"
]

platform = sys.platform
if platform == "linux" or platform == "linux2" or platform == "darwin":
    clearcmd = "clear"
elif platform == "win32" or platform == "win64":
    clearcmd = "cls"

def clear():
    os.system(clearcmd)


def clrprint(text):
    os.system(clearcmd)
    print(text)

def command(query):
    global room1condition, room1condition1, room2condition, room2entity, room3condition, FirstTime1, FirstTime2, FirstTime3, FirstTime4, FirstTime5, FirstTime6, FirstTime7, PuzzleCleared, DoorUnlocked, VaultOpen, lobbyfight, Computer
    ask = input(query)
    if ask == "help": #help command
        clrprint(help.read())
        input("Press ENTER to continue.")
    elif ask == "map": # command to look at the map
        room = open("./roommaps/room" + str(roomstate[1]) + "-" + str(roomstate[0]) + ".txt", "r")
        clrprint(room.read())
        room.close()
        input("Press ENTER to continue.")
    elif ask.startswith("take"): #command to pick up items
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
        input("Press ENTER to continue.")
    elif ask == "what" or ask == "look":
        meta = open("./roommaps/meta.txt", "r")
        for i in meta:
            if i.startswith("room" + str(roomstate[0])):
                clrprint(i[7:-1])
        meta.close()
        input("Press ENTER to continue.")
        if roomstate[0] == 4 and lobbyfight == False:
            combat.combat(random.choice(names), "entity tentacle", 40)
            lobbyfight = True
        elif lobbyfight == True and roomstate[0] == 4:
            clrprint("The entity fades in front of you, as though simply looking at you killed them.")
            input("Press ENTER to continue.")
    elif ask == "bag":
        combat.weapons()
    elif ask == "corridor":
        if roomstate[0] == 1 or roomstate[0] == 3:
            roomstate[0] = 2
            if FirstTime1 == True:
                roomstate[1] = roomstate[0]
                FirstTime1 = False
                dialogue = open("./dialogue.txt", "r")
                print(dialogue.readline())
                print(dialogue.readline())
                clrprint(dialogue.readline())
                input("Press ENTER to continue.")
                print(dialogue.readline())
                clrprint(dialogue.readline())
                dialogue.close()
            input("Press ENTER to continue.")
        else:
            clrprint("You can't get there from here.")
            input("Press ENTER to continue.")
    elif ask == "lobby":
        if room2entity == True:
            combat.combat(random.choice(names), "entity fist", 50)
            room2entity = False
        if roomstate[0] == 2 or roomstate[0] == 4:
            roomstate[0] = 3
            if FirstTime2 == True:
                roomstate[1] = roomstate[0]
                FirstTime2 = False
                dialogue = open("./dialogue.txt", "r")
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
            input("Press ENTER to continue.")
    elif ask == "hall":
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
                clrprint(dialogue.readline())
                input("Press ENTER to continue.")
                print(dialogue.readline())
                clrprint(dialogue.readline())
                dialogue.close()
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
                clrprint(dialogue.readline())
                input("Press ENTER to continue.")
                print(dialogue.readline())
                clrprint(dialogue.readline())
                dialogue.close()
            input("Press ENTER to continue.")
    elif ask == "demise":
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
                clrprint(dialogue.readline())
                input("Press ENTER to continue.")
                print(dialogue.readline())
                clrprint(dialogue.readline())
                dialogue.close()
            input("Press ENTER to continue.")
        elif PuzzleCleared == False:
            clrprint("The door is locked.")
    elif ask == "puzzle":
        PuzzleCleared == False
        if roomstate[0] == 3:
            clrprint("Puzzle Section: Lobby")
        if roomstate[0] == 5:
            clrprint("Puzzle Section: Storage Room")
        if roomstate[0] == 6:
            clrprint("Puzzle Section: Office")
        while PuzzleCleared == False:
            puzzle_ask = input("> ")
            if roomstate[0] == 3:
                if "mind" in puzzle_ask.lower():
                    cleartext = open('./roommaps/puzzles.txt', "r")
                    print(cleartext.readline())
                    clrprint(cleartext.readline())
                    PuzzleCleared = True
                    DoorUnlocked = True
                elif puzzle_ask == "inspect":
                    clrprint("You are presented with a cube, and although it looks completely smooth at first, if you squint your eyes you can just make out a faint enscription: \"WHAT STATE CAN YOU LEAVE OR ENTER WITHOUT CHANGING YOUR ADDRESS?\"")
                elif puzzle_ask == "hint":
                    clrprint("You rack your mind but in your current state you can't think of anything.")
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
            elif roomstate[0] == 6:
                if puzzle_ask == "inspect":
                    clrprint("In the office there is a singular computer, and although it is rather old you feel a strange amount of power coming out of it. On the desk there is a sticky note, and handwritten on it in black marker it says \"Install the 'neofetch' package and run it.\" You feel like this is your final challenge before your first and only chnce of escape.")
                    input("Press ENTER to continue.")
                    choice = input("Ready to turn on the computer? (yes/no)")
                    if choice.lower() == 'yes':
                        clear()
                        arch_start()
                        input("Press ENTER to continue.")
                        clrprint("Seeing the screen flash to life fills you with determination. Back in the living room, you hear a door fly open.")
                        Computer == True
            elif puzzle_ask == "exit":
                clrprint("You step away from the puzzle and return to exploration.")
                input("Press ENTER to continue.")
                break
            elif puzzle_ask == "help":
                clrprint('''inspect - recieve a description on the puzzle.
                exit - step away from the puzzle and come back later.
                hint - gives you a hint if one is available.''')
            else:
                clrprint("That's not the answer.")
            input("Press ENTER to continue.")
            clear()
        PuzzleCleared = False

    clear()
    command("> ")

def start():
    dialogue = open("./dialogue.txt", "r")
    clrprint(dialogue.readline())
    clrprint(dialogue.readline())
    dialogue.close()
    command("\033[0;37;40> ")