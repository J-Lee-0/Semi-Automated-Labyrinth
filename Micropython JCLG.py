import machine
import time
import math
hPin=27
vPin=26
hJoy= machine.ADC(hPin)
vJoy= machine.ADC(vPin)
servoPin1=15
servoPin2=16

servo1=machine.PWM(machine.Pin(servoPin1))
servo2=machine.PWM(machine.Pin(servoPin2))

servo1.freq(50)
servo2.freq(50)
servo1.duty_u16(1638)
servo2.duty_u16(1638)
while True:
    hVal=hJoy.read_u16()
    vVal=vJoy.read_u16()
    
    hCal=int(-.00306*hVal+100.766)
    vCal=int(.00306*vVal-100.766)
    
    deg=math.atan2(vCal,hCal)*360/2/math.pi
    if hCal==0:
        hCal=1
    if deg<0:
        deg=deg+360
    
    mag=math.sqrt(hCal**2+vCal**2)
    if mag<=4:
        hCal=0
        vCal=0
        deg=0
    if deg>180 and deg>270:
        deg=180
    if deg>270 and deg<=360:
        deg=0
    pwmVal=36.41*deg+1638
    servo1.duty_u16(int(pwmVal))
    servo2.duty_u16(int(pwmVal))
    time.sleep(.05)
    print(hCal,vCal,deg)
    time.sleep_ms(200)