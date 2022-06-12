# SPDX-FileCopyrightText: Tony DiCola
# SPDX-License-Identifier: CC0-1.0

# Basic example of clearing and drawing pixels on a SSD1306 OLED oled.
# This example and library is meant to work with Adafruit CircuitPython API.

# Import all board pins.
import board
import busio
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect
import time

displayio.release_displays()

# Create the I2C interface.
i2c = busio.I2C(scl=board.GP21, sda=board.GP20)

if i2c.try_lock():
    print("Starting I2C scan.")
    devices = i2c.scan()
    i2c.unlock()

    print("Found %d I2C device(s)." % (len(devices)))
    for dev in devices:
        print("  I2C address:  %d (0x%x)" % (dev, dev))

else:
    print("Unable to lock I2C interface.")

display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Make the display context
splash = displayio.Group()
display.show(splash)#

# Battery symbol
rect = Rect(95, 0, (127-98), 14, fill=0xFFFFFF)
rect2 = Rect(96, 1, (127-98)-2, 12, fill=0x000000)
rect3 = Rect(126, 3, 128, 7, fill=0xFFFFFF)

def drawBattery():
    global splash

    splash.append(rect)
    splash.append(rect2)
    splash.append(rect3)

def printBatPCT(msg):
    global splash

    # Draw a label
    text_area = label.Label(terminalio.FONT, text=msg, color=0xFFFF00, x=98, y=6)
    splash.append(text_area)
    time.sleep(1)
    splash.remove(text_area)

def printMode(msg):
    global splash

    msg='{message: <6}'.format(message=msg)
    # Draw a label
    text_area = label.Label(terminalio.FONT, text=msg, color=0xFFFF00, x=1, y=6)
    splash.append(text_area)
    time.sleep(1)
    splash.remove(text_area)

def printDb(msg):
    global splash

    # Draw a label
    text_area = label.Label(terminalio.FONT, text=msg, color=0xFFFF00, x=10, y=40, scale=2)
    splash.append(text_area)
    time.sleep(1)
    splash.remove(text_area)


