from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init(): 
	mc = Minecraft.create("127.0.0.1", 4711)  
	return mc

def main():
	mc = init()
	x, y, z = mc.player.getPos()  
	mc.postToChat("Osiris Has Arrived")
	mc = init()
	mc.setBlocks(+164, +64, +164, -164, 0, -164, block.AIR.id) 
	mc.setBlocks(+164, +5, +164, -164, -5, -164, block.SAND.id) 
	x, y, z = mc.player.getPos()
	for i in range(64):
		mc.setBlocks(x+i, y-i,z +i, x-i, y-i, z-i, block.SANDSTONE.id) 
		if i != 0:
			mc.setBlocks(x+i-1,y-i,z+i-1,x-i+1,y-i,z-i+1, block.AIR.id)
	x = 0
	while(x < 10):
		mc.setBlocks(0, +80, 0, 0, 0, 0, block.AIR.id)
		x = x + 7
main()



