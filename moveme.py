#/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block	  
import sys

arg0 = sys.argv[0]
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
print(arg0,arg1,arg2,arg3)
x = int(arg1)
y = int(arg2)
z = int(arg3)

mc = Minecraft.create()
print(x,y,z)

xyz = str(x)+" , "+str(y)+" , "+str(z)
mc.postToChat(xyz)
mc.player.setPos(z,y,z)
