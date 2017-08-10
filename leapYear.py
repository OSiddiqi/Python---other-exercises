class LeapYear():
    def __init__(self, year):
        self.year = year
        if year % 400 == 0:
            return False 
        if year % 100 == 0:
            return False
            print("That's not a leap year!")        
        if year % 4 == 0:
            print("That's a leap year!")
            return True
        else:
            return False
            print("That's not a leap year!")
    year = int(input("Input year: "))