#Makes an obsidian sphere of the radius entered.

from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    return mc
    
def sphere(mc,x,y,z):
    radius=int(input("Radius: "))
    for x1 in range(radius*-1,radius+1):
        for y1 in range(radius*-1,radius+1):
            for z1 in range(radius*-1,radius+1):
                if (x1**2)+(y1**2)+(z1**2)<=(radius+1)**2 and (x1**2)+(y1**2)+(z1**2)>=(radius-1)**2:
                    mc.setBlock(x+radius+x1,y+radius+y1,z+radius+z1,49)
def main():
    mc=init()
    x, y, z = mc.player.getPos()
    sphere(mc,x,y,z)

main()
