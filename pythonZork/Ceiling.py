from Furnitures import Furniture
from Items import Items
from Player import Player
from Inventory import Inventory
class Ceiling:

    items =[]

    def __init__(self,name):
        self.name = name

    
    def show_info(self):
        print("You are in the ceilling now, a fire is burning in a big stove! And there is no residing house windows. As is it looks like the only way out is up to the roof, but it is unreachable ")
        print("The following items are scattered all over the ceiling: ")
        for item in self.items:
            print(item.name)

    def add_items_to_ceiling(self):
        item1 = Items('Tube of water','A tube filled with dirty water! Do not drink this shit')
        item2  = Items('Key','This is a key you can use it to open your way to the roof ')
        item4 = Items('A parachute','This is a very reliable military parachute')

        self.items.append(item1)
        self.items.append(item2)
        self.items.append(item3)
        self.items.append(item4)