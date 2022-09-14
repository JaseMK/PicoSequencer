from neopixel import Neopixel
from machine import Pin

class lightstrip:
    x = 0
    numpix = 16
    pixels = Neopixel(numpix, 0, 28, "GRB")
    yellow = (255, 100, 0)
    orange = (255, 50, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    
    def __init__(self):
        self.x = 5
        self.status = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        for i in range(16):
            self.status[i] = 'off' #values can be [on|off|highlight]
        self.pixels.clear()
        self.pixels.show()
        self.pixels.brightness(20)
        self.pixels.set_pixel_line(0, 15, self.blue)
        self.pixels.show()
        
    def getx(self):
        return self.x
    
    def setStatus(self, position, status):
        self.status[position] = status
        pixelPosition = self.translatePosition(position)
        if status == 'off':
            self.pixels.set_pixel(pixelPosition, self.blue, how_bright = 0)
        if status == 'on':
            self.pixels.set_pixel(pixelPosition, self.blue, how_bright = self.pixels.brightness())
        if status == 'highlight':
            self.pixels.set_pixel(pixelPosition, self.red, how_bright = self.pixels.brightness())
        self.pixels.show()
        
            
    
    def translatePosition(self, input):
        # Translate lighstrip position to actual neopixel id (two block of 8 stacked above each other)
        '''
        0 -> 0
        1 -> 8
        2 -> 1
        3 -> 9
        4 -> 2
        5 -> 10
        6 -> 3
        7 -> 11
        8 -> 4
        9 -> 12
        10 -> 5
        11 -> 13
        12 -> 6
        13 -> 14
        14 -> 7
        15 -> 15
        
        Formula: If even, divide by 2
        If Odd, minus 1, divide by 2, add 8
        '''
        if (input % 2) == 0: # even
            return (input // 2)
        else: # odd
            return (((input - 1)//2) + 8)
        