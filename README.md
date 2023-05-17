# TV Class

This code defines a `TV` class that represents a television. The class has attributes such as `channel`, `volumeLevel`, and `on` to keep track of the TV's current state. It also provides methods to perform operations like turning the TV on/off, changing the channel, and adjusting the volume.

## Class Methods

### `__init__()`

The constructor method initializes a TV object with default values for `channel` (set to 1), `volumeLevel` (set to 1), and `on` (set to `False`).

### `turnOn()`

This method turns on the TV by setting the `on` attribute to `True`.

### `turnOff()`

This method turns off the TV by setting the `on` attribute to `False`.

### `getChannel()`

This method returns the current channel of the TV.

### `setChannel(channel)`

This method sets a new channel level for the TV if the TV is on and the provided channel is within the valid range of 1 to 120.

### `getVolume()`

This method returns the current volume level of the TV.

### `setVolume(volumeLevel)`

This method sets a new volume level for the TV if the TV is on and the provided volume level is within the valid range of 1 to 7.

### `channelUp()`

This method increases the channel number by 1 if the TV is on and the current channel is less than 120.

### `channelDown()`

This method decreases the channel number by 1 if the TV is on and the current channel is greater than 1.

### `volumeUp()`

This method increases the volume level by 1 if the TV is on and the current volume level is less than 7.

### `volumeDown()`

This method decreases the volume level by 1 if the TV is on and the current volume level is greater than 1.

## TestTV Class

This code also defines a `TestTV` class that is used to test the functionality of the `TV` class. It creates two instances of the `TV` class, `tv1` and `tv2`, and performs a series of operations on them to showcase the TV's features.

### `__init__()`

The constructor method initializes the `TestTV` object and creates two instances of the `TV` class, `tv1` and `tv2`.

### `run()`

This method runs the TV test scenario. It turns on `tv1`, sets its channel to 30, and volume level to 3. Then, it turns on `tv2`, sets its channel to 3, and volume level to 2. Finally, it displays the channel and volume level information of both TVs in a message box.

## Usage

To use this code, create an instance of the `TestTV` class and call its `run()` method. This will simulate the TV scenario and display the output in a message box.

Example:

```python
# Importing a messagebox for the output
from tkinter import messagebox

# Create an instance of TestTV and run the test
test = TestTV()
test.run()
