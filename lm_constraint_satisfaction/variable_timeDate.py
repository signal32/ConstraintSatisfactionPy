from . import Variable

class DateTimeVariable(Variable):
    def __init__(self, name, startDateTime, endDateTime):
        Variable.__init__(self,name)
        self.startDateTiime = startDateTime
        self.endDateTime = endDateTime