import time
from neopixel import Neopixel
from machine import Pin
from lightstrip import lightstrip

push_button = Pin(13, Pin.IN, machine.Pin.PULL_UP)  # 13 number pin is input
button_0 = Pin(0, Pin.IN, machine.Pin.PULL_UP)  
button_1 = Pin(1, Pin.IN, machine.Pin.PULL_UP)  
button_2 = Pin(2, Pin.IN, machine.Pin.PULL_UP)  
button_3 = Pin(3, Pin.IN, machine.Pin.PULL_UP)  
button_4 = Pin(4, Pin.IN, machine.Pin.PULL_UP)
button_5 = Pin(5, Pin.IN, machine.Pin.PULL_UP)  


mystrip = lightstrip()
print(mystrip.translatePosition(3))
print(mystrip.translatePosition(9))
print(mystrip.translatePosition(14))
print(mystrip.getx())
print(mystrip.status)
mystrip.setStatus(3,'highlight')
mystrip.setStatus(6,'off')
mystrip.setStatus(8,'highlight')


 
button_last = time.ticks_ms()
neoStatus = False
 
def button_handler(pin):
    global button_last, button_0, button_1, button_2, button_3, button_4, button_5
      
    if pin is button_0:
        if time.ticks_diff(time.ticks_ms(), button_last) > 200:
            toggleNeo(7)
            button_last = time.ticks_ms()
    if pin is button_1:
        if time.ticks_diff(time.ticks_ms(), button_last) > 200:
            toggleNeo(8)
            button_last = time.ticks_ms()
    if pin is button_2:
        if time.ticks_diff(time.ticks_ms(), button_last) > 200:
            toggleNeo(9)
            button_last = time.ticks_ms()
    if pin is button_3:
        if time.ticks_diff(time.ticks_ms(), button_last) > 200:
            toggleNeo(10)
            button_last = time.ticks_ms()
    if pin is button_4:
        if time.ticks_diff(time.ticks_ms(), button_last) > 200:
            toggleNeo(11)
            button_last = time.ticks_ms()
    if pin is button_5:
        if time.ticks_diff(time.ticks_ms(), button_last) > 200:
            toggleNeo(12)
            button_last = time.ticks_ms()


def toggleNeo(location):
    global neoStatus
    if neoStatus == True:
        neoStatus = False
        #pixels.set_pixel(location, yellow)
    else:
        neoStatus = True
        #pixels.set_pixel(location, blue) 
        
    

#pixels.brightness(10)
#pixels.fill(orange)
#pixels.set_pixel_line_gradient(2, 59, green, red)
#pixels.set_pixel_line(21, 25, red)
#pixels.set_pixel(20, (255, 255, 255))

button_0.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
button_1.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
button_2.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
button_3.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
button_4.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
button_5.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
 
while True:
    logic_state = push_button.value()
    #if logic_state == True:     # if push_button pressed
        #pixels.set_pixel(2, red)            # led will turn ON
    #else:                       # if push_button not pressed
        #pixels.set_pixel(2, green)             # led will turn OFF

    #pixels.show()
    #time.sleep(1)