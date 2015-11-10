"""
Blocks World methods for Pyhop 1.1.
Author: Dana Nau <nau@cs.umd.edu>, November 15, 2012
This file should work correctly in both Python 2.7 and Python 3.2.
"""


from MIDCA.modules._plan import pyhop
from _io import open
import time

class Monitor():
    
    def __init__(self, name, block, depth):
        self.name = name
        self.block = block
        self.depth = depth
        self.is_active = True
        self.is_fired = False
        self.tasks = []
        
    def add_task(self, task_name):
        self.tasks.append(task_name)

    
    
"""
Here are some helper functions that are used in the methods' preconditions.
"""
#precondition: state.clear[b1] = true
#pickup_task
#we just generate the monitor for the first task




def clear_block(state, depth, b1, task_name):
    i = 0
    m =  filter(lambda x: x.name.__name__ == "clear_block" and x.block == b1, pyhop.generated_monitors)
    if m: 
        m[0].add_task(task_name)    
        print "monitor is already running for " + b1
    else:
        m = Monitor(clear_block, b1, depth)
        m.add_task(task_name)
        pyhop.generated_monitors.append(m)
    
        while(m.is_fired == False):
                        #f.write (b1 + " true")
            i = i + 1
            time.sleep(2)
            if i > 7:
                m.is_fired = True
                #print("monitor: " + b1 + "is not clear!")
                        
            if state.clear[b1] == False:
                print("monitor: " + b1 + "is not clear!")
                m.is_fired = True
               
#
"""for each task we know what kind of monitors we should run"""
    
def declare_monitors(longApprehend = True):    
    pyhop.declare_monitors('pickup_task',clear_block)
    #unstack_task 
    pyhop.declare_monitors('unstack_task', clear_block)
    #unstack
    pyhop.declare_monitors('unstack', clear_block)
#     #pickup
    pyhop.declare_monitors('pickup', clear_block)      