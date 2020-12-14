# Base project format.
# put this on the desktop : git clone https://github.com/tritechsc/mcpi-python

from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    x, y, z = mc.player.getPos()        
    return mc

def clear_with_air_up(mc, x, y, z,h,k,l):
    air = 0;
    mc.setBlocks(x-h,y,z-l,x+h,y+k,z+l,air)   

def clear_with_air_block(mc, x, y, z,h,k,l):
    air = 0;
    mc.setBlocks(x-h,y-k,z-l,x+h,y+k,z+l,air)   
    
def rocket(mc,x,y,z):
    xs,ys,zs = x,y,z
    
    #bottom
    for k in range (1,40):
        mc.setBlocks(x+1,y+k,z+2,x-1,y+k,z+2,35,0) #back
        mc.setBlocks(x+2,y+k,z-1,x+2,y+k,z+1,35,0) #left
        mc.setBlocks(x+1,y+k,z-2,x-1,y+k,z-2,35,0) #front
        mc.setBlocks(x-2,y+k,z-1,x-2,y+k,z+1,35,0) #right

    #top
    for k in range (39,65):
        mc.setBlocks(x+2,y+k,z+3,x-2,y+k,z+3,35,0) #back
        mc.setBlocks(x+2,y+k,z-2,x+3,y+k,z+2,35,0) #left
        mc.setBlocks(x+2,y+k,z-3,x-2,y+k,z-3,35,0) #front
        mc.setBlocks(x-3,y+k,z-2,x-3,y+k,z+2,35,0) #right
    #base    
    mc.setBlocks(xs+1,ys,zs-1,xs-1,ys+1,zs+1,35,15) 
    # top cone
    mc.setBlocks(xs+2,ys+63,zs-2,xs-2,ys+66,zs+2,35,0)
    mc.setBlock(xs,ys+67,zs,35,)
    
def booster(mc,x,y,z):
    xs,ys,zs = x,y,z
    
    #blocks
    for k in range (1,40):
        mc.setBlocks(x+1,y+k,z+2,x-1,y+k,z+2,35,0) #back
        mc.setBlocks(x+2,y+k,z-1,x+2,y+k,z+1,35,0) #left
        mc.setBlocks(x+1,y+k,z-2,x-1,y+k,z-2,35,0) #front
        mc.setBlocks(x-2,y+k,z-1,x-2,y+k,z+1,35,0) #right

        #base
        mc.setBlocks(xs+1,ys,zs-1,xs-1,ys+1,zs+1,35,15) #base
        #top
        mc.setBlocks(xs+1,ys+39,zs-1,xs-1,ys+40,zs+1,35,0)
        mc.setBlock(xs,ys+41,zs,35,)

def part2(mc,x,y,z,m):
    pass

def post3(mc,x,y,z,m):
    pass



    
def main():
    mc = init()
    x, y, z = mc.player.getPos()
    #clear air
    mc.player.setPos(0,0,0)
    mc.setBlocks(x-50,y,z-50,x+50,y+100,z+50,0)
    booster(mc,x-6,y,z)
    booster(mc,x+6,y,z)
    rocket(mc,x,y,z)
    mc.player.setPos(0,40,-5)


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
