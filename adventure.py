print("Welcome to the Adventure Game!")
print("You find yourself in a dark forest. In front of you is a spooky house.")
print("Your goal is to find the hidden treasure without getting caught!")

# User_Input
choice = input("Do you want to ENTER the house or WALK around it? (type 'enter' or 'walk'): ").lower()

if choice == "enter":
    print("\nYou step inside the house. It's dark and cold.")
    print("You see a STAIRCASE leading upstairs and a DOOR to the basement.")
    
    choice = input("Do you go UPSTAIRS or DOWNSTAIRS? (type 'upstairs' or 'downstairs'): ").lower()
    
    if choice == "upstairs":
        print("\nYou slowly walk upstairs. You find a locked chest!")
        choice = input("Do you want to OPEN the chest or LEAVE it? (type 'open' or 'leave'): ").lower()
        
        if choice == "open":
            print("\nCongratulations! You found the hidden treasure! You win!")
        elif choice == "leave":
            print("\nYou decide to leave the chest alone. As you turn around, you hear a noise.")
            print("A ghost appears and scares you out of the house! You lose!")
        else:
            print("\nInvalid choice. A ghost appears and scares you out of the house! You lose!")

    elif choice == "downstairs":
        print("\nYou carefully descend into the basement. It's very dark and you hear strange noises.")
        choice = input("Do you want to TURN ON your flashlight or LEAVE the basement? (type 'flashlight' or 'leave'): ").lower()
        
        if choice == "flashlight":
            print("\nYou turn on the flashlight and see a treasure chest in the corner!")
            choice = input("Do you want to OPEN the chest or LEAVE it? (type 'open' or 'leave'): ").lower()
            
            if choice == "open":
                print("\nCongratulations! You found the hidden treasure! You win!")
            elif choice == "leave":
                print("\nYou decide to leave the chest alone. Suddenly, the basement door locks behind you.")
                print("You are trapped! You lose!")
            else:
                print("\nInvalid choice. The lights go out, and you are trapped in the basement! You lose!")
        
        elif choice == "leave":
            print("\nYou quickly leave the basement and run out of the house. You are safe, but you didn't find the treasure.")
            print("Game Over.")
        else:
            print("\nInvalid choice. You hear footsteps behind you and run out of the house. You lose!")

    else:
        print("\nInvalid choice. A ghost appears and scares you out of the house! You lose!")

elif choice == "walk":
    print("\nYou decide to walk around the house. The forest is dense and dark.")
    choice = input("Do you want to KEEP WALKING or ENTER a nearby CAVE you find? (type 'walk' or 'cave'): ").lower()
    
    if choice == "walk":
        print("\nYou keep walking and find a path that leads to a small village. You are safe!")
        print("However, you didn't find the treasure. Game Over.")
    
    elif choice == "cave":
        print("\nYou enter the cave. It's damp and eerie.")
        choice = input("Do you want to GO DEEPER into the cave or LEAVE? (type 'deeper' or 'leave'): ").lower()
        
        if choice == "deeper":
            print("\nYou go deeper and find a hidden treasure chest!")
            choice = input("Do you want to OPEN the chest or LEAVE it? (type 'open' or 'leave'): ").lower()
            
            if choice == "open":
                print("\nCongratulations! You found the hidden treasure! You win!")
            elif choice == "leave":
                print("\nYou leave the cave empty-handed. A bear appears and chases you out! You lose!")
            else:
                print("\nInvalid choice. A rock falls, blocking the entrance! You are trapped. You lose!")
        
        elif choice == "leave":
            print("\nYou decide it's too dangerous and leave the cave. You are safe, but you didn't find the treasure.")
            print("Game Over.")
        else:
            print("\nInvalid choice. A rock falls, blocking the entrance! You are trapped. You lose!")

else:
    print("\nInvalid choice. A wild animal appears, and you run away in fear! Game Over.")
