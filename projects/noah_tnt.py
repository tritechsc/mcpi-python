#Makes tnt fall and explode, kind of like vanilla. Sadly, only one tnt can be going at a time.

from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi import event
from time import sleep

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    return mc

def tnt(mc,x,y,z):
    for each in range(10):
        for other in range(1):
            mc.setBlock(x,y,z,46)
            sleep(0.1)
            mc.setBlock(x,y,z,11)
            sleep(0.1)
        if mc.getBlock(x,y-1,z)==0:
            mc.setBlock(x,y,z,0)
            y=y-1
    mc.postToChat("Poof Later Skater! Ur Dun Sun u Dont Want Nun :) ")
    sphere(mc,x,y,z)

def sphere(mc,x,y,z):
    radius=2
    for x1 in range(radius*-2,radius+10):#eye
        for y1 in range(radius*-2,radius+10):
            for z1 in range(radius*-2,radius+10):
                if (x1**6)+(y1**6)+(z1**6)<=(radius+10)**2:
                    mc.setBlock(x+x1+5,y+y1,z+z1+5,56)
                    
    for x1 in range(radius*-1,radius+5):#Nose center
        for y1 in range(radius*-1,radius+5):
            for z1 in range(radius*-1,radius+5):
                if (x1**6)+(y1**6)+(z1**6)<=(radius+6)**2:
                    mc.setBlock(x+x1,y+y1,z+z1,3)
                    
    for x1 in range(radius*-2,radius+10):#eye
        for y1 in range(radius*-2,radius+10):
            for z1 in range(radius*-2,radius+10):
                if (x1**6)+(y1**6)+(z1**6)<=(radius+10)**2:
                    mc.setBlock(x+x1+5,y+y1,z+z1-5,56)
                    
    for x1 in range(radius*-2,radius+5):#smile start
        for y1 in range(radius*-2,radius+7):
            for z1 in range(radius*-2,radius+7):
                if (x1**6)+(y1**6)+(z1**6)<=(radius+7)**2:
                    mc.setBlock(x+x1-7,y+y1,z+z1,56)
                    
    for x1 in range(radius*-2,radius+5):#smile
        for y1 in range(radius*-2,radius+7):
            for z1 in range(radius*-2,radius+7):
                if (x1**6)+(y1**6)+(z1**6)<=(radius+7)**2:
                    mc.setBlock(x+x1-7,y+y1,z+z1+3,56)
                    
    for x1 in range(radius*-2,radius+5):#smile
        for y1 in range(radius*-2,radius+10):
            for z1 in range(radius*-2,radius+10):
                if (x1**6)+(y1**6)+(z1**6)<=(radius+7)**2:
                    mc.setBlock(x+x1-7,y+y1,z+z1-3,56)
                    
    for x1 in range(radius*-2,radius+5):#smile
        for y1 in range(radius*-2,radius+10):
            for z1 in range(radius*-2,radius+10):
                if (x1**6)+(y1**6)+(z1**6)<=(radius+7)**2:
                    mc.setBlock(x+x1-5,y+y1,z+z1-6,56)
                    
    for x1 in range(radius*-2,radius+5):#smile end
        for y1 in range(radius*-2,radius+10):
            for z1 in range(radius*-2,radius+10):
                if (x1**6)+(y1**6)+(z1**6)<=(radius+7)**2:
                    mc.setBlock(x+x1-5,y+y1,z+z1+6,56)
                    
    for x1 in range(radius*-2,radius+10):#right tear
        for y1 in range(radius*-2,radius+10):
            for z1 in range(radius*-2,radius+10):
                if (x1**6)+(y1**6)+(z1**6)<=(radius+5)**2:
                    mc.setBlock(x+x1+1,y+y1,z+z1+7,9)
                    
    for x1 in range(radius*-2,radius+10):#left tear
        for y1 in range(radius*-2,radius+10):
            for z1 in range(radius*-2,radius+10):
                if (x1**6)+(y1**6)+(z1**6)<=(radius+5)**2:
                    mc.setBlock(x+x1+1,y+y1,z+z1-7,9)
                    
    for x1 in range(radius*-2,radius+3):#Eye brow
        for y1 in range(radius*-2,radius+1):
            for z1 in range(radius*-2,radius+2):
                if (x1**6)+(y1**2)+(z1**6)<=(radius+6)**2:
                    mc.setBlock(x+x1+11,y+y1,z+z1,3)
                    
    for x1 in range(radius*-2,radius+3):#Eye brow
        for y1 in range(radius*-2,radius+1):
            for z1 in range(radius*-2,radius+2):
                if (x1**6)+(y1**2)+(z1**6)<=(radius+6)**2:
                    mc.setBlock(x+x1+11,y+y1,z+z1+3,3)
                    
    for x1 in range(radius*-2,radius+3):#Eye brow
        for y1 in range(radius*-2,radius+1):
            for z1 in range(radius*-2,radius+2):
                if (x1**6)+(y1**2)+(z1**6)<=(radius+6)**2:
                    mc.setBlock(x+x1+11,y+y1,z+z1-3,3)
                    
    for x1 in range(radius*-2,radius+3):#Eye brow
        for y1 in range(radius*-2,radius+1):
            for z1 in range(radius*-2,radius+2):
                if (x1**6)+(y1**2)+(z1**6)<=(radius+6)**2:
                    mc.setBlock(x+x1+11,y+y1,z+z1-6,3)
                    
    for x1 in range(radius*-2,radius+3):#Eye brow
        for y1 in range(radius*-2,radius+1):
            for z1 in range(radius*-2,radius+2):
                if (x1**6)+(y1**2)+(z1**6)<=(radius+6)**2:
                    mc.setBlock(x+x1+11,y+y1,z+z1+6,3)
def checkBlock(mc):
    blockEvent=mc.events.pollBlockHits()
    for each in blockEvent:
        x=each.pos.x
        y=each.pos.y
        z=each.pos.z
        if mc.getBlock(x,y,z)==46:
            tnt(mc,x,y,z)

def main():
    mc=init()
    while True:
        checkBlock(mc)

main()
