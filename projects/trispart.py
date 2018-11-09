from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init(): 
	# change 10.183.13.13 to 127.0.0.1 or your ip
	mc = Minecraft.create("127.0.0.1", 4711)
	x, y, z = mc.player.getPos()  
	return mc

#main  
def main():
	mc = init()
	#mc.player.setPos(0, 0, 0)
	'''shell of house'''
	x, y, z = mc.player.getPos() 
	a, b, c = mc.player.getPos() 
	while(int(x)+int(z) == int(a)+int(c)):
		a, b, c = mc.player.getPos()
	x+=(int(a)-int(x))*10
	z+=(int(c)-int(z))*10
	z+=4
	y+=4
	mc.setBlocks(x-5, y-5, z-5, x+5, y+5, z+5, 57)
	mc.setBlocks(x-4,y-4,z-4, x+1, y-2, z+4, 0)
	mc.setBlocks(x-5, y+5, z-5, x+5, y+5, z+5, 20)
	mc.setBlocks(x-4, y-4, z-4, x+4, y+4, z+4, 0)
	#mc.setBlock(x, y+1, z+1, 22)
	#mc.setBlocks(x-5,y-4,z,x-5,y+4,z,11)
	#mc.setBlocks(x+5,y-4,z,x+5,y+4,z,11)
	#mc.setBlocks(x,y-4,z+5,x,y+4,z+5,11)
	#mc.setBlocks(x,y-4,z-5,x,y+4,z-5,11)
	
	
	'''stairs'''
	mc.setBlock(x-4,y-4,z, 20) 
	mc.setBlock(x-4, y-3,z+2, 20)
	mc.setBlock(x-4, y-2,z+4,20)
	mc.setBlock(x-2,y-1,z+4,20)
	
	mc.setBlock(x+5,y-4,z+4,0)
	mc.setBlock(x+5,y-3,z+4,0)
	
	mc.setBlock(x+5,y-4,z-4,0)
	mc.setBlock(x+5,y-3,z-4,0)
	
	mc.setBlock(x-5,y-4,z+4,0)	
	mc.setBlock(x-5,y-3,z+4,0)
	
	mc.setBlock(x-4,y-3,z+5,0)
	mc.setBlock(x-4,y-4,z+5,0)
	mc.setBlock(x-4,y-3,z+4,0)
	mc.setBlock(x-4,y-4,z+4,0)
	
	mc.setBlock(x-5,y-4,z-4,0)
	mc.setBlock(x+5,y-3,z-4,0)
	mc.setBlock(x+5,y-4,z-4,0)
	
	
	mc.setBlock(x-5,y-4,z+5,0)
	mc.setBlock(x+5,y-3,z+5,0)
	mc.setBlock(x+5,y-4,z+5,0)
	
	mc.setBlock(x+4,y-4,z+5,0)
	mc.setBlock(x+4,y-3,z+5,0)
	mc.setBlock(x-5,y-3,z+5,0)
	
	mc.setBlock(x+4,y-3,z-5,0)
	mc.setBlock(x+5,y-3,z-5,0)
	mc.setBlock(x+4,y-4,z-5,0)
	mc.setBlock(x+5,y-4,z-5,0)
	
	mc.setBlock(x-5,y-4,z-5,0)
	mc.setBlock(x-5,y-3,z-5,0)
	mc.setBlock(x-5,y-3,z-4,0)
	mc.setBlock(x-5,y-4,z-4,0)
	mc.setBlock(x-4,y-4,z-5,0)
	mc.setBlock(x-4,y-3,z-5,0)
	
	'''2nd floor'''
	mc.setBlocks(x-3,y-1,z+3,x+3, y-1, z-3,57)
	mc.setBlocks(x+4, y+5, z+2, x+4, y+5, z-1, 0)
	mc.setBlocks(x+4, y+5, z+2, x, y+5, z+2, 0)
	'''2nd stairs'''
	mc.setBlock(x-2,y,z-1,20)
	mc.setBlock(x-1,y+1,z+2,20)
	mc.setBlock(x+2,y+2,z+2,20)
	mc.setBlock(x+4, y+3,z+2,20)
	mc.setBlock(x+4, y+4,z-1, 20)
	mc.setBlock(x,y+6,z,246)
	'''ending'''

	while (0==0):
		if(mc.getBlock(x,y+7,z)>0):
			break
	for i in range(0,1):
		mc.setBlocks(x,y+7,z,x,y+15,z,5)
		mc.setBlocks(x,y+14-2*i,z,x+5,y+15-2*i,z,49)
		mc.setBlocks(x,y+12-2*i,z,x+5,y+13-2*i,z, 35,14)
		mc.setBlocks(x,y+10-2*i,z,x+5,y+11-2*i,z,35,1)
		

main()

  
# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""

