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
from sys import exit




p = Player('Vladimir')
Menu.action()

basement = Basement('Basement')
storageRoom =StorageRoom('Storageroom')
restingRoom =RestingRoom('Restingroom',)
kidsRoom = KidsRoom('kidsRoom')
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


floor_1 = Floor(storageRoom,restingRoom,kidsRoom)
floor_2 = Floor(hallway,closet,finalRoom)

floors= [basement,floor_1,floor_2,ceiling]


iterator = 0




command = input()
while True:
    #parsed_command = Parser.parse(command)
    #tokens = parsed_command.split(' ')
    tokens = command.split()

    #if currentRoom == storageRoom:
     #   if tokens[0] == 'exit':
    #        break

    if tokens[0] == 'go':
        #basement and ceiling has no rooms



        if floors[iterator] != basement and floors[iterator]!= ceiling:
            if floors[iterator].check_if_room_exists(tokens[1]):

                if currentRoom.has_ligher() and currentRoom.has_no_hall():
                    if currentRoom.has_door() == False:
                        currentRoom = floors[iterator].return_current_room(tokens[1])
                        currentRoom.show_info()

                    elif currentRoom.has_door() and currentRoom.open_door():
                        currentRoom = floors[iterator].return_current_room(tokens[1])
                        currentRoom.show_info()


        if tokens[1] =='up':
            if floors[iterator] != basement and floors[iterator]!= ceiling:
                if floors[iterator].room1.all_passed() and floors[iterator].room2.all_passed() and floors[iterator].room3.all_passed():
                    iterator+=1
            elif floors[iterator] == basement and floors[iterator].basement.all_passed():
                    iterator+=1
        #elif tokens[1] == 'down'
       
    elif tokens[0] == 'drop':
            item_to_drob = tokens[1]
            p.drop_item(item_to_drob)


    elif tokens[0] == 'grab':
            item_to_grab = tokens[1]
            p.grab_item(item_to_grab,currentRoom)



    elif tokens[0] == 'open':
        if tokens[1] == 'door':
            if currentRoom.open_door():
                print('The door is now opened')

                    

    elif tokens[0] == 'show':
        if tokens[1] == 'inventory':
            p.inventory.show_items()

    elif tokens[0] == 'inspect':
        for item in currentRoom.items:
            if tokens[1] == item.name:
                 print(item.show_info())
        
      
    command= input()












