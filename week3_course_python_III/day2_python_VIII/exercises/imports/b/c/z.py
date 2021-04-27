import sys
import os
uno = os.getcwd()
dos = os.path.dirname(uno)
tres = os.path.dirname(dos)
sys.path.append(tres)
print(sys.path)
from a.x import f2x
from b.y import f1y
def f1z():
    print("f1z")
    f1y()

def f2z():
    f2x()
    print("f2z")
z1 = 3
z2 = 4
f2z()
f1z()