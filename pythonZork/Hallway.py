from Items import Items
from Commands import Commands
from Player import Player
from Rooms import Room

class Hallway(Room):

    def __init__(self,name):
        self.name =name
        self.items =[]


    def show_info(self):
        print('You are in a long hallway! A door can be seen in the dictance, but between you and the door, there is a big hall, make sure you have something to put over it so you can pass.') 
        print("The only item here is: ")
        for item in self.items:
            print(item.name)

    
    def has_door(self):
        return True

    def add_items(self):
        item1  = Items('Board','A big board')
        self.items.append(item1)
    
    def has_ligher(self):
        return True

    def has_no_hall(self):
        board=''
        for i in self.items:
            if i.name=='Board':
                board = i
                break

        if Player.inventory.check_if_has_item(board):
            return True
        print("You can not pass accross at this point")
        return False
    


    def open_door(self):
        print('You opened the door it was not locked! There are stairs')
        return True

    def all_passed(self):
        if self.has_door() and self.open_door() and self.has_ligher():
            return True
    