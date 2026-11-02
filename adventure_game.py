#Design a journey of using  loop, and case,river flow to find the treasure. The player must navigate through the river, 
# avoiding obstacles and making choices that lead them closer to the treasure. The journey will include challenges such as rapids, fallen trees, and hidden paths. 
# The player must use their wits and decision-making skills to successfully reach the treasure at the end of the river flow.
def river_journey():
    print("\nYou embark on a journey down the river, facing various challenges along the way.")
    while True:
        choice = input("You encounter rapids. Do you want to navigate through them or find a hidden path? (navigate/path) ").lower()
        if choice == "navigate":
            print("\nYou skillfully navigate through the rapids and continue your journey.")
        elif choice == "path":
            print("\nYou find a hidden path that leads you around the rapids, but it takes longer.")
        else:
            print("\nInvalid choice. You get stuck in the rapids and lose valuable time.")
        
        # Check for obstacles
        obstacle_choice = input("You see a fallen tree blocking your path. Do you want to climb over it or go around it? (climb/around) ").lower()
        if obstacle_choice == "climb":
            print("\nYou climb over the fallen tree and continue your journey.")
        elif obstacle_choice == "around":
            print("\nYou go around the fallen tree, but it takes more time.")
        else:
            print("\nInvalid choice. You get stuck and lose valuable time.")

        # Final decision to reach the treasure
        final_choice = input("You see a glimmering object in the distance. Do you want to approach it or keep going? (approach/keep going) ").lower()
        if final_choice == "approach":
            print("\nYou approach the glimmering object and discover it's the hidden treasure! Congratulations!")
            print("\nYou have successfully completed your adventure and found the treasure!")
            break
        elif final_choice == "keep going":
            print("\nYou decide to keep going, but you miss the treasure and eventually get lost.")
            print("\nYou have failed to find the treasure. Better luck next time!")
            break
        else:
            print("\nInvalid choice. You wander aimlessly and lose your way.")


#if player choose tree path design a journey of using loop, and case. The player must navigate through the tree, avoiding obstacles and making choices that lead them closer to the treasure. The journey will include challenges such as branches, birds, and hidden paths.
def tree_journey():
    print("\nYou embark on a journey through the tree, facing various challenges along the way.")
    while True:
        choice = input("You encounter a branch blocking your path. Do you want to climb over it or find a hidden path? (climb/path) ").lower()
        if choice == "climb":
            print("\nYou skillfully climb over the branch and continue your journey.")
        elif choice == "path":
            print("\nYou find a hidden path that leads you around the branch, but it takes longer.")
        else:
            print("\nInvalid choice. You get stuck and lose valuable time.")
        
        # Check for obstacles
        obstacle_choice = input("You see a bird's nest blocking your path. Do you want to go around it or wait for the birds to leave? (around/wait) ").lower()
        if obstacle_choice == "around":
            print("\nYou go around the bird's nest and continue your journey.")
        elif obstacle_choice == "wait":
            print("\nYou wait for the birds to leave, but it takes more time.")
        else:
            print("\nInvalid choice. You get stuck and lose valuable time.")

        # Final decision to reach the treasure
        final_choice = input("You see a glimmering object in the distance. Do you want to approach it or keep going? (approach/keep going) ").lower()
        if final_choice == "approach":
            print("\nYou approach the glimmering object and discover it's the hidden treasure! Congratulations!")
            print("\nYou have successfully completed your adventure and found the treasure!")
            break
        elif final_choice == "keep going":
            print("\nYou decide to keep going, but you miss the treasure and eventually get lost.")
            print("\nYou have failed to find the treasure. Better luck next time!")
            break
        else:
            print("\nInvalid choice. You wander aimlessly and lose your way.")




#Define the function start_game() to display the game introduction 
def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious land filled with challenges and treasures.")
    print("Your goal is to navigate through the land, make choices, and find the hidden treasure.")
    print("Good luck on your adventure!\n")
    #Ask the player for their name and store it in a variable
    player_name = input("What is your name, adventurer? ")
    print(f"Hello, {player_name}! Let's begin your journey.\n")
    #Provide the player with an initial choice (explore a forest or enter a cave) 
    choice = input("Do you want to explore the forest or enter the cave? (forest/cave) ").lower()
    return player_name, choice

#Define the function forest_path() that describes the forest scenario. Provide the player with choices (follow a river or climb a tree).mb a tree)
#Use an if-else structure to handle player choices
def forest_path():
    print("\nYou venture into the forest. The trees are tall and the air is fresh.")
    choice = input("You see a river and a tall tree. Do you want to follow the river or climb the tree? (river/tree) ").lower()
    if choice == "river":
        print("\nYou follow the river and find a hidden waterfall with sparkling water.")
        print("You take a refreshing drink and feel rejuvenated.")
        river_journey()
    elif choice == "tree":
        print("\nYou climb the tree and get a bird's-eye view of the forest.")
        print("From up there, you spot a glimmering object in the distance.")
        tree_journey()
    else:
        print("\nInvalid choice. You wander aimlessly in the forest and get lost.")
#Task 4: Create the cave path
#Actions:
#Define the function cave_path() that describes the cave scenario
#Provide the player with choices (light a torch or proceed in the dark)
#Use conditionals to determine the outcome     
def cave_path():
    print("\nYou enter the cave. It's dark and eerie, with the sound of dripping water echoing through the tunnels.")
    choice = input("Do you want to light a torch or proceed in the dark? (torch/dark) ").lower()
    if choice == "torch":
        print("\nYou light a torch and illuminate the cave walls, revealing ancient drawings and hidden passages.")
        print("You carefully navigate through the cave and find a chest filled with gold coins!")
    elif choice == "dark":
        print("\nYou proceed in the dark, but you stumble over rocks and fall into a pit.")
        print("Unfortunately, you are trapped and cannot continue your adventure.")
        print("\nYou have failed to find the treasure. Better luck next time!")
    else:
        print("\nInvalid choice. You wander aimlessly in the cave and get lost.")


#Task 5: Run the adventure game
#Actions:
# Call start_game() to begin the adventure
# Ensure the program runs in a loop until the player completes their journey
# Provide an option to restart the game after completion
# The player must think critically and choose wisely to advance toward the treasure.





#The game ends in one of the following three ways:
# Winning: Finding the treasure
# Losing: Making a poor decision that ends the adventure
# Restarting: Choosing to replay the game after an unsuccessful attempt
running = True
while running:
    player_name, initial_choice = start_game()
    if initial_choice == "forest":
        forest_path()
    elif initial_choice == "cave":
        cave_path()
    else:
        print("\nInvalid choice. You wander aimlessly and get lost.")
    
    # Ask the player if they want to play again
    replay_choice = input("\nDo you want to play again? (yes/no) ").lower()
    if replay_choice != "yes":
        running = False
        print(f"\nThank you for playing, {player_name}! Goodbye!")



