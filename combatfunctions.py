import sys, os, random, time, gamefunctions as game

weaponsinBag = ["knife", "shovel", "power of friendship"]
weaponinHand = ["double ended dildo"]

def bagadd():
    if len(weaponsinBag) == 3:
        game.clrprint("Not enough space for this item.")
    elif len(weaponsinBag) > 3:
        game.clrprint("How did you even get this many items? Pick a number, from 0 to", len(weaponsinBag) - 1,  "and we'll remove that item, and that'll repeat until you have three items again.")
        while len(weaponsinBag) > 3:
            num = input("> ")
            weaponsinBag.pop(num)

def fight():
    print()

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
    game.clrprint("Placed the", handweapon, "back in the bag!")
    handweapon = weaponinHand[0]
    time.sleep(0.7)
    print("Pulled out the", handweapon + "!")
         

def defend():
    print()

weapons()