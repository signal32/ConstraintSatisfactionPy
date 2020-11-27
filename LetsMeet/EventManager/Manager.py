from LetsMeet.ConditionManager.ConditionSet import ConditionSet
from LetsMeet.EventManager.Event import Event
from LetsMeet.EventManager.solver import Solver
from LetsMeet import ConditionManager

"""Manager for the event type"""
class Manager():
    
    def __init__(self,event: Event = Event()) -> None:
        self.event = event
        self.solver = Solver()

        return
    
    """To create an event manager class for an arbitrary event loaded from data model, use this method"""
    @classmethod
    def fromUUID(cls, uuid: object):
        #TODO get event with this UUID from storage model and initialise class
        event = Event()
        event.uuid = uuid
        return cls(open(event,))


    def initBlank(self):
        self.event.event = ConditionSet()
        return 

    def setProperty(self,key,value):
        if key == "name":
            self.event.name = value
        else:
            #TODO set for key in properties dictionary
            pass
        return

    def getProperty(self,key):
        if key == "name":
            return self.event.name
        else:
            #TODO set for key in properties dictionary
            pass
        return

    def getID(self):
        return self.event.uuid
        

    


    

