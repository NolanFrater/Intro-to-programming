import random #This is still unfinshed.
direction = 0





def invisible(): #After taking the invisibility pills in the hospital #14
    def failure():
        print("that was not the correct option, do you want to try this scenario again or restart the story?")
        print("1, restart scenario")
        print("2. restart story")

        choice = input("> ")

        if choice == "1":
            invisible()
        elif choice == "2":
            introduction()
        else:
            print("please enter one of the provided options")


    print("As the invisibility pills effect wears off, you find yourself in an unusual cell, with some sort of contraption sitting in the corner.")
    print("You see that the contraption has the toilet paper that you gave to Princess, making you believe that you somehow wandered into Princess' cell.")
    print("Princess is not in the cell at the moment, but you don't know what his reaction will be when he finds out that you are in his cell.")
    print("What do you do?")

    print("1. leave the cell")
    print("2. stay in the cell and wait for Princess to come back")
    print("3. mess with the contraption")

    choice = input("> ")

    if choice == "1":
        print("You decide to leave the cell.")
        print("As you leave, you are immediately caught by a guard, who detains you and has you sent to solitary confinement.")
        failure()
    
    elif choice == "2":
        print("You decide to stay in the cell and wait for Princess to come back.")
        print("As you wait, you decide to look through some of the nearby furniture, avoiding the contraption.")
        a_number = random.randint(1, 10)

        if a_number >= 5:
            print("You find a mysterious symbol underneath the bed, likely linking Princess to some unkown organization.")
            print("Princess comes into his cell and finds you messing with his things, he looks a little surprised that you found the symbol.")
            print("Princess calls for backup and a frog suddenly appears next to you.")
            print("The frog jumps onto you.")
            print("The frog happened to be a poison dart frog, and you die from its poison.")
            failure()

        else:
            print("You rummage around Princess' things, but arn't able to find anything of interest.")
            print("Princess comes into his cell and finds you messing with his things, he looks worried, with the idea that you might've found something.")
            print("Princess calls for backup and a frog suddenly appears next to you.")
            print("The frog jumps onto you.")
            print("The frog happened to be a poison dart frog, and you die from its poison.")
            failure()
        
    elif choice == "3":
        print("You decide to mess with the contraption in the corner of the cell")
        print("You find a note on it that says, 'Out of commission'")
        pass

    else:
        print("Please enter one of the provided inputs.")
        invisible()
        

def frog_man(): #After pressing the big blue button in the hospital #13
    def failure():
        print("that was not the correct option, do you want to try this scenario again or restart the story?")
        print("1, restart scenario")
        print("2. restart story")

        choice = input("> ")

        if choice == "1":
            frog_man()

        elif choice == "2":
            introduction()

        else:
            print("please enter one of the provided options")
            failure()

    print("You find yourself on a bed of wet moss, with a small frog sitting on your chest.")
    print("The frog drops a small piece of paper on your chest, and then hops away.")
    print("You read the piece of paper, and it says,")
    print("\n We know that your goal is to escape the prison, it's our goal too, so we want to work with you.")
    print("If you decide to work against us, we will make sure that you never escape this prison and that you will never feel the warmth of hope again.")
    print("If you decide to work with us, we will give you orders that you must follow, and if you follow them correctly, we will all excape.")
    print("\n What do you do?")

    print("1. work with the mysterious organization.")
    print("2. rat out the mysterious organization to the guards.")

    choice = input("> ")

    if choice == "1":
        print("You decide to work with this mysterious organization for now.")
        print("As you are wondering how to contact them, you find a frog themed kids walkie talkie on the ground.")
        print("You pick up the walkie talkie, and you hear a voice ask you, 'Are you working with us?'")
        print("You respond with a simple 'yes', and the voice on the walkie talkie seems to be satisfied with your answer.")
        pass

    elif choice == "2":
        print("You decide to rat out the mysterious organization to the guards, and you tell them everything you know about it.")
        print("The guards attempt to investigate the situation, but the room you were in has suddenly become completely empty, with no signs of the mysterious organization anywhere.")
        print("You are sent back to your cell, and you go throughout the rest of your day like normal.")
        print("The next day, you wake up to find a note on the ceiling of your cell that says, 'Sniches get stitches,'")
        print("You also find that this isn't your cell, it is one of the highest security cells in the prison, leaving you with no chance of escape.")
        failure()

    else:
        print("please enter one of the provided options, this is an important choice.")
        frog_man()


def map_of_Joe(): #After stealing the map from peg-leg Joe #12
    print("You take a look at the map you stole from peg-leg Joe, and it seems to be a map of the prison, with a lot of different rooms and areas marked on it.")
    print("You don't know why rooms on the map are marked, but there is one room marked near the yard, and another near the cafeteria that you could check out.")
    print("What do you want to do?")

    print("1. check out the room near the yard")
    print("2. check out the room near the cafeteria")

    choice = input("> ")
    if choice == "1":
        print("You decide to look for the room near the yard, but it isn't easily found.")
        print("After a few minutes of searching, you find a small door hidden underneath the stairs.")
        pass

    elif choice == "2":
        print("You decide to look for the room near the cafeteria, and it is relatively easy to find.")
        print("The only problem is that the area is heavily monitored by guards, so you have to be very careful to not get caught.")
        pass

    else:
        print("please enter one of the provided options")
        map_of_Joe()


def hospital(): #After licking the frog #11
    def failure():
        print("that was not the correct option, do you want to try this scenario again or restart the story?")
        print("1, restart scenario")
        print("2. restart story")

        choice = input("> ")

        if choice == "1":
            hospital()
        elif choice == "2":
            introduction()
        else:
            print("please enter one of the provided options")
            failure()


    print("You wake up in a hospital bed, with no idea how long you have been unconscious for.")
    print("A nurse walks into the room and says, 'It's nice to finally see you awake, you were out for a good three hours.'")
    print("The nurse continues, 'We are required to ask you to fill out a survey on what happened to you, but nobody really cares about what it says,'")
    print("The nurse hands you a piece of paper and a pen as they leave the room.")
    print("You can also see objects like a big blue button, a box that is labeled as 'invisibility pills', and a bottle of skooma in the room with you.")

    print("What do you do?")
    print("1. fill out the survey")
    print("2. press the big blue button")
    print("3. take the invisibility pills")
    print("4. drink the skooma")

    choice = input("> ")

    if choice == "1":
        print("You decide to fill out the survey, but it feels like it gets longer and longer the more you fill it out.")
        print("The paper seems to grow in size as you write on it, and you start to feel like you are writing for an eternity.")
        print("You decide that the survey is not worth your time, and you throw it in the trash.")
        print("A different nurse seems to barge into the room, and is furious because you threw out the survey.")
        print("The nurse tells everyone they can find that you are evil and that you should be put in solitary confinement for the rest of your life.")
        print("This rumor gets to the prison warden, and you are sent to solitary confinement as soon as you are let out of the hospital.")
        print("You are now in solitary confinement, and you will never be able to escape.")
        failure()
    
    elif choice == "2":
        print("You decide to press the big blue button, and a unknown force grabs you and drags you out of the hospital bed.")
        print("You are brought to a different room, which smells almost like a swamp.")
        frog_man()

    elif choice == "3":
        print("You decide to take the invisibility pills.")
        print("You watch as your arms and legs start to disappear, and your vision starts to get blurry.")
        print("You are now invisible, but light cannot reach your eyes, so you are completely blind.")
        print("You are now invisible and blind, and you have no idea how to get out of the hospital.")
        invisible()

    elif choice == "4":
        print("You decide to drink the skooma, and you feel as if you could run a million miles an hour easily.")
        print("You cannot control your speed as you try to run away from the hospital, causing you to crash into a wall at an extremely high speed.")
        print("You died.")
        failure()
    
    else:
        print("please enter one of the provided options")
        hospital()


def happy_princess(): #After giving Princess the toilet paper #10
    print("You can ask around to see if anyone can do something mildly entertaining.")
    print("Who do you ask?")

    print("1. ask the nearest guard")
    print("2. ask peg-leg Joe")
    print("3. ask the frog man")

    choice = input("> ")
    if choice == "1":
        print("You ask the guard to do something entertaining, but they just look at you with a blank stare and walk away.")
        print("You should go ask someone else.")
        happy_princess()
    
    elif choice == "2":
        print("You ask Peg-leg Joe to do something entertaining.")
        print("He seems to be in a good mood, and start to tell you about his time in the air force, where he lost his leg.")
        print("You start to zone out as he talks, but then you notice that he has some sort of map on his belt.")
        print("You decide to take the map, and Joe is so engrossed in his story that he doesn't even notice.")
        map_of_Joe()

    elif choice == "3":
        print("You ask the wierd person who is always walking around the prison with a frog.")
        print("Nobody knows how he gets the frogs, as each time the guards take the frogs away, he somehow finds a new one in the morning.")
        print("The frog man tells you to lick the frog.")
        print("Do you lick the frog?")

        print("1. yes")
        print("2. no")

        choice = input("> ")

        if choice == "1":
            print("You decide to lick the frog, it tasted terrible and made you almost throw up.")
            print("You start to lose consciousness, as the frog man looks down on you with a smile on his face.")
            hospital()

        elif choice == "2":
            print("You decide to not lick the frog, and the frog man looks disappointed.")
            print("You don't think you will be able to get any more entertainment out of him, so you should probably ask someone else.")

            happy_princess()

        else:
            print("please enter one of the provided options")
            happy_princess()

    else:
        print("please enter one of the provided options")
        happy_princess()


def mineshaft(): #After crawling through the hole in the wall in the mushroom scenario #9 ending #3
    global direction
    def failure():
        global direction
        print("that was not the correct option, do you want to try this scenario again or restart the story?")
        print("1, restart scenario")
        print("2. restart story")

        choice = input("> ")

        if choice == "1":
            direction = 0
            mineshaft()
        elif choice == "2":
            introduction()
        else:
            print("please enter one of the provided options")
            failure()

    if direction == 3:
        print("You finally find an exit to the mineshaft, and you are able to escape the prison.")
        print("Congratulations, you completed one of the endings.")

    elif direction == -3:
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
            print("You go to eat your lunch, it tasted terrible, but you are used to it by now.")
            print("Now that lunch is over, you are sent to the yard for some fresh air and exercise.")
            print("You are bored and want something to happen.")
            happy_princess()

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
    
    else:
        print("please enter one of the provided options")
        Princess()


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


introduction()

