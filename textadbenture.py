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
    
def excape():#After using the nail file to excape your cell
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
         
    elif choice == "4":
         print("As you run at the guard to try to fight them, they immidiatly counter.")
         print("You are slammed into a wall, breaking multiple bones and almost dying.")
         print("The guard passes by you, leaving you to bleed out.")
         print("You died.")
         failure()

    else:
         print("please enter one of the provided variables")
         excape()








def give_Princess():#not an additional scenario, part of the Princess scenario.
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


def Princess(): #after waiting for lunch in introduction
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
       



def introduction():
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
