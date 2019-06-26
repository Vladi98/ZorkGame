from Rooms import Room

class Floor:
    
    info =''
    room1 =''
    room2=''
    room3=''
    def __init__(self,room1,room2,room3):
        self.room1 = room1
        self.room2 = room2
        self.room3 = room3
        self.rooms =[room1.name,room2.name,room3.name]
        

    def show_info(self):
        print('There are three rooms on the floor, each has hidden items which will help you escape and move to the next level!')
        

    def check_if_room_exists(self,room_name):
        flag = False
        if room_name == self.room1.name:
            flag = True

        if room_name == self.room2.name:
            flag = True

        if room_name == self.room3.name:
            flag = True
        
        return flag

    def return_current_room(self, room_name):
        current_room =''
        if room_name == self.room1.name:
            current_room = self.room1

        if room_name == self.room2.name:
            current_room = self.room2

        if room_name == self.room3.name:
            current_room = self.room3

        return current_room


    def set_info(self, newInfo):
        Floor.info = newInfo 






    