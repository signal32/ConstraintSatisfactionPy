from .Date import Date

class DateRange():
    def __init__(self, start: Date, end: Date, minDuration: int = 0) -> None:
        self.start = start
        self.end = end
        self.minDuration = minDuration
        return

    def __repr__(self) -> str:
        return "DateRange: [" + str(self.start)+"] -> ["+str(self.end)+"]"
        
    def __str__(self) -> str:
        return "DateRange: [" + str(self.start)+"] -> ["+str(self.end)+"]"

    # For range = tests to see if o and self overlap
    #TODO implement minDuration
    def __eq__(self, o: object) -> bool:
        if isinstance(o,DateRange):
            if (o.end <= self.end and o.end >= self.start) or (o.start >= self.start and o.start <= self.end):
                return True
            else:
                return False
        else:
            return False