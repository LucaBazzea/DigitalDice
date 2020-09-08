from random import randint

def SixFace():

    print(f"\nYou rolled... {randint(1,6)}")

def TwelveFace():

    print("\nYou rolled...\n")
    print(f"Die 1: {randint(1,6)}")
    print(f"Die 2: {randint(1,6)}")

x = " "

while True:

    x = input("Would you like to roll 1 or 2 dice?\n")

    if x == "1" or x == "2":
        break

if x == 1:
    SixFace()
    
else:
    TwelveFace()