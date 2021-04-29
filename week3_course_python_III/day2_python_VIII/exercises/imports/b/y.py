import sys
import os
uno = os.getcwd()
print(uno)
dos = os.path.dirname(uno)
print(dos)
sys.path.append(dos)
print(sys.path)
from x import f1x, f2x

def f1y():
    print("f1y")
    f1x()
def f2y():
    print("f2y")
    f2x()

y1 = 3
y2 = 4
f1y()
f2y()
