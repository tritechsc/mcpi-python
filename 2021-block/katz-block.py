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

# Lay blocks flat on ground
mc.setBlock(0,0,0,35,0)
mc.setBlock(1,0,0,35,14)
mc.setBlock(2,0,0,35,0)
mc.setBlock(3,0,0,35,14)
mc.setBlock(4,0,0,35,0)
mc.setBlock(5,0,0,35,14)
mc.setBlock(6,0,0,35,0)
mc.setBlock(7,0,0,35,14)
mc.setBlock(8,0,0,35,0)
mc.setBlock(9,0,0,35,14)
mc.setBlock(10,0,0,35,0)
mc.setBlock(11,0,0,35,14)
mc.setBlock(12,0,0,35,0)
mc.setBlock(13,0,0,35,14)
mc.setBlock(14,0,0,35,0)
mc.setBlock(15,0,0,35,14)
mc.setBlock(16,0,0,35,0)
mc.setBlock(17,0,0,35,14)
mc.setBlock(18,0,0,35,0)
mc.setBlock(19,0,0,35,14)
mc.setBlock(20,0,0,35,0)
mc.setBlock(21,0,0,35,14)
mc.setBlock(22,0,0,35,0)
mc.setBlock(23,0,0,35,14)







#  Lay block in the air 

mc.setBlock(4,1,0,35,15) 
mc.setBlock(5,1,0,35,15)
mc.setBlock(6,1,0,35,15)
mc.setBlock(7,1,0,35,15)
mc.setBlock(8,1,0,35,15)
mc.setBlock(9,1,0,35,15)
mc.setBlock(10,1,0,35,15)
mc.setBlock(11,1,0,35,15)
mc.setBlock(12,1,0,35,15)
mc.setBlock(13,1,0,35,15)
mc.setBlock(14,2,0,35,15)
mc.setBlock(15,3,0,35,15)
mc.setBlock(16,4,0,35,15)
mc.setBlock(16,5,0,35,15)
mc.setBlock(16,6,0,35,15)
mc.setBlock(16,7,0,35,15)
mc.setBlock(16,8,0,35,15)
mc.setBlock(15,9,0,35,15)
mc.setBlock(15,10,0,35,15)
mc.setBlock(15,11,0,35,15)
mc.setBlock(15,12,0,35,15)
mc.setBlock(14,13,0,35,15)
mc.setBlock(13,13,0,35,15)
mc.setBlock(12,12,0,35,15)
mc.setBlock(11,11,0,35,15)
mc.setBlock(10,10,0,35,15)
mc.setBlock(9,10,0,35,15)
mc.setBlock(8,10,0,35,15)
mc.setBlock(7,10,0,35,15)
mc.setBlock(6,11,0,35,15)
mc.setBlock(5,12,0,35,15)
mc.setBlock(4,13,0,35,15)
mc.setBlock(3,13,0,35,15)
mc.setBlock(2,12,0,35,15)
mc.setBlock(2,11,0,35,15)
mc.setBlock(2,10,0,35,15)
mc.setBlock(2,9,0,35,15)
mc.setBlock(1,8,0,35,15)
mc.setBlock(1,7,0,35,15)
mc.setBlock(1,6,0,35,15)
mc.setBlock(1,5,0,35,15)
mc.setBlock(1,4,0,35,15)
mc.setBlock(2,3,0,35,15)
mc.setBlock(3,2,0,35,15)
mc.setBlock(8,3,0,35,15)
mc.setBlock(9,3,0,35,15)
mc.setBlock(10,3,0,35,15)
mc.setBlock(11,3,0,35,15)
mc.setBlock(7,3,0,35,15)
mc.setBlock(6,3,0,35,15)
mc.setBlock(5,3,0,35,15)
mc.setBlock(5,4,0,35,15)
mc.setBlock(11,4,0,35,15)
mc.setBlock(8,4,0,35,15)
mc.setBlock(7,6,0,35,15)
mc.setBlock(5,6,0,35,15)
mc.setBlock(4,6,0,35,15)
mc.setBlock(4,7,0,35,15)
mc.setBlock(11,6,0,35,15)
mc.setBlock(12,6,0,35,15)
mc.setBlock(11,7,0,35,15)
mc.setBlock(14,4,0,35,6)
mc.setBlock(13,4,0,35,6)
mc.setBlock(13,5,0,35,6)
mc.setBlock(14,5,0,35,6)
mc.setBlock(3,4,0,35,6)
mc.setBlock(2,4,0,35,6)
mc.setBlock(2,5,0,35,6)
mc.setBlock(3,5,0,35,6)

mc.player.setPos(10,6,-10)


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


mc.setBlock(0,0,5,35,0)     # WHITE   0,  0,  0
mc.setBlock(2,2,5,35,0)     # ORANGE  2,  0,  2
mc.setBlock(-2,2,5,35,0)    # PINK   -2,  0,  2
mc.setBlock(-2-2,5,35,0)    # BLUE   -2,  0, -2
mc.setBlock(2,-2,5,35,0)    # YELLOW  2,  0, -2
''' 