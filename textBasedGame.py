import random
import time
def displayInfo():
    getName()
    startAdventure()
def getName():
    player_name= input("What's your name: ")
    print("Hello {}".format(player_name))

def startAdventure():
       print("""
You are in a land full of dragons. In front of
you are two caves. In one cave the dragon is
friendly will give you his treasure.
However a sleeping guard is Front of you and with a surprise. In the
other room, the dragon is greedy  with dragon eggs worth more than diamond, Gold and will
eat you on sight"""[1:])
       door_picked= input("Do you pick 1 or  2 >")
       if door_picked =="1":
           one_door_room()
       elif door_picked=="2":
           two_door_room()
       else:
            print("Sorry, it's either '1' or '2' as the answer.You're the weakest link, goodbye!")
            
def one_door_room():
    # The variable treasure_chest is an object type called a list
    # A list maybe empty as well.
    # So our treasure_chest list contains 6 items.
    treasure_chest = ["diamonds", "gold", "silver", "sword", "Ruby"]
    print("""You see a cave with a friendly dragon will give
you his treasure .However a sleeping guard is Front of you and with a surprise""")
    action= input("What will you do ?")
     # This is a way to see if the text typed by player is in the list
    if action.lower() in ["treasure", "chest", "left"]:
        print("Oooh, treasure!") 
        
        print("Press Forward ? Press '1'")
        print("Leave the room Press '2'")
        choice = input("> ")
        if choice == "1":
            print("""Jump over the guard
            Let's see what's in here... /grins
            The chest creaks open, and the guard is still sleeping. That's one heavy sleeper!
            As you are looking through the chest. You found  exit  sign with another Guard
            However this one is light sleeper""")
            for treasure in treasure_chest:
                print(treasure)
             # So much treasure, what to do? Take it or leave it.
            print("What do you want to do?")
            print("Take all {} treasure, press '1'".format(len(treasure_chest)))
            print("Leave Room, press '2'")

            treasure_choice = input("> ")
            if treasure_choice == "1":
                print("\tWoohoo! Bounty  and a shiney new sword. /drops your crappy sword in the empty treasure chest.")
                print("\tYou just received [{}]".format(", ".join(treasure_chest)))
            elif treasure_choice == "2":
                print("It will still be here (I hope), right after I get past this guard")
            
            # Picked up treasure or left it, you will now encounter the guard.
            # Let's call the guard() function here.
            guard()
    else:
        # Let's call the guard() function here as well, no point writing a bunch of same code 
        # twice (or more). It's good to be able to re-use code.
        print("The light sleeping guard is getting more interesting, let's go that way!")
        guard()
                




def two_door_room():
       print("""There you see a great red dragon with a marvelous Egg .
It stares at you through one narrowed eye.Do you flee for your life or stay?""")
       choice = input(">")
       if choice =="flee":
           start_adventure()
       else:
           stay()
def stay():
    print("""You tried to get the Dragon' Egg.
Dragon see you ....grinsn It eats you, Wll that was Bad""")
    exit()
def died(why):
    print(why)
    exit()
def guard():
    print("""You approach the exit, he's still sleeping
Suddenly you knocked a wooden cask with a mug on it... CRASSH!
Oi, what you doing 'ere?
Guard woke the other guard'
""")
    guard_moving= False
    while True:
        next_action=input("run | door > "). lower()
        if next_action == " run" and guard_moving: 
            died(" They speed from them was like a jacguar and you found yourself in prison")
        elif next_action == "run" and not guard_moving:
            print("Guard jumps up and looks the other way, missing you entirely.")
            
            guard_moved = True
        elif next_action == "door" and guard_moving:
            print("You just slipped through the door before the guard realised it.")
            print("You are now outside, home free! Huzzah!")
            return
        elif next_action == "door" and not guard_moving:
            died("Guards were faster than they looks and you found yourself in prison...")
        else:
            print("Not sure what you meant there... try again.")
if __name__ == '__main__':
    displayInfo()       
    
