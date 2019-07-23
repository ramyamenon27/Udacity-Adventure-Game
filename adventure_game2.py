import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def story_intro(items, danger):
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {danger} is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold a trusty"
                " (but not very effective) dagger.\n")
    adventure_options(items, danger)


def adventure_options(items, danger):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    pick_game(items, danger)


def pick_game(items, danger):
    response = input("(Please enter 1 or 2)\n")
    if response == '1':
        house(items, danger)
    elif response == '2':
        cave(items, danger)
    else:
        pick_game(items, danger)


def yes_no():
    response = input("Would you like to play again? (y/n)")
    if response == 'y':
        print_pause("Excellent! Restarting the game...")
        start_adventure_game()
    elif response == 'n':
        print_pause("Thanks for playing! See you next time.")
    else:
        yes_no()


def fight_run(items, danger):
    response = input("Would you like to (1) fight"
                     " or (2) run away?")
    if response == '1':
        if "sword" in items:
            print_pause(f"As the {danger} moves to attack,"
                        " you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your hand"
                        " as you brace yourself for the attack.")
            print_pause(f"But the {danger} takes one look"
                        " at your shiny new toy and runs away!")
            print_pause(f"You have rid the town of the {danger}."
                        " You are victorious!")
            yes_no()
        if "sword" not in items:
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {danger}.")
            print_pause("You have been defeated!")
            yes_no()
    elif response == '2':
        print_pause("You run back into the field."
                    "Luckily you don't seem to have been followed.\n")
        adventure_options(items, danger)
    else:
        fight_run(items, danger)


def house(items, danger):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door"
                f" opens and out steps a {danger}.")
    print_pause(f"Eep! This is"
                f" the {danger}'s house!")
    print_pause(f"The {danger} attacks you!")
    if "sword" not in items:
        print_pause("You feel a bit under-prepared for this,"
                    " what with having only a tiny dagger.")
    fight_run(items, danger)


def cave(items, danger):
    print_pause("You peer cautiously into the cave.")
    if "sword" not in items:
        items.append("sword")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger"
                    "and take the sword with you.")
    elif "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now.")
    print_pause("You walk back out to the field.\n")
    adventure_options(items, danger)


def start_adventure_game():
    items = []
    list_of_dangers = ["troll", "dragon", "pirate", "wicked fairie"]
    danger = random.choice(list_of_dangers)
    story_intro(items, danger)


start_adventure_game()
