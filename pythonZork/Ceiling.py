from Furnitures import Furniture
from Items import Items
from Player import Player
from Inventory import Inventory
from KidsRoom import KidsRoom
from Basement import Basement
from Rooms import Room

class Ceiling(Room):

    items =[]

    def __init__(self,name):
        self.name = name

    
    def show_info(self):
        print("You are in the ceilling now, a fire is burning in a big stove! And there is no residing house windows. As is it looks like the only way out is up to the roof, but it is unreachable ")
        print("The following items are scattered all over the ceiling: ")
        for item in self.items:
            print(item.name)

    def add_items(self):
        item1 = Items('Tube of water','A tube filled with dirty water! Do not drink this shit')
        item2  = Items('Key','This is a key you can use it to open your way to the roof ')
        item3 = Items('A parachute','This is a very reliable military parachute')

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


    def smash_armored_window(self):
        keyItem =''
        for i in KidsRoom.items:
            if i.name=='Hammer':
                keyItem = i
                break
        if Player.inventory.check_if_has_item(keyItem):
            print('You opened the window, you Rock! Now type jump to escape the house!')
            return True
        
        print('Cannot open the window you need to have something to smash it')
        return False

    def jump_with_parachute(self):
        print("Congratulations! You passed the game! You are one tough s_n of a b___h")
        
