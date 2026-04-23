import random

def failure(): #I need to figure out how to make this work with every scenario; play the function it's in when 1 is pressed.
    print("that was not the correct option, do you want to try this scenario again or restart the story?")
    print("1, restart scenario")
    print("2. restart story")

    choice = input("> ")

    if choice == "1":
        pass
    elif choice == "2":
        introduction()
    else:
        print("please enter one of the provided options")

def princessless():#You ignored Princess and ate lunch #5 ending #1
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

    choice == input("> ")

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

def basement_monster():
    print("")

def basement(): #After interacting with donuts in break room #6
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
        pass

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
         pass
       



def introduction():#first encounter #1
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
