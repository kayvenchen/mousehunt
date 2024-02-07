'''
Write your answer for the full OO version of the game here.

Author: Kayven Chen
SID: 530654658
Unikey: kche4026
'''

import interface, trap, hunter
import train as t
from game_final import run_setup, get_title, name_check, should_skip

def main(Trap=trap.Trap(), Interface=interface.Interface(), 
         Hunter=hunter.Hunter()):
    has_personalization = run_setup()
    print(get_title())
    if has_personalization == True:
        player_name = name_check()
        hunter.Hunter.set_name(self=Hunter, player_name=player_name)
    print(f"Welcome to the Kingdom, Hunter {player_name}!")
    train_input = input("Before we begin, let's train you up!\n" 
                     "Press \"Enter\" to start training or "
                     "\"skip\" to Start Game: ")
    train_input = train_input.strip().lower()
    if train_input == "":
        print("")
        trap_name = t.main()
        trap.Trap.set_trap_name(self=Trap, trap=trap_name)
        trap.Trap.set_one_time_enchantment(self=Trap, enchant=True)
    elif train_input ==  "skip" or should_skip(train_input) == True:
        trap.Trap.set_trap_name(self=Trap , trap="Cardboard and Hook Trap")
        trap.Trap.set_one_time_enchantment(self=Trap, enchant=False)
    # Game Menu
    while True:
        print(f"\nWhat do ye want to do now, Hunter {player_name}?")
        print(interface.Interface.get_menu(self=Interface))
        game_input = input("Enter a number between 1 and 4: ")
        interface.Interface.move_to(self=Interface, choice=game_input)

if __name__ == '__main__':
    main()
