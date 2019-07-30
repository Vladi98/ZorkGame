
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

    
    def has_ligher(self):
        return True

    def has_window(self):
        return False

    def smash_armored_window(self):
        return False

    def has_no_hall(self):
        return True

    def all_passed(self):
        False

    @abc.abstractmethod
    def jump_with_parachute(self,parameter_list):
        raise NotImplementedError