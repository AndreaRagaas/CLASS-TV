#Create a class named TV
class TV:
    #Defining TV attributes
    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False

    #Constructs a default TV object
    #Turn on this TV
    def turnOn(self):
        self.on = True
    #Turn off this TV
    def turnOff(self):
        self.on = False