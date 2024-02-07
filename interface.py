'''
Write your solution for the class Interface here.
This is your answer for Question 8.4.

Author: Kayven Chen
SID: 530654658
Unikey: kche4026
'''

import hunter
import cshop
import mouse

class Interface:
    def __init__(self, player=hunter.Hunter(), 
                 menu={1:"Exit game", 
                       2:"Join the Hunt", 
                       3:"The Cheese Shop", 
                       4:"Change Cheese"}):
        self.player = player
        self.menu = menu
    

    def change_cheese(self):
        trap_cheese = self.player.trap.get_trap_cheese()
        cheese = self.player.cheese
        trap = self.player.trap
        name = self.player.get_name()
        e_flag = self.player.trap.get_one_time_enchantment()
        while True:
            print(f"Hunter {name}, you currently have:")
            print(self.player.get_cheese())
            print("")
            cheese_type = input("Type cheese name to arm trap: ")
            cheese_type = cheese_type.strip().capitalize()
            if e_flag == True:
                print(f"Your {trap} has a one-time enchantment granting "
                      f"{trap.get_benefit(cheese_type)}.")
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
                        arm_trap_input = input("Do you want to arm your trap "
                                               f"with {cheese_type}? ")
                        arm_trap_input = arm_trap_input.strip().lower() 
                        if arm_trap_input == "back":
                            break
                        elif arm_trap_input == "yes":
                            self.player.arm_trap(cheese_type)
                            trap_cheese = self.player.trap.get_trap_cheese()
                            print(f"{trap} is now armed with {trap_cheese}!")
                            break
                        elif arm_trap_input == "no":
                            print("")
                            continue
            print("")


    def cheese_shop(self):
        shop = cshop.CheeseShop()
        shop.move_to(Hunter=self.player)


    def hunt(self):
        '''
        Handles the hunt mechanic.
        It includes the inputs and outputs of sounding the horn, the result of 
        the hunt, the gold and points earned, and whether users want to continue 
        after failing consecutively.
        '''
        trap_cheese = self.player.trap.get_trap_cheese()
        cheese = self.player.cheese
        count = 0
        enchant = self.player.trap.get_one_time_enchantment()
        gold = self.player.get_gold()
        points = self.player.get_points()
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
                    caught_mouse = str(mouse.generate_mouse(trap_cheese, 
                                                            enchant))
                    if caught_mouse != "None":
                        gold += mouse.loot_lut(caught_mouse)[0]
                        points += mouse.loot_lut(caught_mouse)[1]
                        if (enchant == True and 
                            trap_cheese == "Cheddar" and 
                            caught_mouse == "Brown"):
                            points += 25
                        elif (enchant == True and 
                              trap_cheese == "Marble" 
                              and caught_mouse == "Brown"):
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
        self.player.set_gold(loot=gold)
        self.player.set_points(loot=points)
        self.player.trap.set_one_time_enchantment(False)
    
    def get_menu(self):
        menu = list(self.menu.items())
        formatted_string = ""
        i = 0
        while i < len(menu):
            if i == len(menu)-1:
                formatted_string = (formatted_string + 
                                    f"{menu[i][0]}. {menu[i][1]}")
            else:
                formatted_string = (formatted_string + 
                                    f"{menu[i][0]}. {menu[i][1]}\n")
            i += 1
        return formatted_string
    
    def move_to(self, choice:int):
        # Game Menu
        try: 
            choice = int(choice)
        except ValueError:
            pass
        if choice == 1:
            quit()
        # hunt
        elif choice == 2:
            self.hunt()
        # cheese shop
        elif choice == 3:
            print(cshop.CheeseShop.greet(cshop.CheeseShop()))
            print("")
            self.cheese_shop()
        # change cheese
        elif choice == 4:
            self.change_cheese()
        # out of range
        elif isinstance(choice, int):
            if choice < 1 or choice > 4:
                print("Must be within 1 and 4.")
        # invalid
        else:
            print("Invalid input. Try again!")

