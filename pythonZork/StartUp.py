from Floors import Floor
from Commands import Commands
from Inventory import Inventory
from Rooms import Room
from Items import Items
from Basement import Basement
from Menu import Menu
from Player import Player
from StorageRoom import StorageRoom
from RestingRoom import RestingRoom
from KidsRoom import KidsRoom
from Hallway import Hallway
from Closet import Closet
from FinalRoom import FinalRoom
from Ceiling import Ceiling
from Parser import Parser
from Map import Map
from sys import exit




p = Player('Vladimir')
Menu.action()

basement = Basement('Basement')
storageRoom =StorageRoom('Storageroom')
restingRoom =RestingRoom('Restingroom',)
kidsRoom = KidsRoom('Kidsroom')
hallway = Hallway('Hallway')
closet = Closet('Closet')
finalRoom = FinalRoom('Finalroom')
ceiling = Ceiling('Ceiling')


basement.add_items()
storageRoom.add_items()
restingRoom.add_items()
kidsRoom.add_items()
hallway.add_items()
finalRoom.add_items()
ceiling.add_items()

currentRoom = basement
currentRoom.show_info()


floor_0 = Floor(basement)
floor_1 = Floor(storageRoom,restingRoom,kidsRoom)
floor_2 = Floor(hallway,closet,finalRoom)
floor_3 = Floor(ceiling)

floor_0.info = 'This is the first and lowest level of the house in other words here the basement. To go to the basement use the GO command!'
floor_0.info+=' There are no other rooms on this level. To move up to the next floor you should open the current floors all doors.Good luck!'
floor_1.info = 'This is the second level There are three rooms here: Storageroom, Restingroom, Kidsroom. To move freely in all of them you must passed their chalenges and open the doors!'
floor_2.info = 'This is the third level of the house. The rooms on this level are: Hallway, Closet, Finalroom. This level link directly to level four which is the final one!'
floor_3.info = 'This is the final level and the only room here is the ceiling. It is the highest point of the house, here is your chance to leave the house live a free happy life! There are no other rooms on this level'


floors= [floor_0,floor_1,floor_2,floor_3]

iterator = 0

command = input()
while True:
    parsed_command = Parser.parse(command)
    tokens = parsed_command.split(' ')

    if tokens[0] == 'go':

        if tokens[1] =='up':

            if floors[iterator].all_passed_floor():
                if(iterator>=3):
                    print('You are already at the highest level of the house')
                    iterator =3

                else:
                    print("Moving up...")
                    iterator+=1
                    floors[iterator].show_info()
                    currentRoom=''

        elif tokens[1] =='down':

            if(iterator<=0):
                iterator = 0
                print('You are already at the lowest level of the house')

            else:
                print('Moving down...')
                iterator-=1
                currentRoom =''
                floors[iterator].show_info()


        if floors[iterator].check_if_room_exists(tokens[1]):           
                currentRoom = floors[iterator].return_current_room(tokens[1])
                currentRoom.show_info()


    elif tokens[0] == 'drop':
            item_to_drob = tokens[1]
            p.drop_item(item_to_drob)


    elif tokens[0] == 'grab':
            if(len(Player.inventory.collection_of_items)<Inventory.max_capacity):
                item_to_grab = tokens[1]
                p.grab_item(item_to_grab,currentRoom)
            else:
                print("Sorry! You can not carry any more items")



    elif tokens[0] == 'open':
        if tokens[1] == 'door':
            if currentRoom =='':
                print('You are not in a room!')

            elif currentRoom.has_door():
                if currentRoom.open_door():
                    print('The door is now opened')              
            else:
                print("This room has no door")

        elif tokens[1]=='window':
            if currentRoom.has_window():
                if currentRoom.smash_armored_window():
                    print("You smashed the window! Now you can jump!")                  
            else:
                print("No windows in this room")
                

    elif tokens[0] == 'jump' and tokens[1] == 'window':
        if currentRoom.has_window() and currentRoom.smash_armored_window() and currentRoom.jump_with_parachute():
            print("Congratulations! You passed the game! You are one tough bastard!")



    elif tokens[0] == 'show':
        if tokens[1] == 'inventory':
            p.inventory.show_items()
        if tokens[1] == 'map':
            print(Map.roomDirections)


    elif tokens[0] == 'inspect':
        for item in currentRoom.items:
            if tokens[1] == item.name:
                 print(item.show_info())

    elif tokens[0]=='exit' and tokens[1] =='game':
        exit(0)
        

    command= input()












