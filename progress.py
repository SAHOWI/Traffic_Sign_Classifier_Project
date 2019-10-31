#Data Analysis
import random
import numpy
from matplotlib import pyplot
import numpy as np


import sys

### util function -> update progress bar

def update_progress(progress, final_count):
    barLength = 1 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= final_count:
        progress = final_count
        status = "Done...\r\n"
        
    
    block = int((barLength*progress/final_count)*10)
    #print('block->', block, ' barLength->', barLength, ' barlength-block->', (barLength-block), 
    #     ' progress %', int((progress/final_count)*100))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), 
                                              int((progress/final_count)*100), status)
    sys.stdout.write(text)
    sys.stdout.flush()


update_progress(10,100)
