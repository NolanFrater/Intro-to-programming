import random
direction = 0


def happy_princess(): #After giving Princess the toilet paper #10
    print("")


def mineshaft(): #After crawling through the hole in the wall in the mushroom scenario #9 ending #3
    def failure():
        direction = 0
        print("that was not the correct option, do you want to try this scenario again or restart the story?")
        print("1, restart scenario")
        print("2. restart story")

        choice = input("> ")

        if choice == "1":
            mineshaft()
        elif choice == "2":
            introduction()
        else:
            print("please enter one of the provided options")
            failure()

    if direction >= 3:
        print("You finnally find an exit to the mineshaft, and you are able to escape the prison.")
        print("Congradulations, you completed one of the endings.")
    
    elif direction <= -3:
        print("You get so lost in the mineshaft that you eventually die from starvation and dehydration.")
        print("You died.")
        failure()

    else:
        print("The mineshaft has tunnels leading in every direction, and you have no idea which one to take.")
        print("What do you do?")

        print("1. take the left tunnel")
        print("2. take the middle tunnel")
        print("3. take the right tunnel")

        choice = input("> ")

        if choice == "1":
            print("You take the left tunnel, and find yourself at another crossroads, with tunnels leading in every direction.")
            print("You still have no idea on which tunnel to take.")
            direction -= 1
            mineshaft()
    
        elif choice == "2":
            print("You take the middle tunnel, and find yourself at another crossroads, with tunnels leading in every direction.")
            print("You still have no idea on which tunnel to take.")
            direction += 1
            mineshaft()
    
        elif choice == "3":
            print("You take the right tunnel, and find yourself at another crossroads, with tunnels leading in every direction.")
            print("You still have no idea on which tunnel to take.")
            direction -= 1
            mineshaft()
    
        else:
            print("please enter one of the provided options")
            mineshaft()


def mushroom(): #After ignoring game show host #8
    direction = 0
    def failure():
        print("that was not the correct option, do you want to try this scenario again or restart the story?")
        print("1, restart scenario")
        print("2. restart story")

        choice = input("> ")

        if choice == "1":
            mushroom()
        elif choice == "2":
            introduction()
        else:
            print("please enter one of the provided options")

    print("As you come to your senses, you find yourself in a small room with a single purple mushroom in the middle of it.")
    print("The mushroom is emitting a strange glow, and you can feel a strange energy coming from it.")
    print("You have a strong urge to eat the mushroom, but you also feel like it could be dangerous.")
    print("What do you do?")

    print("1. eat the mushroom")
    print("2. leave the mushroom alone and try to find another way out of the room")

    choice = input("> ")

    if choice == "1":
        print("You decide to eat the mushroom, and it tastes terrible, like a mix of dirt and rotten fruit.")
        print("As you swallow the mushroom, you start to feel a strange sensation in your body.")
        print("You start to see things that aren't there, and you feel like you are losing control of your body.")
        print("You start to hallucinate.")
        print("You fully believe that you are free from the prison, and you lay down in the middle of the room, taking in your new found freedom.")
        failure()
    
    elif choice == "2":
        print("You decide to leave the mushroom alone, and you start to look around the room for another way out.")
        print("You find a small hole in the wall, and you decide to crawl through it.")
        print("As you crawl through the hole, you find yourself in some sort of dimly lit mineshaft, with tunnels leading in every direction.")
        mineshaft()


def princessless():#You ignored Princess and ate lunch #5 ending #1
    def failure():
        print("that was not the correct option, do you want to try this scenario again or restart the story?")
        print("1, restart scenario")
    print("2. restart story")

    choice = input("> ")

    if choice == "1":
        princessless()
    elif choice == "2":
        introduction()
    else:
        print("please enter one of the provided options")


    print("As you eat your lunch and continue to ignore Princess, you feel as if most of the prison is watching you.")
    print("You are now considered the most evil person in this prison, why would you make Princess sad?")
    print("Because you are now considered the most evil person, you are called to the prison warden's office")
    print("You cannot refuse a request by the prison warden, they hold the highest amount of power within the prison.")
    print("As you enter the warden's office, you see a stack of papers with your name on them.")
    print("The warden says, 'You have been moved to a higher security cell because of how needlessly evil you are'")
    print("How do you respond?")

    print("1. fight the warden")
    print("2. run")
    print("3. take his chair hostage")

    choice = input("> ")

    if choice == "1":
        print("You challenge the warden to a duel")
        print("The warden, fully confident that he will win, accepts.")
        print("As you get ready to fight him, you see him drink something.")
        chances = random.randint(1, 10)

        if chances >= 2:
            print("The warden attacks before you can even react, killing you instantly.")
            failure()
        else:
            print("Before you can even react, the warden goes to attack you but trips.")
            print("This leaves you with an opening that you cannot pass up.")
            print("You kill the warden, making you the new ruler of this prison.")
            print("You rule the prison with an iron fist, cementing yourself as one of the most evil wardens this prison has seen.")
            print("Congradulations, you completed one of the endings.")
    
    elif choice == "2":
        print("You try to run from the wardens office, but you forgot about the guards blocking the enerance.")
        print("The guards quickly stop and detain you, leaving you to be sent to the high security cell.")
        print("You don't have any chance to excape the new cell, you might as well be dead.")
        failure()
    
    elif choice == "3":
        print("You grab the decorative chair in the corner of the room and hold it hostage.")
        print("The warden panics and call all the guards over to the office on a 'code red' emergency.")
        print("You are quickly killed, with the chair unharmed, by the waves of guards pouring into the office.")
        failure()

    else:
        print("please enter a valid input next time.")
        princessless()


def basement_monster(): #After approaching the noises in the basement #7 ending #2
    def failure():
        print("that was not the correct option, do you want to try this scenario again or restart the story?")
        print("1, restart scenario")
        print("2. restart story")

        choice = input("> ")

        if choice == "1":
            basement_monster()
        elif choice == "2":
            introduction()
        else:
            print("please enter one of the provided options")

    print("The creature that used to be a washing machine grabs onto you and drags you to a corner of the basement")
    print("You are thrown into a hole in the wall by the washing machine creature, and find yourself in another room.")
    print("Bright lights turn on and you find yourself on a stage of a gameshow.")
    print("You hear an energetic voice shout out,'Welcome to Prison Pardons, the only place where, if you win, you get out of jail!'")
    print("You very confused.")
    print("The voice continues speaking, 'You can choose any game you want to play, but if you lose you will die.'")
    print("What game should you play?")
    
    print("1. Blackjack")
    print("2. roulette")
    print("3. Monopoly")
    print("4. go fish")
    print("5. do nothing")
    
    choice = input("> ")

    if choice == "1":
        print("You decide to play some blackjack")
        print("You seem to start off strong, but you end up on a losing streak pretty quickly.")
        print("The last thing you hear before you die is the gameshow announcer saying some cheesy line like,'The house always wins.'")
        failure()

    elif choice == "2":
        print("You decide to play a game of roulette")
        winrate = random.randint(1, 20)

        if winrate >= 2:
            print("You start off with a small win, but you end up losing all of your winnings and more pretty quickly.")
            print("The last thing you hear before you die is the gameshow announcer saying some cheesy line like,'Better luck next time.'")
            failure()

        else:
            print("You win the game of roulette, even with all the odds agianst you.")
            print("The gameshow announcer seems surprised as you black out at the table.")
            print("You wake up in a random forest, with no memory of how you got there.")
            print("You are now free, but you have no idea where you are or how to get back to civilization.")
            print("Congradulations, you completed one of the endings.")

    elif choice == "3":
        print("You decide to play a game of monopoly")
        print("You should've known better, the announcer was involved in the creation of the game, so of course you are going to lose.")
        print("You see a shadow below you, and as you look up you see that a house is falling on you.")
        print("You are crushed by the house.")
        print("You died.")
        failure()

    elif choice == "4":
        print("You decide to play a game of go fish")
        print("The announcer seems surprised that you chose such a simple game, but he accepts.")
        print("This is a game you are familiar with, giving you a lot of confidence going into the game.")
        print("The announcer can't seem to understand how you are winning, and starts to get very angry, making him even easier to read.")
        print("You win the game of go fish, and the announcer seems angry.")
        print("You mysteriously black out at the table, and wake up in a random forest, with no memory of how you got there.")
        print("You are now free, but you have no idea where you are or how to get back to civilization.")
        print("Congradulations, you completed one of the endings.")

    elif choice == "5":
       print("You decide to do nothing, hoping that the gameshow announcer will get bored and let you go.")
       print("The announcer seems to be dissapointed in your choice, but he accepts it, saying that he wont force you to play a game if you don't want to.")
       print("A hole opens up in the floor, and you fall through it, landing in a new room.")
       mushroom()

    else:
        print("please enter one of the provided options")
        basement_monster()
        

def basement(): #After interacting with donuts in break room #6
    def failure(): #I need to figure out how to make this work with every scenario; play the function it's in when 1 is pressed.
        print("that was not the correct option, do you want to try this scenario again or restart the story?")
        print("1, restart scenario")
        print("2. restart story")

        choice = input("> ")

        if choice == "1":
            basement()
        elif choice == "2":
            introduction()
        else:
            print("please enter one of the provided options")
    
    print("You slide down the laundry chute into the basement of the prison.")
    print("It is extremely dark, making your vision extremely limited.")
    print("You didn't even know the prison had a basement.")
    print("You begin to hear noises coming from somewhere in the darkness, what do you do?")

    print("1. approach the noises")
    print("2. run as fast as you can away from the noises.")

    choice = input("> ")
    if choice == "1":
        print("You cautiously go to investigate the noises.")
        print("As you get closer, you see that it was just a really old washing machine, which is a lot less scary than you thought it would be.")
        print("You soon realise that your relief was short-lived as the washing machine begins to transform into some angry mess of wires.")
        basement_monster()

    elif choice == "2":
        print("You don't like the sound of the noises, so you run as far away as you can.")
        print("While running, you end up tripping on a pile of laundry which leads to you hitting your head on something hard.")
        print("You died.")
        failure()
    else:
        print("You should know to enter either a '1' or a '2', is it really that hard")
        basement()


def break_room():# After running into the guard break room #4
    def failure():
        print("that was not the correct option, do you want to try this scenario again or restart the story?")
        print("1, restart scenario")
        print("2. restart story")

        choice = input("> ")

        if choice == "1":
            break_room()
        elif choice == "2":
            introduction()
        else:
            print("please enter one of the provided options")


    print("As you enter the break room, you see that it is empty, with the sole exeption of a box of donuts.")
    print("You also see a door leading to the armory and an air duct that you could try to climb through.")
    print("What do you do?")

    print("1. Eat the donuts")
    print("2. Climb through the air duct")
    print("3. Enter the armory.")
    
    choice = input("> ")
    if choice == "1":
        print("You decide to eat the donuts.")
        print("As you move the box that the donuts are in, you find that it was covering the laundry chute.")
        print("You hear the bell marking the start of lunch, and a break for the guards.")
        print("You jump down the laundry chute in a panic to aviod getting caught.")
        basement()

    elif choice == "2":
        print("You jump into the air duct.")
        print("As you crawl through the vents, you begin to hear a creaking noise from below you.")
        print("The air duct was not made to be able to handle the weight of a human crawling through it, so it collapses.")
        print("You fall out of the air duct right into the convieniently placed lava moat.")
        print("You died.")
        failure()

    elif choice == "3":
        print("You decide to run into the armory.")
        print("While looking around the armory you find a large red button with a warning saying DO NOT TOUCH.")
        print("You take the obvious action and press the button as soon as you see it.")
        print("The prison explodes, you died.")
        failure()
    
    else:
        print("Is it really that hard to type a 1, 2, or 3, please stick to valid inputs next time.")
        break_room()
        

def excape():#After using the nail file to excape your cell #3
    def failure():
        print("that was not the correct option, do you want to try this scenario again or restart the story?")
        print("1, restart scenario")
        print("2. restart story")

        choice = input("> ")

        if choice == "1":
            excape()
        elif choice == "2":
            introduction()
        else:
            print("please enter one of the provided options")


    print("You enter the main area of the prison, there are no innmates walking around at this time.")
    print("You hear footsteps around the corner, it is one of the prison guards.")
    print("How do you deal with the prison guard?")

    print("1. run back into your cell")
    print("2. Run in the opposite direction of the gaurd")
    print("3. Run into the guard break room")
    print("4. Try to fight the guard")

    choice = input("> ")

    if choice == "1":
          print("As the guard goes around the corner, they notice that your cell is missing an iron bar.")
          print("You panic as they call for backup, and before you can do anything, the rest of the guards end up killing you.")
          print("You were determined a security risk and died.")
          failure()

    elif choice == "2":
         print("You try to run in the opposite direction of the footsteps, but you forgot to tie your shoes.")
         print("You trip onto an inconvieniently placed spike.")
         print("You died.")
         failure()
         
    elif choice == "3":
        print("You see the enterance of the guard break room and decide to run into it to hide")
        print("The guard passes by without noticing anything wrong.")
        break_room()
        
    elif choice == "4":
         print("As you run at the guard to try to fight them, they immidiatly counter.")
         print("You are slammed into a wall, breaking multiple bones and almost dying.")
         print("The guard passes by you, leaving you to bleed out.")
         print("You died.")
         failure()

    else:
         print("please enter one of the provided variables")
         excape()


def give_Princess():#not an additional scenario, part of the Princess scenario. #2.5
    def failure():
        print("that was not the correct option, do you want to try this scenario again or restart the story?")
        print("1, restart scenario")
        print("2. restart story")

        choice = input("> ")

        if choice == "1":
            give_Princess()
        elif choice == "2":
            introduction()
        else:
            print("please enter one of the provided options")


    print("What do you give him?")
    print("1. meth")
    print("2. a roll of toilet paper")
    print("3. your lunch money")

    Choice_1 = input("> ")

    if Choice_1 == "1":
            print("'This is really insulting, you know I'm trying to quit.'")
            print("Princess strangles you to death for even trying to suggest drugs.")
            failure()
        
    elif Choice_1 == "2":
            print("'Thanks, I really needed this for a project I was working on.")
            print("you watch as Princess merrilly jaunts away, leaving you unable to guess what the toilet paper is for.")
            pass

    elif Choice_1 == "3":
            print("'What could I use this for, everything is free in the cafeteria?'")
            print("You die from embarrasment, you should've known that money barely has any use in this prison.")
            failure()

    else:
            print("Please enter one of the provided options.")
            give_Princess()


def Princess(): #after waiting for lunch in introduction #2
    def failure():
        print("that was not the correct option, do you want to try this scenario again or restart the story?")
        print("1, restart scenario")
        print("2. restart story")

        choice = input("> ")

        if choice == "1":
            Princess()
        elif choice == "2":
            introduction()
        else:
            print("please enter one of the provided options")


    print("As you walk into the cafeteria you hear a voice shout out your name,")
    print("'Hey John, do you have the thing I asked for.' You see a large figure heading your way,")
    print("It is Princess, the only person in this prison that is considered more evil than you.")
    print("He was jailed for being too pretty, but the 27 counts of first degree murder didn't help his case.")
    print("How do you answer Princess' question?")

    print("1. yes")
    print("2. no")

    choice = input("> ")

    if choice == "1":
         give_Princess()

    elif choice == "2":
         print("Princess seems a little let down, but remains calm because of the therapy he has been taking every Thursday.")
         print("You grab your lunch, its the same slop as normal, and you are avoided by the any other innmates because of the crimes you committed.")
         princessless()
       

def introduction():#first encounter #1
    def failure():
        print("that was not the correct option, do you want to try this scenario again or restart the story?")
        print("1, restart scenario")
        print("2. restart story")

        choice = input("> ")

        if choice == "1":
            introduction()
        elif choice == "2":
            introduction()
        else:
            print("please enter one of the provided options")


    print("This is you, John Weke, and you are a well known petty criminal.")
    print("You find yourself in this cell because you stole one too many lolipops from the local babies.")
    print("You can hear one of the guards approaching your cell.")
    print("As the guard approaches, you can see that they are holding a package.")
    print("The guard stops in front of your cell and says,'We recieved a package for you, you sick excuse for a human.'")
    print("The guard leaves almost as soon as they entered, with a face full of disgust and hatred.")
    print("As you open the package you see three items, an energy drink labeled 50 hour energy, a bright pink nail file, and a small stick of dynamyte.")
    print("What will you use to try to escape the cell?")

    print("1. the 50 hour energy")
    print("2. the nail file")
    print("3. the stick of dynamyte")
    print("4. do nothing with these items")

    choice = input("> ")
    
    if choice == "1":
        print("You start to feel the effects of the 50 hour energy kick in.")
        print("You find yourself able to bend the bars of the cell and time seems to be moving slower")
        print("As you walk out of the prison, your heart stops because of the deadly levels of caffene in the 50 hour energy.")
        print("You died.")
        failure()

    elif choice == "2":
        print("You take the hot pink nail file and decide to try to file down the iron bars that are keeping you from entering the rest of the prison.")
        print("You were able to successfully file down the bars without the guards spotting you.")
        print("The nail file took too much damage from this and can no longer be used.")
        print("You leave your prison cell and enter the rest of the prison, entering the main area of the prison.")
        excape()
        
    elif choice == "3":
        print("You throw the stick of dynamyte out the window of your cell, hoping to explode the wall.")
        print("You succeed in blowing up the wall, but the blast sends large pieces of the wall towards you, killing you.")
        print("You died.")
        failure()    
    
    elif choice == "4":
        print("You wait around for lunch")
        print("After waiting for an agonizing ten minutes, you hear the lunch bell.")
        print("You step out of your cell, entering the cafeteria of the prison with the rest of the inmates.")
        Princess()

    else:
        print("please enter one of the provided answers")
        introduction()


mineshaft()