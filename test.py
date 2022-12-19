
import platform
# import sys
# from PyQt5.QtChart import QChart, QChartView, QLineSeries
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.sip import *
# from PySide2extn import *
# from matplotlib import pyplot as plt
# import multiprocessing as mp
import time
import subprocess
from PyQt5 import QtCore

# import numpy as np
import os
# os.system(["sudo","-l"])

infoCPU = str(subprocess.check_output(["inxi", "-Fxz"])).split("\\n")[25].split(" ")
for i in range(0, len(infoCPU)):
    print(str(i)+" "+infoCPU[i])

# for i in range (len(infoCPU[k])):s
#     print(i)
#     print(infoCPU[k][i])
# print(infoCPU[k][33:])
    
    

