
from Player import Player
from Items import Items
from Rooms import Room
from Basement import Basement

class FinalRoom(Room):

    items=[]
    def __init__(self,name):
        self.name = name
        #self.link_previous =link_previous

    
    def show_info(self):
        print("This is the final room of the second floor. It links directly to the cailing")
        print("The following items are scattered all over the room: ")
        for item in self.items:
            print(item.name)


    def add_items(self):
        item1 = Items('Finalroomkey','A key for the Finalroom door')
        item2  = Items('Bottle','Empty bottle')
        item3 = Items('Granade','This is a lighter use it to see where you are')
        item4 = Items('AK-47','The AK-47 is a gas-operated, 7.62×39mm assault rifle, developed in the Soviet Union by Mikhail Kalashnikov. It is the originating firearm of the Kalashnikov rifle (or "AK") family.')

        self.items.append(item1)
        self.items.append(item2)
        self.items.append(item3)
        self.items.append(item4)

    def has_door(self):
        return True
   

    def open_door(self):
        keyItem =''
        for i in Player.inventory.collection_of_items:
            if i.name=='Finalroomkey':
                keyItem = i
                break

        if Player.inventory.check_if_has_item(keyItem):
            return True
        
        print('Cannot open the Finalroom door you dont have the neccesary key')
        return False

    def all_passed(self):
        if self.has_door() and self.open_door() and self.has_ligher():
            return True
        return False