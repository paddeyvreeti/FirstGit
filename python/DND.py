# Dungeons and Dragons knockoff: Blood Moon Chronicles
import time
import sys

def type_text(text, speed=0):
    for char in text: 
        sys.stdout.write(char)
        sys.stdout. flush()
        time.sleep(speed)
    print() 
    time.sleep(0)

#Inventory definitions using dictionary
e = {}
#Function to add item to inventory
def add2inven(item, quantity =1 ):
    if item in e: 
        e[item] += quantity
    else:
        e[item] = quantity 
    type_text(f"You've picked up: {item} (x{quantity})")

#Function to delete item from inventory
def delinven(item, quantity = 1):
    if item in e: 
        if e[item] > quantity:
            inventory -= quantity
        else:
            del e[item]
        type_text(f"You used {item} x{quantity}")
    else: 
        type_text(f"You dont have any {item}")

def showe(): 
    if e: 
        for item, quanity in e.items():
            print(f"-{item} (x{quanity})")
    else: 
        type_text("You have no items.")


        

while True:
    x1 = input('Type PLAY to Start!\n').upper()
    if x1 == "PLAY":
        while True: ##### CHOOSE YOUR CHARACTER #####
            x2 = input('Would you like to play a BOY or a GIRL\n').upper()

            if x2 == 'BOY':    
                x2 = type_text("Great! His name is Marcello! He's a handsome fellow\n")
                break
            elif x2 =='GIRL':
                x2 = type_text("YAY her name it Preethi :D, she's awesome\n")
                break
            else:
                type_text("try again please\n")
         
        type_text("The world is divided between two ancient and powerful clans—the Lycans (Werewolves) and the Nosferatu (Vampires)")
        type_text("For centuries, they have fought over dominion of the night, but a fragile truce has kept the balance.")
        type_text("However, a prophecy foretells that a chosen one who transcends mortality—will tip the scales and end the war forever.")
        type_text("You are that chosen one. . .\n")
         
        while True: # Now time to choose your superpowers....
            power = input("Now, would you rather be a WEREWOLF or VAMPIRE\n").upper() 
            print()

            if power == 'WEREWOLF':
                power = type_text("Such an advantageous choice! You've possesed speed running abilities >>>>")
                break
            elif power =='VAMPIRE': 
                power = type_text("So Spooky, you think you're dracula or something?? JK you dont have to consume anything except for blood now!")
                break
            else:
                 type_text("Try Again Plz\n")
        print()
        type_text("Time for youre first quest...")
        type_text("You've recieved a letter from sombebody you used to know")
        print()

        while True: # Your first quest is coming up choosing between throwing the paper or reading it 
            quest = input("Do you THROW and burn the letter into the fire or open and READ to find out what it says?\n").upper()
            
            if quest == "THROW": #beginning of throw option
                print()
                type_text("The dry paper catches instantly, curling and blackening as the words dissolve into smoke")
                type_text("The bushes rustle around you as if something unseen was watching. . .")
                type_text("You snuggle in your sleeping bag brushing it off however sleeping uneasily")
                print()
                type_text('"Something is coming. . . "')
                print()
                type_text("You wake up to find a mysterious symbol burned into the campfire ") 
                type_text("Ponder on what the two occurences could mean as you pack up your things and hide any tracy of yourself at the encampment")
                print() 
                type_text("Stumbling across the forest, you make your merrily way trying to navigate with the shredded map Dad had in his drawer"
                "before his disappearance")
                type_text("Your map is alive... the routes ahead fade in and out, reacting only when you make decisions ")
                type_text("Coming across what looks like a fork on your way, there is a bright and sunny CLEAR road or DARK and broody unpaved path")
                print()  

                while True: 
                    quest1 = input("Which do you choose? The CLEAR path or DARK one?\n").upper()
                    if quest1 == "CLEAR": #choosing clear or dark
                         print()
                         type_text("After a few steps about to head onto what you think is the right path, the map flips out of your hands aggressively towards"
                             " the dark pathway")
                         print()
                         type_text('"What the." You say realizing theres that the air is still')
                         type_text('You try to grab the map and proceed but it revolts against your actions by burning your hands')
                         print()
                         type_text('"WHAT THE HECK IS WRONG WITH YOU" ') 
                         print()
                         type_text("It flutters towards the dark path waiting for you to go with it")
                         print()
                         type_text('"No way...", turns out that the map has a mind of its own and doesnt trust your own gut (LOL) ')
                         print()
                         time.sleep(0)
                         type_text("You roll your eyes, 'I guess Dad wasnt lying . . .' ")
                         print()
                         break
 
                    elif quest1 == "DARK": 
                         type_text('It doesnt look very welcoming, but it may be worth a shot')
                         type_text("The map glows as if it approves of your decision.")
                         type_text("Treading into the dark broody forest we go. . .")
                         break
                    else:
                        type_text("Try Again Plz\n")
                #place entirely after going down the forest        
                type_text("'I wonder what would've happened if I hadn't burned that letter. . .")
                break

            elif quest == "READ":
                 type_text("You unfold the dry paper as it appears to be an apology letter from Mom") 
                 print()
                 type_text("Dear Child,")
                 time.sleep(1)
                 type_text("If you’re reading this, then you must have found the letter I left behind.")
                 type_text("I know it’s been years since we last spoke, and I can’t imagine the anger or confusion you must be feeling. ")
                 type_text("But please, know that every decision I made, every secret I kept, was because I wanted to protect you.")
                 print()
                 time.sleep(1)
                 type_text("You have no idea what we’ve been up against, and the dangers that still lurk in the shadows.")
                 type_text("I’ve tried to shield you from the truth, but it’s time you knew—the world we live in is not as simple as it seems.")
                 type_text(" The creatures you’ve heard about in stories… they are real.")
                 time.sleep(1)
                 type_text("And the powers you’ve inherited are far more important than you realize.")
                 print()
                 time.sleep(1)
                 type_text("I didn’t want to leave, but I had no choice. ")
                 type_text("You must trust the path ahead of you, even if it leads to things you don’t understand.")
                 type_text("The map you hold in your hands… it will guide you, but only if you learn to listen to it.")
                 type_text("Don’t fear the darkness—it’s part of who you are now.")
                 print()
                 time.sleep(1)
                 type_text("d I hope this letter reaches you in time. Please, find your way. The world is waiting for you to fulfill your destiny.")
                 print()
                 time.sleep(3)
                 type_text("You stare in the abyss of darkness past the letter and campfire, filled with determination and dread")
                 type_text("Suddenly the bushes rustle around you as if something unseen was watching you. . .")
                 type_text("You snuggle in your sleeping bag brushing it off however sleeping uneasily")
                 print()
                 type_text('"Something is coming. . . "')
                 print()
                 type_text("You wake up to find a mysterious symbol burned into the campfire ") 
                 type_text("Ponder on what the two occurences could mean as you pack up your things and hide any tracy of yourself at the encampment")
                 print() 
                 type_text("It was time to hit the nearest town to restock on supplies, specifically food")
                 print()
                 type_text("Your stomach rumbles")
                 type_text("Ashford Hollow was only a while out so you decide to tread on following the map that Dad had in his drawer before his disappearance")
                 type_text("Your map is alive... the routes ahead fade in and out, reacting only when you make decisions ")
                 print()
                 type_text("You arrive at town. . . ")
                 print()
                 time.sleep(1)
                 type_text("Lets find the nearest foodstand...")
                 type_text("There is either The Crimson Stall or The Silver Fryer ")
                  
                 while True: 
                    quest2 = input("Which stand do you choose to refuel? CRIMSON or SILVER\n").upper()
                    if quest2 == "CRIMSON": 
                         print()
                         time.sleep(1)
                         type_text("This stand is run by a mysterious old woman with a crooked smile.")
                         type_text("She offers a steaming pot of “Nightshade Stew,” a dark, velvety concoction that smells both savory and unsettling. ")
                         time.sleep(    1)
                         print()
                         type_text("The stall is surrounded by shadows, despite it being midday, and there’s an odd sense of urgency in the air.")
                         type_text("The stew promises to give strength, but rumors say it’s best consumed with caution.")
                         print()
                         break
                    
                    elif quest2 == "SILVER":
                         print()
                         time.sleep(1)
                         type_text("A gleaming, brightly-lit food truck with a cheerful vendor who seems overly eager to serve you. ")
                         type_text("He offers “Silver-Leafed Fritters,” crispy golden treats stuffed with cheese and herbs, and promises they’ll provide you with energy and happiness.")
                         time.sleep(1)
                         print()
                         type_text("The fryer seems to be a popular spot, with people laughing and chatting nearby.")
                         type_text("The smell is mouth-watering, and there’s a warmth to the air around it.")
                         type_text("")
                         break
                
                    else: type_text("Try Again Plz\n") 
                     
                 type_text("You sit to enjoy your food for the time being")
                 break

            else: type_text("Try Again Plz\n")
        break
    else: 
        type_text("Invalid choice. Try again!")
        break
