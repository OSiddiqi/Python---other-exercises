class TooHot():
    def tooHot(temperature, isSummer):
        self.temperature = temperature
        self.isSummer = isSummer

        temperatureLimit = 90

        if(isSummer == True):
            temperatureLimit = 100
            return temperatureLimit
        elif (temperature >=60 and temperature <= temperatureLimit):
            print("True")
            return True
        else:
            print("False")
            return False
    print(40, True)