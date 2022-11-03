# microbit-module: KitronikACCESSbit@1.1.0
# Copyright (c) Kitronik Ltd 2022. 
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from microbit import *
import music

def moveServo(Position):
    # PWM works between 0-1023 which equivalent to 0msecs - 20msecs
    # servo pulse is between 0.5msecs - 2.5msecs 
    # this translate back to between 25-125
    # 125-25=100  servo moves 180 degrees 100/180=0.555
    # due to the pulse starting at 25 this an ofset that needs to be added on.
    # taking example of 90degrees (0.555*90)+25=74.95 
    # which is the mid-point between 25-125 or 0-180
    Degree = 0 # down
    
    if Position == "up":
        Degree = 90
        
    pulsePeriod = int(0.555 * Degree) + 25 
    
    pin0.set_analog_period(20)
    pin0.write_analog(pulsePeriod)
    
    sleep(2000)
    # digital write to zero for micro:bit timer does not distrupt servo when beeps are played
    pin0.write_digital(0)

def soundBuzzer(lengthOfBeep, numberOfTimes):
    lengthInmSecs = 300 # short
    
    if lengthOfBeep == "long":
        lengthInmSecs = 800
    
    for numberOfTimes in range(0, numberOfTimes, 1):
        music.pitch(800, duration=lengthInmSecs, pin=pin1, wait=True)

while True:
    moveServo("up")
    soundBuzzer("short", 2)
    moveServo("down")
    soundBuzzer("long", 1)

