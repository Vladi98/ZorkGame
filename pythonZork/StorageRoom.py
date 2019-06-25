from Furnitures import Furniture
from Items import Items
from Player import Player
from Rooms import Room

class StorageRoom(Room):

    def __init__(self,name,links):
        self.name =name
        self.links = links
        self.items =[]


    def show_info(self):
        print('This is a storage room! Looks like just another room filled with boxes and barrels, but look out! Rah! It has a chain over the door','It links to the resting rooms')
        print('It has the following furnitures inside:')
     
        print('and the following items scattered all over the room: ')
        for item in self.items:
            print(item.name)

    
    def has_door(self):
        return True

    def add_items(self):
        item1 = Items('Iphone 10','A brand new Iphone')
        item2  = Items('Storagekey','This is a key which unlocks the storage room door')

        self.items.append(item1)
        self.items.append(item2)

    def open_door(self):
        keyItem =''
        axeItem =''
        for i in self.items:
            if i.name=='Storagekey':
                keyItem = i
            if i.name =='Axe':
                axeItem = i

        if Player.inventory.check_if_has_item(keyItem) and Player.inventory.check_if_has_item(axeItem):
            print('Congrats! The door is now opened')
            return True
        else:
            print('Cannot open the door you either dont have a key or you dont have anything to smash the chain')
            return False
