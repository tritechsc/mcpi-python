from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
from random import randint

def init(): 
	# change 192.168.1.13 to 127.0.0.1 or your ip
	#mc = Minecraft.create("10.183.4.123", 4711)
	#mc = Minecraft.create("10.183.13.13", 4711)
	mc = Minecraft.create("127.0.0.1", 4711)
	x, y, z = mc.player.getPos()  
	return mc
	

 
def igloo(mc, x, y, z):
	
 
	mc.setBlocks(x-2, y, z, x-2, y, z-4, 80)
	mc.setBlocks(x-1, y+1,z, x-1, y+1, z-4, 80)
	mc.setBlocks(x, y+2, z, x, y+2, z-4, 80)
	mc.setBlocks(x+1, y+2, z, x+1, y+2, z-4, 80)
	mc.setBlocks(x+3, y, z, x+3, y, z-4, 80)
	mc.setBlocks(x+1, y+3, z-4, x, y+3, z-4, 80)
	mc.setBlocks(x+2, y+1, z, x+2, y+1, z-4, 80)
	mc.setBlock(x+2, y+2, z-4, 80)
	mc.setBlock(x+3, y+1, z-4, 80)
	mc.setBlock(x-2, y+1, z-4, 80)
	mc.setBlock(x-1, y+2, z-4, 80)
	mc.setBlocks(x+4, y, z-4, x+4, y+1, z-7, 80)
	mc.setBlocks(x+5, y, z-5, x+4, y+1, z-7, 80)
	mc.setBlocks(x+5, y, z-6, x+5,y+1, z-8, 80)
	mc.setBlocks(x-3, y, z-4, x-3, y+1, z-6, 80)
	mc.setBlocks(x-4, y, z-5, x-4, y+1, z-7, 80)
	mc.setBlocks(x-4, y, z-6, x-4 , y+1, z-8, 80)
	mc.setBlock(x-3, y+2, z-6, 80)
	mc.setBlock(x-3, y+2, z-6, 80)
	mc.setBlock(x-2, y+2, z-5, 80)
	mc.setBlock(x-2, y+3, z-6, 80)
	mc.setBlock(x+4, y+2, z-6, 80)
	mc.setBlock(x+3, y+2, z-5, 80)
	mc.setBlock(x+3, y+3, z-6, 80)
	mc.setBlocks(x, y+4, z-5, x+1, y+4, z-5, 80)
	mc.setBlock(x-1, y+3, z-5, 80)
	mc.setBlock(x+2, y+3, z-5, 80)
	mc.setBlocks(x+2, y+4, z-6, x-1, y+4, z-8, 80)
	mc.setBlocks(x-2, y+3, z-7, x-2, y+3, z-8, 80)
	mc.setBlocks(x-3, y+2, z-7, x-3, y+2, z-8, 80)
	mc.setBlocks(x+3, y+3, z-7, x+3, y+3, z-8, 80)
	mc.setBlocks(x+4, y+2, z-7, x+4, y+2, z-8, 80)
	mc.setBlocks(x-2, y+3, z-9, x+3, y+3, z-9, 80)
	mc.setBlock(x-3, y+2, z-9, 80)
	mc.setBlock(x+4, y+2, z-9, 80)
	mc.setBlocks(x+4, y+2, z-10, x-3, y+2, z-10, 80)
	mc.setBlocks(x-4, y, z-9, x-4, y+1, z-10, 80)
	mc.setBlocks(x+5, y, z-9, x+5, y+1, z-10, 80)
	mc.setBlocks(x-4, y, z-11, x+5, y+1, z-11, 80)
	
def loop(mc, x, y, z):
	for n in range(0,10):
		mc = init()
		x, y, z = mc.player.getPos()  
		zz = z + 1
		#mc.player.setPos(0, 0, 0)
		#mc.setBlocks(x-128, y, z-128, x+128, y-100-63, z+128,0)
		mc.setBlocks(x-128, y-n, z-128, x+128, y-n, z+128, 80)
		mc.player.setPos(0, 100, 0)

def snow(mc, x, y, z):
	count = 0
	while count < 100:
		mc = init()
		x, y, z = mc.player.getPos() 
		x = randint(-100,100)
		z = randint(-100,100)
		if count%4 == 0:
			mc.setBlock(x, y, z, 35, count%16)
			mc.setBlock(x-1, y, z, 35, count%16)
			mc.setBlock(x+1, y, z, 35, count%16)
			mc.setBlock(x, y+1, z, 35, count%16)
			mc.setBlock(x, y-1, z, 35, count%16)
			mc.setBlock(x, y, z+1, 35, count%16)
			mc.setBlock(x, y, z-1, 35, count%16)
		mc.setBlock(x, y, z, 35, count%16)
		print(count%16)
		count = count + 1
	
def main():
	mc = init()
	#mc.player.setPos(0, 0, 0)
	x, y, z = mc.player.getPos() 
	#loop(mc, x, y, z)
	igloo(mc, x, y, z)
	snow(mc, x, y, z)
	
main()
