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
    


def introduction():
    print("This is you, Marter Weke, and you are a well known petty criminal.")
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
        print("You leave your prison cell and enter the rest of the prison, taking the unused items with you.")
        return has_dynamyte == True
        return has_50_hour == True
        pass
        
    elif choice == "3":
        print("You throw the stick of dynamyte out the window of your cell, hoping to explode the wall.")
        print("You succeed in blowing up the wall, but the blast sends large pieces of the wall towards you, killing you.")
        print("You died.")
        failure()    
    
    elif choice == "4":
        print("You wait around for lunch")
        print("After waiting for an agonizing ten minutes, you hear the lunch bell.")
        print("You step out of your cell, leaving everything behind.")
        pass




introduction()
