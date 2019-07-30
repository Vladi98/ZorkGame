
from Items import Items
from Player import Player
from Inventory import Inventory
from KidsRoom import KidsRoom
from Basement import Basement
from Rooms import Room
from Menu import Menu
class Ceiling(Room):

    items =[]

    def __init__(self,name):
        self.name = name

    
    def show_info(self):
        print("You are in the ceilling now, a fire is burning in a big stove! And there is a big window. As is it looks like the only way out is through this window, but it is looks like an armored winow")
        print("The following items are scattered all over the ceiling: ")
        for item in self.items:
            print(item.name)

    def add_items(self):
        item1 = Items('Tube of water','A tube filled with dirty water! Do not drink it')
        item2  = Items('Key','This is a key you can use it to open your way to the roof ')
        item3 = Items('Parachute','This is a very reliable military parachute')

        self.items.append(item1)
        self.items.append(item2)
        self.items.append(item3)


    def has_ligher(self):
        lighter =''
        for i in Basement.items:
            if i.name=='Lighter':
                lighter = i
                break
        if Player.inventory.check_if_has_item(lighter):
            return True
        
        print('You can not proceed, because it is too dark! Find something to help you see in the dark')
        return False


    def has_door(self):
        return False

    def smash_armored_window(self):
        keyItem =''
        for i in Player.inventory.collection_of_items:
            if i.name=='Hammer':
                keyItem = i
                break
        if Player.inventory.check_if_has_item(keyItem):
            return True
        
        print('Cannot open the window you need to have something to smash it')
        return False

    def jump_with_parachute(self):
        parachute =''
        for i in Player.inventory.collection_of_items:
            if i.name=='Parachute':
                parachute = i
                break
        if Player.inventory.check_if_has_item(parachute):
            return True
            Menu.action()

        print("You cannot jump because you will die! You need a parachute!")
        return

    def has_window(self):
        return True

    def all_passed(self):
        if self.has_window() and self.smash_armored_window() and self.jump_with_parachute():
            return True
        return False

        
