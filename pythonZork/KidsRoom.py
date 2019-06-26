from Rooms import Room
from Items import Items

class KidsRoom(Room):

    items =[]

    def __init__(self,name):
        self.name =name      
        


    def show_info(self):
        print('You are in the kids room! The hall room is filled with toys and there are some pictures of kids on the wall','This is the final room of this level, it leads to the stairs which lead to the second level')
        print('It has the following furnitures inside:')
     
        print('and the following items scattered all over the room: ')
        for item in self.items:
            print(item.name)

    
    def has_door(self):
        return False

    def has_ligher(self):
        return True

    def add_items(self):
        item1 = Items('Nice warm jacket','A very warm jacket')
        item2  = Items('Hammer','A legit heavy hummer used as a weapon in the 18th century! The kids can not lift it obviously, but you can!')
        item3  = Items('Gun(toy)','Just a toy gun loaded with rubber arrows')
        self.items.append(item1)
        self.items.append(item2)
        self.items.append(item3)

    def all_passed(self):
        if  self.has_ligher():
            return True
