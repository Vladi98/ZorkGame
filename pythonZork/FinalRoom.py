
from Player import Player
from Items import Items
from Rooms import Room
from Basement import Basement

class FinalRoom(Room):

    def __init__(self,name):
        self.name = name
        self.items =[]
        #self.link_previous =link_previous

    
    def show_info(self):
        print("This is the final room of the second floor. It links directly to the cailing")
        print("The following items are scattered all over the basement: ")
        for item in self.items:
            print(item.get_name())


    def add_items(self):
        item1 = Items('Machete','This is a big and sharp machete you can use it to free yourself')
        item2  = Items('Bottle','Empty bottle')
        item3 = Items('Granade','This is a lighter use it to see where you are')
        item4 = Items('AK-47','The AK-47 is a gas-operated, 7.62×39mm assault rifle, developed in the Soviet Union by Mikhail Kalashnikov. It is the originating firearm of the Kalashnikov rifle (or "AK") family.')

        self.items.append(item1)
        self.items.append(item2)
        self.items.append(item3)
        self.items.append(item4)

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
        keyItem =''
        for i in Basement.items:
            if i.name=='Basementkey':
                keyItem = i
                break

        if Player.inventory.check_if_has_item(keyItem):
            print('The door is now open! There are stairs')
            return True
        
        print('Cannot open the door you dont have the neccesary key')
        return False

    def all_passed(self):
        if self.has_door() and self.open_door() and self.has_ligher():
            return True