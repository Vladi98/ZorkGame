from Commands import Commands
from Player import Player
from Rooms import Room
from Items import Items


class Basement(Room):

    items =[]

    def __init__(self,name):
        self.name = name
        #self.link_previous =link_previous

    
    def show_info(self):
        print("This is the basement, it is dark in here! This is your starting position! There is a door use it to exit the basement!")
        print("The following items are scattered all over the basement: ")
        for item in self.items:
            print(item.get_name())


    def add_items(self):


        item1 = Items('Machete','This is a big and sharp machete you can use it to free yourself')
        item2  = Items('Basementkey','This is a key use it to open the door')
        item3 = Items('Lighter','This is a lighter use it to see where you are')
        item4 = Items('Axe','This is an axe use it to cut and break things')

        self.items.append(item1)
        self.items.append(item2)
        self.items.append(item3)
        self.items.append(item4)

    def has_door(self):
        return True
   

    def has_ligher(self):
        lighter =''
        for i in Player.inventory.collection_of_items:
            if i.name=='Lighter':
                lighter = i
                break

        if Player.inventory.check_if_has_item(lighter):
            return True
        
        print('You can not proceed, because it is too dark! Find something to help you see in the dark')
        return False

    def open_door(self):
        keyItem =''
        for i in Player.inventory.collection_of_items:
            if i.name=='Basementkey':
                keyItem = i
                break

        if Player.inventory.check_if_has_item(keyItem):
            return True
        
        print('Cannot open the Basement door you dont have the neccesary key')
        return False


    def all_passed(self):
        if self.has_door() and self.open_door() and self.has_ligher():
            return True
        return False

