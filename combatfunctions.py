import sys, os, random, time, gamefunctions as game, json

names = ["Olivia", "Noah",
"Emma", "Liam",
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

weaponatkstat = {
    "blunt knife": 5#,
}

weaponsinBag = ["blunt knife", "shovel", "power of friendship"]
weaponinHand = ["double ended dildo"]

def bagadd(item):
    if len(weaponsinBag) == 3:
        game.clrprint("Not enough space for this item.")
    elif len(weaponsinBag) > 3:
        game.clrprint("How did you even get this many items? Pick a number, from 0 to", len(weaponsinBag) - 1,  "and we'll remove that item, and that'll repeat until you have three items again.")
        while len(weaponsinBag) > 3:
            num = input("> ")
            weaponsinBag.pop(num)
    else:
        weaponsinBag.append(item)

def fight():
    firstgoer = random.randint(0, 2)
    handweapon = weaponinHand[0]
    index = random.randrange(1.0, 3.0)
    
    if firstgoer == 0:
        game.clrprint("YOU attack first!")
        time.sleep(0.7)
        print("Attacked with", handweapon.upper(), "for", int(index * int(weaponatkstat[handweapon])), "damage!")
        if index == 2.0:
            print("Critical hit!")
        input("Press ENTER to continue")
    else:
        print("lol u lost")
        input("Press ENTER to continue")


def weapons():
    game.clrprint("You have:")
    for i in weaponsinBag:
        print(i)
    print("Items in bag: " + str(len(weaponsinBag)))
    choice = input("Select a weapon (any weapon that was listed or none): ").lower()
    if choice == weaponsinBag[0].lower():
        choicenum = 0
    elif choice == weaponsinBag[1].lower():
        choicenum = 1
    elif choice == weaponsinBag[2].lower():
        choicenum = 2
    handweapon = weaponinHand[0]
    weaponinHand.append(weaponsinBag[choicenum])
    weaponsinBag.append(weaponinHand[0])
    weaponinHand.pop(0)
    weaponsinBag.pop(choicenum)
    game.clrprint("Placed the " + handweapon + " back in the bag!")
    handweapon = weaponinHand[0]
    time.sleep(0.7)
    print("Pulled out the", handweapon + "!")
    input("Press ENTER to continue")
         

def defend():
    print()

weapons()
fight()
fight()
fight()
fight()
fight()