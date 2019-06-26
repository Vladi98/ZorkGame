from Items import Items

class Inventory:

    collection_of_items =[]
    max_capacity = 3
    def __init__(self,info):
        self.info =info

    def add_item(self,item):
        Inventory.collection_of_items.append(item)
        print("You picked {} and added it to your inventory! Good luck!".format(item.name))

    def drop_item(self,item):
        self.collection_of_items.remove(item)
        print("You dropped {} and removed it from your inventory! Good luck!".format(item.name))

    def show_items(self):
        if len(Inventory.collection_of_items)==0:
            print('You dont have any items currently stored in the inventory')
        else:
            print("The current items in your inventory are: ")
            for item in Inventory.collection_of_items:
                print(item.name)

    def check_if_has_item(self,item):
        if item in Inventory.collection_of_items:
            return True
        return False
        
    def inspect_certain_item(self,item):
        print(item.info)

    @staticmethod
    def set_max_capacity(self,capacity):
        self.max_capacity = capacity

    