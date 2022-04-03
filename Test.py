from matplotlib import pyplot
import numpy as np
import matplotlib.pyplot as ppl

x = [0.0481, 0.0461, 0.0492, 0.0502, 0.0511, 0.0430, 0.0460, 
     0.0488,0.0453, 0.0497, 0.0521, 0.0519, 0.0531, 0.0466, 
     0.0463, 0.0500,0.0436, 0.0528, 0.0490, 0.0464, 0.0479, 
     0.0486, 0.0509, 0.0544,0.0515, 0.0475, 0.0504, 0.0516, 
     0.0438, 0.0537, 0.0470, 0.0482,0.0484, 0.0498, 0.0494]
n = len(x)
X = 0
for i in range(n):
  X += x[i] 
X = X/n
S = 0
for i in range(n):
  S += (x[i]-X)**2 
S = np.sqrt(S/(n-1))
N = n
xZ = []
for i in range(N):
  z = (x[i] - X) / S
  if z < 0.8:
    xZ.append(x[i])
nZ = len(xZ)
XZ = 0
for i in range(nZ):
  XZ += xZ[i] 
XZ = XZ/nZ
SZ = 0
for i in range(nZ):
  SZ += (xZ[i]-X)**2 
SZ = np.sqrt(SZ/(nZ-1))
