'''
Write your solution for the class CheeseShop here.
This is your answer for Question 8.3.

Author: Kayven Chen
SID: 530654658
Unikey: kche4026
'''

import hunter

class CheeseShop:
    def __init__(self, cheeses={"Cheddar":10, "Marble":50, "Swiss":100}, 
                 menu={1:"Buy cheese", 2:"View inventory", 3:"Leave shop"}):
        self.cheeses = cheeses
        self.menu = menu


    def get_cheeses(self):
        cheeses = list(self.cheeses.items())
        formatted_string = ""
        i = 0
        while i < len(cheeses):
            if i == len(cheeses)-1:
                formatted_string = formatted_string + \
                                   f"{cheeses[i][0]} - {cheeses[i][1]} gold"
            else:
                formatted_string = formatted_string + \
                                   f"{cheeses[i][0]} - {cheeses[i][1]} gold\n"
            i += 1
        return formatted_string


    def get_menu(self):
        menu = list(self.menu.items())
        formatted_string = ""
        i = 0
        while i < len(menu):
            if i == len(menu)-1:
                formatted_string = formatted_string + \
                                   f"{menu[i][0]}. {menu[i][1]}"
            else:
                formatted_string = formatted_string + \
                                   f"{menu[i][0]}. {menu[i][1]}\n"
            i += 1
        return formatted_string


    def greet(self):
        return f"Welcome to The Cheese Shop!\n{self.get_cheeses()}"


    def buy_cheese(self, gold:int):
        '''returns remaining gold and quantity of each cheese bought'''
        cheese_bought = [0, 0, 0]
        cheese_menu = tuple(self.cheeses.items())
        while True:
            print(f"You have {gold} gold to spend.")
            player_request = input("State [cheese quantity]: ")
            player_request = player_request.strip().lower()
            if player_request == "back":
                break
            # check if we sell the cheese
            i = 0
            while i < len(cheese_menu):
                cheese_found = False
                cheese = cheese_menu[i][0].lower().strip()
                if cheese == (player_request.split(" ")[0].lower().strip()):
                    cheese_found = True
                    cheese_price = cheese_menu[i][1]
                    break
                i += 1
            if cheese_found == False:
                print(f"We don't sell {player_request.split(' ')[0].lower()}!")
            elif cheese_found == True:
                try:
                    cheeese_quantity = int(player_request.split(" ")[1])
                except ValueError:
                    print("Invalid quantity.")
                    continue
                except TypeError:
                    print("Missing quantity.")
                    continue
                
                if cheeese_quantity > 0:
                    gold_spent = cheeese_quantity * cheese_price
                    if gold_spent > gold:
                        gold_spent = 0
                        print("Insufficient gold.")
                    else:
                        cheese_bought[i] += cheeese_quantity
                        gold -= gold_spent
                        print(f"Successfully purchase {cheeese_quantity} " 
                              f"{cheese}.") 
                else:
                    print("Must purchase positive amount of cheese.")
        cheese_bought = tuple(cheese_bought)
        return gold, cheese_bought


    def move_to(self, Hunter):
        while True:
            print(f"How can I help ye?\n{self.get_menu()}")
            shop_input = input()
            try:
                shop_input= int(shop_input)
            except ValueError:
                pass
            if shop_input == 1:
                gold=hunter.Hunter.get_gold(self=Hunter)
                buy_function = self.buy_cheese(gold=gold)
                hunter.Hunter.set_gold(self=Hunter, loot=buy_function[0])
                hunter.Hunter.update_cheese(self=Hunter, 
                                            cheese_quantity=buy_function[1])
                print("")
            elif shop_input == 2:
                print(hunter.Hunter.display_inventory(self=Hunter))
                print("")
            elif shop_input == 3:
                break
            elif isinstance(shop_input, int): 
                if shop_input < 1 or shop_input > 3:
                    raise ValueError
            else:
                print("I did not understand.\n")

