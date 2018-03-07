#Paints wool in a 3x3x3 area centered in the block clicked.

from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi import event
from random import randint

def init():
	mc = Minecraft.create("127.0.0.1", 4711)
	return mc
	
def colorchange(mc,x,y,z):
	colorchoice=randint(0,15)
	for x1 in range(-1,2):
		for y1 in range(-1,2):
			for z1 in range(-1,2):
				if mc.getBlock(x+x1,y+y1,z+z1)==35:
					mc.setBlock(x+x1,y+y1,z+z1,35,colorchoice)
	
def checkBlock(mc):
	blockEvent=mc.events.pollBlockHits()
	for each in blockEvent:
		x=each.pos.x
		y=each.pos.y
		z=each.pos.z
		if mc.getBlock(x,y,z)==35:
			colorchange(mc,x,y,z)
	
def main():
	mc=init()
	while True:
		checkBlock(mc)

main()
