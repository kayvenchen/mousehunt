'''
Write your solution for the class Hunter here.
This is your answer for Question 8.2.

Author: Kayven Chen
SID: 530654658
Unikey: kche4026
'''

import trap
import name

class Hunter:
    def __init__(self):
        self.name = "Bob"
        self.cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
        self.trap = trap.Trap()
        self.gold = 125
        self.points = 0

    def set_name(self, player_name):
      if name.is_valid_name(player_name):
          self.name = player_name


    def set_cheese(self, cheese_type):
        if (isinstance(cheese_type, tuple) and 
            len(cheese_type) == len(self.cheese)):
            i = 0
            while i < len(cheese_type):
                self.cheese[i][1] = cheese_type[i]
                i += 1


    def set_gold(self, loot):
        if isinstance(loot, int):
            self.gold = loot


    def set_points(self, loot):
        if isinstance(loot, int):
            self.points = loot


    def get_name(self) -> str:
        return self.name


    def get_cheese(self) -> str:
        i = 0
        formatted_string = ""
        while i < len(self.cheese):
            if i == len(self.cheese) -1:
                formatted_string = (formatted_string + 
                                    f"{self.cheese[i][0]} - {self.cheese[i][1]}")
            else:
                formatted_string = (formatted_string + 
                                    f"{self.cheese[i][0]} - {self.cheese[i][1]}\n")
            i += 1
        return formatted_string


    def get_gold(self) -> int:
        return self.gold


    def get_points(self) -> int:
        return self.points
    

    def display_inventory(self) -> str:
        return f"Gold - {self.gold}\n{self.get_cheese()}\nTrap - {self.trap}"


    def update_cheese(self, cheese_quantity:tuple):
        if isinstance(cheese_quantity, tuple):
            i = 0
            while i < len(cheese_quantity):
                self.cheese[i][1] += cheese_quantity[i]
                i += 1

    def update_gold(self, loot:int):
        if isinstance(loot, int):
            self.gold += loot


    def update_points(self, loot:int):
        if isinstance(loot, int):
            self.points += loot


    def consume_cheese(self, cheese_type:str):
        i = 0
        while i < len(self.cheese):
            if cheese_type == self.cheese[i][0]:
                self.cheese[i][1] -= 1
                break
            i += 1


    def have_cheese(self, cheese_type:str="Cheddar"):
        i = 0
        while i < len(self.cheese):
            if cheese_type == self.cheese[i][0]:
                return(self.cheese[i][1])
            i += 1
        return 0


    def arm_trap(self, cheese_type:str):
        i = 0
        while i < len(self.cheese):
            if (cheese_type.capitalize() == self.cheese[i][0] and 
                self.cheese[i][1] > 0):
                self.trap.set_trap_cheese(cheese_type.capitalize())
                self.trap.set_arm_status()
                break
            else:
                self.trap.set_trap_cheese(None)
                self.trap.set_arm_status()
            i += 1
    
    def __str__(self):
        return f"Hunter {self.name}\n{self.display_inventory()}"
    
