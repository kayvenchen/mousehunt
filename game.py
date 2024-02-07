'''
This file should borrow code from your Assignment 1.
However, it will require some modifications for this assignment.

Author: Kayven Chen
SID: 530654658
Unikey: kche4026
'''

'''
Keep this line!
'''
import random

'''
We recommend you import your 'name', 'train' and 'shop' modules to complete this 
question. It will save trouble in needing to copy and paste code from previous 
questions. However if you wish not to, you are free to remove the imports below.
Feel free to import other modules that you have written.
'''
import name as n
import train as t
import shop as s

# you can make more functions or global read-only variables here if you please!

def get_game_menu():
    '''
    Returns a string displaying all possible actions at the game menu.
    '''
    return ("1. Exit game\n"
           "2. Join the Hunt\n"
           "3. The Cheese Shop\n"
           "4. Change Cheese")


def change_cheese(name: str, trap: str, cheese: list, 
                  e_flag: bool = False) -> tuple:
    '''
    Handles the inputs and ouputs of the change cheese feature.
    '''
    trap_status = False
    trap_cheese = None
    while True:
        print(f"Hunter {name}, you currently have:")
        i = 0
        while i < len(cheese):
            print(f"{cheese[i][0]} - {cheese[i][1]}")
            i += 1
        print("")
        cheese_type = input("Type cheese name to arm trap: ")
        cheese_type = cheese_type.strip().capitalize()
        if cheese_type == "Back":
            break
        else:
            i = 0
            while i < len(cheese):
                if cheese_type == cheese[i][0]:
                    break
                i += 1
            if i == len(cheese):
                print("No such cheese!")
            else:
                if cheese[i][1] <= 0:
                    print("Out of cheese!")
                else:
                    arm_trap_input = input("Do you want to arm your trap with "
                                           f"{cheese_type}? ")
                    arm_trap_input = arm_trap_input.strip().lower() 
                    if arm_trap_input == "back":
                        break
                    elif arm_trap_input == "yes":
                        trap_cheese = cheese_type
                        trap_status = True
                        print(f"{trap} is now armed with {trap_cheese}!")
                        break
                    elif arm_trap_input == "no":
                        print("")
                        continue
        print("")
    return trap_status, trap_cheese


def consume_cheese(to_eat: str, cheese: str) -> tuple:
    '''
    Handles the consumption of cheese.
    Parameters:
        to_eat:    str,        the type of cheese to consume during the hunt.
        cheese:    str,        all the cheeses and quantities the player 
                               currently posseses.
    Returns:
        cheddar:   tuple,      the updated cheddar after the consumption.   
        marble:    tuple,      the updated marble after the consumption.
        swiss:     tuple,      the updated swiss after the consumption.
    Example:
    >>> consume_cheese('cheddar', [['cheddar', 2], ['marble', 0], ['swiss', 1]]
        return value: (('cheddar', 1), ('marble', 0), ('swiss', 1))
        
    >>> consume_cheese('marble', [['cheddar', 2], ['marble', 0], ['swiss', 1]] 
        return value: (('cheddar', 2), ('marble', 0), ('swiss', 1))
    '''
    i = 0
    while i < len(cheese):
        # check which cheese and if we have that cheese
        if to_eat == cheese[i][0] and cheese[i][1] > 0:
            cheese[i][1] -= 1
            break
        elif to_eat == cheese[i][0] and cheese[i][1] < 0:
            # cheese should never be negative so force cheese to be 0 if less
            # than 0
            cheese[i][1] = 0
        i += 1
    


def hunt(gold: int, cheese: list, trap_cheese: str | None, points: int) -> tuple:
    '''
    Handles the hunt mechanic.
    It includes the inputs and outputs of sounding the horn, the result of 
    the hunt, the gold and points earned, and whether users want to continue 
    after failing consecutively.
    Parameters:
        gold:        int,        the quantity of gold the player possesses.
        cheese:      list,       all the cheese and quantities the player 
                                 currently posseses.
        trap_cheese: str | None, the type of cheese that the trap is currently 
                                 armed with. if its not armed, value is None.
        points:      int,        the quantity of points that the player 
                                 currently posseses.
    Returns:
        gold:        int,        the updated quantity of gold after the hunt.   
        cheese:      tuple,      all the cheese and updated quantities after 
                                 the hunt.
        points:      int,        the updated quantity of points after the hunt.
    '''
    count = 0
    if trap_cheese != None:
        i = 0
        while i < len(cheese):
            if cheese[i][0] == trap_cheese:
                trap_cheese_amount = cheese[i][1]
                break
            i += 1
    else:
        trap_cheese_amount = 0
    while True:
        print("Sound the horn to call for the mouse...")
        horn_input = input("Sound the horn by typing \"yes\": ")
        horn_input.strip().lower()
        if horn_input == "yes":
            if trap_cheese_amount == 0:
                count += 1
                print("Nothing happens. You are out of cheese!")
            else:
                is_caught = random.random()
                if is_caught <= 0.5:
                    points += 115
                    gold += 125
                    count = 0
                    print("Caught a Brown mouse!")
                else:
                    count += 1
                    print("Nothing happens.")
                trap_cheese_amount -= 1
                cheese[i][1] = trap_cheese_amount

        elif horn_input == "stop hunt":
            break
        else:
            count += 1
            print("Do nothing.")       
        print(f"My gold: {gold}, My points: {points}\n")

        # if player fails to catch the mouse 5 times in a row
        if count == 5:
            continue_hunt = input("Do you want to "
                                    "continue to hunt? ")
            continue_hunt.strip().lower()
            if continue_hunt == "no":
                break
            count = 0
    return gold, points


def main():
    # Bob?
    title = "Mousehunt"
    logo = "       ____()()\n      /      @@\n`~~~~~\_;m__m._>o"
    author = "An INFO1110/COMP9001 Student"
    credits = f"Inspired by Mousehunt© Hitgrab\nProgrammer - {author}\n" \
               "Mice art - Joan Stark"
    print(f"{title}\n\n{logo}\n\n{credits}\n")
    name = str(input("What's ye name, Hunter?\n"))
    if n.is_valid_name(name) == False:
        name = "Bob"
    print(f"Welcome to the Kingdom, Hunter {name}!")
    # To train or not to train?
    train_input = input("Before we begin, let's train you up!\n" 
                     "Press \"Enter\" to start training or "
                     "\"skip\" to Start Game: ")
    train_input = train_input.strip().lower()
    if train_input == "":
        print("")
        trap = t.main()
    elif train_input == "skip":
        trap = "Cardboard and Hook Trap"
    gold = 125
    points = 0
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    trap_cheese = None
    # Game Menu
    while True:
        print(f"\nWhat do ye want to do now, Hunter {name}?")
        print(get_game_menu())
        game_input = input("")
        try: 
            game_input = int(game_input)
        except ValueError:
            pass
        if game_input == 1:
            break
        elif game_input == 2:
            hunt(gold, cheese, trap_cheese, points)
         # cheese shop
        elif game_input == 3:
            shop = s.main(trap, gold, cheese)
            gold = shop[0]
            cheese = shop[1]
        elif game_input == 4:
            trap_status, trap_cheese = change_cheese(name, trap, cheese)
            

if __name__ == '__main__':
    main()

