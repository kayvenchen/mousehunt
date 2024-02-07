'''
Write your solution to 1. Upgraded Cheese Shop here.
It should borrow code from Assignment 1.

Author: Kayven Chen
SID: 530654658
Unikey: kche4026
'''

CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))

# you can make more functions or global read-only variables here if you please!

def buy_cheese(gold: int) -> tuple:
    '''
    Feature for players to buy cheddar from shop
    '''
    initial_gold = gold
    gold_spent = 0
    cheese_bought = [0, 0, 0]
    while True:
        print(f"You have {gold} gold to spend.")
        player_request = input("State [cheese quantity]: ")
        player_request = player_request.strip().lower()
        if player_request == "back":
            break
        i = 0
        while i < len(CHEESE_MENU):
            cheese_found = False
            cheese = CHEESE_MENU[i][0].lower()
            if cheese == (player_request.split(" ")[0]).lower():
                cheese_found = True
                cheese_price = CHEESE_MENU[i][1]
                try:
                    cheeese_quantity = int(player_request.split(" ")[1])
                except ValueError:
                    print("Invalid quantity.")
                    break
                except TypeError:
                    print("Missing quantity.")
                    break
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
                i = len(CHEESE_MENU)
            else:
                i += 1
        if cheese_found == False:
            print(f"We don't sell {player_request.split(' ')[0].lower()}!")
    gold_spent = initial_gold - gold
    cheese_bought = tuple(cheese_bought)
    return gold_spent, cheese_bought
    
def display_inventory(gold: int, cheese: int, trap: str) -> None:
    '''
    Prints contents of inventory
    '''
    print(f"Gold - {gold}\nCheddar - {cheese[0][1]}\nMarble - {cheese[1][1]}\n"
          f"Swiss - {cheese[2][1]}\nTrap - {trap}")


def main(trap, gold, cheese):
    '''Cheese shop returns gold and cheese'''
    print("Welcome to The Cheese Shop!\nCheddar - 10 gold\n"
          "Marble - 50 gold\nSwiss - 100 gold\n")
    while True:
        shop_input = input("How can I help ye?\n"
                           "1. Buy cheese\n"
                           "2. View inventory\n"
                           "3. Leave shop\n")
        try:
            shop_input= int(shop_input)
        except ValueError:
            pass
        if shop_input == 1:
            buy_function = buy_cheese(gold)
            gold = gold - buy_function[0]
            i = 0
            while i < len(buy_function[1]):
                cheese[i][1] += buy_function[1][i]
                i += 1
            print("")
        elif shop_input == 2:
            display_inventory(gold, cheese, trap)
            print("")
        elif shop_input == 3:
            break
        else:
            print("I did not understand.\n")
    return gold, cheese

if __name__ == "__main__":
    gold = 125
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    trap = 'Cardboard and Hook Trap'
    main(trap, gold, cheese)

