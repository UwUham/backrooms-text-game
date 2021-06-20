import sys, os, random, time, gamefunctions

weaponsinBag = ["knife", "shovel", "power of friendship"]
weaponinHand = ["double ended dildo"]

def fight():
    print()

def weapons():
    print("You have:")
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
    print("Placed the", handweapon, "back in the bag!")
    handweapon = weaponinHand[0]
    print("Pulled out the", handweapon)
         

def defend():
    print()

weapons()