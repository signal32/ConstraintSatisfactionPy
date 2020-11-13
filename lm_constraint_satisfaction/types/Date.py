# Note: Currently using python datetime implementation of date. Do not use this one, comparisons need implemented correctly first!

class Date():
    def __init__(self,day: int,month: int,year: int,minute: int) -> None:
        self.day = day
        self.month = month
        self.year = year
        self.minute = minute
        return

    def __str__(self) -> str:
        return str(self.day)+"/"+str(self.month)+"/"+str(self.year)+" + "+ str(self.minute)+"minutes"

    def __eq__(self, o: object) -> bool:
        print("eq")
        if self.day == o.day and self.month == o.month and self.year == o.year and self.minute == o.minute:
            return True
        else:
            return False
    
    def __lt__(self, o: object) -> bool:
        print("labas")
        if self.day <= o.day and self.month <= o.month and self.year <= o.year and self.minute < o.minute:
            return True
        else:
            return False

    def __le__(self, o: object) -> bool:
        print("le")
        if self.day <= o.day and self.month <= o.month and self.year <= o.year and self.minute <= o.minute:
            return True
        else:
            return False

    def __gt__(self, o: object) -> bool:
        print("gt")
        if self.day >= o.day and self.month >= o.month and self.year >= o.year and self.minute > o.minute:
            return True
        else:
            return False

    def __ge__(self, o: object) -> bool:
        print("ge")
        if self.day >= o.day and self.month >= o.month and self.year >= o.year and self.minute >= o.minute:
            return True
        else:
            return False