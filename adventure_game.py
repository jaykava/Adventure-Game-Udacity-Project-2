import time
import random


def playadventure():
    i = []
    v = random.choice(["Shark", "Fish", "Hippo"])
    inn(i, v)
    forward(i, v)


num = 8
for iss in range(num):
    for j in range((num - iss) - 1):
        print(end=" ")
    for j in range(iss + 1):
        print("*", end="  ")
    print()


def inn(i, v):
    print("Welcome To The Adventure!\n")
    time.sleep(2)
    print("You are about to Adventure on a journey to a castle\n")
    time.sleep(2)
    print("To Your left side is a Sea.\n")
    time.sleep(2)
    print("To Your right is a dark jungle.\n")
    time.sleep(2)
    print("Also another side is fire...\n")
    time.sleep(2)


def jungle(i, v):
    print("You into the jungle.\n")
    time.sleep(2)
    print("go fast other wise you eaten by lions\n")
    time.sleep(2)
    print("\nYou walk back to the ground.\n")
    if "stone" not in i:
        print("good job you are nice playing.\n")
        time.sleep(2)
    while True:
        choice2 = input("Now Would you like to (1)right or (2)"
                        "left?")
        if choice2 == "1":
            if "stone" in i:
                print("you are going to die so be careful.\n")
                time.sleep(2)
                print("You back to the new safe place.\n")
                time.sleep(2)
                print("You win this game level\n")
            else:
                print("You into the jungle.\n")
                time.sleep(2)
                print("It is biggest jungle.\n")
                time.sleep(2)
                print("You has never see this type of biggest jungle\n")
                time.sleep(2)
                print("In this jugle may be you find tressure!\n")
                time.sleep(2)
                print("You back to the checkpoint.\n")
            plays()
            break
        if choice2 == "2":
            print("You runs back to the castle of adventure park\n")
            forward(i, v)
            break


def fire(i, v):
    print("Now You into the Fire.\n")
    time.sleep(2)
    print("\nohh! This is the firestone!\n")
    time.sleep(2)
    if "fires" not in i:
        print("good job you are nice playing.\n")
        time.sleep(2)
    while True:
        choice2 = input("Now Would you like to (1)right or (2)"
                        "left?")
        if choice2 == "1":
            if "fires" in i:
                print("you are going to die so be careful.\n")
                time.sleep(2)
                print("You back to the new safe place.\n")
                time.sleep(2)
                print("You win this game level\n")
            else:
                print("You have some things that you use.\n")
                time.sleep(2)
                print("Now you can use your mind and cross the fires.\n")
                time.sleep(2)
                print("ohh ! you are so brillient...\n")
                time.sleep(2)
                print("you are now going to another level.\n")
                time.sleep(2)
                print("You walk back out to the castle.\n")
                time.sleep(2)
                i.append("fires")
            forward(i, v)
            plays()
            break
        if choice2 == "2":
            print("You runs back to the castle of adventure park\n")
            forward(i, v)
            break


def Sea(i, v):
    print("You going to Seashore of the Sea.\n")
    time.sleep(2)
    print("\ngod! This is the " + v + " Sea!")
    time.sleep(2)
    if "stone" not in i:
        print("good job you are nice playing.\n")
        time.sleep(2)
    while True:
        choice2 = input("Now Would you like to (1)right or (2)"
                        "left?")
        if choice2 == "1":
            if "stone" in i:
                print("wooho yoou are going to right path.\n")
                time.sleep(2)
                print("this game is about to finish..\n")
                time.sleep(2)
                print("You win this game level\n")
            else:
                print("\nYou play nice...")
                time.sleep(2)
                print("you swim so slow!")
                time.sleep(2)
                print("But shark is eats you..\n")
                time.sleep(2)
            plays()
            break
        if choice2 == "2":
            print("You runs back to the castle of adventure park\n")
            forward(i, v)
            break


def forward(i, v):
    print("Enter 1 to forward side the Sea.\n")
    print("Enter 2 to into the jungle.\n")
    print("Enter 3 to into the fire.\n")
    print("What would you choose?")
    while True:
        choice1 = input("(Please enter 1 or 2 or 3)\n")
        if choice1 == "1":
            Sea(i, v)
            break
        elif choice1 == "2":
            jungle(i, v)
            break
        elif choice1 == "3":
            fire(i, v)
            break


def plays():
    another = input("Would you like to play another time? (y/n)").lower()
    if another == "y":
        print("\n\n\nHurray! the game starting soon...\n\n\n")
        playadventure()
    elif another == "n":
        print("\n\nThank you for playing!\n\n")
    else:
        plays()


playadventure()
