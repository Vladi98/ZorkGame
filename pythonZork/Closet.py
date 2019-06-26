from Rooms import Room
from Basement import Basement
from Player import Player

class Closet(Room):


    def __init__(self,name):
        self.name =name
        self.items =[]


    def show_info(self):
        print('You are in the closet! A very tiny and dark place. You should have a lighter in you to see the door and open it. This closet links directly to the hallway which will take you to the second floor.') 
        print('There are no items here! It is empty!')

    
    def has_door(self):
        return True



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
        


    def open_door(self):
        print('You opened the door it was not locked! There are stairs')
        return True

    def all_passed(self):
        if self.has_door() and self.open_door() and self.has_ligher():
            return True

