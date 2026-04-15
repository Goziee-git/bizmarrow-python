import math
from datetime import datetime, date

class Info:
    def __init__(self, *args):
        self.fname =  args[0] 
        self.lname = args[1]
        self.Birth_ = args[2]
        self._cached_age = None
        self._age_calculatedDate = None

    def get_full_name(self):
        return f"my fullname is {self.lname} {self.fname}"

    def calculate_age(self):
        """computed method: calculate current age"""
        today = date.today()
        age = today.year - self.Bdate.year
        return age
