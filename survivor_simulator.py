# STK library imports
from agi.stk12.stkdesktop import STKDesktop
from agi.stk12.stkobjects import *
from agi.stk12.stkutil import *
from agi.stk12.vgt import *
 
# Python helper library imports
import os
import random
import math
 
# Get reference to the current instance of STK
STK_PID = os.getenv('STK_PID')
stk = STKDesktop.AttachToApplication(pid=int(STK_PID))
root = stk.Root
 
 
def random_place_gen(area, num_people, lat=37.6213, long=-122.379):
    num = 1
 
    # 1 degree is 111 km
    x = (math.sqrt(area / math.pi)) / 111
    y = math.sqrt(area / math.pi) / 111
 
    for i in range(num_people):
        coin_flip = random.randint(0,1)
        if coin_flip == 0:
            lat = random.uniform(lat, lat + x)
            long = random.uniform(long, long + y)
        else:
            lat = random.uniform(lat, lat - x)
            long = random.uniform(long, long - y)
        commandList = [[f'New / */Place Person{num}'], [f'SetPosition */Place/Person{num} Geodetic {lat} {long} 0.0']]
        num += 1
        root.ExecuteMultipleCommands(commandList, 2)
