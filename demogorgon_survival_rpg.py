# File: demogorgon_survival_rpg.py
# Author: Sadia Rahman
# Date: 10/29/2018
# Section: 9
# E-mail: rasadia1@umbc.edu
# Description: This is a simple text rpg


from random import randint

#Constants for the player's stats
MAX_HEALTH = 100
MIN_HEALTH = 0

#Constant for the Demogorgon
DEM_MAX_HEALTH = 300

#Constants for the survival conditions
SURVIVE_DAYS = 7
SURVIVE_DISTANCE = 150

#Constants for items available in this game
FOOD = ["Reece's Pieces", "Pop Rocks", "Ovaltine", "WonderBread", "Twinkies", "Eggo Waffle"]
ITEMS = ["Sword", "Walkie Talkie", "Flashlight", "Laser Cannon", "Walkman", "Rubber Band", "Hi-C", "Bicycle", "Heelys"]
WEAPONS =["Sword", "Walkie Talkie", "Flashlight", "Laser Vannon", "Rubber Band"]
DISTANCE_MULTIPLIERS = ["Bicycle", "Heelys"]
EGGO_WAFFLES = 10

# displayMenu() This function displays the options the player can choose from
#               to do during each morning
# input         this function just prints the options
# output        this function just prints the options

def displayMenu():
    print("What would you like to do this morning?")
    print()
    print("1 - View Inventory")
    print("2 - View Current Stats")
    print("3 - Eat Eggo Waffle")
    print("4 - Do Nothing")
    print()

# equipmentChange(inventory, equippedItem) This function both displays inventory and inputs
#                                          equipped items(weapons) should the user choose to
#                                          check their inventory in the morning.
# input                                    inventory, equippedItem; 
# output                                   equippedItem; it returns equipped so that the user's
#                                          weapon stays constant throughout the game until the
#                                          player decides otherwise

def equipmentChange(inventory, equippedItem):

    #Just some display lines
    print("Here's your inventory...")
    print()
    print(inventory)
    print()
    print("Would you like to equip an item?")
    print()
    print("1 - Equip")
    print("2 - Unequip")
    print("3 - I changed my mind")
    print()
    
    equip = int(input("Enter your option: (3 to go back to main menu) "))
    print()

    #As long as the user enters a number that is not 3, the user will be prompted options within this loop
    while equip != 3:
        print("Your options are: ")
        c = 0
        e = 1
        while c < len(inventory):
            print(e, " - ", inventory[c])
            c += 1
            e += 1
        print()
        #If the user opts for 1, they code will allow them to equip an item from their inventory as their weapon
        if equip == 1:
            askUser = int(input("Enter an option: "))
            it = askUser - 1
            equippedItem = inventory[it]
            print("You have equipped", equippedItem)
            equip = int(input("Enter your option:(3 to go back) "))

        #If the player wants to unequip, they will enter 1, leaving them weaponless
        elif equip == 2:
            print("You have unequipped", equippedItem)
            equippedItem = ""
            equip = int(input("Enter your option:(3 to go back)  "))

        #If the player enters a number that is not 1, 2 or 3, the player will be prompted to enter a valid option
        else:
            print("That's not a valid option!")
            equip = int(input("Enter your option:*3 to go back)  "))

    return equippedItem

# distanceCovered(inventory, health, distance) This function caculates the distance travelled each day
#                                              with certain conditions applied, depending on the items
#                                              present in the inventory.
# input                                        inventory, health, distance;
# output                                       distance

def distanceCovered(inventory, health, distance):

    #If the player's inventory contains both Bicycle and Heelys, Bicycle will take priority and
    #it's multiplying value will take precedance
    if "Bicycle" and "Heelys" in inventory:
        distanceOG = (health / 4) + 5
        distance += distanceOG * 1.5

    #If the user just has a Bicyle, then the distance is multiplied by 1.5
    elif "Bicycle" in inventory:
        distanceOG = (health / 4) + 5
        distance += distanceOG * 1.5

    #If the user has just a Heelys, then the distance is multiplied by 1.25
    elif "Heelys" in inventory:
        distanceOG = (health / 4) + 5
        distance += distanceOG * 1.25

    #If neither item exists in the list, then the distance will be added normally 
    else:
        distance += (health / 4) + 5

    return distance

# printDemogorgonEncounter(health, demogorgonHealth) This function displayes the dialouge when
#                                                    the player faces the monster along with the
#                                                    options as to what the player could do.
# input                                              health, demogorgonHealth;
# output                                             N/A

def printDemogorgonEncounter(health, demogorgonHealth):
    print("You hear a growl in the corner...THE DEMOGORGON HAS FOUND YOU!")
    print("It's reptilian face opens up like a flower, saliva dripping to the floor - those teeth look sharp...")
    print("It's hungry...")
    print()
    print("Your current health", health)
    print("The monster's health", demogorgonHealth)
    print()
    print("Are you going to...")
    print()
    print("1 - Fight?")
    print("2 - Flail?")
    print("3 - Flee?")
    print()

# fleeTheGorgon(health, demogorgonDamage) When the player encounters the monster, should the opt to flee
#                                         the monster, the following code contributes the the choices and
#                                         the consequences of it.
# input                                   health, demogorgonDamage
# output                                  health

def fleeTheGorgon(health, demogorgonDamage):
    
    escapeRandom = randint(1, 10)

    #If the random function generates a number between 1 through 3, the player will encounter the demogorgon
    if escapeRandom <= 3:
        print()
        print("You've escaped the monster!")
        return health
    
    #If the random function generates a number between 4 and 10, the player will manage to escape the demogorgon
    else:
        print("You keep running until the monster's movement seemed to have disappeared...")
        print("You stop, feeling relief you have escaped...except you're wrong.")
        print("The monster appears before you, tired and breathing hard, slashes at you and then disappears")    
        health = health - (demogorgonDamage / 2)
        return health


def main():

    #changeable variables that will change as the program runs
    flagS = "yes"
    days = 1
    distance = 0
    inventory = ["Walkie Talkie", "Flashlight"]
    curHealth = 100
    equippedItem = ""
    damage = 0
    demogorgonDamage = 20
    demogorgonHealth = 300

    #This is the main loop that'll run through the whole game
    while flagS == "yes":

        #The variable is set to the opposite of the condition, it is later changed depending on conditions
        flagS = "no"
        print("The sun rises, glowing red in the distance, however, light refuses to spread through the forest...")
        print("It is day", days)
        print()

        #The menu for morning tasks is displayed
        displayMenu()

        askUser1 = int(input("Enter your option: "))

        #Choices distibuted to whichever choice the player opts for
        while askUser1 != 4:

            #If the user opts for 1, the code will run the option to view the inventory and possibly equip weapons
            if askUser1 == 1:
                
                equippedItem = equipmentChange(inventory, equippedItem)
                print()
                askUser1 =int(input("Okay then! Anything else you'd like to do in the morning? (Pick an option) "))

            #If the user opts for 2, they are shown their current stats
            elif askUser1 == 2:
                print()
                print("So far...")
                print("Your health is: ", curHealth)
                print("You have so far travelled: ", distance)
                print("Your current weapon is: ", equippedItem)
                print()
                askUser1 = int(input("Okay then! Anything else you'd like to do in the morning? (Pick an option) "))

            #If the user opts for 3, they are presented with the option to eat a waffle
            elif askUser1 == 3:
                eqgoEaten = "no" #this variable is set as to limit the number of waffled eaten in a day

                #If the player's health is 100, they cannot eat the waffle
                if curHealth == MAX_HEALTH:
                    print("You have full health! Save the waffle for another day...")

                #If the player's health is above 90, their health will be 100
                elif curHealth > 90:

                    #If the player has already had a waffle, they cannot have another...
                    if eggoEaten == "yes":
                        print("You already had a waffle!")

                    #...Otherwise they can
                    elif eggoEaten == "no":
                        curHealth = MAX_HEALTH
                        print("You have full health!")
                        eggoEaten = "yes"

                #If the player has a health of 90 or less, 10 is added.        
                elif curHealth <= 90:
                    if eqggoEaten == "yes":
                        print("You already had a waffle!")
                    elif eggoEaten == "no":
                        curHealth += EGGO_WAFFLE
                        print("Your health is", curHealth,"!")
                        eggoEaten = "yes"
                askUser1 = int(input("Please enter an option: "))
            #If the user enters a non valid number they will be asked to re eneter a valid one
            else:
                askUser1 = int(input("That's a valid option! Please choose something from the list: "))
                
            print("I guess you're done with your morning! Moving on!")
                    

        #The following establishes the amount of damage player can inflict with whichever weapon they are equipped with
        if equippedItem == "Laser Cannon":
            damage = 100
        elif equippedItem == "Sword":
            damage = 50
        elif equippedItem == "Rubber Band":
            damage = 25
        elif equippedItem == "Walkie Talkie":
            damage = 10
        elif equippedItem == "Flashlight":
            damage = 5

        #The display menu for when the player is done with morning tasks and are prompted to move on
        print()
        print("The Demogorgon looms in the distance.")
        print()
        print("What would you like to do?")
        print()
        print("1 - Pack up camp and look for civilization?")
        print("2 - Stay put at camp?")
        print()

        askUser2 = int(input("Enter your option: "))

        
        randomEvents = randint(1, 10)
        stayOrPack = randint(1, 10)

        #If the player decided to pack and move on
        if askUser2 == 1:

            print()
            print("You've packed everything, making your way to what is hopefully civilization...")

            #If the random function generated a 1 or a 2, the player will find a bag of food
            if randomEvents <= 2:
                
                print()
                print("You have found a backpack with food!")
                
                randomFood = randint(1, 5)
                #the first possible random food is reeces pieces
                if randomFood == 1:

                    print()
                    print("You have found Reece's Pieces!")
                    keep = input("Do you want to eat it now? (Yes or No) ")
                    #The player has to choose whether they want to eat it
                    if keep == "Yes":
                        curHealth -= 30
                        print("You ate the Reece's Pieces and your health is now", curHealth)
                    elif keep == "No":
                        print("You put the Reece's Pieces back in the bag and start to move on forward.")
                #The second is pop rocks
                elif randomFood == 2:
                    #pop rocks and reece's pieces are different because they have a negative impact on the health
                    print()
                    print("You have found Pop Rocks!")
                    keep = input("Do you want to eat it now? (Yes or No) ")
                    if keep == "Yes":
                        curHealth -= 5
                        print("You ate the Pop Rocks and your health is now", curHealth)
                    elif keep == "No":
                        print("You put the Pop Rocks back in the bag and start to move on forward.")
                #third is ovaltine
                elif randomFood == 3:

                    print()
                    print("You have found Ovaltine!")
                    keep = input("Do you want to eat it now? (Yes or No) ")
                    if keep == "Yes":
                        #Even if the player chooses to eat the food, if they have maximum health they cannot consume it.
                        if curHealth == MAX_HEALTH:
                            print("You cannot consume that! You have full health!")
                        #and any health at which the addition of the wood will go over 100, will just reset the health at 100
                        elif curHealth > 85:
                            curHealth = MAX_HEALTH
                            print("You ate the Ovaltine. You have full health now!")
                        elif curHealth <= 85:
                            curHealth+= 15
                            print("You ate the Ovaltine. Your health is now", curHealth)

                    elif keep == "No":
                        print()
                        print("You put the Ovaltine back in the bag and you start to move on forward.")
                #fourth food is WOnderBread
                elif randomFood == 4:
                    #Each of the positive-impact food have nearly identical layouts
                    print()
                    print("You have found WonderBread!")
                    keep = input("Do you want to eat it now? (Yes or No) ")
                    if keep == "Yes":
                        if curHealth == MAX_HEALTH:
                            print("You cannot consume that! You have full health!")
                        elif curHealth > 75:
                            curHealth = MAX_HEALTH
                            print("You ate the WonderBread. You have full health!")
                        elif curHealth <= 75:
                            curHealth += 25
                            print("You eat the WonderBread. Your health is now", curHealth)

                    elif keep == "No":
                        print()
                        print("You put the WonderBread back in the bag and you start to move on forward.")
                #and fifth is the twinkies
                elif randomFood == 5:

                    print()
                    print("You have found Twinkies!")
                    keep = input("Do you want to eat it now? (Yes or No) ")
                    if keep == "Yes":
                        if curHealth == MAX_HEALTH:
                            print("You cannot consume that! You have full health!")
                        elif curHealth > 70:
                            curHealth = MAX_HEALTH
                            print("You ate the Twinkies. You have full health!")
                        elif curHealth <= 70:
                            curHealth += 30
                            print("You eat the Twinkies. Your health is now", curHealth)

                    elif keep == "No":
                        print()
                        print("You put the twinkies back in the bag and start to move forward.")
            #Each of the food have an equal chance of happening
                        
            #If the random function generates numbers 3 or 4, the player will stumble upon a shed
            elif randomEvents > 2 and randomEvents <= 4:

                print()
                print("You have stumbled upon a shed!")
                print()
                print("Here's your current inventory...")
                print(inventory)
                print()

                randomItems = randint(1, 7)
                #The first possible item that the player can find is a sword
                if randomItems == 1:
                    
                    print("You have found a Sword!")
                    keep1 = input("Do you want to keep it? (Yes or No) ")
                    #the user has to choose to keep it or put it back
                    if keep1 == "Yes":
                        inventory.append("Sword") #If the user chooses to add the sword, the sword will be added to the inventory
                        print("You have added 'Sword' to your inventory!")
                        print("Your inventory is...")#The user will also get to see what they have
                        print(inventory)
                    elif keep1 == "No":
                        print()#If the user chooses to not keep the item, the player will just move on
                        print("You put the Sword back in the shed and start to move forward!")
                #The second item bicycle
                elif randomItems == 2:
                    #All of the possible items have identical layouts
                    print("You have found a Bicycle!")
                    keep1 = input("Do you want to keep it? (Yes or No) ")

                    if keep1 == "Yes":
                        inventory.append("Bicycle")
                        print("Your inventory is...")
                        print(inventory)
                    elif keep1 == "No":
                        print()
                        print("You put the Bicycle back into the shed and start to move forward!")
                #The third item is Hi-C
                elif randomItems == 3:

                    print("You have found a Hi-C!")
                    keep1 = input("Do you want to keep it? (Yes or No) ")

                    if keep1 == "Yes":
                        inventory.append("Hi-C")
                        print("Your inventory is...")
                        print(inventory)
                    elif keep1 == "No":
                        print()
                        print("You put the Hi-C back intot the shed and start to move forward!")
                #The fourth thing are Heelys
                elif randomItems == 4:

                    print("You have found a Heelys!")
                    keep1 = input("Do you want to keep it? (Yes or No) ")

                    if keep1 == "Yes":
                        inventory.append("Heelys")
                        print("Your inventory is...")
                        print(inventory)
                    elif keep1 == "No":
                        print()
                        print("You put the Heelys back into the shed and start to move forward!")
                #The fifth item is a Laser Cannon
                elif randomItems == 5:

                    print("You have found a Laser Cannon!")
                    keep1 = input("Do you want to keep it? (Yes or No) ")

                    if keep1 == "Yes":
                        inventory.append("Laser Cannon")
                        print("Your inventory is...")
                        print(inventory)
                    elif keep1 == "No":
                        print()
                        print("You put the Laser Cannon back into the shed and you start to move forward!")
                    #The 6th item is a rubber band
                elif randomItems == 6:

                    print("You have found a Rubber Band!")
                    keep1 = input("Do you wnat to keep it? (Yes or No) ")

                    if keep1 == "Yes":
                        inventory.append("Rubber Band")
                        print("Your inventory is...")
                        print(inventory)
                    elif keep1 == "No":
                        print()
                        print("You put the Rubber Band back into the shed and you start to move forward!")
                #The 7th item is a walkman
                elif randomItems == 7:

                    print("You have found a Walkman!")
                    keep1 = input("Do you want to keep it? (Yes or No) ")

                    if keep1 == "Yes":
                        inventory.append("Walkman")
                        print("Your inventory is...")
                        print(inventory)
                    elif keep1  == "No":
                        print()
                        print("You put the Walkman back into the shed and start to move forward!")
            #If the random function generates number 5 or 6, they will fall into a trench, lose a day and only cover half the distance they normally would have
            elif randomEvents > 4 and randomEvents <= 6:

                print()
                print("As you walk onwards, you suddenly fall into a trench!")
                days += 1
                distanceOG = (curHealth / 4) + 5
                distance += distanceOG / 2
            #Finally, if the player is lucky to land a 10, nothing will happen to them and they will travel unscathed!
            elif randomEvents == 10:
                print()
                print("You continue to walk until you notice the large glowing sun to hve disappeared. You set up camp and wait till the next day.")

            distance = distanceCovered(inventory, curHealth, distance)#The distance function will only occur if the player decides to leave camp
        #If the player decides to stay...                     
        elif askUser2 == 2:
            #Theres a 30% chance nothing will happen, they will be fully rested (get max health) 
            if stayOrPack > 7 and stayOrPack <= 10:
                print("You sit by your camp, resting yourself till the sun sets and the new day begins...")
                curHealth = MAX_HEALTH
        #There are two instances when the player could be attacked by the monster. If they pack and go, theres a 30% chance the mosnster will attack
        #If they stay at camp theres a 70% chance they will attacked
        if (randomEvents > 6 and randomEvents <= 9) and (stayOrPack <= 7):
            # FIGHT THE GORGON
            if "Hi-C" in inventory:
                demogorgonHealth = demogorgonHealth / 2 #If the player has a Hi-C, the monster health will be half
            if "Walkman" in inventory:
                less = (25 * demogorgonDamage) / 100
                demogorgonDamage = demogorgonDamage - less #If the player has a Walkman, the monsters damage will be 25% less
    
            printDemogorgonEncounter(curHealth, demogorgonHealth) #Displays the options available when the moster appears
            choice = int(input("Enter your choice: "))
            while choice > 3 or choice < 1:#The user can only put in 1, 2, 3
                choice = int(input("Invalid choice, please enter from the options: "))
                #If the user chooses, 1, they will hit the monster (if they have a weapon) and be hit back
            if choice == 1:
                curHealth = curHealth - demogorgonDamage
                if equippedItem == "":
                    print("You cannot fight. You dont have a weapon!")
                    print("The Demogorgon slashes at you!")
                    print("It growls at you and then runs off into the forest...")
                    print("Leaving your health at", curHealth)#If the player has no weapon, the player will be hit only
                else:
                    print("You hit the Demogorgon with your", equippedItem,", inflicting", damage,"amount of damage on it.")
                    print("The Demogorgon strikes back! Dealing you with", demogorgonDamage,"damage.")
                    de_health = demogorgonHealth - damage#If the player does have a weapon, both the player and the monster are hurt
            elif choice == 2:
                print()
                print("...but why? Anyway...")#If the user choose 2, they will die
                print("The Demogorgon growls menancingly at you, strikes you so hard, knocking you out!")
                curHealth = MIN_HEALTH
            elif choice == 3:#If they player opts to flee, theres a 30% chance that they will escape the monster, and 70% to be attacked by half its health
                curHealth = fleeTheGorgon(curHealth, demogorgonDamage)#Fleed option
            print("Your health: ", curHealth)
            print("Monster's health: ", demogorgonHealth)

            #The days will only update if the days is less than 7
        if days < 7:
            days += 1
            #If the monsters health hits 0 or less, it will be restored to 300, it can never die 
        if demogorgonHealth <= 0:
            demogorgonHealth = DEM_MAX_HEALTH
            #If the player's health is greater than 0...... 
        if curHealth > MIN_HEALTH:
            #...and survived for 7 days or reached 150 m, the loop will end
            if days == 7 or distance >= 150:
                flagS = "no"
                #Other wise it will loop again
            else:
                flagS = "yes"
        elif curHealth == MIN_HEALTH:#If the player dies, the loop will end too
            flagS = "no"

    #Say the loop has ended, but it ended with you at 0 health, the losing end credits will appear
    if curHealth == MIN_HEALTH:
        print()
        print("YOU DIED")
        print()
        print("You travelled", distance)
        print("You survived for", days)
        print()
        print("(T - T)")

    #If the player manages to survive for 7 days or travelled 150 miles, then they will have the winning credits
    if curHealth > MIN_HEALTH and (days == 7 or distance == 150):
        print("CONGRATUALTIONS! YOU SURVIVED!")
        print()
        print("Your health is", curHealth)
        print("You travelled", distance)
        print("You survived for", days)
        print()
        print("I hope you enjoyed the game \(^V^)/ ")

main()

                
            
    
