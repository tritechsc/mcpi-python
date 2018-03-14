from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init(): 
	# change 192.168.1.13 to 127.0.0.1 or your ip
	mc = Minecraft.create("10.183.4.122", 4711)
	x, y, z = mc.player.getPos()  
	return mc

def alien(mc,x,y,z):
	mc.setBlocks(x-2, y, z+3, x+0, y+3, z+2, 103)
	mc.setBlock(x-2, y+2, z+3, 246)
	mc.setBlock(x+0, y+2, z+3, 246)
	mc.setBlock(x-1, y-1, z+3, 103)
	mc.setBlock(x-2, y-1, z+3, 103)
	mc.setBlock(x-1, y-3, z+3, 103)
	mc.setBlock(x-1, y-4, z+3, 103)
	mc.setBlock(x-1, y-3, z+3, 103)
	mc.setBlock(x-1, y-2, z+3, 103)
	mc.setBlock(x-3, y-1, z+3, 103)
	mc.setBlock(x-4, y-1, z+3, 103)
	mc.setBlock(x+0, y-1, z+3, 103)
	mc.setBlock(x+1, y-1, z+3, 103)
	mc.setBlock(x+2, y+0, z+3, 103)
	mc.setBlock(x-3, y-1, z+3, 103)
	mc.setBlock(x+0, y-4, z+3, 103)
	mc.setBlock(x-2, y-4, z+3, 103)
	mc.setBlock(x+1, y-5, z+3, 103)	
	mc.setBlock(x-3, y-5, z+3, 103)
	mc.postToChat("I come in peace")
	
#main  
def main():
	mc = init()
	#mc.player.setPos(0, 0, 0)
	x, y, z = mc.player.getPos()  
	xr =0 
	yr =5
	zr =5
	for n in range (0,2):
		alien(mc,x+xr,y+yr ,z + zr)
		xr = xr + 0
		yr = yr + 0 
		zr = zr + 23

	count = 5 
	while count > 3:
		count = count + 5


main()
