'''
Answer for Question 5 - The Training Again from Assignment 1.

Author: Kayven Chen
SID: 530654658
Unikey: kche4026
'''

# you can make more functions or global read-only variables here if you please!


def should_skip(keyboard_input):
    skip = False
    esc_key = chr(27)
    if keyboard_input == esc_key:
        skip = True
    return skip

def intro():
    '''
    Prints the introduction by Larry.
    '''
    print("Larry: I'm Larry. I'll be your hunting instructor.")


def travel_to_camp():
    '''
    Prints the game conversation of travelling and reaching the camp.
    '''
    print("Larry: Let's go to the Meadow to begin your training!")
    travel_input = input("Press Enter to travel to the Meadow...")
    if should_skip(travel_input) == True:
        return True
    print("Travelling to the Meadow...")
    print("Larry: This is your camp. Here you'll set up your mouse trap.")


def setup_trap() -> tuple:
    '''
    Prints the game conversation of getting your first trap and setting it.
    '''
    trap = "Cardboard and Hook Trap"
    left_trap = "High Strain Steel Trap"
    right_trap = "Hot Tub Trap"
    cheddar = 0
    print("Larry: Let's get your first trap...")
    view_traps_input = input("Press Enter to view traps that Larry is holding...")
    if should_skip(view_traps_input) == True:
        return True
    print(f'''Larry is holding...\nLeft: {left_trap}\nRight: {right_trap}''')
    trap_input = input("Select a trap by typing \"left\" or \"right\": ")
    if should_skip(trap_input) == True:
        return True
    trap_input = trap_input.strip().lower()
    if trap_input == "left" or trap_input == "right":
        print("Larry: Excellent choice.")
        if trap_input == "left":
            trap = left_trap
        elif trap_input == "right":
            trap = right_trap
        print(f"Your \"{trap}\" is now set!")
        print("Larry: You need cheese to attract a mouse.")
        cheddar += 1
        print("Larry places one cheddar on the trap!")
    else:
        print("Invalid command! No trap selected.")
        print("Larry: Odds are slim with no trap!")
    return trap, cheddar 


def sound_horn() -> str:
    '''
    Prints the game conversation to sound horn
    '''
    print("Sound the horn to call for the mouse...")
    horn_input = None
    horn_input = input("Sound the horn by typing \"yes\": ")
    if should_skip(horn_input) == True:
        return True
    horn_input = horn_input.strip().lower()
    return horn_input
    


def basic_hunt(cheddar: int, horn_input: str) -> bool:  
    '''
    Prints the hunt and Larry's feedback of hunt.
    '''
    hunt_status = False
    if horn_input == "yes" and cheddar == 1:
        hunt_status = True
        print("Caught a Brown mouse!")
        print("Congratulations. Ye have completed the training.")
    else:
        print("Nothing happens.")
        if horn_input != "yes" and cheddar == 0:
            pass
        else:
            print("To catch a mouse, you need both trap and cheese!")
    return hunt_status
    

def end(hunt_status: bool):
    '''
    Prints the 'Good luck~' message if hunt was successful
    '''
    if hunt_status == True:
        print("Good luck~")

def main():
    intro()
    travel = travel_to_camp()
    if travel == True:
        pass
    else:
        while True:
            trap = setup_trap()
            if trap == True:
                break
            horn_input = sound_horn()
            if horn_input == True:
                break
            hunt_status = basic_hunt(trap[1], horn_input)
            end(hunt_status)
            continue_game = input("\nPress Enter to continue training and "
                                "\"no\" to stop training: ")
            continue_game = continue_game.strip().lower()
            if continue_game == "no" or should_skip(continue_game) == True:
                break
        try:
            return trap[0]
        except:
            pass


if __name__ == '__main__':
    main()

