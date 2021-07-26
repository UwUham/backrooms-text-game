global damagedealt, damagetaken, YourHP # defining variables to be used in combat
damagedealt = 0 # defining variables to be used in combat
damagetaken = 0 # defining variables to be used in combat
YourHP = 100 # defining variables to be used in combat

import random, time, gamefunctions as game # importing required libraries



weaponatkstat = { # defining attack stats for weapons
    "blunt knife": 5, # defining attack stats for weapons
    "entity fist": 10, # defining attack stats for weapons
    "shield": 0, # defining attack stats for weapons
    "lightsaber": 10, # defining attack stats for weapons
    "key": 0, # defining attack stats for weapons
    "kitchen knife": 20, # defining attack stats for weapons
    "entity tentacle": 30, # defining attack stats for weapons
    "baby hand": 0, # defining attack stats for weapons
    "scalpel": 40, # defining attack stats for weapons
    "usb": 999 # defining attack stats for weapons
} # defining attack stats for weapons

weapondefstat = { # defining defense stats for weapons
    "blunt knife": 15, # defining defense stats for weapons
    "entity fist": 10, # defining defense stats for weapons
    "shield": 10, # defining defense stats for weapons
    "lightsaber": 1, # defining defense stats for weapons
    "key": 0, # defining defense stats for weapons
    "kitchen knife": 15, # defining defense stats for weapons
    "entity tentacle": 5, # defining defense stats for weapons
    "baby hand": 1, # defining defense stats for weapons
    "scalpel": 5, # defining defense stats for weapons
    "usb": 999 # defining defense stats for weapons
} # defining defense stats for weapons

weaponflavours = { # creating flavour text for enemy attacks
"entity tentacle": "'s tentacles surround you, and tightly holding you in place the entity manages to get a few valuable hits in", # creating flavour text for enemy attacks
"entity fist": " punches you", # creating flavour text for enemy attacks
"baby hand": " swings with his hand, but due to having undeniably small arms and hands, misses and attacks" # creating flavour text for enemy attacks
} # creating flavour text for enemy attacks

systemnames = ["Fear", # defining names for the final boss
"Anger", # defining names for the final boss
"Disgust", # defining names for the final boss
"Sadness", # defining names for the final boss
"Rage", # defining names for the final boss
"Loneliness", # defining names for the final boss
"Melancholy", # defining names for the final boss
"Annoyance", # defining names for the final boss
"Hate", # defining names for the final boss
"Liam" # defining names for the final boss
] # defining names for the final boss

systemweaponflavour = {"Fear": " swings his terror mace around wildly", # creating flavour texr for the final boss
"Anger": " violently slashes with his angry claws", # creating flavour texr for the final boss
"Disgust": " swings her hand of dissatisfaction at you", # creating flavour texr for the final boss
"Sadness": " projectile cries at you with very sharp tears", # creating flavour texr for the final boss
"Rage": " attempts to impale you with his rage spear but misses", # creating flavour texr for the final boss
"Loneliness": " stabs at you with her knife, but misses and attacks", # creating flavour texr for the final boss
"Melancholy": " sits in silence, menacingly staring at you with peircing eyes", # creating flavour texr for the final boss
"Annoyance": " laughs unbearably loudly, giving you a massive headache and attacking", # creating flavour texr for the final boss
"Hate": " fills you with sorrow, and you forget why you're here in the first place for a second, before you remember and he attacks you", # creating flavour texr for the final boss
"Liam": " swings with his hand, but due to having undeniably small arms and hands, misses and attacks" # creating flavour texr for the final boss
} # creating flavour texr for the final boss

systemweaponatkstats = {"Fear": 10, # defining attack stats for final boss weapons
"Anger": 15, # defining attack stats for final boss weapons
"Disgust": 5, # defining attack stats for final boss weapons
"Sadness": 15, # defining attack stats for final boss weapons
"Rage": 0, # defining attack stats for final boss weapons
"Loneliness": 0, # defining attack stats for final boss weapons
"Melancholy": 5, # defining attack stats for final boss weapons
"Annoyance": 10, # defining attack stats for final boss weapons
"Hate": 20, # defining attack stats for final boss weapons
"Liam": 0} # defining attack stats for final boss weapons


weaponsinBag = [] # creating variables for the bag and the hand
weaponinHand = [] # creating variables for the bag and the hand

def bagadd(item): # create the bagadd function
    if len(weaponsinBag) == 3: # if the bag is full:
        game.clrprint("Not enough space for this item.") # tell the user that the bag is full
    elif len(weaponsinBag) > 3: # check if something has happened eg. editing the game files to have more then 3 items:
        game.clrprint("How did you even get this many items? Pick a number, from 0 to " + len(weaponsinBag) - 1 + " and we'll remove that item, and that'll repeat until you have three items again.") # create a user friendly handler that removes items from the bag until it is normal again.
        while len(weaponsinBag) > 3: # part of the Super Secret Handler that eats your items.
            num = input("> ") # part of the Super Secret Handler that eats your items.
            if num.isdigit(): # part of the Super Secret Handler that eats your items.
                num = int(num) # part of the Super Secret Handler that eats your items.
                weaponsinBag.pop(num) # part of the Super Secret Handler that eats your items.
            else: # if the user does not pick a number:
                print("Nice try, but no. Quit messing with the game and pay the price.") # talk to user
    else: # if nothing is wrong:
        weaponsinBag.append(item) # take the item

def PlayerIsHoldingKitchenKnifeForJoesBirthdayIn1982(var):
    if "kitchen knife" in weaponinHand or "kitchen knife" in weaponsinBag:
        print("You have a kitchen knife with the tag \"Joe's birthday\" on it, and underneath it says 18/8/1982.")
    else:
        print(var)

def heal():
    global YourHP
    YourHP = 100
    game.clrprint("You rested and became fully healthy once again.")
    input("Press ENTER to continue.")

def drop(what):
    global weaponsinBag, weaponinHand
    if what in weaponsinBag:
        weaponsinBag.remove(what)
        game.itemappend(what)
        game.clrprint("Dropped the " + what + ".")
    elif what in weaponinHand:
        weaponinHand.remove(what)
        game.itemappend(what)
        game.clrprint("Dropped the " + what + ".")
    else:
        game.clrprint("You do not have a " + what + " in your inventory!")
    input("Press ENTER to continue.")
        

def fight(entityName, entityWeapon):
    if len(weaponinHand) == 1:
        global damagetaken, damagedealt
        firstgoer = random.randint(0, 2)
        handweapon = weaponinHand[0]
        index = random.randrange(1, 3)

        if firstgoer == 0:
            game.clrprint("YOU attack first!")
            time.sleep(0.7)
            print("Attacked with", handweapon.upper(), "for", int(index * int(weaponatkstat[handweapon])), "damage!")
            damagedealt = weaponatkstat[handweapon]
            if index == 2:
                print("Critical hit!")
                damagedealt = int(weaponatkstat[handweapon]) * 2
            input("Press ENTER to continue")
            index = random.randrange(1, 3)
            game.clrprint(entityName.upper() + " attacks!")
            time.sleep(0.7)
            print(entityName.upper(), weaponflavours[entityWeapon], "for", int(index * int(weaponatkstat[entityWeapon])), "damage!")
            damagetaken = weaponatkstat[entityWeapon]
            if index == 2:
                print("Critical hit!")
                damagetaken = weaponatkstat[entityWeapon] * 2
            input("Press ENTER to continue")
        else:
            game.clrprint(entityName.upper() + " attacks first!")
            time.sleep(0.7)
            print(entityName.upper(), weaponflavours[entityWeapon], "for", int(index * int(weaponatkstat[entityWeapon])), "damage!")
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
    elif len(weaponsinBag) > 0:
        game.clrprint("Select a weapon first.")
    else:
        game.clrprint("You fought without a weapon and lost.")
        damagetaken = 100


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
    if len(weaponinHand) == 1:
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
    elif len(weaponsinBag) > 0:
        game.clrprint("Select a weapon first.")
    else:
        game.clrprint("You fought without a weapon and lost.")
        damagetaken = 100

def combat(entityName, entityWeapon, entityHP):
    global YourHP
    entityHPcache = entityHP
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
        combat(entityName, entityWeapon, entityHPcache)

def sysfight():
    global damagetaken, damagedealt
    damagetaken = 0
    damagedealt = 0
    if len(weaponinHand) == 1:
        firstgoer = random.randint(0, 2)
        handweapon = weaponinHand[0]
        index = random.randrange(1, 3)

        if firstgoer == 0:
            game.clrprint("YOU attack first!")
            time.sleep(0.7)
            print("Attacked with", handweapon.upper(), "for", int(index * int(weaponatkstat[handweapon])), "damage!")
            if index != 2:
                damagedealt = damagedealt + weaponatkstat[handweapon]
            if index == 2:
                print("Critical hit!")
                damagedealt = damagedealt + int(weaponatkstat[handweapon]) * 2
            input("Press ENTER to continue")
            count = 0
            while count <= 2:
                index = random.randrange(1, 3)
                entityName = random.choice(systemnames)
                game.clrprint(entityName.upper() + " attacks!")
                time.sleep(0.7)
                print(entityName.upper(), systemweaponflavour[entityName], "for", int(index * int(systemweaponatkstats[entityName])), "damage!")
                if index != 2:
                    damagetaken = damagetaken + systemweaponatkstats[entityName]
                if index == 2:
                    print("Critical hit!")
                    damagetaken = damagetaken + systemweaponatkstats[entityName] * 2
                input("Press ENTER to continue")
                count = count + 1
        else:
            count = 0
            while count <= 2:
                entityName = random.choice(systemnames)
                game.clrprint(entityName.upper() + " attacks first!")
                time.sleep(0.7)
                print(entityName.upper(), systemweaponflavour[entityName], "for", int(index * int(systemweaponatkstats[entityName])), "damage!")
                if index != 2:
                    damagetaken = damagetaken + systemweaponatkstats[entityName]
                if index == 2:
                    print("Critical hit!")
                    damagetaken =  damagetaken + systemweaponatkstats[entityName] * 2
                input("Press ENTER to continue")
                count = count + 1
            index = random.randrange(1, 3)
            game.clrprint("YOU attack!")
            time.sleep(0.7)
            print("Attacked with", handweapon.upper(), "for", int(index * int(weaponatkstat[handweapon])), "damage!")
            if index != 2:
                damagedealt = damagedealt + weaponatkstat[handweapon]
            if index == 2:
                print("Critical hit!")
                damagedealt = damagedealt + weaponatkstat[handweapon] * 2
            input("Press ENTER to continue")
        game.clear()
    elif len(weaponsinBag) > 0:
        game.clrprint("Select a weapon first.")
    else:
        game.clrprint("You fought without a weapon and lost.")
        damagetaken = 100


def system():
    global YourHP, damagedealt, damagetaken
    entityHP = 210
    entityName = "THE SYSTEM"
    game.clrprint("THE SYSTEM wants to fight!")
    while entityHP > 0 and YourHP > 0:
        print("What would you like to do? (fight, defend, weapons, help)")
        print("Your health: " + str(YourHP))
        print("THE SYSTEM health: " + str(entityHP))
        run = input("> ")
        if run == "help":
            print('''
fight - attack the entity.\n
defend - protect yourself from the entity.\n
weapons - switch your held weapon with one in your bag (if available)\n''')
            input("Press ENTER to continue.")
            game.clear()
        elif run == "fight":
            sysfight()
            entityHP = entityHP - damagedealt
            YourHP = YourHP - damagetaken
            damagedealt = 0
            damagetaken = 0
        elif run == "defend":
            game.clrprint("You can't defend against multiple entities at once!")
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
        if YourHP < 30:
            print("Health restored to 30!")
            YourHP = 30
    elif YourHP <= 0:
        game.clrprint("Defeated by " + entityName.upper() + "!")
        lost = True
    if entityHP <= 0:
        input("Press ENTER to continue.")
    elif lost == True:
        input("Press ENTER to try again.")
        lost = False
        YourHP = 100
        entityHP = 210
        system()
