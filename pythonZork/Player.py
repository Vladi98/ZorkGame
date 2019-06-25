from Inventory import Inventory
from Items import Items
from Commands import Commands

class Player:

    inventory = Inventory("This is the inventory of the player")    

    def __init__(self,name):
        self.name =name


    
    def grab_item(self,item_name,currentRoom):
        item = ''
        for i in currentRoom.items:
            if(i.name ==item_name ):
                item =i
                break
        if item not in currentRoom.items:
            print('The item doesnt exist!')

        if item in currentRoom.items and item not in Player.inventory.collection_of_items:         
            Player.inventory.add_item(item)

        elif item in currentRoom.items and item in Player.inventory.collection_of_items:
            print('You already have this item')
        

    def drop_item(self,item_name):
        item =''
        for i in Player.inventory.collection_of_items:
            if(i.name ==item_name ):
                item =i
                break
        if item in Player.inventory.collection_of_items:
            Player.inventory.drop_item(item)
        else:
            print("The current item doesn't exist in your inventory")


    def show_info(self):
        print('Made by Vladimir Dachkinov - fullstack intern in Mentormate')

    

