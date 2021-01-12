from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
# set player to 0,0,0
#mc.player.setPos(0,0,0)
# CLEAR AN AREA WITH AIR TO BUILD
                                           
x, y, z = mc.player.getPos()
xyzString = str(x)+" , "+str(y)+" , "+str(z)
#print(xyzString)
# mc.setBlock (x,y,z, material_number) 
mc.postToChat("THIS IS A MUSHROOM")
mc.postToChat(xyzString)

#  Lay block in the air 
h,k,l = 1,0,1; c = 0        # ROW 0
mc.setBlock(x+h,y+k,z+l,35,6) 	# 1 
h,k,l = 1,0,2
mc.setBlock(x+h,y+k,z+l,35,6) 	# 2
h,k,l = 2,0,2
mc.setBlock(x+h,y+k,z+l,35,6) 	# 3
h,k,l = 2,0,1
mc.setBlock(x+h,y+k,z+l,35,6) 	# 4

h,k,l = 1,1,1				 # ROW 1
mc.setBlock(x+h,y+k,z+l,35,6) 	# 5 ROW 1
h,k,l = 1,1,2
mc.setBlock(x+h,y+k,z+l,35,6) 	# 6
h,k,l = 2,1,2
mc.setBlock(x+h,y+k,z+l,35,6) 	# 7
h,k,l = 2,1,1
mc.setBlock(x+h,y+k,z+l,35,6) 	# 8 


h,k,l = 0,2,0; c = 4		# ROW 2
mc.setBlock(x+h,y+k,z+l,35,c) 	# 9 
h,k,l = 0,2,1
mc.setBlock(x+h,y+k,z+l,35,14) 	# 10
h,k,l = 0,2,2;c = 14
mc.setBlock(x+h,y+k,z+l,35,c) 	# 11
h,k,l = 0,2,3; c = 4
mc.setBlock(x+h,y+k,z+l,35,c) 	# 12
h,k,l = 1,2,3
mc.setBlock(x+h,y+k,z+l,35,c) 	# 13
h,k,l = 2,2,3
mc.setBlock(x+h,y+k,z+l,35,c) 	# 14
h,k,l = 3,2,3
mc.setBlock(x+h,y+k,z+l,35,14) 	# 15
h,k,l = 3,2,2
mc.setBlock(x+h,y+k,z+l,35,c) 	# 16
h,k,l = 3,2,1
mc.setBlock(x+h,y+k,z+l,35,c) 	# 17
h,k,l = 3,2,0
mc.setBlock(x+h,y+k,z+l,35,c) 	# 18
h,k,l = 2,2,0
mc.setBlock(x+h,y+k,z+l,35,14) 	# 19
h,k,l = 1,2,0
mc.setBlock(x+h,y+k,z+l,35,c) 	# 20

h,k,l = 0,3,0; c = 4		# ROW 3
mc.setBlock(x+h,y+k,z+l,35,c) 	# 21
h,k,l = 0,3,1
mc.setBlock(x+h,y+k,z+l,35,c) 	# 22
h,k,l = 0,3,2
mc.setBlock(x+h,y+k,z+l,35,c) 	# 23
h,k,l = 0,3,3
mc.setBlock(x+h,y+k,z+l,35,14) 	# 24
h,k,l = 1,3,3
mc.setBlock(x+h,y+k,z+l,35,c) 	# 25
h,k,l = 2,3,3
mc.setBlock(x+h,y+k,z+l,35,c) 	# 26
h,k,l = 3,3,3
mc.setBlock(x+h,y+k,z+l,35,c) 	# 27
h,k,l = 3,3,2
mc.setBlock(x+h,y+k,z+l,35,14) 	# 28
h,k,l = 3,3,1
mc.setBlock(x+h,y+k,z+l,35,c) 	# 29
h,k,l = 3,3,0
mc.setBlock(x+h,y+k,z+l,35,c) 	# 30
h,k,l = 2,3,0
mc.setBlock(x+h,y+k,z+l,35,c) 	# 31
h,k,l = 1,3,0
mc.setBlock(x+h,y+k,z+l,35,c) 	# 32

h,k,l = 1,4,1; c = 14				 # ROW 4
mc.setBlock(x+h,y+k,z+l,35,c) 	# 33 ROW 4
h,k,l = 1,4,2;c = 4
mc.setBlock(x+h,y+k,z+l,35,c) 	# 34
h,k,l = 2,4,2 
mc.setBlock(x+h,y+k,z+l,35,c) 	# 35
h,k,l = 2,4,1 
mc.setBlock(x+h,y+k,z+l,35,c) 	# 36
   
mc.player.setPos(x,y+5,z)


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
