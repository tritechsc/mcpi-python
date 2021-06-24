import time
from mcpi.minecraft import Minecraft
from mcpi import block

ip="10.183.3.20"
mc = Minecraft.create(ip,4711)
air = 0
mc.setBlocks(15,0,-9,-8,64,11,air)
#x, y, z = mc.player.getTilePos()                                                  
x, y, z = mc.player.getPos()


#mc.setBlock(-15,35,-10,57)

#rocket body
for x in range(4,40):
	mc.setBlock(0,x,0,35,0)
	mc.setBlock(1,x,0,35,0)
	mc.setBlock(2,x,0,35,0)
	mc.setBlock(-1,x,1,35,0)
	mc.setBlock(-1,x,2,35,0)
	mc.setBlock(-1,x,3,35,0)
	mc.setBlock(0,x,4,35,0)
	mc.setBlock(1,x,4,35,0)
	mc.setBlock(2,x,4,35,0)
	mc.setBlock(3,x,1,35,0)
	mc.setBlock(3,x,2,35,0)
	mc.setBlock(3,x,3,35,0)
for x in range(4,44):	
	mc.setBlock(0,x,1,35,0)
	mc.setBlock(0,x,2,35,0)
	mc.setBlock(0,x,3,35,0)
	mc.setBlock(1,x,3,35,0)
	mc.setBlock(2,x,3,35,0)
	mc.setBlock(2,x,2,35,0)
	mc.setBlock(2,x,1,35,0)
	mc.setBlock(1,x,1,35,0)
for x in range(4,45):
	mc.setBlock(1,x,2,35,0)

for x in range(4,20): #external boosters
	mc.setBlock(-1,x,0,35,11) #1
	mc.setBlock(3,x,0,35,11) #2
	mc.setBlock(3,x,4,35,11) #3
	mc.setBlock(-1,x,4,35,11) #4
for x in range(4,18):
	mc.setBlock(-2,x,-1,35,11) #1
	mc.setBlock(-2,x,0,35,11)
	mc.setBlock(-1,x,-1,35,11)
	mc.setBlock(-2,x,4,35,11) #2
	mc.setBlock(-2,x,5,35,11)
	mc.setBlock(-1,x,5,35,11)
	mc.setBlock(3,x,5,35,11) #3
	mc.setBlock(4,x,5,35,11)
	mc.setBlock(4,x,4,35,11)
	mc.setBlock(3,x,-1,35,11) #4
	mc.setBlock(4,x,-1,35,11)
	mc.setBlock(4,x,0,35,11)
for x in range(4,12):
	mc.setBlock(-3,x,-2,35,11) #1
	mc.setBlock(-3,x,-1,35,11)
	mc.setBlock(-3,x,0,35,11)
	mc.setBlock(-2,x,-2,35,11)
	mc.setBlock(-1,x,-2,35,11)
	mc.setBlock(-3,x,4,35,11) #2
	mc.setBlock(-3,x,5,35,11)
	mc.setBlock(-3,x,6,35,11)
	mc.setBlock(-2,x,6,35,11)
	mc.setBlock(-1,x,6,35,11)
	mc.setBlock(3,x,6,35,11) #3
	mc.setBlock(4,x,6,35,11)
	mc.setBlock(5,x,6,35,11)
	mc.setBlock(5,x,5,35,11)
	mc.setBlock(5,x,4,35,11)
	mc.setBlock(3,x,-2,35,11) #4
	mc.setBlock(4,x,-2,35,11)
	mc.setBlock(5,x,-2,35,11)
	mc.setBlock(5,x,-1,35,11)
	mc.setBlock(5,x,0,35,11)

mc.setBlock(0,3,1,35,15) #main engine nozzle
mc.setBlock(0,3,2,35,15)
mc.setBlock(0,3,3,35,15)
mc.setBlock(1,3,3,35,15)
mc.setBlock(2,3,3,35,15)
mc.setBlock(2,3,2,35,15)
mc.setBlock(2,3,1,35,15)
mc.setBlock(1,3,1,35,15)

mc.setBlock(-3,3,-1,35,15) #booster nozzle
mc.setBlock(-2,3,-2,35,15)
mc.setBlock(-2,3,0,35,15)
mc.setBlock(-1,3,-1,35,15)
mc.setBlock(-3,3,5,35,15) #2
mc.setBlock(-2,3,6,35,15)
mc.setBlock(-1,3,5,35,15)
mc.setBlock(-2,3,4,35,15)
mc.setBlock(3,3,5,35,15) #3
mc.setBlock(4,3,6,35,15)
mc.setBlock(4,3,4,35,15)
mc.setBlock(5,3,5,35,15)
mc.setBlock(3,3,-1,35,15) #4
mc.setBlock(4,3,-2,35,15)
mc.setBlock(4,3,0,35,15)
mc.setBlock(5,3,-1,35,15)

#support beam
for x in range(0,4):
	mc.setBlock(-1,x,0,41)
	mc.setBlock(-1,x,4,41)
	mc.setBlock(3,x,4,41)
	mc.setBlock(3,x,0,41)

#deposit player on viewing platform
mc.postToChat("Soyuz Rocket - Delta77")
mc.player.setPos(1,0,2)
time.sleep(5)



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
