from Rooms import Room

class KidsRoom(Room):

    items =[]

    def __init__(self,name):
        self.name =name      
        


    def show_info(self):
        print('You are in the kids room! The hall room is filled with toys and there are some pictures of kids on the wall','This is the final room of this level, it leads to the stairs which lead to the second level')
        print('It has the following items inside: ')
        for item in self.items:
            print(item.name)


    
    def has_door(self):
        return False


    def add_items(self):
        
        from Items import Items
        item1 = Items('Nice warm jacket','A very warm jacket')
        item2  = Items('Hammer','A legit heavy hummer used as a weapon in the 18th century! The kids can not lift it obviously, but you can!')
        item3  = Items('Gun(toy)','Just a toy gun loaded with rubber arrows')
        self.items.append(item1)
        self.items.append(item2)
        self.items.append(item3)

    def all_passed(self):
        return True
