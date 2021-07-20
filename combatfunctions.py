global damagedealt, damagetaken, YourHP
damagedealt = 0
damagetaken = 0
YourHP = 100

import random, time, gamefunctions as game



weaponatkstat = {
    "blunt knife": 5,
    "entity fist": 10,
    "shield": 0,
    "lightsaber": 10,
    "key": 0,
    "kitchen knife": 20,
    "entity tentacle": 30,
    "baby hand": 0,
    "scalpel": 40,
    "usb": 999
}

weapondefstat = {
    "blunt knife": 15,
    "entity fist": 10,
    "shield": 10,
    "lightsaber": 1,
    "key": 0,
    "kitchen knife": 15,
    "entity tentacle": 5,
    "baby hand": 1,
    "scalpel": 5,
    "usb": 999
}

weaponflavours = {
"entity tentacle": "'s tentacles surround you, and tightly holding you in place the entity manages to get a few valuable hits in",
"entity fist": " punches you",
"baby hand": " swings with his hand, but due to having undeniably small arms and hands, misses and attacks"
}

systemnames = ["Fear",
"Anger",
"Disgust",
"Sadness",
"Rage",
"Loneliness",
"Melancholy",
"Annoyance",
"Hate",
"Liam"
]

systemweaponflavour = {"Fear": " swings his terror mace around wildly",
"Anger": " violently slashes with his angry claws",
"Disgust": " swings her hand of dissatisfaction at you",
"Sadness": " projectile cries at you with very sharp tears",
"Rage": " attempts to impale you with his rage spear but misses",
"Loneliness": " stabs at you with her knife, but misses and attacks",
"Melancholy": " sits in silence, menacingly staring at you with peircing eyes",
"Annoyance": " laughs unbearably loudly, giving you a massive headache and attacking",
"Hate": " fills you with sorrow, and you forget why you're here in the first place for a second, before you remember and he attacks you",
"Liam": " swings with his hand, but due to having undeniably small arms and hands, misses and attacks"
}

systemweaponatkstats = {"Fear": 10,
"Anger": 15,
"Disgust": 5,
"Sadness": 15,
"Rage": 0,
"Loneliness": 0,
"Melancholy": 5,
"Annoyance": 10,
"Hate": 20,
"Liam": 0}


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

def PlayerIsHoldingKitchenKnifeForJoesBirthdayIn1982(var):
    if "kitchen knife" in weaponinHand or "kitchen knife" in weaponsinBag:
        print("You have a kitchen knife with the tag \"Joe's birthday\" on it, and underneath it says 18/8/1982.")
    else:
        print(var)

def heal():
    YourHP = 100
    game.clrprint("You rested and became fully healthy once again.")
    input("Press ENTER to continue.")

def drop(what, num):
    num = str(num)
    drops = open("./roomdrops/" + num + ".txt", "w")
    dropsread = open("./roomdrops/" + num + ".txt", "r")
    if len(dropsread.read()) > 0:
        game.clrprint("You've already dropped an item here, you can't drop another.")
    elif what in weaponsinBag:
        drops.write(what + "\n")
        weaponsinBag.remove(what)
        game.clrprint("Dropped the " + what + '.')
    elif what in weaponinHand:
        drops.write(what + "\n")
        weaponinHand.remove(what)
        game.clrprint("Dropped the " + what + '.')
    else:
        game.clrprint("You don't have that item." + what)
    input("Press ENTER to continue.")
    drops.close()
    dropsread.close()


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
        index = random.randrange(1, 4)

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
