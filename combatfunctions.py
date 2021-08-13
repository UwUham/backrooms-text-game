'''
Combatfunctions.py is a module we made to handle our extra feature, a combat engine.
In-game, the combat engine aims to create an Undertale, OMORI or Pokemon-like turn-based RPG-style fighting experience.
As a developer, you can modify the stats of existing weapons by changing the values in the weaponatkstat and weapondefstat libraries, or create new ones by adding existing entries.
Please note that you need to make your custom weapons obtainable in-game, by editing the gamefunctions.py file.
'''
global damagedealt, damagetaken, YourHP # defining variables to be used in combat
damagedealt = 0 # defining variables to be used in combat
damagetaken = 0 # defining variables to be used in combat
YourHP = 100 # defining variables to be used in combat
doyouhaveaweapon = True # defining variables to be used in combat
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

def bagadd(item): # create the bagadd function, which is used to add items to your bag.
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

def PlayerIsHoldingKitchenKnifeForJoesBirthdayIn1982(var): # this runs code in here to interact with a pussle in gamefunctions
    if "kitchen knife" in weaponinHand or "kitchen knife" in weaponsinBag: # if the kitchen knife is in your hand or your bag
        print("You have a kitchen knife with the tag \"Joe's birthday\" on it, and underneath it says 18/8/1982.") # give hint text
    else: # if the player does not have the knife
        print(var) # print specified text

def heal(): # create the heal function, which does what it says on the tin: heal your character to maximum HP
    global YourHP # set your hp to 100
    YourHP = 100 # set your hp to 100
    game.clrprint("You rested and became fully healthy once again.") # tell the player that their health is now full
    input("Press ENTER to continue.") # wait for user input

def drop(what): # create the drop function, which drops your currently held item or an item in your bag
    global weaponsinBag, weaponinHand # set the variables used to global
    if what in weaponsinBag: # if the specified item is in your bag
        weaponsinBag.remove(what) # remove the item
        game.itemappend(what) # interact with gamefunctions to put the item on the ground
        game.clrprint("Dropped the " + what + ".") # tell the user they dropped the item
    elif what in weaponinHand: # if the specified item is in your hand
        weaponinHand.remove(what) # remove the item
        game.itemappend(what) # interact with gamefunctions to put the item on the ground
        game.clrprint("Dropped the " + what + ".") # tell the user that they dropped the item
    else: # if the item is not in the player's inventory
        game.clrprint("You do not have a " + what + " in your inventory!") # tell the player as such
    input("Press ENTER to continue.") # wait for user input
        

def fight(entityName, entityWeapon): # create the fight function, which is used in combat to initialise a turn
    if len(weaponinHand) == 1: # if you are holding a weapon
        global damagetaken, damagedealt, doyouhaveaweapon # set variables as global
        firstgoer = random.randint(0, 2) # randomly deciding who goes first
        handweapon = weaponinHand[0] # creating a variable to refer to your weapon for ease purposes
        index = random.randrange(1, 3) # randomly deciding if the hit will be a critical hit or not. thanks to python's poor pseudo-randomisation, crits behave really weirdly.

        if firstgoer == 0: # if you are going first
            game.clrprint("YOU attack first!") # tell the user that they are attacking
            time.sleep(0.7) # wait
            print("Attacked with", handweapon.upper(), "for", int(index * int(weaponatkstat[handweapon])), "damage!") # tell the user about their attack and how much damage they did
            damagedealt = weaponatkstat[handweapon] # take damage based off of your weapon's attack stat
            if index == 2: # if you hit a critical hit
                print("Critical hit!") # tell the user that you did a critical hit
                damagedealt = int(weaponatkstat[handweapon]) * 2 # change the amount of damage dealt accordingly
            input("Press ENTER to continue") # wait for user input
            index = random.randrange(1, 3) # randomly deciding crit
            game.clrprint(entityName.upper() + " attacks!") # tell the user that the entity it attacking
            time.sleep(0.7) # wait
            print(entityName.upper(), weaponflavours[entityWeapon], "for", int(index * int(weaponatkstat[entityWeapon])), "damage!") # tell the user about their attack and how much damage they did
            damagetaken = weaponatkstat[entityWeapon] # set the amount of damage taken
            if index == 2: # if the entity hits a critical
                print("Critical hit!") # tell the user
                damagetaken = weaponatkstat[entityWeapon] * 2 # set damage
            input("Press ENTER to continue")  # wait for user input
        else: # if the entity is going first
            game.clrprint(entityName.upper() + " attacks first!") # tell the user that the entity is attacking
            time.sleep(0.7) # wait
            print(entityName.upper(), weaponflavours[entityWeapon], "for", int(index * int(weaponatkstat[entityWeapon])), "damage!") # tell the user about their attack and how much damage they did
            damagetaken = weaponatkstat[entityWeapon] # set damage
            if index == 2.0: # if entity hits a crit
                print("Critical hit!") # tell the user
                damagetaken = weaponatkstat[entityWeapon] * 2 # set damage
            input("Press ENTER to continue") # wait for user input
            index = random.randrange(1, 3) # decide crit
            game.clrprint("YOU attack!") # tell the user they are attacking
            time.sleep(0.7) # wait
            print("Attacked with", handweapon.upper(), "for", int(index * int(weaponatkstat[handweapon])), "damage!") # tell the user about their attack and how much damage they did
            damagedealt = weaponatkstat[handweapon] # set damage
            if index == 2: # if you crit
                print("Critical hit!") # tell the user that they crit
                damagedealt = weaponatkstat[handweapon] * 2 # set damage
            input("Press ENTER to continue") # wait for user input
        game.clear() # clear the screen
    elif len(weaponsinBag) > 0: # if there are items in your bag but not in your hand:
        game.clrprint("Select a weapon first.")
    else: # if both your bag and your hand are enpty
        game.clrprint("You fought without a weapon and lost.") # tell the user they lost
        damagetaken = 100 # kill the character
        doyouhaveaweapon = False # tell the game the user does not have a weapon
        input("Press ENTER to continue.") # wait for user input


def weapons(): # create the weapons function, which is used to interact with your bag
    global choicenum, swap # set a variable as global
    if len(weaponsinBag) != 0: # if there is something in your bag
        swap = True # a switch boolean
        game.clrprint("You have:") # print the items in your bag
        for i in weaponsinBag: # print the items in your bag
            print(i) # print the items in your bag
        print("Items in bag: " + str(len(weaponsinBag))) # print the items in your bag
        choice = input("Select an item (any weapon that was listed or none): ").lower() # selecting a choice and handling it accordingly
        if choice == weaponsinBag[0].lower(): # selecting a choice and handling it accordingly
            choicenum = 0 # selecting a choice and handling it accordingly
        elif choice == weaponsinBag[1].lower(): # selecting a choice and handling it accordingly
            choicenum = 1 # selecting a choice and handling it accordingly
        elif choice == weaponsinBag[2].lower(): # selecting a choice and handling it accordingly
            choicenum = 2 # selecting a choice and handling it accordingly
        elif choice == "none": # selecting a choice and handling it accordingly
            swap = False # selecting a choice and handling it accordingly
        else: # selecting a choice and handling it accordingly
            print("Not a valid choice.") # selecting a choice and handling it accordingly
            swap = False # flip the switch boolean
        if swap == True: # if you selected a weapon
            if len(weaponinHand) == 1: # if there is an item in your hand
                handweapon = weaponinHand[0] # swapping the places of the item in the bag and the item in the hand
                weaponinHand.append(weaponsinBag[choicenum]) # swapping the places of the item in the bag and the item in the hand
                weaponsinBag.append(weaponinHand[0]) # swapping the places of the item in the bag and the item in the hand
                weaponinHand.pop(0) # swapping the places of the item in the bag and the item in the hand
                weaponsinBag.pop(choicenum) # swapping the places of the item in the bag and the item in the hand
                game.clrprint("Placed the " + handweapon + " back in the bag!") # swapping the places of the item in the bag and the item in the hand
                handweapon = weaponinHand[0] # swapping the places of the item in the bag and the item in the hand
                time.sleep(0.7) # swapping the places of the item in the bag and the item in the hand
                print("Pulled out the", handweapon + "!") # swapping the places of the item in the bag and the item in the hand
            elif len(weaponinHand) == 0: # if there is not an item in your hand
                weaponinHand.append(weaponsinBag[choicenum]) # take out the weapon
                weaponsinBag.pop(0) # take out the weapon
                handweapon = weaponinHand[0] # take out the weapon
                time.sleep(0.7) # take out the weapon
                print("Pulled out the", handweapon + "!") # take out the weapon
    else: # if your bag is empty
        game.clrprint("Your bag is empty!") # tell the player
    input("Press ENTER to continue.") # wait for user input
    game.clear() # clear the screen
         

def defend(entityName, entityWeapon): # create the defend function, which differently initalises a turn to work more defensively
    global damagedealt, damagetaken, doyouhaveaweapon # set variables as global
    if len(weaponinHand) == 1: # if there is an item in your hand
        if weapondefstat[weaponinHand[0]] > weaponatkstat[entityWeapon]: # if your defense stat is higher than the enemy's attack stat
            damagedealt = weaponatkstat[entityWeapon]/2 # half the enemy's attack
            damagetaken = 0 # take 0 damage
            game.clrprint("Fully defended against " + entityName + " and reflected " + str(damagedealt) + " damage back.") # tell the player what happened
        elif weapondefstat[weaponinHand[0]] <= int(weaponatkstat[entityWeapon])/2: # if your defense stat is equal to or less than half of the enemys attack:
            damagetaken = weaponatkstat[entityWeapon] # defining damage
            damagedealt = 0 # defining damage
            game.clrprint("Defense failed, " + str(damagetaken) + " damage taken.") # tell the user that their defense failed
        else: # if the defense stat is above half
            damagetaken = int(weaponatkstat[entityWeapon]/2) # half the damage taken
            damagedealt = 0 # set the damage dealt to 0
            game.clrprint("Defended against " + entityName + " partially and took " + str(damagetaken) + " damage.") # tell the user how much damage they took
    elif len(weaponsinBag) > 0: # if you don't have a weapon in your hand but have one in your bag
        game.clrprint("Select a weapon first.") # tell the user to pick a weapon
    else: # if the user does not have a weapon
        game.clrprint("You fought without a weapon and lost.") # lose the fight
        damagetaken = 100 # lose the fight
        doyouhaveaweapon = False # tell the game the user does not have a weapon
        input("Press ENTER to continue.") # wait for user input

def combat(entityName, entityWeapon, entityHP): # create the combat function, which begins a fight and changes your terminal enviroment to something combat based
    global YourHP, doyouhaveaweapon # make your hp variable global
    entityHPcache = entityHP # cache the entity's hp
    game.clrprint(entityName.upper() + " wants to fight!") # tell the user the battle has been intitalized
    while entityHP > 0 and YourHP > 0: # if neither of you have died yet:
        print("What would you like to do? (fight, defend, weapons, help)") # open the combat menu
        print("Your health: " + str(YourHP)) # show hp stats
        print("Entity health: " + str(entityHP)) # show hp stats
        run = input("> ") # create a command environment so the user can make a choice
        if run == "help": # print the combat health text
            print('''
fight - attack the entity.\n
defend - protect yourself from the entity.\n
weapons - switch your held weapon with one in your bag (if available)\n''') # print the combat health text
            input("Press ENTER to continue.") # wait for user input
            game.clear() # clear the screen
        elif run == "fight": # call the fight function and adjust HP accordingly
           fight(entityName, entityWeapon) # call the fight function and adjust HP accordingly
           entityHP = entityHP - damagedealt # call the fight function and adjust HP accordingly
           YourHP = YourHP - damagetaken # call the fight function and adjust HP accordingly
        elif run == "defend": # call the defend function and adjust HP accordingly
           defend(entityName, entityWeapon) # call the defend function and adjust HP accordingly
           entityHP = entityHP - damagedealt # call the defend function and adjust HP accordingly
           YourHP = YourHP - damagetaken # call the defend function and adjust HP accordingly
           input("Press ENTER to continue.") # wait for user input
           game.clear() # clear the screen
        elif run == "weapons": # if the user selects weapons:
           weapons() # call the weapons function
        else: # if the user says anything else:
            print("Not a valid choice.") # tell the user that they did not select a valid choice
            input("Press ENTER to continue.") # wait for user input
            game.clear() # clear the screen
    if entityHP <= 0: # if the entity HP is 0:
        game.clrprint("Successfully defeated " + entityName.upper() + "!") # tell the user that they beat the entity
    elif YourHP <= 0: # if your HP is 0:
        game.clrprint("Defeated by " + entityName.upper() + "!") # tell the user that they lost to the entity
        lost = True # set a variable to say you lost the fight
    if YourHP < 30: # if you have less than 30 hp:
        print("Health restored to 30!") # restore the user's HP
        YourHP = 30 # restore the user's HP
    if entityHP <= 0: # if the entity has less than or equal to 0 HP:
        input("Press ENTER to continue.") # wait for user input
    elif lost == True and doyouhaveaweapon == True: # if you lost but don't have a weapon
        retry = input("Try again? (yes/no) ").lower() # wait for user input
        if retry == "yes": # if user says yes
            lost = False # set lost to false
            YourHP = 100 # fight retry sequence
            retryloop = 1 # loop stuff
            combat(entityName, entityWeapon, entityHPcache) # retry the fight
        elif retry == "no": # if user says no
            YourHP = 100 # set hp to 100
            game.clrprint("You wake up again, in the room where the fight began. You feel healthy.") # tell the user that they are alive
            input("Press ENTER to continue.") # wait for user input
            game.clear() # clear the screen
            retryloop = 1 # loop stuff
            game.command("> ") # go back out to the exploration mode
        else: # item invalidation
            print("Please select an option.") # item invalidation
            input("Press ENTER to continue.") # item invalidation
            game.clear() # item invalidation
    elif lost == True and doyouhaveaweapon == False: # if the user has no weapon but lost the game:
        doyouhaveaweapon = True # set the weapon switch to true
        game.clrprint("You wake up again, in the room where the fight began. You feel healthy, however you still do not have a weapon.") # tell the user that they are alive
        input("Press ENTER to continue.") # wait for user input
        game.clear() # clear the screen
        game.command("> ") # go back out to the exploration mode

def sysfight(): # creating the sysfight function, a rework of our old combat engine created entirely to work exclusively with the final boss.
    global damagetaken, damagedealt, doyouhaveaweapon # defining required variables
    damagetaken = 0 # defining required variables
    damagedealt = 0 # defining required variables
    if len(weaponinHand) == 1: # if the player is holing a weapon
        firstgoer = random.randint(0, 2) # defining variables
        handweapon = weaponinHand[0] # defining variables
        index = random.randrange(1, 3) # defining variables

        if firstgoer == 0: # if you are going first
            game.clrprint("YOU attack first!") # tell the user they are attacking first
            time.sleep(0.7) # wait for a moment
            print("Attacked with", handweapon.upper(), "for", int(index * int(weaponatkstat[handweapon])), "damage!") # tell the user how they attacked and how much they hit for
            if index != 2: # if the user didn't hit a crit
                damagedealt = damagedealt + weaponatkstat[handweapon] # set the damage
            if index == 2: # if the user did hit a crit
                print("Critical hit!") # tell the user that they hit a crit
                damagedealt = damagedealt + int(weaponatkstat[handweapon]) * 2 # double the damage and set it
            input("Press ENTER to continue") # wait for user input
            count = 0 # defining a variable for a loop
            while count <= 2: # go through the entity attack sequence three times
                index = random.randrange(1, 3) # go through the entity attack sequence three times
                entityName = random.choice(systemnames) # go through the entity attack sequence three times
                game.clrprint(entityName.upper() + " attacks!") # go through the entity attack sequence three times
                time.sleep(0.7) # go through the entity attack sequence three times
                print(entityName.upper(), systemweaponflavour[entityName], "for", int(index * int(systemweaponatkstats[entityName])), "damage!") # go through the entity attack sequence three times
                if index != 2: # go through the entity attack sequence three times
                    damagetaken = damagetaken + systemweaponatkstats[entityName] # go through the entity attack sequence three times
                if index == 2: # go through the entity attack sequence three times
                    print("Critical hit!") # go through the entity attack sequence three times
                    damagetaken = damagetaken + systemweaponatkstats[entityName] * 2 # go through the entity attack sequence three times
                input("Press ENTER to continue") # go through the entity attack sequence three times
                count = count + 1 # go through the entity attack sequence three times
        else: # if the SYSTEM goes first:
            count = 0 # repeat the enemy attack sequence three times
            while count <= 2: # repeat the enemy attack sequence three times
                entityName = random.choice(systemnames) # repeat the enemy attack sequence three times
                game.clrprint(entityName.upper() + " attacks first!") # repeat the enemy attack sequence three times
                time.sleep(0.7) # repeat the enemy attack sequence three times
                print(entityName.upper(), systemweaponflavour[entityName], "for", int(index * int(systemweaponatkstats[entityName])), "damage!") # repeat the enemy attack sequence three times
                if index != 2: # repeat the enemy attack sequence three times
                    damagetaken = damagetaken + systemweaponatkstats[entityName] # repeat the enemy attack sequence three times
                if index == 2: # repeat the enemy attack sequence three times
                    print("Critical hit!") # repeat the enemy attack sequence three times
                    damagetaken =  damagetaken + systemweaponatkstats[entityName] * 2 # repeat the enemy attack sequence three times
                input("Press ENTER to continue") # repeat the enemy attack sequence three times
                count = count + 1 # repeat the enemy attack sequence three times
                index = random.randrange(1, 3) # decide critical hit
            index = random.randrange(1, 3) # decide critical hit
            game.clrprint("YOU attack!") # go through your attack sequence
            time.sleep(0.7) # go through your attack sequence
            print("Attacked with", handweapon.upper(), "for", int(index * int(weaponatkstat[handweapon])), "damage!") # go through your attack sequence
            if index != 2: # go through your attack sequence
                damagedealt = damagedealt + weaponatkstat[handweapon] # go through your attack sequence
            if index == 2: # go through your attack sequence
                print("Critical hit!") # go through your attack sequence
                damagedealt = damagedealt + weaponatkstat[handweapon] * 2 # go through your attack sequence
            input("Press ENTER to continue") # go through your attack sequence
        game.clear() # go through your attack sequence
    elif len(weaponsinBag) > 0: # make sure the player is holding a weapon
        game.clrprint("Select a weapon first.") # make sure the player is holding a weapon
    else: # if you don't have a weapon in the final boss fight somehow:
        game.clrprint("You fought without a weapon and lost.") # go through the lost battle sequence
        damagetaken = 100 # go through the lost battle sequence
        doyouhaveaweapon = False # go through the lost battle sequence
        input("Press ENTER to continue.") # go through the lost battle sequence


def system(): # set the function for the final battle, initialising an identical combat environment with reworked turns to work with the system's special mechanic
    global YourHP, damagedealt, damagetaken, doyouhaveaweapon
    entityHP = 210 # init text and variables
    entityName = "THE SYSTEM" # init text and variables
    game.clrprint("THE SYSTEM wants to fight!") # init text and variables
    while entityHP > 0 and YourHP > 0: # while both members are alive
        print("What would you like to do? (fight, defend, weapons, help)") # open the fight menu
        print("Your health: " + str(YourHP)) # open the fight menu
        print("THE SYSTEM health: " + str(entityHP)) # open the fight menu
        run = input("> ") # open the fight menu
        if run == "help": # if you need the help text in the final battle for whatever reason:
            print('''
fight - attack the entity.\n
defend - protect yourself from the entity.\n
weapons - switch your held weapon with one in your bag (if available)\n''') # print help text and wait for user input
            input("Press ENTER to continue.") # print help text and wait for user input
            game.clear() # clear the screen
        elif run == "fight": # if the user fights
            sysfight() # go through the fight sequence
            entityHP = entityHP - damagedealt # go through the fight sequence
            YourHP = YourHP - damagetaken # go through the fight sequence
            damagedealt = 0 # go through the fight sequence
            damagetaken = 0 # go through the fight sequence
        elif run == "defend": # if the user tries to defend
            game.clrprint("You can't defend against multiple entities at once!") # to be honest i had no idea how defending was gonna work here, so i just scrapped it
            input("Press ENTER to continue.") # wait for user input
            game.clear() # clear the screen
        elif run == "weapons": # if the user switches weapons
           weapons() # switch weapons
        else: # if the user says anything else:
            print("Not a valid choice.") # tell the user that choice is invalid
            input("Press ENTER to continue.") # wait for user input
            game.clear() # clear the screen
    if entityHP <= 0: # if the entitiy is dead:
        game.clrprint("Successfully defeated " + entityName.upper() + "!") # fight win text/sequence
        if YourHP < 30: # fight win text/sequence
            print("Health restored to 30!") # fight win text/sequence
            YourHP = 30 # fight win text/sequence
    elif YourHP <= 0: # if you are dead
        game.clrprint("Defeated by " + entityName.upper() + "!") # fight loss sequence
        lost = True # fight loss sequence
    if entityHP <= 0: # fight loss sequence
        input("Press ENTER to continue.") # fight loss sequence
    elif lost == True and doyouhaveaweapon == True: # if you lost but don't have a weapon
        retry = input("Try again? (yes/no) ").lower() # wait for user input
        if retry == "yes": # if user says yes
            lost = False # set lost to false
            YourHP = 100 # fight retry sequence
            entityHP = 210 # fight retry sequence
            system() # fight retry sequence
            retryloop = 1 # loop stuff
        elif retry == "no": # if user says no
            YourHP = 100 # set hp to 100
            game.clrprint("You wake up again, in the room where the fight began. You feel healthy.") # tell the user that they are alive
            input("Press ENTER to continue.") # wait for user input
            game.clear() # clear the screen
            retryloop = 1 # loop stuff
            game.command("> ") # go back out to the exploration mode
        else: # item invalidation
            print("Please select an option.") # item invalidation
            input("Press ENTER to continue.") # item invalidation
            game.clear() # item invalidation
    elif lost == True and doyouhaveaweapon == False: # if you lost due to not having a weapon
        YourHP = 100 # set hp to 100
        game.clrprint("You wake up again, in the room where the fight began. You feel healthy, however you still do not have a weapon.") # tell the user that they are alive
        input("Press ENTER to continue.") # wait for user input
        game.clear() # clear the screen
        game.command("> ") # go back out to the exploration mode        
