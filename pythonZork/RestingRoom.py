from Rooms import Room
from Player import Player
from Items import Items

class RestingRoom(Room):


    def __init__(self,name):
        self.name =name
        self.items =[]


    def show_info(self):
        print('You are now in the resting room! This is the most comfortable and modern room in the house. It comes fully equipped with state-of-the-art amenities including a Samsung smart TV, iHome docking station, USB ports, Keurig Coffee Brewer, mini-fridge, humidifier, in-room safe, plush robes and slippers, and Wi-Fi. ','It links to the resting rooms')
        print('It has the following furnitures inside:')
     
        print('and the following items scattered all over the room: ')
        for item in self.items:
            print(item.name)

    
    def has_door(self):
        return True

    def add_items(self):
        item1  = Items('Military bag','A big bag used by the military forces in WWII')
        item2  = Items('Sunglases','A big travelling suitcase')
        item3  = Items('Wire rope','A very durable and reliable rope')

        self.items.append(item1)
        self.items.append(item2)
        self.items.append(item3)


    def open_door(self):
        keyItem =''
        for i in self.items:
            if i.name=='Iphone10':
                keyItem = i

        if Player.inventory.check_if_has_item(keyItem):
            password = input('Enter password: ')
            if password=='MentorMate1':
                print('Congrats! The door is now opened')
                return True
            else:
                print('Incorrect password!')
                return False
        else:
            print('Cannot open the door it is protected via password. The password is the same as MentorMate1 Wifi - password. To enter the password you must have an electronic device in you, currently you dont! :)')
            return False



    def all_passed(self):
        if self.has_door() and self.open_door():
            return True