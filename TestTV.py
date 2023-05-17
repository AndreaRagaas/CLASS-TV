#Import the TV class from the TV module
from TV import TV

#Create a new class named TestTV
class TestTV:
    #Initialized two TV objects
    def __init__(self):
        #the first TV
        self.tv1 = TV()
        #the second TV
        self.tv2 = TV()
    #Defining the method to run the TV
    def run(self):