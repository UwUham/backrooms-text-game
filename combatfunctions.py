global damagedealt, damagetaken, YourHP
damagedealt = 0
damagetaken = 0
YourHP = 100

import sys, os, random, time, gamefunctions as game


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

weaponatkstat = {
    "blunt knife": 5,
    "entity fist": 10,
    "shield": 0,
    "lightsaber": 10,
    "key": 0,
    "kitchen knife": 20,
    "entity tentacle": 30
}

weapondefstat = {
    "blunt knife": 15,
    "entity fist": 10,
    "shield": 10,
    "lightsaber": 1,
    "key": 0,
    "kitchen knife": 15,
    "entity tentacle": 5
}


weaponsinBag = []
weaponinHand = []

def bagadd(item):
    if len(weaponsinBag) == 3:
        game.clrprint("Not enough space for this item.")
    elif len(weaponsinBag) > 3:
        game.clrprint("How did you even get this many items? Pick a number, from 0 to", len(weaponsinBag) - 1,  "and we'll remove that item, and that'll repeat until you have three items again.")
        while len(weaponsinBag) > 3:
            num = input("> ")
            if num.isdigit():
                num = int(num)
                weaponsinBag.pop(num)
            else:
                print("Nice try, but no. Quit messing with the game and pay the price.")
    else:
        weaponsinBag.append(item)

def fight(entityName, entityWeapon):
    global damagetaken, damagedealt
    firstgoer = random.randint(0, 2)
    handweapon = weaponinHand[0]
    index = random.randrange(1.0, 3.0)
    
    if firstgoer == 0:
        game.clrprint("YOU attack first!")
        time.sleep(0.7)
        print("Attacked with", handweapon.upper(), "for", int(index * int(weaponatkstat[handweapon])), "damage!")
        damagedealt = weaponatkstat[handweapon]
        if index == 2.0:
            print("Critical hit!")
            damagedealt = int(weaponatkstat[handweapon]) * 2
        input("Press ENTER to continue")
        index = random.randrange(1, 3)
        game.clrprint(entityName.upper() + " attacks!")
        time.sleep(0.7)
        print(entityName.upper(), "attacks with", entityWeapon.upper(), "for", int(index * int(weaponatkstat[entityWeapon])), "damage!")
        damagetaken = weaponatkstat[entityWeapon]
        if index == 2:
            print("Critical hit!")
            damagetaken = weaponatkstat[entityWeapon] * 2
        input("Press ENTER to continue")
    else:
        game.clrprint(entityName.upper() + " attacks first!")
        time.sleep(0.7)
        print(entityName.upper(), "attacks with", entityWeapon.upper(), "for", int(index * int(weaponatkstat[entityWeapon])), "damage!")
        damagetaken = weaponatkstat[entityWeapon]
        if index == 2.0:
            print("Critical hit!")
            damagetaken = weaponatkstat[entityWeapon] * 2
        input("Press ENTER to continue")
        index = random.randrange(1, 3)
        game.clrprint("YOU attack!")
        time.sleep(0.7)
        print("Attacked with", handweapon.upper(), "for", int(index * int(weaponatkstat[handweapon])), "damage!")
        damagedealt = weaponatkstat[handweapon]
        if index == 2:
            print("Critical hit!")
            damagedealt = weaponatkstat[handweapon] * 2
        input("Press ENTER to continue")
    game.clear()


def weapons():
    if len(weaponsinBag) != 0:
        swap = True
        game.clrprint("You have:")
        for i in weaponsinBag:
            print(i)
        print("Items in bag: " + str(len(weaponsinBag)))
        choice = input("Select an item (any weapon that was listed or none): ").lower()
        if choice == weaponsinBag[0].lower():
            choicenum = 0
        elif len(weaponsinBag) >= 2:
            if choice == weaponsinBag[1].lower():
                choicenum = 1
        elif len(weaponsinBag) >= 3:    
            if choice == weaponsinBag[2].lower():
                choicenum = 2
        elif choice == "none":
            swap = False
        else:
            print("Not a valid choice.")
            swap = False
        if swap == True:
            if len(weaponinHand) == 1:
                handweapon = weaponinHand[0]
                weaponinHand.append(weaponsinBag[choicenum])
                weaponsinBag.append(weaponinHand[0])
                weaponinHand.pop(0)
                weaponsinBag.pop(choicenum)
                game.clrprint("Placed the " + handweapon + " back in the bag!")
                handweapon = weaponinHand[0]
                time.sleep(0.7)
                print("Pulled out the", handweapon + "!")
            elif len(weaponinHand) == 0:
                weaponinHand.append(weaponsinBag[choicenum])
                weaponsinBag.pop(0)
                handweapon = weaponinHand[0]
                time.sleep(0.7)
                print("Pulled out the", handweapon + "!")
    else:
        game.clrprint("Your bag is empty!")
    input("Press ENTER to continue.")
    game.clear()
         

def defend(entityName, entityWeapon):
    global damagedealt, damagetaken
    if weapondefstat[weaponinHand[0]] > weaponatkstat[entityWeapon]:
        damagedealt = weaponatkstat[entityWeapon]/2
        damagetaken = 0
        game.clrprint("Fully defended against " + entityName + " and reflected " + str(damagedealt) + " damage back.")
    elif weapondefstat[weaponinHand[0]] <= int(weaponatkstat[entityWeapon])/2:
        damagetaken = weaponatkstat[entityWeapon]
        damagedealt = 0
        game.clrprint("Defense failed, " + str(damagetaken) + " damage taken.")
    else:
        damagetaken = weaponatkstat[entityWeapon]/2
        damagedealt = 0
        game.clrprint("Defended against " + entityName + " partially and took " + damagetaken + " damage.")

def combat(entityName, entityWeapon, entityHP):
    global YourHP
    game.clrprint(entityName.upper() + " wants to fight!")
    while entityHP > 0 and YourHP > 0:
        print("What would you like to do? (fight, defend, weapons, help)")
        print("Your health: " + str(YourHP))
        print("Entity health: " + str(entityHP))
        run = input("> ")
        if run == "help":
            print('''
fight - attack the entity.\n
defend - protect yourself from the entity.\n
weapons - switch your held weapon with one in your bag (if available)\n''')
            input("Press ENTER to continue.")
            game.clear()
        elif run == "fight":
           fight(entityName, entityWeapon)
           entityHP = entityHP - damagedealt
           YourHP = YourHP - damagetaken
        elif run == "defend":
           defend(entityName, entityWeapon)
           entityHP = entityHP - damagedealt
           YourHP = YourHP - damagetaken
           input("Press ENTER to continue.")
           game.clear()
        elif run == "weapons":
           weapons()
        else:
            print("Not a valid choice.")
            input("Press ENTER to continue.")
            game.clear()
    if entityHP <= 0:
        game.clrprint("Successfully defeated " + entityName.upper() + "!")
    elif YourHP <= 0:
        game.clrprint("Defeated by " + entityName.upper() + "!")
        lost = True
    if YourHP < 30:
        print("Health restored to 30!")
        YourHP = 30
    if entityHP <= 0:
        input("Press ENTER to continue.")
    elif lost == True:
        input("Press ENTER to try again.")
        lost = False
        YourHP = 100
        combat(entityName, entityWeapon, entityHP)