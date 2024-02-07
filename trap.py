'''
Write your solution for the class Trap here.
This is your answer for Question 8.1.

Author: Kayven Chen
SID: 530654658
Unikey: kche4026
'''

class Trap:
    def __init__(self):
        self.trap_name = ""
        self.trap_cheese = None
        self.arm_status = False
        self.one_time_enchantment = False
        

    def set_trap_name(self, trap) -> str:
        type_of_traps = ("Cardboard and Hook Trap", 
                         "High Strain Steel Trap", 
                         "Hot Tub Trap")
        i = 0
        while i < len(type_of_traps):
            if trap == type_of_traps[i]:
                self.trap_name = trap
                break
            i += 1


    def set_trap_cheese(self, cheese) -> int:
        i = 0
        types_of_cheese = ["Cheddar", "Marble", "Swiss"]
        while i < len(types_of_cheese):
            if cheese == types_of_cheese[i]:
                self.trap_cheese = types_of_cheese[i]
                break
            else:
                self.trap_cheese = None
            i += 1


    def set_arm_status(self) -> int:
        if not self.trap_cheese == None or self.set_trap_name == "":
            self.arm_status = True
        else:
            self.arm_status = False


    def set_one_time_enchantment(self, enchant) -> int:
        if self.trap_name != "Cardboard and Hook Trap":
            self.one_time_enchantment = True
        # toggle enchant so that when it's used it's GONE??
        if enchant == False:
            self.one_time_enchantment = False


    def get_trap_name(self):
        return self.trap_name


    def get_trap_cheese(self):
        return self.trap_cheese


    def get_arm_status(self):
        return self.arm_status


    def get_one_time_enchantment(self):
        return self.one_time_enchantment


    @staticmethod
    def get_benefit(cheese:str):
        benefits = {"Cheddar": "+25 points drop by next Brown mouse",
                    "Marble":"+25 gold drop by next Brown mouse",
                    "Swiss": "+0.25 attraction to Tiny mouse"}
        return benefits[cheese]


    def __str__(self):
        if self.one_time_enchantment:
            return f"One-time Enchanted {self.trap_name}" 
        else:
            return self.trap_name
