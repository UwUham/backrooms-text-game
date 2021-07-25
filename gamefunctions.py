import random, sys, os, time, combatfunctions as combat
from terminal import arch_start
from credits import credit

room1condition = False
room1condition1 = False
room2entity = True
room2condition = False
room3condition = False
room6condition = False
room8condition = False
FirstTime1 = True
FirstTime2 = True
FirstTime3 = True
FirstTime4 = True
FirstTime5 = True
FirstTime6 = True
FirstTime7 = True
FirstTime8 = True
PuzzleCleared = False
DoorUnlocked = False
VaultOpen = False
Computer = False
lobbyfight = False
switch = True
roomstate = [1, 1]
pg13 = ""

room1items = []
room2items = []
room3items = []
room4items = []
room5items = []
room6items = []
room7items = []
room8items = []
room9items = []

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
elif platform == "win32":
    clearcmd = "cls"

def clear():
    os.system(clearcmd)

def itemappend(name):
    if roomstate[0] == 1:
        room1items.append(name)
    elif roomstate[0] == 2:
        room2items.append(name)
    elif roomstate[0] == 3:
        room3items.append(name)
    elif roomstate[0] == 4:
        room4items.append(name)
    elif roomstate[0] == 5:
        room5items.append(name)
    elif roomstate[0] == 6:
        room6items.append(name)
    elif roomstate[0] == 7:
        room7items.append(name)
    elif roomstate[0] == 8:
        room8items.append(name)
    elif roomstate[0] == 9:
        room9items.append(name)

def clrprint(text):
    os.system(clearcmd)
    print(text)

def command(query):
    global FirstTime8, room1items, room2items, room3items, room4items, room5items, room6items, room7items, room8items, room9items, room1condition, switch, room1condition1, room2condition, room2entity, room3condition, room8condition, room6condition, FirstTime1, FirstTime2, FirstTime3, FirstTime4, FirstTime5, FirstTime6, FirstTime7, PuzzleCleared, DoorUnlocked, VaultOpen, lobbyfight, Computer
    ask = input(query).lower()
    if ask == "help": #help command
        help = open("help.txt", "r")
        clrprint(help.read())
        help.close()
        input("Press ENTER to continue.")
    elif ask == "map": # command to look at the map
        room = open("./roommaps/room" + str(roomstate[1]) + "-" + str(roomstate[0]) + ".txt", "r")
        clrprint(room.read())
        room.close()
        input("Press ENTER to continue.")
    elif ask.startswith("take"): #command to pick up items
        if roomstate[0] == 1:
            if ask[5:] in room1items:
                combat.bagadd(ask[5:])
                clrprint("Took the " + ask[5:] + ".")
                room1items.remove(ask[5:])
                switch = True
        elif roomstate[0] == 2:
            if ask[5:] in room2items:
                combat.bagadd(ask[5:])
                clrprint("Took the " + ask[5:] + ".")
                room2items.remove(ask[5:])
                switch = True
        elif roomstate[0] == 3:
            if ask[5:] in room3items:
                combat.bagadd(ask[5:])
                clrprint("Took the " + ask[5:] + ".")
                room3items.remove(ask[5:])
                switch = True
        elif roomstate[0] == 4:
            if ask[5:] in room4items:
                combat.bagadd(ask[5:])
                clrprint("Took the " + ask[5:] + ".")
                room4items.remove(ask[5:])
                switch = True
        elif roomstate[0] == 5:
            if ask[5:] in room5items:
                combat.bagadd(ask[5:])
                clrprint("Took the " + ask[5:] + ".")
                room5items.remove(ask[5:])
                switch = True
        elif roomstate[0] == 6:
            if ask[5:] in room6items:
                combat.bagadd(ask[5:])
                clrprint("Took the " + ask[5:] + ".")
                room6items.remove(ask[5:])
                switch = True
        elif roomstate[0] == 7:
            if ask[5:] in room7items:
                combat.bagadd(ask[5:])
                clrprint("Took the " + ask[5:] + ".")
                room7items.remove(ask[5:])
                switch = True
        elif roomstate[0] == 8:
            if ask[5:] in room8items:
                combat.bagadd(ask[5:])
                clrprint("Took the " + ask[5:] + ".")
                room8items.remove(ask[5:])
                switch = True
        elif roomstate[0] == 9:
            if ask[5:] in room2items:
                combat.bagadd(ask[5:])
                clrprint("Took the " + ask[5:] + ".")
                room2items.remove(ask[5:])
                switch = True
        if switch == False:
            if roomstate[0] == 1: #handlers for individual rooms: eg room1
                if ask.endswith("blunt knife") and room1condition == False:
                    clrprint("Took the blunt knife.")
                    combat.bagadd("blunt knife")
                    switch = False
                    room1condition = True
                if ask.endswith("cube") and room1condition1 == False:
                    clrprint("Took the cube.")
                    combat.bagadd("mysterious cube")
                    room1condition1 = True
            elif roomstate[0] == 2: #same but for room2
                if ask.endswith("key") and room2condition == False:
                    clrprint("Took the key.")
                    combat.bagadd("key")
                    room2condition = True
            elif roomstate[0] == 3: #same but for room3
                if ask.endswith("kitchen knife") and room3condition == False:
                    clrprint("Took the kitchen knife.")
                    combat.bagadd("kitchen knife")
                    room3condition = True
            elif roomstate[0] == 8:
                if ask.endswith("scalpel") and room8condition == False:
                    clrprint("Took the scalpel.")
                    combat.bagadd("scalpel")
                    room8condition = True
            elif roomstate[0] == 6:
                if ask.endswith("usb") and room6condition == False and Computer == True:
                    clrprint("You found a 2GB USB drive plugged into the pc. It looks like this is what was holding the distribution of Backrooms Linux that you used earlier. Maybe you can weaponise this to make somethitng a little bit easier later...")
                    combat.bagadd("usb")
                    room6condition = True
            else:
                clrprint("That item is not here!")
        switch = False
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
    elif ask == "bedroom":
        if roomstate[0] == 2:
            roomstate[0] = 1
            clrprint("Bedroom")
            input("Press ENTER to continue.")
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
            else:
                clrprint("Corridor")
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
