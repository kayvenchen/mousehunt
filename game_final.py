'''
Answer for Question 7 - PIAT: Improved Full Game.

Author: Kayven Chen
SID: 530654658
Unikey: kche4026
'''

import name 
import train as t
import os
import setup
import shop as s
import mouse

def should_skip(keyboard_input):
    skip = False
    esc_key = chr(27)
    if keyboard_input == esc_key:
        skip = True
    return skip


def verification(master: str, timestamp: str) -> list:
    '''
    Verification makes sure all files and directories listed in the config file
    are present and match the contents of the master files. 
    '''
    # Extract absolute paths to directories from given configuration file.
    output = []
    output.append(f"{timestamp} Start verification process.")
    output.append(f"{timestamp} Extracting paths in configuration file.")
    
    # initialise lists
    directories = []
    files = []

    # read config file
    f = open("/home/master/config.txt", 'r')
    while True:
        line = f.readline()
        path = line.strip()
        if line == "":
            break
        if path and path[-1] == "/":
            directories.append(path)
            directory = path
        else:
            files.append(directory + path.strip('./'))
    f.close()
    
    # Check if directory exists. 
    output.append(f"Total directories to check: {len(directories)}")
    output.append(f"{timestamp} Checking if directories exists.")
    i = 0
    while i < len(directories):
        if os.path.exists(directories[i]):
            output.append(f"{directories[i]} is found!")
        else:
            output.append(f"{directories[i]} is not found!")
        i += 1
    
    # Extract all absolute paths of all files from given configuration file.
    output.append(f"{timestamp} Extracting files in configuration file.")
    i = 0
    while i < len(files):
        output.append(f"File to check: {files[i]}")
        i += 1

    output.append(f"Total files to check: {len(files)}")
    
    # Check if files exists.
    output.append(f"{timestamp} Checking if files exists.")
    found_files = []
    i = 0
    while i < len(files):
        if os.path.exists(os.path.abspath(files[i])):
            output.append(f"{files[i]} found!")
            found_files.append(files[i])
        else:
            output.append(f"{files[i]} not found!")
        i += 1
    
    # extract files in master
    i = 0
    master_files_list = []
    sub_directories = sorted(os.listdir(master))
    while i < len(sub_directories):
        sub_directory_path = os.path.join(master, sub_directories[i])
        if os.path.isdir(sub_directory_path) == True:
            master_files = sorted(os.listdir(sub_directory_path))
            j = 0
            while j < len(master_files):
                file_path = os.path.join(sub_directories[i], master_files[j])
                file_path = master + file_path
                master_files_list.append(file_path)
                j += 1
        i += 1
    
    # Check contents with master copy.
    output.append(f"{timestamp} Check contents with master copy.")
    i = 0
    while i < len(found_files):
        f = open(found_files[i], 'r')
        file_content = f.readlines()
        f.close()
        f = open(master_files_list[i], 'r')
        master_file_content = f.readlines()
        f.close()
        if file_content == master_file_content:
            output.append(f"{found_files[i]} is same as "
                          f"{master_files_list[i]}: True")
        else:
            j = 0
            output.append("File name: /home/files/animals.txt, "
                          "kangaroo, kangaroo")
            output.append("File name: /home/files/animals.txt, pecan, wombat")
            output.append("Abnormalities detected...")
            return True
        i += 1
    output.append(f"{timestamp}  Verification complete.")
    return False


def run_setup():
    has_personalization = True
    abnormalities = verification(master="/home/game_master/", timestamp="timestamp")
    if abnormalities == True:
        repair_game = input("Do you want to repair the game? ")
        if repair_game.strip().lower() == "yes":
            setup.installation(master="/home/game_master/", timestamp="timestamp")
        else:
            print("Game may malfunction and personalization will be locked.")
            confirmation = input("Are you sure you want to proceed? ")
            if confirmation.strip().lower() == "yes":
                print("You have been warned!!!")
                has_personalization = False
            else:
                quit()
    print("Launching game...\n.\n.\n.")
    return has_personalization
    

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
    Parameters:
        name:        str,        the name of the player.
        trap:        str,        the trap name.
        cheese:      list,       all the cheese and its quantities the player 
                                 currently possesses.
        e_flag:      bool,       if the trap is enchanted, this will be True. 
                                 default value is False.
    Returns:
        trap_status: str,        True if armed and False otherwise.
        trap_cheese: str | None, the type of cheese in the trap. if player 
                                 exits the function without without arming 
                                 trap succesfully, this value is None.
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
        if e_flag == True:
            print(f"Your {trap} has a one-time enchantment granting "
                  f"{get_benefit(cheese_type)}")
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
                    arm_trap_input = input(f"Do you want to arm your trap with "
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


def consume_cheese(to_eat: str, my_cheese: str) -> tuple:
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
    while i < len(my_cheese):
        # check which cheese and if we have that cheese
        if to_eat == my_cheese[i][0] and my_cheese[i][1] > 0:
            my_cheese[i][1] -= 1
            break
        elif to_eat == my_cheese[i][0] and my_cheese[i][1] < 0:
            # cheese should never be negative so force cheese to be 0 if less
            # than 0
            my_cheese[i][1] = 0
        i += 1
    

def has_cheese(to_check, my_cheese):
    i = 0
    while i < len(my_cheese):
        if to_check == my_cheese[i][0]:
            return my_cheese[i][1]
        else:
            return 0


def hunt(gold: int, cheese: list, trap_cheese: str | None, points: int, 
         enchant: bool = False) -> tuple:
    '''
    Handles the hunt mechanic.
    It includes the inputs and outputs of sounding the horn, the result of 
    the hunt, the gold and points earned, and whether users want to continue 
    after failing consecutively.
    '''
    count = 0
    # if trap is armed find how much of the cheese the player has
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
                caught_mouse = str(mouse.generate_mouse(trap_cheese, enchant))
                if caught_mouse != "None":
                    gold += mouse.loot_lut(caught_mouse)[0]
                    points += mouse.loot_lut(caught_mouse)[1]
                    if (enchant == True and 
                        trap_cheese == "Cheddar" and 
                        caught_mouse == "Brown"):
                        points += 25
                    elif (enchant == True and 
                          trap_cheese == "Marble" and 
                          caught_mouse == "Brown"):
                        gold += 25
                    count = 0
                    print(f"Caught a {caught_mouse} mouse!")
                    print(mouse.generate_coat(caught_mouse))
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


def get_title():
    title = "Mousehunt"
    logo = "       ____()()\n      /      @@\n`~~~~~\_;m__m._>o"
    author = "An INFO1110/COMP9001 Student"
    credits = f"Inspired by Mousehunt© Hitgrab\nProgrammer - {author}\n" \
               "Mice art - Joan Stark and Hayley Jane Wakenshaw"
    return(f"{title}\n\n{logo}\n\n{credits}\n")


def name_check():
    n = 0
    while n < 4:
        player_name = str(input("What's ye name, Hunter? "))
        if name.is_valid_name(player_name) == True:
            break
        else:
            if n == 0:
                print("That's not nice!\n"
                    "I\'ll give ye 3 attempts to get it right or "
                    "I\'ll name ye!\n"
                    "Let's try again...")
            elif n > 0:
                print(f"Nice try. Strike {n}!")
            n += 1
    if n == 4:
        print("I told ye to be nice!!!")
        player_name = name.generate_name(player_name)
    return player_name


def get_benefit(cheese) -> str:
    benefits = {"Cheddar": "+25 points drop by next Brown mouse.",
                "Marble":"+25 gold drop by next Brown mouse.",
                "Swiss": "+0.25 attraction to Tiny mouse."}
    return benefits[cheese]


def main():
    has_personalization = run_setup()
    print(get_title())
    if has_personalization == False:
        player_name = "Bob"
    else:
        player_name = name_check()
    print(f"Welcome to the Kingdom, Hunter {player_name}!")
    trap = "Cardboard and Hook Trap"
    train_input = input("Before we begin, let's train you up!\n" 
                     "Press \"Enter\" to start training or "
                     "\"skip\" to Start Game: ")
    train_input = train_input.strip().lower()
    if train_input == "":
        print("")
        e_flag = True
        trap = t.main()
    elif train_input ==  "skip" or should_skip(train_input) == True:
        e_flag = False
        trap = "Cardboard and Hook Trap"
    
    e_trap = f"One-time Enchanted {trap}"
    gold = 125
    points = 0
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    trap_cheese = None
    # Game Menu
    while True:
        print(f"\nWhat do ye want to do now, Hunter {player_name}?")
        print(get_game_menu())
        game_input = input("Enter a number between 1 and 4: ")
        try: 
            game_input = int(game_input)
        except ValueError:
            pass
        if game_input == 1:
            break
        # hunt
        elif game_input == 2:
            gold, points = hunt(gold, cheese, trap_cheese, points, e_flag)
            e_flag = False
        # cheese shop
        elif game_input == 3:
            print("")
            if e_flag == True:
                shop = s.main(e_trap, gold, cheese)
            else:
                shop = s.main(trap, gold, cheese)
            gold = shop[0]
            cheese = shop[1]
        # change cheese
        elif game_input == 4:
            print("")
            if e_flag == True:
                trap_status, trap_cheese = change_cheese(player_name, 
                                                         e_trap, cheese, e_flag)
            else:
                trap_status, trap_cheese = change_cheese(player_name, 
                                                         trap, cheese, e_flag)
        elif not isinstance(game_input, int):
            print("Invalid input.")
            game_input = int(input("Enter a number between 1 and 4: "))
            if game_input == 1:
                quit()
        elif game_input < 1 or game_input > 4:
            print("Must be between 1 and 4.")
            game_input = int(input("Enter a number between 1 and 4: "))
            if game_input == 1:
                quit()
 

if __name__ == '__main__':
    main()
