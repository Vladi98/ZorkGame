

import abc
class Room:


    @abc.abstractmethod
    def show_info(self, parameter_list):
       raise NotImplementedError

    

    @abc.abstractmethod
    def add_items(self,parameter_list):
        raise NotImplementedError

    @abc.abstractmethod
    def open_door(self,parameter_list):
        raise NotImplementedError

    @abc.abstractmethod
    def has_door(self,parameter_list):
        raise NotImplementedError
