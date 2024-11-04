import time
import random
import os

name = input("What is your name? ")

#Welcome
def intro():
    time.sleep(2)
    print()
    print ("The Shadow - A Choose Your Own Adventure Game")
    time.sleep(2.5)
    print()
    print ("Welcome" ,name)
    time.sleep(2)

#Introduction 1
def intro1():
    print()
    print ("This game lets you make decisions through navigating the world as the main character.")
    time.sleep(4)
    print ("Take notes, the decisions you make will impact the storyline.")
    time.sleep(1)
    print ()
    start = input("Start adventure(Y/N)? ")
    print()
    if start.lower().strip() == "n":
        print ("Come back when you are ready.")
        time.sleep(2)
        exit(code=None)
    else:
        print ("Your journey starts now.")
    time.sleep(1.2)

#Introduction 2
def intro2():
    print()
    print ("Your mother has fallen ill at the appearance of an unknown disease, which has rendered her bedridden and in an unconscious state.")
    time.sleep(5)
    print ("You learn that her illness is curable, only by a special medicine obtainable in the depths of the dark, forbidden woods.")
    time.sleep(5)
    print ("Time is running out, and you set off on a deadly adventure to obtain said medicine, hand in hand with your younger brother Jimmy Jacobs.")
    time.sleep(5)
    print ("Little do you know, of the sinister dangers that await you, and the malevolent forces that spin a thread of misfortune and death in the fabric of your story.")
    
    time.sleep(10)
    print()
    print()
    
    print ("Quest Received: Obtain potion from the secret shack")
    time.sleep(3)
    print()
    print()
    print ("Jimmy Jacobs: I don't want to go into the scary woods," ,name,".")
    print (name, ": Mom needs us. Don't worry, I'll protect you Jimmy.")
    time.sleep(4)

#The Fox: Adventurer’s Bravery
#Chapter 1 Part 1
def c1p1():
    print()
    print ("CHAPTER 1")
    time.sleep(2.5)
    print()
    print ("As you head deeper into the forest, you discover a fox.")
    print ("The fox circles you and Jimmy Jacobs, growling slightly.")
    print()
    time.sleep(5)

    print ("Jimmy Jacobs: HELP, IT'S GOING TO DEVOUR US!")
    print (name,": Stay calm, Jimmy.")
    
    time.sleep(5)
    print()
    
    print ("The fox smells the food in Jimmy Jacobs' bag and slowly approaches him.")
    time.sleep(5)
    print()

    print ("Jimmy Jacobs: AAAAAHHHH")
    time.sleep(2)
    print (name,": What part of staying calm do you not understand?")
    time.sleep(5)
    print()

    print ("Creeaaak")
    time.sleep(1)
    print ("Jimmy Jacobs: AAAHHHHHHHHHH")
    time.sleep(2)
    print (name,": Seriously?")
    time.sleep(2)
    print ("You glance to the direction of the sound and...is that a shadowy figure?")
    time.sleep(2)
    print()

    print ("Inventory: Rock and Food")
    time.sleep(2)
    print()

    scenario_1 = input("Throw the rock(R) or feed the fox(F)? ")
    if scenario_1.lower().strip() == "r":
        print ("The fox runs away in fear.")
    else:
        print ("The fox eats the food in peace and gives an assuring nod, thanking you for your kindness.")

#The Frog: Game #1
#Chapter 1 Part 2
def c1p2():
    time.sleep(2)
    print()
    print("...")
    time.sleep(2)
    print()
    print ("Along the way through the woods, you spot a frog with a pointy hat.")
    time.sleep(2.5)
    print ("Hmm, looks like it wants a rock, paper and scissors duel.")
    print()

    duel_1 = input("Would you like to duel(Y/N)? ")
    if duel_1.lower().strip() == 'n':
        time.sleep(2.5)
        print()
        print ("The frog laughs at you and runs away.")
        time.sleep(2)
        print()
        c2p2()

    else:
        time.sleep(2)
        print()
        game1()

def game1():
    print ("Welcome to your first duel. Win to obtain a reward.")
    time.sleep(1.5)
    print ("Good luck!")

    game = ["Rock", "Paper", "Scissors"]
    count = 0
    score = 0
    frogscore = 0
            
    while count == 0:
        for i in range (5):
            answer = input ("Rock(1), Paper(2) or Scissors(3)? ")

            frog = random.choice(game)
            print ("Frog picks", frog)

            if answer == "1" and frog  == "Rock":
                print ("Its a tie!")
                count +=1

            elif answer == "2" and frog  == "Paper":
                print ("Its a tie!")
                count +=1

            elif answer == "3" and frog  == "Scissors":
                print ("Its a tie!")
                count +=1

            elif answer == "1" and frog == "Scissors":
                print ("You win!")
                count +=1
                score +=1

            elif answer == "2" and frog == "Rock":
                print ("You win!")
                count +=1
                score +=1

            elif answer == "3" and frog == "Paper":
                print ("You win!")
                count +=1
                score +=1

            elif answer.upper() == "1" and frog == "Paper":
                print ("You lose!")
                count +=1
                frogscore +=1

            elif answer.upper() == "2" and frog == "Scissors":
                print ("You lose!")
                count +=1
                frogscore +=1

            elif answer.upper() == "3" and frog == "Rock":
                print ("You lose!")
                count +=1
                frogscore +=1

        time.sleep(2.5)
        print()
        print ("The duel ends.")
        time.sleep(2.5)
        print()

        if score > frogscore:
            print ("Your score is", score)
            print ("The frog's score is", frogscore)
            print ("You win!")

        if score == frogscore:
            print ("Your score is", score)
            print ("The frog's score is", frogscore)
            print ("The frog respects the tie.")

        if score < frogscore:
            print ("Your score is", score)
            print ("The frog's score is", frogscore)
            print ("The frog wins...")
            print()
            repeat_2 = input("Would you like to repeat the duel(Y/N)? ")
            print()
            if repeat_2.lower().strip() == "n":
                print ("The frog laughs at you.")
                time.sleep(2)
                print ("You clench your fist and demand another duel.")
                time.sleep(2)
                print()
                game1()

            else:
                time.sleep(2)
                game1()

    print()
    time.sleep(2.5)
    print ("Obtained: 2 Golden Tickets")
    time.sleep(2.5)
    print()
    c2p1()

#The Ship: Game #2
#Chapter 2 Part 1
def c2p1():
    print()
    print ("CHAPTER 2")
    time.sleep(2.5)
    print()

    print ("You hear the sound of running water. Finally, a river!")
    print ("There is a ship that leads near the end of the river. It requires golden tickets.")
    time.sleep(5)
    print()
    print ("You gladly pass the golden tickets and hop on the ship.")
    time.sleep(2)
    print ("The ship was incredibly huge.")
    time.sleep(2)
    print()

    print ("In the corner of your eyes, you see it. The shadowy figure. Why has it been following us?")
    time.sleep(2.5)

    print ("Soon enough, you hear the sound of music.")
    time.sleep(2.5)
    print()
    Discover = input("Would you like to discover(Y/N)? ")
    if Discover.lower().strip() == "y":
        print ("You waltz towards the source.")
        time.sleep(2)
        print()
    else:
        print ("You couldn't help yourself as you waltz towards the source.")
        time.sleep(2)
        print()

    time.sleep(2)
    print ("You spot a man with a fancy tuxedo.")
    time.sleep(2)
    print ("Jimmy Jacobs: Look, ",name,"! He's got a monocle!")
    time.sleep(2)
    print (name,": I suppose he does...why does that interest you?")
    time.sleep(2)
    print()

    print ("You start to dance slightly.")
    time.sleep(2)
    print ("What's this, the gentleman is dancing too.")
    time.sleep(3)
    print()
    print (name,": Hmm, he's got the moves but I can do better.")
    time.sleep(2)
    print ("You dance with your heart out and see the gentleman vigorously dancing too.")
    time.sleep(5)
    print()

    print ("He approaches.")
    time.sleep(2.5)
    print()

    print ("Gentleman: You sure have got the moves")
    time.sleep(2)
    print (name,": I suppose I do, better than anyone tonight.")
    time.sleep(2)
    print ("Gentleman: My, my. I bet you can't even do half of my dances.")
    time.sleep(3)
    print (name,": Oh really. Bet I can.")
    time.sleep(2)
    print ("Gentleman: If that's so. I challange you to a duel. You can win...my one of a kind axe.")
    time.sleep(3)
    print()

    duelc2p1 = input("Would you like to duel(Y/N)? ")
    if duelc2p1.lower().strip() == "y":
        game2()
    else:
        print()
        print ("Gentleman: HAH, I knew it. You couldn't even try.")
        time.sleep(2)
        print ("You clench your fist and accept the duel.")
        game2()

def game2():
    time.sleep(2)
    print()
    print ("Welcome to your second duel. Win to obtain a reward.")
    time.sleep(1.5)
    print ("Good luck!")
    time.sleep(1.5)
    print()

    print ("Gentleman: Let me explain how this will go down.")
    time.sleep(2)
    print ("Gentleman: I will do my extrodinary dances and you'll have to remember them quick.")
    time.sleep(2)
    print ("Gentleman: There will be 5 rounds. I will dance quicker and my dances will become more complex.")
    time.sleep(5)
    print()

    prepared1 = input("Are you ready(Y/N)? ")
    if prepared1.lower().strip() == "n":
        print ("Gentleman: Why? Are you not up for the challenge?")
        time.sleep(2)
        print (name, ": Well, hurry up old man")
        dancegame()
    else:
        print()
        print (name, ": Well, hurry up old man")
        dancegame()

def dancegame():
    time.sleep(2)
    print()
    print ("ROUND 1")
    time.sleep(3)
    print()
    
    print ("Moonwalk, Dougie, Twist", end = "\r")
    time.sleep(3)

    ingredient = input("..What are the dances? ")
    if ingredient.lower().strip() == "moonwalk, dougie, twist":
        print()
        time.sleep(2)
        print()
    else:
        print()
        print ("Gentleman: What's wrong? Are my dances too hard?")
        time.sleep(2)
        print ("You clench your fist and try again.")
        dancegame()

    print ("ROUND 2")
    time.sleep(2)
    print()

    print ("Single Ladies, Jump, Tango", end = "\r")
    time.sleep(2.5)

    ingredient = input(".....What are the dances? ")
    if ingredient.lower().strip() == "single ladies, jump, tango":
        print ()
        time.sleep(2)
        print()
    else:
        print()
        print ("Gentleman: What's wrong? Are my dances too hard?")
        time.sleep(2)
        print ("You clench your fist and try again.")
        dancegame()

    print ("ROUND 3")
    time.sleep(2.5)
    print()

    print ("Cha Cha, Body Rolls, Rumba", end = "\r")
    time.sleep(2.3)

    ingredient = input(".....What are the dances? ")
    if ingredient.lower().strip() == "cha cha, body rolls, rumba":
        print ()
        time.sleep(2)
        print()
    else:
        print()
        print ("Gentleman: What's wrong? Are my dances too hard?")
        time.sleep(2)
        print ("You clench your fist and try again.")
        dancegame()

    print ("ROUND 4")
    time.sleep(2.5)
    print()

    print ("Kangsta Wok, Capoeira, Pirouette", end = "\r")
    time.sleep(2.3)

    ingredient = input("...........What are the dances? ")
    if ingredient.lower().strip() == "kangsta wok, capoeira, pirouette":
        print()
        time.sleep(2)
        print()

        print ("ROUND 5")
        time.sleep(2)
        print()

        print ("Arabesque, Ciseaux, Stanky Leg", end = "\r")
        time.sleep(1.5)

        ingredient = input(".........What are the dances? ")
        if ingredient.lower().strip() == "arabesque, ciseaux, stanky leg":
            time.sleep(2)
            print()
            print ("Gentleman: Wow, you've outdone me.")
            time.sleep(1)
            print ("Gentleman: You really do mean what you say. You got my respect.")
            time.sleep(3)
            print ("Gentleman: Have my axe. You earned it.")
            time.sleep(2)
            print()
            print ("Out of respect, you thanked the gentleman.")
            time.sleep(3)
            print()
            print ("You left the ship the next morning")
            time.sleep(4)
            c3()
        else:
            print()
            print("...")
            time.sleep(2)
            print ("Gentleman: Not bad. You sure got the moves.")
            time.sleep(2)
            print ("Gentleman: Hmm, fine. I suppose you can have my axe.")
            time.sleep(2)
            print()
            print ("Out of respect, you thanked the gentleman.")
            time.sleep(3)
            print()
            print ("You left the ship the next morning")
            time.sleep(4)
            print()
    else:
        print()
        print ("...")
        time.sleep(2)
        print ("Gentleman: Not bad. You sure got the moves.")
        time.sleep(2)
        print ("Gentleman: Hmm, fine. I suppose you can have the axe.")
        time.sleep(2)
        print()
        print ("Out of respect, you and Jimmy Jacobs thanked the gentleman.")
        time.sleep(3)
        print()
        print()
        print ("You left the ship the next morning")
        time.sleep(4)
        print()
    c3()
    
#The Old House: Game #3
#Chapter 2 Chapter 2 Part 2
def c2p2():
    print()
    print ("CHAPTER 2")
    time.sleep(2.5)
    print()

    print ("You hear the sound of running water. Finally, a river!")
    time.sleep(2)
    print ("There is a ship that leads near the end of the river. It requires golden tickets.")
    time.sleep(3)
    print()
    print (name, ": Too bad we don't have any golden tickets.")
    time.sleep(3)
    print()
    print ("You choose to follow the river's path through the woods")
    time.sleep(2)
    print()
    
    print ("You stumble upon an old house that smells strange.")
    time.sleep(2.5)
    print ("In the corner of your eyes, you see it. The shadowy figure.") 
    time.sleep(4)
    print()
    print("...")
    time.sleep(2)
    print ("Why has it been following us?")
    time.sleep(2)
    print("An old lady appears from the house and gestures you to join her inside.")
    time.sleep(2)
    print()
    
    input ("Do you want to go inside(Y/N)? ")
    print ("As dusk falls, Jimmy Jacobs was too afraid to venture out so you decided to stay the night.")
    time.sleep(2.5)
    print()

    print ("???: What are your names children?")
    time.sleep(3)
    print ("Jimmy Jacobs: The name's Jimmy and this is my older sibling" ,name, ".")
    time.sleep(2)
    print ("Jimmy Jacobs: What is yours?")
    time.sleep(3)
    print()
    print ("Martha: My name's Martha. Oh, and I had recently made some peanut butter omlettes.")
    time.sleep(5)
    print ("Martha: You're welcome to have some, children.")
    time.sleep(2)
    print()
    print ("Jimmy Jacobs: Yes please, I'm starving.")
    time.sleep(3)
    print (name, ": Umm...I'll pass on this one. Thank you.")
    time.sleep(3)
    print()
    print ("Martha glares at you")
    time.sleep(3)
    print()
    print ("Martha: Suit yourself, picky child.")
    time.sleep(3)
    print()
    print()

    print ("You stay the night")
    time.sleep(4)
    print()
    print()

    print ("Day has come and you see Jimmy eating one of her odd dishes")
    time.sleep(4)
    print ("Jimmy Jacobs: It's really good,",name,".")
    time.sleep(3)
    print ("Martha: If you weren't so picky, you'd actually love my dishes.")
    time.sleep(3)
    print()
    print("...")
    time.sleep(2)
    print (name, ": No thanks, the dishes look...")
    time.sleep(1)
    print (name, ": unedible...")
    time.sleep(4)
    print()
    print ("Martha's jaws are on the floor")
    time.sleep(2)
    print()
    print ("Martha: How dare you call my divine dishes...unedible! They must be too rich and complex for your taste.")
    time.sleep(5)
    print (name, ": Oh really? I bet you I can make them easily.")
    time.sleep(3)
    print()

    print ("Martha: Well, how about a duel? You sure talk a lot.")
    time.sleep(3)
    print ("Martha: You can have my new axe if you can make this difficult dish better than me.")
    time.sleep(4)
    print (name, ": Deal.")
    time.sleep(1)
    print()

    duel_2 = input ("Would you like to duel(Y/N)? ")
    if duel_2.lower().strip() == "n":
        print()
        print ("Martha: What's wrong? I knew my dishes are too complex.")
        time.sleep(3)
        print ("You clench your fist and accept the duel Martha.")
        game3()
    else:
        print("You duel Martha.")
        game3()
        
def game3():
    time.sleep(2)
    print()
    print ("Welcome to your second duel. Win to obtain a reward.")
    time.sleep(1.5)
    print ("Good luck!")
    time.sleep(1.5)
    print()

    print ("Martha: Let me explain how this will go down.")
    time.sleep(2)
    print ("Martha: I will tell you my secret ingredients and you'll have to remember them quick.")
    time.sleep(2)
    print ("Martha: There will be 5 rounds. The time you memorize these ingredients will be shorter and the ingredients will become more complex.")
    time.sleep(5)
    print ("Martha: You snooze, you lose child.")
    time.sleep(5)
    print()

    prepared2 = input("Are you ready(Y/N)? ")
    if prepared2.lower().strip() == 'n':
        print()
        print ("Martha: I guess my dish is too divine.")
        time.sleep(2)
        print (name,": Bring it on, Martha")
        cookinggame()
    else:
        print()
        print (name, ": Bring it on, Martha")
        cookinggame()

def cookinggame():

    time.sleep(2)
    print()
    print ("ROUND 1")
    time.sleep(3)
    print()
    
    print ("Flour, Sugar, Eggs", end = "\r")
    time.sleep(3)

    ingredient = input("What are the ingredients? ")
    if ingredient.lower().strip() == "flour, sugar, eggs":
        print ()
        time.sleep(2)
        print()
    else:
        print()
        print ("Martha: Oh, you poor child.")
        time.sleep(2)
        print ("You clench your fist and try again.")
        cookinggame()

    print ("ROUND 2")
    time.sleep(2)
    print()

    print ("Cheese, Mushroom, Banana", end = "\r")
    time.sleep(2.5)

    ingredient = input("What are the ingredients? ")
    if ingredient.lower().strip() == "cheese, mushroom, banana":
        print ()
        time.sleep(2)
        print()
    else:
        print()
        print ("Martha: Hahaha, try again child.")
        time.sleep(2)
        print ("You clench your fist and try again.")
        cookinggame()

    print ("ROUND 3")
    time.sleep(2.5)
    print()

    print ("Vanilla, Quinoa, Oats", end = "\r")
    time.sleep(2)

    ingredient = input("What are the ingredients? ")
    if ingredient.lower().strip() == "vanilla, quinoa, oats":
        print ()
        time.sleep(2)
        print()
    else:
        print()
        print ("Martha: Oh, you were so close.")
        time.sleep(2)
        print ("You clench your fist and try again.")
        cookinggame()

    print ("ROUND 4")
    time.sleep(2.5)
    print()

    print ("Magnolia, Chickweed, Whitchetty Grub", end = "\r")
    time.sleep(2.3)

    ingredient = input("..........What are the ingredients? ")
    if ingredient.lower().strip() == "magnolia, chickweed, whitchetty grub":
        print()
        time.sleep(2)
        print()

        print ("ROUND 5")
        time.sleep(2)
        print()

        print ("Bruschetta, Beignet, Anise", end = "\r")
        time.sleep(1.5)

        ingredient = input("What are the ingredients? ")
        if ingredient.lower().strip() == "bruschetta, beignet, anise":
            time.sleep(2)
            print()
            print ("Martha: Wow, you've outdone me.")
            time.sleep(1)
            print ("Martha: You really do mean what you say. You got my respect, child. Have this axe.")
            time.sleep(2)
            print()
            print ("Out of respect, you thanked Martha.")
            time.sleep(3)
            print()
            print("You left the next morning, thanking Martha for the stay")
            time.sleep(4)
            c3()

        else:
            print()
            print ("...")
            time.sleep(2)
            print ("Martha: Not bad, I'm impressed.")
            time.sleep(1)
            print ("Martha: Fine, you can have the axe.")
            time.sleep(2)
            print()
            print ("Out of respect, you thanked Martha.")
            time.sleep(3)
            print()
            print("You left the next morning, thanking Martha for the stay")
            time.sleep(4)
            print()
    else:
        print()
        print ("...")
        time.sleep(2)
        print ("Martha: Not bad, I'm impressed.")
        time.sleep(1)
        print ("Martha: Fine, you can have the axe.")
        time.sleep(2)
        print()
        print ("Out of respect, you thanked Martha.")
        time.sleep(3)
        print()
        print()
        print("You left the next morning, thanking Martha for the stay")
        print()
        time.sleep(4)
        print()
    c3()

#The Cabin: Mrs. Pelgrem
#Chapter 3
def c3():
    print()
    print ("Your journey continues.")
    time.sleep(2)
    print()
    print()

    print ("Creeaaak")
    time.sleep(1)
    print ("You hear that eerie sound again. You glanced away and see a lovely garden and...Jimmy?")
    time.sleep(4)
    print()
    print (name, ": WHAT ARE YOU DOING?")
    time.sleep(2)
    print ("Jimmy Jacobs: Sorry, I'm really hungry.")
    time.sleep(3)
    print()

    print ("???: Hey!")
    time.sleep(1)
    print ("???: What are you doing there?")
    time.sleep(2)

    print ("Jimmy Jacobs: Nothing.")
    time.sleep(2)
    print ("???: With my tomatoes in your hands?")
    time.sleep(2)
    print()

    print (name, ": Sorry, excuse him.")
    time.sleep(2)
    print ("Jimmy Jacobs: The name is Jimmy Jacobs and beside me is" ,name)
    time.sleep(3)
    print ("???: Pelgrem, Mrs. Pelgrem. It's fine. It's getting dark, would you like to stay the night?")
    time.sleep(4)
    print()

    input("Stay the night(Y/N)? ")
    print("Jimmy Jacobs: Yes, please")
    time.sleep(1)
    print()
    print("...nevermind")
    time.sleep(2)
    print()

    print("You enter Mrs. Pelgrem's cabin.")
    time.sleep(4)
    print()

    print("Pelgrem: So what brings you children here?")
    time.sleep(2)
    print("Jimmy Jacobs: We're on a journey to get medicine for mama.")
    time.sleep(4)
    print("Jimmy Jacobs: She's gone ill...")
    time.sleep(5)

    print()
    print("You spot a tear in Jimmy's eye")
    time.sleep(3)
    print()

    print("Pelgrem: I am so sorry to hear that, dear.")
    time.sleep(2)
    print()
    comfort = input("Would you like to comfort Jimmy(Y/N)? ")
    if comfort.strip().lower() == 'y':
        print("You hug Jimmy in an effort to comfort him")
        time.sleep(2)
        print()
        print(name, ": She'll be fine, don't worry.")
    else:
        print()
        print(name, ": Don't cry, toughen up. She'll be okay.")

    time.sleep(4)
    print("Pelgrem: You two will make it through this, together. I just know it.")
    time.sleep(4)
    print("Pelgrem: It's getting late, you children should rest up.")
    time.sleep(5)

    print()
    print()
    print ("You stay the night")
    time.sleep(4)
    print()
    print()
    
    print("Pelgrem: Before you go, I want to give you something.")
    time.sleep(3)
    print("Jimmy: Is that a bike!!")
    time.sleep(2)
    print("Pelgrem: It's not much but it'll help you through your journey.")
    time.sleep(4)
    print()
    print (name, ": Thank you so much, Mrs. Pelgrem.")
    time.sleep(2)
    print ("Pelgrem: No worries, have a safe journey. If there is anything, you are more than welcome to come by.")
    time.sleep(5)
    print ("Pelgrem: Also, keep an eye out for this black cat that lurks around the area. It will claw your eyes out.")
    time.sleep(6)
    print (name, ": Will do...")
    time.sleep(3)
    print()

def hollowtree():
    print()
    print ("Your journey continues along the river.")
    time.sleep(3)
    print()
    print()

    print ("Along the road, you hear scratches inside of a hollow tree.")
    time.sleep(3)
    print ("You approach the tree and hear horrendous growls.")
    time.sleep(3)
    print()

    print ("Jimmy Jacobs: Ohh, it's got to be a poor animal stuck in there. We have to save it!")
    time.sleep(5)
    print (name, ": What if it's the black cat Mrs. Pelgrem warned us about?")
    time.sleep(3)
    print ("Jimmy Jacobs: But...")
    time.sleep(2)

    print()
    print ("Inventory: Brand New Axe")
    time.sleep(2)
    print()

    chop1 = input("Would you like to free the creature(Y/N)? ")
    print()
    if chop1.lower().strip() == "y":
        print ("You carefully chopped the tree open to see two glowing amber eyes staring back at you.")
        time.sleep(4)
        print ("You spot matted black fur. The cat!")
        time.sleep(2)
        print()

        print ("Prepare yourself, Jimmy.")
        time.sleep(2)
        print ("The cat darted a glance and walked away peacefully.")
        time.sleep(2)
        print ("Jimmy Jacobs: Phew.")
        time.sleep(2)
        print()

        savecat = "save"

    else:
        peak = input ("Would you like to take a peak(Y/N)? ")
        print()
        if peak.lower().strip() == "y":
            print ("You see two glowing amber eyes staring back at you.")
            time.sleep(3)
            print (name, ": Creepy. Definitely the cat.")
            time.sleep(2)
            print()

            chop2 = input("Would you like to free the cat(Y/N)? ")
            print()
            if chop2.lower().strip() == "y":
                print ("You carefully chopped the tree open to see two glowing amber eyes staring back at you.")
                time.sleep(4)
                print()

                print ("Prepare yourself, Jimmy.")
                time.sleep(2)
                print ("The cat darted a glance and walked away peacefully.")
                time.sleep(2)
                print ("Jimmy Jacobs: Phew.")
                time.sleep(2)
                print()
                
                savecat = "save"
                
            else:
                print()
                print ("Jimmy Jacobs: It's inhumane.")
                time.sleep(2)
                print (name, ": It'll probably get out on it's own.")
                time.sleep(1)
                print (name, ": It's best to be safe, Jimmy")
                print()

                savecat = "nosave"
        else:
            print()
            print ("Jimmy Jacobs: It's inhumane.")
            time.sleep(2)
            print (name, ": It'll probably get out on it's own.")
            time.sleep(1)
            print (name, ": It's best to be safe, Jimmy")
            print()

            savecat = "nosave"

    return savecat

#The Hunt Game
#Chapter 4
def c4():
    print()
    print()
    print ("Your journey continues as you and Jimmy bike along the river.")
    time.sleep(4)
    print()
    print()

    print ("Jimmy Jacobs: I can't wait to see mama again.")
    time.sleep(2)
    print (name, ": Me too.")
    time.sleep(2)
    print()

    print ("Jimmy Jacobs: WATCH OUT!")
    time.sleep(1)
    print ("You look in front of you to see a log.")
    time.sleep(2)
    print()

    print ("WHAAAAM")
    time.sleep(2)
    print (name, ": I'm so sorry, Jimmy. I didn't see it.")
    time.sleep(2)
    print()

    time.sleep(2.5)
    print ("Creeeaaaak")
    time.sleep(2.5)
    print()
    print ("...")
    time.sleep(2)

    print ("You look behind you to see the monster inches away.")
    time.sleep(2)
    print ("You gripped Jimmy Jacobs' hand and immediately raced on the bike, startling Jimmy Jacobs.")
    time.sleep(5)
    print()

    print ("Jimmy Jacobs: UMM WHY ARE YOU SPEEDING?")
    time.sleep(2)
    print (name, ": The monster.")
    time.sleep(1)
    print ("Jimmy Jacobs: THE WHAT!?")
    time.sleep(1)
    print()
    route1()

def route1():
    print ("No time for welcomes")
    time.sleep(2.5)
    print()
    
    choice1 = input("You are by the river side. Turn left or right(L/R)? ")
    if choice1.lower().strip() == "l":
        print("You begin to cycle left.")
        print()
    else:
        print("You begin to cycle right.")
        print()


    choice2 = input("You are on a dirt road. Turn left or right(L/R)? ")
    if choice2.lower().strip() == "l":
        print("You turned left.")
        print()
    else:
        print("You turned right.")
        print()


    choice3 = input("You see a danger sign. Go the dangerous route?(Y/N)? ")
    if choice3.lower().strip() == "y":
        print ("Jimmy Jacobs: ARE YOU BLIND!")
        time.sleep(1)
        print (name, ": TRUST ME, JIMMY!")
        print()
        route2p1()
    else:
        print ("Jimmy Jacobs: HURRY IT ALMOST GOT US!")
        time.sleep(1)
        print (name, ": TRUST ME, JIMMY!")
        print()
        route2p2()

def route2p1():
    choice4_1 = input("You are on a rocky path. Turn left or right(L/R)? ")
    if choice4_1.lower().strip() == "l":
        print ("WOOSH")
        time.sleep(2)
        print ("A giant branch swings and hits the monster.")
        time.sleep(1)
        print ("The monster hides into the darkness.")
        print()
    else:
        print ("WOOSH")
        time.sleep(2)
        print ("A giant branch swings and hits the monster.")
        time.sleep(2)
        print ("The monster cowers.")
        print()

    choice5_1 = input("You see masses of white strings tied to two trees on your path. Duck(Y/N)? ")
    if choice5_1.lower().strip() == "n":
        print ("You squint your eyes and see... SPIDERS!")
        time.sleep(1)
        print ("WHAAM")
        time.sleep(2)
        print ("You run into the ginormous cobweb.")
        time.sleep(1)
        print ("Jimmy Jacobs: WHAT IS WRONG WITH YOU!")
        time.sleep(2)
        print (name, ": SORRY!")
        time.sleep(2)
        print()
        print ("The monster turns left and disappears into the darkness.")
        time.sleep(4)

    else:
        print ("You squint your eyes and see... SPIDERS!")
        time.sleep(1)
        print (name, ": DUCK, JIMMY!")
        time.sleep(2)
        print()
        print ("The monster turns left and disappears into the darkness.")
        time.sleep(4)

def route2p2():
    choice5_2 = input("You see a log in front of you. Ride over it(Y/N)? ")
    if choice5_2.lower().strip() == "y":
        print("Jimmy Jacobs: HEY, WATCH IT!")
        time.sleep(1)
        print(name, ": SORRY!")
        print()

    choice6_2 = input("You see a meadow filled with tall flowers. Go through the flowers(Y/N)? ")
    if choice6_2.lower().strip() == "y":
        print ("Jimmy Jacobs: ARE YOU BLIND!")
        time.sleep(1)
        print (name, ": TRUST ME, JIMMY!")
        time.sleep(2)
        print()
        print ("The monster disappears into the field of tall flowers.")
        time.sleep(4)
    else:
        print ("You follow the clear path.")
        time.sleep(2)
        print()
        print ("The monster disappears into the field of tall flowers.")
        time.sleep(4)

#The Cave: The Adventurer's Fate
#Chapter 5
def c5():
    print()
    print ("You lost the monster.")
    time.sleep(2)
    print ("It's getting dark. You see a cave.")
    time.sleep(2.5)
    print()

    input ("Would you like to hide inside(Y/N)? ")
    print ("Jimmy Jacobs runs inside the cave, trembling in fear. You follow.")
    time.sleep(3)
    print()
    print ("Jimmy Jacobs: I'm scared.")
    time.sleep(1)
    print (name, ": We'll be alright, Jimmy. Don't worry.")
    time.sleep(4)
    print()
    print()

    print ("You huddled in the cave until the morning comes.")
    time.sleep(4)
    print()
    print()

    print (name, ": We have to get going fast while it's still dark out this early in the morning.")
    time.sleep(5)
    print (name, ": If we go now, I'm sure we can make it to Mrs. Plegrem's cabin.")
    time.sleep(4)
    print()

    print (name, ": Jimmy, we have to go.")
    time.sleep(2)
    print ("Jimmy Jacobs: Please, we should stay. What if the monster is out there.")
    time.sleep(4)
    print (name, ": Either way, we can't stay here forever. Mama's condition gets worse by the day.")
    time.sleep(6)
    print ("Jimmy Jacobs: ...")
    time.sleep(4)
    print()

    print ("He is visibly shaking.")
    time.sleep(3)
    print()

    jimmyfate = input ("Would you leave him alone to come back(1), stay with him(2) or convince him to leave the cave(3)? ")
    if jimmyfate == "1":
        jimmyfate == "1"
        print()
        print (name, ": Fine, I'll go back to Mrs. Pelgrem's cabin for help and come back.")
        time.sleep(4)
        print ("Jimmy Jacobs: Wait, you're going. Please don't leave me.")
        time.sleep(3)
        print ("Jimmy Jacobs: I'm scared.")
        time.sleep(2)
        print (name, ": It's alright. I'll be back, I promise.")
        time.sleep(6)
        print()
    elif jimmyfate == "2":
        jimmyfate = "2"
        print()
        print (name, ": It's alright. I'll stay with you Jimmy.")
        time.sleep(2)
        print (name, ": Just for a little while longer. We still have to leave, you know.")
        time.sleep(3)
        print ("Jimmy Jacobs: Thank you. We can leave when it gets brighter outside.")
        time.sleep(3)
        print (name, ": Fine.")
        time.sleep(2)
        print()
        print ("You decide to stay with him for a while before finally leaving.")
        time.sleep(6)
        print()
    else:
        jimmyfate = "3"
        print()
        print (name, ": If we stay here, the monster will soon find us.")
        time.sleep(2)
        print ("Jimmy Jacobs: The monster will find us even if we go outside.")
        time.sleep(3)
        print (name, ": It's dark outside, meaning we can hide in the darkness and try to make no noise.")
        time.sleep(6)
        print ("Jimmy Jacobs: How would we know if the monster is not outside.")
        time.sleep(3)
        print()

        print (name, ": I'll poke my head out and listen for any sounds.")
        time.sleep(3)
        print (name, ": If there aren't, it should be safe.")
        time.sleep(2)
        print ("Jimmy Jacobs: Okay.")
        time.sleep(2)
        print()

        print ("You silently poke your head out, waiting for any noise.")
        time.sleep(3)
        print (name, ": None, let's go.")
        time.sleep(2)
        print ("Jimmy Jacobs: Okay.")
        time.sleep(2)
        print (name, ": It's alright Jimmy, I'll protect you.")
        time.sleep(6)
        print()

    return jimmyfate

#THE ENDING
def realending(jimmyfate, savecat):

    print()
    #Good Ending 
    if savecat == "save" and jimmyfate == "3": #save cat and convinced Jimmy to leave
        print("You and Jimmy Jacob walk quietly out the cave, leaving the bicycle behind.")
        time.sleep(5)
        print()
        print()
        
        print("After a while...")
        time.sleep(2.5)
        print("Creeeaak")
        time.sleep(2)
        print()

        print(name, ": RUN, JIMMY!")
        time.sleep(1)
        print("You grab Jimmy's hand and run as fast as you can.")
        time.sleep(2)
        print("You spot Mrs. Pelgrem's cabin lit up in the dark.")
        time.sleep(2)
        print()

        print("You and Jimmy dash to Mrs. Pelgrem's house.")
        time.sleep(2)
        print()
        
        print("CREEEEAAAAKKK")
        time.sleep(1)
        print("Jimmy Jacobs: HURRY, IT'S GETTING CLOSER!")
        time.sleep(2)
        print()

        print("You and Jimmy keep running until you hear hisses and screams followed by silence.")
        time.sleep(4)
        print()

        print("You start banging on the door to see Mrs. Pelgrem with hair rollers on.")
        time.sleep(2)
        print("Jimmy Jacobs: AAAHHHH")
        time.sleep(2)
        print("Pelgrem: Rude...What's happening?")
        time.sleep(2)
        print("Jimmy Jacobs: The monster.")
        time.sleep(1)
        print("Pelgrem: THE WHAT?!")
        time.sleep(3)
        print()

        print("You explained everything to Mrs. Pelgrem and she agreed to let you stay until the coast is clear.")
        time.sleep(6)
        print("Pelgrem: My husband will be back by the afternoon, we shall wait till then.")
        time.sleep(4)
        print("Pelgrem: Don't worry, children. You are safe.")
        time.sleep(5)
        print()

        print("You hug Jimmy Jacobs with tears in your eyes.")
        time.sleep(3)
        print(name, ": We're safe. We're finally safe. We can get the medicine with Mrs. Pelgrem and her husband once the coast is clear.")
        time.sleep(8)
        print()

        print("In the moment, you glance out the window to see")
        time.sleep(3)
        print("A sweet old man...")
        time.sleep(5)
        print("Why is he staring back at me?")
        time.sleep(4)
        print()
        print ("With a smile and a scar on his face.")

    #Bad Ending 1
    elif savecat == "nosave" and jimmyfate == "3": #NOT save cat and convinced Jimmy to leave
        print("You and Jimmy Jacob walk quietly out the cave, leaving the bicycle behind.")
        time.sleep(5)
        print()
        print()

        print("After a while...")
        time.sleep(2.5)
        print("Creeeaak")
        time.sleep(2)
        print()

        print(name, ": RUN, JIMMY!")
        time.sleep(1)
        print("You grab Jimmy's hand and run as fast as you can.")
        time.sleep(2)
        print("You spot Mrs. Pelgrem's cabin lit up in the dark.")
        time.sleep(2)
        print()

        print("You and Jimmy dash to Mrs. Pelgrem's house.")
        time.sleep(2)
        print()

        print("CREEEEAAAAKKK")
        time.sleep(1)
        print("Jimmy Jacobs: HURRY, IT'S GETTING CLOSER!")
        time.sleep(2)
        print()

        print("You start banging on the door to see Mrs. Pelgrem with hair rollers on.")
        time.sleep(2)
        print("Jimmy Jacobs: AAAHHHH")
        time.sleep(2)
        print("Pelgrem: Rude...What's happening?")
        time.sleep(2)
        print("Jimmy Jacobs: The monster.")
        time.sleep(1)
        print("Pelgrem: THE WHAT?!")
        time.sleep(3)
        print()

        print("You explained everything to Mrs. Pelgrem and she agreed to let you stay until the coast is clear.")
        time.sleep(6)
        print("Pelgrem: My husband will be back by the afternoon, we shall wait till then.")
        time.sleep(4)
        print("Pelgrem: Don't worry, children. You are safe.")
        time.sleep(5)
        print()

        print("You hug Jimmy Jacobs with tears in your eyes.")
        time.sleep(3)
        print(name, ": We're safe. We're finally safe. We can get the medicine with Mrs. Pelgrem and her husband once the coast is clear.")
        time.sleep(8)
        print()
        
        print("Knock, Knock")
        time.sleep(2)
        print("You look through the window.")
        time.sleep(4)
        print()

        print("Huh, just a sweet old man...")

    #Neutral Ending
    elif savecat == "save" and jimmyfate == "2": #save cat and stayed with Jimmy
        print("Staying a while longer in the cave with Jimmy Jacobs turned out to be two days.")
        time.sleep(5)
        print()
        print()

        print(name, ": I can't do this. We're both thirsty, hungry and in pain. We have to go.")
        time.sleep(5)
        print("Suddenly, you hear...")
        time.sleep(2.5)
        print()

        print("Creeeaak")
        time.sleep(2)
        print()

        print(name, ": RUN, JIMMY!")
        time.sleep(1)
        print("You grab Jimmy's hand and run as fast as you can.")
        time.sleep(2)
        print("You spot Mrs. Pelgrem's cabin lit up in the dark.")
        time.sleep(2)
        print()

        print("You and Jimmy dash to Mrs. Pelgrem's house.")
        time.sleep(2)
        print()

        print("CREEEEAAAAKKK")
        time.sleep(1)
        print("Jimmy Jacobs: HURRY, IT'S GETTING CLOSER!")
        time.sleep(2)
        print()

        print("You and Jimmy keep running until you hear hisses and screams followed by silence.")
        time.sleep(4)
        print()

        print("You start banging on the door to see Mrs. Pelgrem with hair rollers on.")
        time.sleep(2)
        print("Jimmy Jacobs: AAAHHHH")
        time.sleep(2)
        print("Pelgrem: Rude...What's happening?")
        time.sleep(2)
        print("Jimmy Jacobs: The monster.")
        time.sleep(1)
        print("Pelgrem: THE WHAT?!")
        time.sleep(3)
        print()

        print("You explained everything to Mrs. Pelgrem and she agreed to let you stay until the coast is clear.")
        time.sleep(6)
        print("Pelgrem: My husband will be back by the afternoon, we shall wait till then.")
        time.sleep(4)
        print("Pelgrem: Don't worry, children. You are safe.")
        time.sleep(5)
        print()

        print("You hug Jimmy Jacobs with tears in your eyes.")
        time.sleep(3)
        print(name, ": We're safe. We're finally safe. We can get the medicine with Mrs. Pelgrem and her husband once the coast is clear.")
        time.sleep(8)
        print()

        print(name, ": Umm, you can stop crying now.")
        time.sleep(2)
        print("Jimmy Jacobs: No...it's too late.")
        time.sleep(2.5)
        print()

        print("Jimmy Jacobs: We killed mama.")
        time.sleep(4)
        print(name, ": No...no I'm sure we have time. Don't say that.")
        time.sleep(5)
        print()

        print("In the moment, you glance out the window to see")
        time.sleep(3)
        print("A sweet old man...")
        time.sleep(5)
        print("Why is he staring back at me?")
        time.sleep(4)
        print()
        print ("With a smile and a scar on his face.")


    #Bad Ending 2
    elif savecat == "nosave" and jimmyfate == "2": #NOT save cat and stayed with Jimmy
        print("Staying a while longer in the cave with Jimmy Jacobs turned out to be two days.")
        time.sleep(5)
        print()
        print()

        print(name, ": I can't do this. We're both thirsty, hungry and in pain. We have to go.")
        time.sleep(5)
        print("Suddenly, you hear...")
        time.sleep(2.5)
        print()

        print("Creeeaak")
        time.sleep(2)
        print()

        print(name, ": RUN, JIMMY!")
        time.sleep(1)
        print("You grab Jimmy's hand and run as fast as you can.")
        time.sleep(2)
        print("You spot Mrs. Pelgrem's cabin lit up in the dark.")
        time.sleep(2)
        print()

        print("You and Jimmy dash to Mrs. Pelgrem's house.")
        time.sleep(2)
        print()

        print("CREEEEAAAAKKK")
        time.sleep(1)
        print("Jimmy Jacobs: HURRY, IT'S GETTING CLOSER!")
        time.sleep(2)
        print()

        print("You start banging on the door to see Mrs. Pelgrem with hair rollers on.")
        time.sleep(2)
        print("Jimmy Jacobs: AAAHHHH")
        time.sleep(2)
        print("Pelgrem: Rude...What's happening?")
        time.sleep(2)
        print("Jimmy Jacobs: The monster.")
        time.sleep(1)
        print("Pelgrem: THE WHAT?!")
        time.sleep(3)
        print()

        print("You explained everything to Mrs. Pelgrem and she agreed to let you stay until the coast is clear.")
        time.sleep(6)
        print("Pelgrem: My husband will be back by the afternoon, we shall wait till then.")
        time.sleep(4)
        print("Pelgrem: Don't worry, children. You are safe.")
        time.sleep(5)
        print()

        print("You hug Jimmy Jacobs with tears in your eyes.")
        time.sleep(3)
        print(name, ": We're safe. We're finally safe. We can get the medicine with Mrs. Pelgrem and her husband once the coast is clear.")
        time.sleep(8)
        print()

        print(name, ": Umm, you can stop crying now.")
        time.sleep(2)
        print("Jimmy Jacobs: No...it's too late.")
        time.sleep(2.5)
        print()

        print("Jimmy Jacobs: We killed mama.")
        time.sleep(2)
        print("Jimmy Jacobs: ITS TOO LATE! WE KILLED HER!")
        time.sleep(4)
        print("...")
        time.sleep(2)
        print()

        print("Knock, Knock")
        time.sleep(2)
        print("You look through the window.")
        time.sleep(4)
        print()

        print("Huh, just a sweet old man...")

    #Bad Ending 3
    else: #left Jimmy
        print("You left Jimmy Jacobs in the cave alone.")
        time.sleep(5)
        print()
        print()

        print("Suddenly, you hear...")
        time.sleep(2.5)
        print("Creeeaak")
        time.sleep(2)
        print()

        print("You run, as fast as you can.")
        time.sleep(2)
        print("You spot Mrs. Pelgrem's cabin lit up in the dark.")
        time.sleep(2)
        print()

        print("Without thinking, you dash to Mrs. Pelgrem's house.")
        time.sleep(2)
        print()

        print("CREEEEAAAAKKK")
        time.sleep(1)
        print(name, ": AAHHHHHHH")
        time.sleep(2)
        print("You run faster than ever.")
        time.sleep(2)
        print()

        print("You started banging on the door to see Mrs. Pelgrem with hair rollers on.")
        time.sleep(3)
        print(name, ": LET ME IN!! NOW!")
        time.sleep(2)
        print("Pelgrem: Rude...What's happening?")
        time.sleep(2)
        print(name, ": NO TIME FOR THAT TOO! JIMMY IS OUT THERE IN A CAVE ALONE!")
        time.sleep(3)
        print("Pelgrem: IN A CAVE??!!! ALONE?!")
        time.sleep(3)
        print()

        print("You explained everything to Mrs. Pelgrem and she offered to help.")
        time.sleep(5)
        print()

        print("The both of you sprinted to the cave only to find...")
        time.sleep(4)
        print("His backpack? The bicylce too...")
        time.sleep(4)
        print()

        print(name, ": No...he probably went out to look for me.")
        time.sleep(4)
        print(name, ": Right?")
        time.sleep(3)
        print("Pelgrem: ...")
        time.sleep(6)
        print()

        print(name, ": He'll be back...right?")

def endingmessage():
    time.sleep(10)
    print()
    print ("If you have made it this far. Thank you so much for playing.")
    time.sleep(3)
    print ("Hope you enjoyed it!")
    time.sleep(3)
    print()

def chapters():
    print()
    print ("CHAPTERS")
    print()
    print ("1. INTRO")
    print ("2. INTRO 2")
    print ("3. CHAPTER 1 PART 1 - The Fox")
    print ("4. CHAPTER 1 PART 2 - Frog Duel")
    print ("5. CHAPTER 2 PART 1 - Dancing Game")
    print ("6. CHAPTER 2 PART 2 - Cooking Game")
    print ("7. CHAPTER 3 - Mrs. Pelgrem")
    print ("8. CHAPTER 4 - Hunt Game")
    print ("9. CHAPTER 5 - Fate")
    print ("10. THE ENDING")
    print()
    chapterplay()

def chapterplay():
    chapterplay = int(input("Which chapter would you like to play? "))
    if chapterplay == 1:
        intro1()
        intro2()
        c1p1()
        c1p2()
        savecat = hollowtree()
        c4()
        jimmyfate = c5()
        realending(jimmyfate, savecat)
        endingmessage()

    elif chapterplay == 2:
        intro2()
        c1p1()
        c1p2()
        savecat = hollowtree()
        c4()
        jimmyfate = c5()
        realending(jimmyfate, savecat)
        endingmessage()

    elif chapterplay == 3:
        c1p1()
        c1p2()
        savecat = hollowtree()
        c4()
        jimmyfate = c5()
        realending(jimmyfate, savecat)
        endingmessage()

    elif chapterplay == 4: 
        c1p2()
        savecat = hollowtree()
        c4()
        jimmyfate = c5()
        realending(jimmyfate, savecat)
        endingmessage()

    elif chapterplay == 5: 
        question1 = input("Would you like to skip to the duel(Y/N)? ")
        if question1.lower().strip() == "y":
            game2()
        else:
            c2p1()
        savecat = hollowtree()
        c4()
        jimmyfate = c5()
        realending(jimmyfate, savecat)
        endingmessage()

    elif chapterplay == 6:
        question2 = input("Would you like to skip to the duel(Y/N)? ")
        if question2.lower().strip() == "y":
            game3()
        else:
            c2p2()
        savecat = hollowtree()
        c4()
        jimmyfate = c5()
        realending(jimmyfate, savecat)
        endingmessage()

    elif chapterplay == 7:
        c3()
        savecat = hollowtree()
        c4()
        jimmyfate = c5()
        realending(jimmyfate, savecat)
        endingmessage()

    elif chapterplay == 8: 
        question = input("Did you save the cat (Y/N)? ")
        if question.lower().strip() == "y":
            savecat = "save"
        else:
            savecat = "nosave"
        c4()
        jimmyfate = c5()
        realending(jimmyfate, savecat)
        endingmessage()

    elif chapterplay == 9: 
        question = input("Did you save the cat (Y/N)? ")
        if question.lower().strip() == "y":
            savecat = "save"
        else:
            savecat = "nosave"
        jimmyfate = c5()
        realending(jimmyfate, savecat)
        endingmessage()

    elif chapterplay == 10:
        question = input("Did you save the cat (Y/N)? ")
        if question.lower().strip() == "y":
            savecat = "save"
        else:
            savecat = "nosave"
        
        question2 = input("Did you leave him alone to come back(1), stay with him(2) or convince him to leave the cave(3)? ")
        if question2 == "1":
            jimmyfate = "1"
        elif question2 == "2":
            jimmyfate = "2"
        else:
            jimmyfate = "3"

        realending(jimmyfate, savecat) 
        endingmessage()

    else:
        print("Error, not a valid chapter.")
        time.sleep(3)
        chapters()

intro() 
chapters()