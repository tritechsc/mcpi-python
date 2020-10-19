#!/usr/bin/env python3
# Base project format.
# while loop example
from mcpi.minecraft import Minecraft
from mcpi import block

ip = "127.0.0.1"
mc = Minecraft.create(ip, 4711)
mc.player.setPos(0,0,0)
mc.setBlocks(-127,0,-127,128,64,128,0)

mc.player.setPos(0,0,0)
x,y,z = 0,0,0
color = 0

# loop 1 * * * * * * * *
count = 0
while(count < 10):
	mc.setBlock(x, y+1, z+count,35,color)
	# 35,color set the wool color
	color = color + 1
	count = count + 1
# end while loop

# loop 2 * * * * * * * *
count = 0
while(count < 10):
	mc.setBlock(x+1, y+1, z+count,35,color)
	# 35,color set the wool color
	color = color + 1
	count = count + 1
# end while loop

# loop 3 * * * * * * * *
count = 0
while(count < 10):
	mc.setBlock(x+2, y+1, z+count,35,color)
	# 35,color set the wool color
	color = color + 1
	count = count + 1
# end while loop

# add 7 more loop blocks

mc.player.setPos(0,20,0)
'''
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
'''



