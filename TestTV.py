#Import the TV class from the TV module
from TV import TV
#Importing a messagebox for the output
from tkinter import messagebox

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
        #To turn on the tv1
        self.tv1.turnOn()
        #Setting the channel of tv1 to 30
        self.tv1.setChannel(30)
        #Setting the volume level of tv1 to 3
        self.tv1.setVolume(3)

        #To turn on the tv2
        self.tv2.turnOn()
        #Setting the channel of tv2 to 3
        self.tv2.setChannel(3)
        #Setting the volume level of tv2 to 2
        self.tv2.setVolume(2)

    #The outputs printed in a messagebox stating the channel and volume level of tv1 and tv2
        message = f"tv1's channel is {self.tv1.getChannel()} and volume level is {self.tv1.getVolume()}\n"
        message += f"tv2's channel is {self.tv2.getChannel()} and volume level is {self.tv2.getVolume()}"
        messagebox.showinfo("TV Information", message)

#Create an instance of TestTV and run the test
test = TestTV()
test.run()