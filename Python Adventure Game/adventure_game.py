# Adventure game project
# This is a text based game where you play as an explorer looking for treasure.
# You make choices and they decide if you win or lose.
# Made for the Python course end project.


def get_choice(question, options):
    # keep asking the player until they type one of the valid options
    while True:
        answer = input(question).strip().lower()
        if answer in options:
            return answer
        print("That's not a valid option. Please type one of:", ", ".join(options))
        print()


def start_game():
    print("=" * 50)
    print("THE QUEST FOR THE LEGENDARY TREASURE")
    print("=" * 50)
    print()
    print("You are an explorer searching for a legendary treasure.")
    print("The choices you make will decide if you find it or not.")
    print()

    # ask for the player's name and save it
    name = input("What is your name, explorer? ").strip()
    if name == "":
        name = "Explorer"

    print()
    print("Welcome " + name + "! Your adventure begins now.")
    print("There are two ways you can go:")
    print("  1. A dark forest")
    print("  2. A mysterious cave")
    print()

    choice = get_choice("Where do you want to go? (1 or 2) ", ["1", "2"])

    if choice == "1":
        return forest_path(name)
    else:
        return cave_path(name)


def forest_path(name):
    print()
    print("You walk into a dark forest.")
    print("There is a river on your left and a tall tree in front of you.")
    print()

    choice = get_choice("Do you follow the river (1) or climb the tree (2)? ", ["1", "2"])

    if choice == "1":
        print("You follow the river and you reach a big waterfall.")
        choice2 = get_choice("Do you build a raft (1) or swim across (2)? ", ["1", "2"])
        if choice2 == "1":
            print("You build a raft from some branches and cross safely.")
            print("On the other side you find a golden key in the mud!")
            return treasure_room(name, True)
        else:
            print("The water is way too fast and the current sweeps you away.")
            return "lose"
    else:
        print("You climb up the tree and you can see a temple far away.")
        print("There is also a bird nest near you with something shiny inside.")
        choice2 = get_choice("Do you go to the temple (1) or grab the shiny thing (2)? ", ["1", "2"])
        if choice2 == "1":
            print("You climb back down and walk towards the temple.")
            # no key on this path, but they still get a chance in the treasure room
            return treasure_room(name, False)
        else:
            print("A big angry bird attacks you and you fall down from the tree.")
            return "lose"


def cave_path(name):
    print()
    print("You go inside a mysterious cave. It is really dark in here.")
    print("You have a torch with you but it is not lit yet.")
    print()

    choice = get_choice("Do you light the torch (1) or go in the dark (2)? ", ["1", "2"])

    if choice == "1":
        print("You light the torch and now you can see two tunnels.")
        choice2 = get_choice("Do you take the left tunnel (1) or the right one (2)? ", ["1", "2"])
        if choice2 == "1":
            print("The left tunnel has a golden key sitting on a rock. You grab it.")
            return treasure_room(name, True)
        else:
            print("The right tunnel just leads to a locked door.")
            return treasure_room(name, False)
    else:
        print("You walk into the dark and you can't see anything at all.")
        choice2 = get_choice("Do you stop and light the torch now (1) or keep going (2)? ", ["1", "2"])
        if choice2 == "1":
            print("Good idea. Now you see a golden key hanging on the wall. You take it.")
            return treasure_room(name, True)
        else:
            print("You step into a hole you couldn't see and fall down.")
            return "lose"


def treasure_room(name, has_key):
    print()
    print("You finally make it to the treasure room.")
    print("There is a huge golden door with a big lock on it.")
    print()

    if has_key:
        choice = get_choice("Do you use the key (1) or try to break the door (2)? ", ["1", "2"])
        if choice == "1":
            print("The key fits and the door opens up!")
            print("You found the treasure! You win, " + name + "!")
            return "win"
        else:
            print("You try to smash the door open but the roof collapses on you.")
            return "lose"
    else:
        choice = get_choice("Do you look for another way in (1) or smash the lock (2)? ", ["1", "2"])
        if choice == "1":
            print("You search around and find a hidden lever. The door opens!")
            print("You found the treasure! You win, " + name + "!")
            return "win"
        else:
            print("You hit the lock with a rock and it sets off a trap.")
            return "lose"


def main():
    print("Setup works! Starting the game...")
    print()

    playing = True
    while playing:
        result = start_game()

        print()
        if result == "win":
            print("Congratulations, you completed the quest!")
        else:
            print("Game over. You didn't find the treasure this time.")

        again = get_choice("Do you want to play again? (y/n) ", ["y", "n"])
        if again == "n":
            print("Thanks for playing!")
            playing = False
        else:
            # add some space then the loop starts a fresh game
            print()
            print()


main()
