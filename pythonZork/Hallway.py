from Items import Items
from Commands import Commands
from Player import Player
from Rooms import Room

class Hallway(Room):

    items =[]
    def __init__(self,name):
        self.name =name
        


    def show_info(self):
        print('You are in a long hallway! A door can be seen in the dictance, but between you and the door, there is a big hall, make sure you have something to put over it so you can pass. Also the hall needs to be covered before going up') 
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
        for i in Player.inventory.collection_of_items:
            if i.name=='Board':
                board = i
                break

        if Player.inventory.check_if_has_item(board):
            return True
        print("You can not pass accross at this point")
        return False
    


    def open_door(self):
        if self.has_no_hall():
            print('You opened the Hallway door it was not locked! There are stairs')
            return True
        return False

    def all_passed(self):
        if self.has_door() and self.open_door() and self.has_ligher() and self.has_no_hall():
            return True
        return False
    