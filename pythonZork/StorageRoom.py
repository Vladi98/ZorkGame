
from Items import Items
from Player import Player
from Rooms import Room

class StorageRoom(Room):

    items=[]

    def __init__(self,name,):
        self.name =name


    def show_info(self):
        print('This is a storage room! Looks like just another room filled with boxes and barrels, but look out! Rah! It has a chain over the door. It links to the resting rooms')
        print('It has the following items scattered all over the room: ')
        for item in self.items:
            print(item.name)

    
    def has_door(self):
        return True

    def add_items(self):
        item1 = Items('Iphone10','A brand new Iphone')
        item2  = Items('Storagekey','This is a key which unlocks the storage room door')

        self.items.append(item1)
        self.items.append(item2)

    def open_door(self):
        keyItem =''
        axeItem = ''
        for i in self.items:
            if i.name=='Storagekey':
                keyItem = i

        for item in Player.inventory.collection_of_items:
            if item.name == "Axe" or item.name == 'Hammer':
                axeItem = item

        if Player.inventory.check_if_has_item(keyItem) and Player.inventory.check_if_has_item(axeItem):
            print('You opened the Storageroom door!')
            return True
        else:
            print('Cannot open the Storageroom door you either dont have a key or you dont have anything to smash the chain')
            return False

    
    def all_passed(self):
        if self.has_door() and self.open_door():
            return True
        return False
