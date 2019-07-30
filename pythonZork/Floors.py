from Rooms import Room
from Basement import Basement

class Floor:
    
    info =''
    def __init__(self,*args):
        self.args = args
        self.info =''

               

    def check_if_room_exists(self,room_name):
        flag =False
        for room in self.args:
            if room_name == room.name:
                flag = True
        return flag



    def return_current_room(self, room_name):
        current_room ='No such room in the house'
        for room in self.args:
            if room_name == room.name:
                current_room = room

        return current_room

    def all_passed_floor(self):
        flag = True
        for room in self.args:
            if room.all_passed() == False:
                flag = False
                return flag

        return flag


    def show_info(self):
        print(self.info) 





    