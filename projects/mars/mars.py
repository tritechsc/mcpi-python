from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init(): 
	mc = Minecraft.create("10.183.4.121", 4711)
	x, y, z = mc.player.getPos()  
	return mc

def main():
 mc = Minecraft.create("10.183.4.121", 4711)
 #planet mars
 sphere(mc,-92,22,-15,20,20,20,87)
 sphere(mc,-92,22,-15,18,18,18,0)
 #roket on/in mars
 cylinder(mc,-92,42,-15,4,4,4,1,42)
 cylinder(mc,-92,42,-15,3,3,3,1,0)
 #door way for mars
 mc.setBlock(-91.5,43,-11.5,0)
 mc.setBlock(-91.5,42,-11.5,0)
 #lighting in the planet
 mc.setBlock(-89.3,38.0,-16.7,0)
 mc.setBlock(-89.4,4.0,-16.4,89)
 #time set
 mc.setTime()

def sphere(mc,px,py,pz,X,Y,Z,block):
 for x in range(-X,X):
  for y in range(-Y,Y):
   for z in range(-Z,Z):
    if ((x/X)**2)+((y/Y)**2)+((z/Z)**2)<1:
     mc.setBlock(px+x,py+y,pz+z,block)

def cylinder(mc,px,py,pz,X,Y,Z,axis,block):
 if axis%3==0:
  for x in range(-X,X):
   for y in range(-Y,Y):
    if ((x/X)**2)+((y/Y)**2)<1:
     mc.setBlocks(px+x,py+y,pz-Z,px+x,py+y,pz+Z,block)
 elif axis%3==1:
  for x in range(-X,X):
   for z in range(-Z,Z):
    if ((x/X)**2)+((z/Z)**2)<1:
     mc.setBlocks(px+x,py-Y,pz+z,px+x,py+Y,pz+z,block)
 elif axis%3==2:
  for y in range(-Y,Y):
   for z in range(-Z,Z):
    if ((y/Y)**2)+((z/Z)**2)<1:
     mc.setBlocks(px-X,py+y,pz+z,px+X,py+y,pz+z,block)
main()
