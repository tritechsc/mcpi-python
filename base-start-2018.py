# Base project format.
# put this on the desktop : git clone https://github.com/tritechsc/mcpi
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    x, y, z = mc.player.getPos()		
    return mc

def clear_with_air_up(mc, x, y, z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y,z,x+h,y+k,z+l,air)	

def clear_with_air_block(mc, x, y, z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y-k,z-l,x+h,y+k,z+l,air)	
	
def core(mc,x,y,z,m):
	pass

def engine(mc,x,y,z,m):
	pass

def posta(mc,x,y,z,m):
	pass

def postb(mc,x,y,z,m):
	pass

def layer (mc, x, y, z, s ,e,w, m):
	# s start , e end m material  , w width m material 
	w = int(w/2)
	print("w ",w)
	mc.setBlocks(x-w,y,z+s,x+w,y,z+e-1,m)

def body(mc,x, y, z):
	clear_with_air_up(mc, x, y, z,5,7,15)
	s,e,w = 0,11,5
	layer(mc, x,y,z+2,s,e,w,42)
	y  = y + 1; s,e,w = 0,11,7
	layer(mc, x,y,z+2,s,e,w,42)
	
def main():
	mc = init()
	#mc.player.setPos(0, 50, 0)
	# x, y, z = mc.player.getPos()
	# mc.player.setPos(x, y, z)
	x, y, z = mc.player.getPos()
	print("position ",x,y,z)
	#clear_with_air(mc,x,y,s,e,k,l)
	# s start, e end , w width
	s,e,w = 0,11,5
	body(mc, x,y,z)
	#posta(mc, x,y-5,z+4,42)
	#core(mc,x,y-7,z,42)
	#postb(mc,x,y-4,z+15,42)
	#engine(mc,x-5,y,z+15,42)
	#mc.player.setPos(0,70,0)

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
