from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
# set player to 0,0,0
mc.player.setPos(0,0,0)
# CLEAR AN AREA WITH AIR TO BUILD
air = 0
mc.setBlocks(-19,-1,-19,19,64,19,air) # clear some air                                               
x, y, z = mc.player.getPos()
xyzString = str(x)+" , "+str(y)+" , "+str(z)
print(xyzString)
# mc.setBlock (x,y,z, material_number) 

#  Lay block in the air
mc.setBlock(2,1,2,15)
mc.setBlock(2,2,2,1)
mc.setBlock(2,3,2,2)
mc.setBlock(2,4,2,3)
mc.setBlock(2,5,2,4)
#1
mc.setBlock(2,6,2,5)
mc.setBlock(2,7,2,7)
mc.setBlock(2,8,2,14)
mc.setBlock(2,9,2,15)
mc.setBlock(2,10,2,16)
#2
mc.setBlock(3,1,2,17)
mc.setBlock(3,2,2,18)
mc.setBlock(3,3,2,19)
mc.setBlock(3,4,2,20)
mc.setBlock(3,5,2,21)
#3
mc.setBlock(3,6,2,24)
mc.setBlock(3,7,2,30)
mc.setBlock(3,8,2,35)
mc.setBlock(3,9,2,41)
mc.setBlock(3,10,2,42)
#4
mc.setBlock(4,1,2,43)
mc.setBlock(4,2,2,44)
mc.setBlock(4,3,2,45)
mc.setBlock(4,4,2,46)
mc.setBlock(4,5,2,47)
#5
mc.setBlock(4,6,2,48)
mc.setBlock(4,7,2,49)
mc.setBlock(4,8,2,53)
mc.setBlock(4,9,2,54)
mc.setBlock(4,10,2,55)









mc.player.setPos(0,0,0)


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
#   IRON_BLOCK           42#
#   STONE_SLAB_DOUBLE    43
#   STONE_SLAB           44
#   BRICK_BLOCK          45
#   TNT                  46
#   BOOKSHELF            47
#   MOSS_STONE           48
#   OBSIDIAN             49#
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
