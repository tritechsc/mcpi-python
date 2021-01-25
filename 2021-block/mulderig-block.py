from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
# set player to 0,0,0
mc.player.setPos(0,0,0)
# CLEAR AN AREA WITH AIR TO BUILD
air = 0
mc.setBlocks(-19,0,-19,19,64,19,air) # clear some air                                               
x, y, z = mc.player.getPos()
xyzString = str(x)+" , "+str(y)+" , "+str(z)
print(xyzString)
# mc.setBlock (x,y,z, material_number) 

#  Lay block in the air 
mc.setBlock(0,0,0,35,15) 	# White 0
mc.setBlock(1,0,0,35,15) 	# ORANGE 1
mc.setBlock(-6,1,0,35,15) 	# Dark Pink 2
mc.setBlock(-5,1,0,35,15) 	# Light Blue 3 
mc.setBlock(-1,1,0,35,15)  	# Yellow 4
mc.setBlock(0,1,0,35,3)   # Light Green 5
mc.setBlock(1,1,0,35,15)   # Light Pink 6
mc.setBlock(3,1,0,35,15)   # Dark Grey 7
mc.setBlock(4,1,0,35,15)   # Light Gray 8
mc.setBlock(-7,2,0,35,15)   # Teal 9
mc.setBlock(-6,2,0,35,3)   # Violet 10
mc.setBlock(-5,2,0,35,15)   # Dark blue 11
mc.setBlock(-3,2,0,35,15)   # Brown 12
mc.setBlock(-2,2,0,35,15)   # Dark Green 13
mc.setBlock(-1,2,0,35,15)   # Red 14
mc.setBlock(0,2,0,12)   # Black 15 
mc.setBlock(1,2,0,35,15)
mc.setBlock(2,2,0,35,15)
mc.setBlock(3,2,0,35,9)
mc.setBlock(4,2,0,35,15)
mc.setBlock(-7,3,0,35,15)
mc.setBlock(-6,3,0,12)
mc.setBlock(-5,3,0,35,15)
mc.setBlock(-4,3,0,35,15)
mc.setBlock(-3,3,0,35,9)
mc.setBlock(-2,3,0,35,7)
mc.setBlock(-1,3,0,35,4)
mc.setBlock(0,3,0,35,5)
mc.setBlock(1,3,0,35,5)
mc.setBlock(2,3,0,35,7)
mc.setBlock(3,3,0,35,4)
mc.setBlock(4,3,0,35,5)
mc.setBlock(5,3,0,35,15)
mc.setBlock(-7,4,0,35,15)
mc.setBlock(-6,4,0,12)
mc.setBlock(-5,4,0,35,4)
mc.setBlock(-4,4,0,35,7)
mc.setBlock(-3,4,0,35,7)
mc.setBlock(-2,4,0,35,7)
mc.setBlock(-1,4,0,35,4)
mc.setBlock(0,4,0,35,5)
mc.setBlock(1,4,0,35,5)
mc.setBlock(2,4,0,35,5)
mc.setBlock(3,4,0,35,5)
mc.setBlock(4,4,0,35,5)
mc.setBlock(5,4,0,35,15)
mc.setBlock(-7,5,0,35,15)
mc.setBlock(-6,5,0,35,4)
mc.setBlock(-5,5,0,12)
mc.setBlock(-4,5,0,12)
mc.setBlock(-3,5,0,35,7)
mc.setBlock(-2,5,0,35,4)
mc.setBlock(-1,5,0,12)
mc.setBlock(0,5,0,35,5)
mc.setBlock(1,5,0,35,5)
mc.setBlock(2,5,0,35,5)
mc.setBlock(3,5,0,35,5)
mc.setBlock(4,5,0,35,15)
mc.setBlock(-13,6,0,35,15)
mc.setBlock(-12,6,0,35,15)
mc.setBlock(-11,6,0,35,15)
mc.setBlock(-10,6,0,35,15)
mc.setBlock(-6,6,0,35,15)
mc.setBlock(-5,6,0,12)
mc.setBlock(-4,6,0,12)
mc.setBlock(-3,6,0,35,4)
mc.setBlock(-2,6,0,12)
mc.setBlock(-1,6,0,12)
mc.setBlock(0,6,0,35,4)
mc.setBlock(1,6,0,35,5)
mc.setBlock(2,6,0,35,5)
mc.setBlock(3,6,0,12)
mc.setBlock(4,6,0,35,15)
mc.setBlock(-14,7,0,35,15)
mc.setBlock(-13,7,0,35,5)
mc.setBlock(-12,7,0,35,5)
mc.setBlock(-11,7,0,35,5)
mc.setBlock(-10,7,0,35,5)
mc.setBlock(-9,7,0,35,15)
mc.setBlock(-6,7,0,35,15)
mc.setBlock(-5,7,0,12)
mc.setBlock(-4,7,0,12)
mc.setBlock(-3,7,0,12)
mc.setBlock(-2,7,0,12)
mc.setBlock(-1,7,0,12)
mc.setBlock(0,7,0,35,5)
mc.setBlock(1,7,0,35,5)
mc.setBlock(2,7,0,35,5)
mc.setBlock(3,7,0,35,15)
mc.setBlock(-15,8,0,35,15)
mc.setBlock(-14,8,0,35,5)
mc.setBlock(-13,8,0,35,5)
mc.setBlock(-12,8,0,35,5)
mc.setBlock(-11,8,0,35,5)
mc.setBlock(-10,8,0,35,5)
mc.setBlock(-9,8,0,35,5)
mc.setBlock(-8,8,0,35,15)
mc.setBlock(-7,8,0,35,15)
mc.setBlock(-6,8,0,35,5)
mc.setBlock(-5,8,0,35,7)
mc.setBlock(-4,8,0,12)
mc.setBlock(-3,8,0,12)
mc.setBlock(-2,8,0,12)
mc.setBlock(-1,8,0,35,5)
mc.setBlock(0,8,0,35,12)
mc.setBlock(1,8,0,35,14)
mc.setBlock(2,8,0,35,12)
mc.setBlock(3,8,0,12)
mc.setBlock(4,8,0,35,15)
mc.setBlock(5,8,0,35,15)
mc.setBlock(6,8,0,35,15)
mc.setBlock(-15,9,0,35,15)
mc.setBlock(-14,9,0,35,0)
mc.setBlock(-13,9,0,35,5)
mc.setBlock(-12,9,0,35,5)
mc.setBlock(-11,9,0,35,0)
mc.setBlock(-10,9,0,35,0)
mc.setBlock(-9,9,0,35,5)
mc.setBlock(-8,9,0,35,5)
mc.setBlock(-7,9,0,35,5)
mc.setBlock(-6,9,0,35,5)
mc.setBlock(-5,9,0,35,15)
mc.setBlock(-4,9,0,35,15)
mc.setBlock(-3,9,0,35,15)
mc.setBlock(-2,9,0,35,15)
mc.setBlock(-1,9,0,35,14)
mc.setBlock(0,9,0,35,14)
mc.setBlock(1,9,0,35,13)
mc.setBlock(2,9,0,35,13)
mc.setBlock(3,9,0,12)
mc.setBlock(4,9,0,12)
mc.setBlock(5,9,0,35,14)
mc.setBlock(6,9,0,12)
mc.setBlock(7,9,0,35,15)
mc.setBlock(-16,10,0,35,15)
mc.setBlock(-15,10,0,35,5)
mc.setBlock(-14,10,0,35,5)
mc.setBlock(-13,10,0,35,5)
mc.setBlock(-12,10,0,35,0)
mc.setBlock(-11,10,0,35,5)
mc.setBlock(-10,10,0,35,5)
mc.setBlock(-9,10,0,35,15)
mc.setBlock(-8,10,0,35,5)
mc.setBlock(-7,10,0,35,5)
mc.setBlock(-6,10,0,35,15)
mc.setBlock(-2,10,0,35,15)
mc.setBlock(-1,10,0,35,14)
mc.setBlock(0,10,0,35,14)
mc.setBlock(1,10,0,35,5)
mc.setBlock(2,10,0,35,0)
mc.setBlock(3,10,0,35,9)
mc.setBlock(4,10,0,12)
mc.setBlock(5,10,0,12)
mc.setBlock(6,10,0,12)
mc.setBlock(7,10,0,35,15)
mc.setBlock(-16,11,0,35,15)
mc.setBlock(-15,11,0,35,5)
mc.setBlock(-14,11,0,35,15)
mc.setBlock(-13,11,0,35,5)
mc.setBlock(-12,11,0,35,5)
mc.setBlock(-11,11,0,35,5)
mc.setBlock(-10,11,0,35,15)
mc.setBlock(-8,11,0,35,15)
mc.setBlock(-7,11,0,35,15)
mc.setBlock(-4,11,0,35,15)
mc.setBlock(-3,11,0,35,15)
mc.setBlock(-2,11,0,35,14)
mc.setBlock(-1,11,0,35,14)
mc.setBlock(0,11,0,35,14)
mc.setBlock(1,11,0,35,5)
mc.setBlock(2,11,0,35,0)
mc.setBlock(3,11,0,35,15)
mc.setBlock(4,11,0,35,7)
mc.setBlock(5,11,0,12)
mc.setBlock(6,11,0,35,15)
mc.setBlock(-16,12,0,35,15)
mc.setBlock(-15,12,0,35,15)
mc.setBlock(-13,12,0,35,15)
mc.setBlock(-12,12,0,35,15)
mc.setBlock(-11,12,0,35,15)
mc.setBlock(-5,12,0,35,15)
mc.setBlock(-4,12,0,35,14)
mc.setBlock(-3,12,0,35,14)
mc.setBlock(-2,12,0,35,14)
mc.setBlock(-1,12,0,35,14)
mc.setBlock(0,12,0,35,5)
mc.setBlock(1,12,0,35,5)
mc.setBlock(2,12,0,35,5)
mc.setBlock(3,12,0,35,5)
mc.setBlock(4,12,0,35,14)
mc.setBlock(5,12,0,35,9)
mc.setBlock(6,12,0,35,9)
mc.setBlock(7,12,0,35,15)
mc.setBlock(-6,13,0,35,15)
mc.setBlock(-5,13,0,35,12)
mc.setBlock(-4,13,0,35,12)
mc.setBlock(-3,13,0,35,14)
mc.setBlock(-2,13,0,35,14)
mc.setBlock(-1,13,0,35,5)
mc.setBlock(0,13,0,35,5)
mc.setBlock(1,13,0,35,5)
mc.setBlock(2,13,0,35,5)
mc.setBlock(3,13,0,35,5)
mc.setBlock(4,13,0,35,14)
mc.setBlock(5,13,0,35,9)
mc.setBlock(6,13,0,35,3)
mc.setBlock(7,13,0,35,3)
mc.setBlock(8,13,0,35,15)
mc.setBlock(-7,14,0,35,15)
mc.setBlock(-6,14,0,35,14)
mc.setBlock(-5,14,0,35,14)
mc.setBlock(-4,14,0,35,14)
mc.setBlock(-3,14,0,35,14)
mc.setBlock(-2,14,0,35,14)
mc.setBlock(-1,14,0,35,5)
mc.setBlock(0,14,0,35,5)
mc.setBlock(1,14,0,35,5)
mc.setBlock(2,14,0,35,5)
mc.setBlock(3,14,0,35,14)
mc.setBlock(4,14,0,35,7)
mc.setBlock(5,14,0,35,9)
mc.setBlock(6,14,0,35,3)
mc.setBlock(7,14,0,35,9)
mc.setBlock(8,14,0,35,3)
mc.setBlock(9,14,0,35,15)
mc.setBlock(10,14,0,35,15)
mc.setBlock(-6,15,0,35,15)
mc.setBlock(-5,15,0,35,12)
mc.setBlock(-4,15,0,35,14)
mc.setBlock(-3,15,0,35,14)
mc.setBlock(-2,15,0,35,14)
mc.setBlock(-1,15,0,35,14)
mc.setBlock(0,15,0,35,14)
mc.setBlock(1,15,0,35,14)
mc.setBlock(2,15,0,35,14)
mc.setBlock(3,15,0,35,14)
mc.setBlock(4,15,0,35,14)
mc.setBlock(5,15,0,35,7)
mc.setBlock(6,15,0,35,7)
mc.setBlock(7,15,0,35,9)
mc.setBlock(8,15,0,35,3)
mc.setBlock(9,15,0,35,3)
mc.setBlock(10,15,0,35,9)
mc.setBlock(11,15,0,35,15)
mc.setBlock(-10,16,0,35,15)
mc.setBlock(-9,16,0,35,15)
mc.setBlock(-8,16,0,35,15)
mc.setBlock(-7,16,0,35,15)
mc.setBlock(-6,16,0,35,12)
mc.setBlock(-5,16,0,35,14)
mc.setBlock(-4,16,0,35,14)
mc.setBlock(-3,16,0,35,14)
mc.setBlock(-2,16,0,35,14)
mc.setBlock(-1,16,0,35,14)
mc.setBlock(0,16,0,35,14)
mc.setBlock(1,16,0,35,14)
mc.setBlock(2,16,0,35,14)
mc.setBlock(3,16,0,35,14)
mc.setBlock(4,16,0,35,7)
mc.setBlock(5,16,0,35,2)
mc.setBlock(6,16,0,35,7)
mc.setBlock(7,16,0,35,15)
mc.setBlock(8,16,0,35,15)
mc.setBlock(9,16,0,35,9)
mc.setBlock(10,16,0,35,3)
mc.setBlock(11,16,0,35,3)
mc.setBlock(12,16,0,35,15)
mc.setBlock(-11,17,0,35,15)
mc.setBlock(-10,17,0,35,14)
mc.setBlock(-9,17,0,35,14)
mc.setBlock(-8,17,0,35,14)
mc.setBlock(-7,17,0,35,14)
mc.setBlock(-6,17,0,35,14)
mc.setBlock(-5,17,0,35,14)
mc.setBlock(-4,17,0,35,14)
mc.setBlock(-3,17,0,35,14)
mc.setBlock(-2,17,0,35,14)
mc.setBlock(-1,17,0,35,14)
mc.setBlock(0,17,0,35,14)
mc.setBlock(1,17,0,35,14)
mc.setBlock(2,17,0,35,14)
mc.setBlock(3,17,0,35,14)
mc.setBlock(4,17,0,35,7)
mc.setBlock(5,17,0,35,2)
mc.setBlock(6,17,0,35,1)
mc.setBlock(7,17,0,35,15)
mc.setBlock(9,17,0,35,15)
mc.setBlock(10,17,0,35,15)
mc.setBlock(11,17,0,35,3)
mc.setBlock(12,17,0,35,3)
mc.setBlock(13,17,0,35,15)
mc.setBlock(-11,18,0,35,15)
mc.setBlock(-10,18,0,35,12)
mc.setBlock(-9,18,0,35,14)
mc.setBlock(-8,18,0,35,14)
mc.setBlock(-7,18,0,35,14)
mc.setBlock(-6,18,0,35,15)
mc.setBlock(-5,18,0,35,15)
mc.setBlock(-4,18,0,35,14)
mc.setBlock(-3,18,0,35,14)
mc.setBlock(-2,18,0,35,14)
mc.setBlock(-1,18,0,35,14)
mc.setBlock(0,18,0,35,14)
mc.setBlock(1,18,0,35,14)
mc.setBlock(2,18,0,35,14)
mc.setBlock(3,18,0,35,7)
mc.setBlock(4,18,0,35,2)
mc.setBlock(5,18,0,35,10)
mc.setBlock(6,18,0,35,1)
mc.setBlock(7,18,0,35,5)
mc.setBlock(8,18,0,35,15)
mc.setBlock(11,18,0,35,15)
mc.setBlock(12,18,0,35,15)
mc.setBlock(13,18,0,35,15)
mc.setBlock(-12,19,0,35,15)
mc.setBlock(-11,19,0,35,14)
mc.setBlock(-10,19,0,35,14)
mc.setBlock(-9,19,0,35,14)
mc.setBlock(-8,19,0,35,15)
mc.setBlock(-7,19,0,35,15)
mc.setBlock(-4,19,0,35,15)
mc.setBlock(-3,19,0,35,12)
mc.setBlock(-2,19,0,35,14)
mc.setBlock(-1,19,0,35,14)
mc.setBlock(0,19,0,35,14)
mc.setBlock(1,19,0,35,15)
mc.setBlock(2,19,0,35,15)
mc.setBlock(3,19,0,35,15)
mc.setBlock(4,19,0,35,2)
mc.setBlock(5,19,0,35,7)
mc.setBlock(6,19,0,35,1)
mc.setBlock(7,19,0,35,5)
mc.setBlock(8,19,0,35,15)
mc.setBlock(-11,20,0,35,15)
mc.setBlock(-10,20,0,35,15)
mc.setBlock(-9,20,0,35,15)
mc.setBlock(-4,20,0,35,15)
mc.setBlock(-3,20,0,35,14)
mc.setBlock(-2,20,0,35,14)
mc.setBlock(-1,20,0,35,14)
mc.setBlock(0,20,0,35,15)
mc.setBlock(3,20,0,35,15)
mc.setBlock(4,20,0,35,15)
mc.setBlock(5,20,0,35,1)
mc.setBlock(6,20,0,35,15)
mc.setBlock(7,20,0,35,5)
mc.setBlock(8,20,0,35,15)
mc.setBlock(-3,21,0,35,15)
mc.setBlock(-2,21,0,35,15)
mc.setBlock(-1,21,0,35,15)
mc.setBlock(5,21,0,35,15)
mc.setBlock(7,21,0,35,15)


mc.player.setPos(0,0,-15)


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
