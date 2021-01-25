from mcpi.minecraft import Minecraft
from mcpi import block
import random
import time


mc = Minecraft.create()
# set player to 0,0,0
mc.player.setPos(0,0,0)
# CLEAR AN AREA WITH AIR TO BUILD
air = 0
mc.setBlocks(-24,-1,-36,24,64,36,air) # clear some air                                               
mc.player.setPos(0,0,0)
for n in range (0,54):

	h = random.randint(-1,1) #x
	k = random.randint(-1,1)	#y
	l = random.randint(-1,1)	#z
	c = random.randint(0,5)	#color
	mc.setBlock(h,k,l,35,c)
	time.sleep(0.25)
mc.player.setPos(4,0,-4)
