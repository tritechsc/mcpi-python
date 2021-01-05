import time
import math
from mcpi.minecraft import Minecraft
from mcpi import block

def isprime(n):
	nd = float(n)
	prime = True
	pivot = int(math.sqrt(nd))
	if n > 1:
		for d in range (2,n):
			d = float(d)
			#print ((nd / d),int(nd / d))
			if ((nd / d) == int(nd / d) ):
				prime = False
				break
	else:
		prime = False
		
	return prime

mc = Minecraft.create()

mc.player.setPos(0,0,0)
mc.postToChat("CLEAR AN AREA WITH AIR TO BUILD")
air = 0
mc.setBlocks(-19,0,-19,19,64,19,air) # clear some air
#x, y, z = mc.player.getTilePos()                                                  
x, y, z = mc.player.getPos()
mc.postToChat("PLAYER POSITION")
xyzString = str(x)+" , "+str(y)+" , "+str(z)
mc.postToChat(xyzString)
# mc.setBlock (x,y,z, material) 
mc.player.setPos(0,5,-5)
# Lay blocks flat on ground
xz =  [[0,0],[1,0],[1,1],[0,1],[-1,1],
	  [-1,0],[-1,-1],[0,-1],[1,-1],[2,-1],
	  [2,0],[2,1],[2,2],[1,2],[0,2],
	  [-1,2],[-2,2],[-2,1],[-2,0],[-2,-1],
	  [-2,-2],[-1,-2],[0,-2],[1,-2],[2,-2],
	  [3,-2],[3,-1],[3,0],[3,1],[3,2],[3,3]]
for n in range(len(xz)):
	print(" n + 1 ",n + 1," ",end="")
	x = xz[n][0]
	z = xz[n][1]
	ip = isprime(n+1)
	mc.setBlock(x,0,z,80) 
	if ip == True:
		print(n+1)
		mc.setBlock(x,0,z,79) 
	time.sleep(1)
	print(n,n+1,ip)
	print(x,z)
	
		


'''
wool 35,0  WHITE
wool 35,1  ORANGE
wool 35,2  DARK PINK 
wool 35,3  LIGHT BLUE 
wool 35,4  YELLOW
wool 35,5  GREEN
wool 35,6  LIGHT PINK
wool 35,7  DARK GRAY
wool 35,8  LIGHT GRAY
wool 35,9  TEAL OR DARKER BLUE 
wool 35,10 VIOLET
wool 35,11  DARK BLUE
wool 35,12  BROWN
wool 35,13  DARK GREEN
wool 35,14  RED
wool 35,15  BLACK


#mc.setBlocks(-128,0,-128,128,64,128,0)
#API Blocks
#====================
#   AIR                   0
#   STONE                 1
#   GRASS                 2
#   DIRT                  3
#   COBBLESTONE           4
#   WOOD_PLANKS           5
#   SAPLING               6
#   BEDROCK               7
#   WATER_FLOWING         8
#   WATER                 8
#   WATER_STATIONARY      9
#   LAVA_FLOWING         10
#   LAVA                 10
#   LAVA_STATIONARY      11
#   SAND                 12
#   GRAVEL               13
#   GOLD_ORE             14
#   IRON_ORE             15
#   COAL_ORE             16
#   WOOD                 17
#   LEAVES               18
#   GLASS                20
#   LAPIS_LAZULI_ORE     21
#   LAPIS_LAZULI_BLOCK   22
#   SANDSTONE            24
#   BED                  26
#   COBWEB               30
#   GRASS_TALL           31
#   WOOL                 35
#   FLOWER_YELLOW        37
#   FLOWER_CYAN          38
#   MUSHROOM_BROWN       39
#   MUSHROOM_RED         40
#   GOLD_BLOCK           41
#   IRON_BLOCK           42
#   STONE_SLAB_DOUBLE    43
#   STONE_SLAB           44
#   BRICK_BLOCK          45
#   TNT                  46
#   BOOKSHELF            47
#   MOSS_STONE           48
#   OBSIDIAN             49
#   TORCH                50
#   FIRE                 51
#   STAIRS_WOOD          53
#   CHEST                54
#   DIAMOND_ORE          56
#   DIAMOND_BLOCK        57
#   CRAFTING_TABLE       58
#   FARMLAND             60
#   FURNACE_INACTIVE     61
#   FURNACE_ACTIVE       62
#   DOOR_WOOD            64
#   LADDER               65
#   STAIRS_COBBLESTONE   67
#   DOOR_IRON            71
#   REDSTONE_ORE         73
#   SNOW                 78
#   ICE                  79
#   SNOW_BLOCK           80
#   CACTUS               81
#   CLAY                 82
#   SUGAR_CANE           83
#   FENCE                85
#   GLOWSTONE_BLOCK      89
#   BEDROCK_INVISIBLE    95
#   STONE_BRICK          98
#   GLASS_PANE          102
#   MELON               103
#   FENCE_GATE          107
#   GLOWING_OBSIDIAN    246
#   NETHER_REACTOR_CORE 247


mc.setBlock(0,0,5,35,0) 	# WHITE   0,  0,  0
mc.setBlock(2,2,5,35,1) 	# ORANGE  2,  0,  2
mc.setBlock(-2,2,5,35,2) 	# PINK   -2,  0,  2
mc.setBlock(-2-2,5,35,3) 	# BLUE   -2,  0, -2
mc.setBlock(2,-2,5,35,4)  	# YELLOW  2,  0, -2
''' 
