import sys
sys.path.append("../")
from PythonProfiler import *
import time

@profiler
def func(x, y):
    for i in range(100):
        print(i, x, y)
        time.sleep(0.01)


func(1, 2)
