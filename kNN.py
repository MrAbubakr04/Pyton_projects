import numpy as np
import math 

def Evclid_metric(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


print(Evclid_metric(5,3,4,7))