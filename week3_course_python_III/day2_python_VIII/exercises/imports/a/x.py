import sys
import os
uno = os.getcwd()
dos = os.path.dirname(uno)
sys.path.append(dos)
from c.z import f2z
def f1x():
    print("f1x")

def f2x():
    print("f2x")
    f2z()
x1 = 1
x2 = 2
f2x()