#Makes tnt fall and explode, kind of like vanilla. Sadly, only one tnt can be going at a time.

from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi import event
from time import sleep

def init():
	mc = Minecraft.create("127.0.0.1", 4711)
	return mc

def tnt(mc,x,y,z):
	for each in range(30):
		for other in range(1):
			mc.setBlock(x,y,z,46)
			sleep(0.1)
			mc.setBlock(x,y,z,80)
			sleep(0.025)
		if mc.getBlock(x,y-1,z)==0:
			mc.setBlock(x,y,z,0)
			y=y-1
	mc.postToChat("Boom!")
	sphere(mc,x,y,z)

def sphere(mc,x,y,z):
	radius=2
	for x1 in range(radius*-1,radius+1):
		for y1 in range(radius*-1,radius+1):
			for z1 in range(radius*-1,radius+1):
				if (x1**2)+(y1**2)+(z1**2)<=(radius+1)**2:
					mc.setBlock(x+x1,y+y1,z+z1,0)

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
