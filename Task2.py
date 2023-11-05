import random

# Define game variables
inventory = []
player_health = 100

# Define the game's story and choices
story = [
    "You wake up in a mysterious forest. What do you do?\n1. Explore the forest\n2. Stay put\n",
    "While exploring, you find a rusty sword. Do you pick it up?\n1. Yes\n2. No\n",
    "You encounter a friendly traveler who offers you a healing potion. Do you accept it?\n1. Yes\n2. No\n",
    "You stumble upon a cave entrance. What's your choice?\n1. Enter the cave\n2. Keep exploring the forest\n",
    "Inside the cave, you find a dragon guarding a treasure. Do you fight it?\n1. Yes\n2. No\n"
]

endings = {
    "win": "Congratulations! You defeated the dragon and found the treasure!",
    "lose": "The dragon was too powerful and you didn't make it out of the cave.",
    "quit": "You decide not to continue your adventure. Thanks for playing!"
}

# Define game functions
def explore_forest():
    print("You explore the forest, and...")
    outcome = random.choice(["find a hidden path", "meet a friendly squirrel", "discover a beautiful waterfall"])
    print(f"You {outcome} in the forest.")

def fight_dragon():
    global player_health
    player_health -= 30
    print("You engage in a fierce battle with the dragon!")
    if player_health <= 0:
        print("Unfortunately, the dragon overpowers you.")
    else:
        print("With great effort, you defeat the dragon!")

# Main game loop
print("Welcome to the Text Adventure Game!")
while True:
    for i, scene in enumerate(story):
        choice = input(scene)
        if i == 0:  # First scene
            if choice == "1":
                explore_forest()
            elif choice == "2":
                print(endings["quit"])
                exit()
        elif i == 1:
            if choice == "1":
                inventory.append("rusty sword")
            elif choice == "2":
                pass
        elif i == 2:
            if choice == "1":
                inventory.append("healing potion")
            elif choice == "2":
                pass
        elif i == 3:
            if choice == "1":
                print("You enter the cave...")
            elif choice == "2":
                explore_forest()
        elif i == 4:
            if choice == "1":
                fight_dragon()
                if player_health <= 0:
                    print(endings["lose"])
                else:
                    print(endings["win"])
            elif choice == "2":
                print(endings["quit"])
            exit()
    
    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

print("Thanks for playing!")
