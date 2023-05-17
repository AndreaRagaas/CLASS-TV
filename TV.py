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
    #Returns the channel for this TV
    def getChannel(self):
        return self.channel
    #Set a new channel level for this TV
    def setChannel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel
    #Gets the volume level for this TV
    def getVolume(self):
        return self.volumeLevel
    #Sets a new volume level for this TV
    def setVolume(self, volumeLevel):
        if self.on and 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel