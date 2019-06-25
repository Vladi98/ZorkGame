from Rooms import Room

class KidsRoom(Room):


    def __init__(self,name,links):
        self.name =name
        self.links = links
        self.items =[]


    def show_info(self):
        print('You are in the kids room! The hall room is filled with toys and there are some pictures of kids on the wall','This is the final room of this level, it leads to the stairs which lead to the second level')
        print('It has the following furnitures inside:')
     
        print('and the following items scattered all over the room: ')
        for item in self.items:
            print(item.name)

    
    def has_door(self):
        return False

    def add_items(self):
        item1 = Items('Nice warm jacket','A very warm jacket')
        item2  = Items('Hammer','A legit heavy hummer used as a weapon in the 18th century! The kids can not lift it obviously!')
        item3  = Items('','This is a key which unlocks the storage room door')
        item4  = Items('Storagekey','This is a key which unlocks the storage room door')
        item5  = Items('Storagekey','This is a key which unlocks the storage room door')


        self.items.append(item1)
        self.items.append(item2)