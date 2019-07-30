from Commands import Commands
from Rooms import Room
from Basement import Basement
from Ceiling import Ceiling
from Closet import Closet
from Hallway import Hallway
from FinalRoom import FinalRoom
from StorageRoom import StorageRoom
from RestingRoom import RestingRoom
from KidsRoom import KidsRoom



class Parser:

    @staticmethod
    def parse(command):

        basement = Basement('Basement')
        storageRoom =StorageRoom('Storageroom')
        restingRoom =RestingRoom('Restingroom',)
        kidsRoom = KidsRoom('Kidsroom')
        hallway = Hallway('Hallway')
        closet = Closet('Closet')
        finalRoom = FinalRoom('Finalroom')
        ceiling = Ceiling('Ceiling')


        #basement.add_items()
        #storageRoom.add_items()
        #restingRoom.add_items()
        #kidsRoom.add_items()
        #hallway.add_items()
        #finalRoom.add_items()
        #ceiling.add_items()

        rooms = ['Basement','Storageroom','Restingroom','Kidsroom','Hallway','Closet','Finalroom','Ceiling']




        tokens = command.split()
        string=''
        for token in tokens:


            if(token in Commands.list_of_commands):
                string+= token

            if token == 'door':
                string+= ' '+token
                return string

            if token == 'window':
                string+= ' '+token
                return string

            if token == 'up':
                string+= ' '+token
                return string

            if token == 'down':
                string+= ' '+token
                return string

            if token in rooms:
                string += ' '+token
                return string

            elif token == 'inventory':
                string+= ' '+token
                return string

            elif token == 'map':
                string+= ' '+token
                return string

            elif token =='game':
                string+= ' '+token
                return string

            for item in basement.items:
                if item.name == token:
                    string+=' ' +token
                    return string

            for item in storageRoom.items:
                if item.name == token:
                    string+=' ' +token
                    return string

            for item in restingRoom.items:
                if item.name == token:
                    string+=' ' +token
                    return string

            for item in kidsRoom.items:
                if item.name == token:
                    string+=' ' +token
                    return string

            for item in hallway.items:
                if item.name == token:
                    string+=' ' +token
                    return string

            for item in closet.items:
                if item.name == token:
                    string+=' ' +token
                    return string

            for item in finalRoom.items:
                if item.name == token:
                    string+=' ' +token
                    return string

            for item in ceiling.items:
                if item.name == token:
                    string+=' ' +token
                    return string
            
        return "Not a valid command"
    

#print(Parser.parse("grab ther Finalroomkey"))