#Made in conjunction with Craig Coleman, and Kevin Forrister
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init(): 
    mc = Minecraft.create("127.0.0.1", 4711)
    x, y, z = mc.player.getPos()  
    return mc

def clear_with_air(mc, x, y, z):
    air = 0
    mc.setBlocks(x-50, y-10, z, x+60, y+50, z+50, air) 

def fin_a(mc,x,y,z):
    wool = 35,14
    #mc.setBlocks(x, y-1, z+21, x, y-1, z+22, wool)
    #mc.setBlock(x, y-2, z+20, wool)
    #mc.setBlocks(x-1, y-2, z+21, x+1, y-2, z+21, wool)
    #mc.setBlocks(x-1, y-2, z+22, x+1, y-2, z+22, wool)
    #mc.setBlocks(x-1, y-3, z+21, x+1, y-3, z+21, wool)
    #mc.setBlocks(x-1, y-3, z+22, x+1, y-3, z+22, wool)
    
def fin_b(mc,x,y,z):  # down fin
    iron = 35,8
    mc.setBlock(x, y, z+2, iron)
    mc.setBlock(x, y-1, z+2, iron)
    mc.setBlock(x, y-2, z+1, iron)
    mc.setBlocks(x-1, y-2, z+2, x+1, y-2, z+2, iron)
    
def fin_c(mc,x,y,z):  # down fin
    iron = 35,8
    mc.setBlock(x, y, z+2, iron)
    mc.setBlock(x, y+1, z+2, iron)
    mc.setBlock(x, y+2, z+1, iron)
    mc.setBlocks(x-1, y+2, z+2, x+1, y+2, z+2, iron)

def bridge(mc,x,y,z):
    wool = 35,14
    iron   =  35,8
    wool2 = 35,15
    air = 0
    redstone = 73
    glass = 102
    #base
    mc.setBlocks(x-2, y, z, x+2, y+5, z+5, wool2)
    #cab
    mc.setBlocks(x-2, y+6, z, x+2, y+10, z+5, wool2)
    #clear space for windows
    #mc.setBlocks(x-1, y+1, z+1, x+1, y+6, z+5, air)
    mc.setBlocks(x-3, y, z+2, x+3, y+9, z+2, air)
    mc.setBlocks(x-1, y, z-2, x+1, y+9, z+7,air)
    mc.setBlocks(x-1, y, z, x+1, y+9, z, glass)
    mc.setBlocks(x-2, y, z+1, x-2, y+9, z+1,glass)
    mc.setBlocks(x-2, y, z+2, x-2, y+9, z+2,glass)
    mc.setBlocks(x-2, y, z+3, x-2, y+9, z+3,glass)
    mc.setBlocks(x-2, y, z+4, x-2, y+9, z+4,glass)
    mc.setBlocks(x+2, y, z+1, x+2, y+9, z+1,glass)
    mc.setBlocks(x+2, y, z+2, x+2, y+9, z+2,glass)
    mc.setBlocks(x+2, y, z+3, x+2, y+9, z+3,glass)
    mc.setBlocks(x+2, y, z+4, x+2, y+9, z+4,glass)
    #an
    mc.setBlocks(x-1,y, z+7, x+1, y+12, z+9,wool)
    mc.setBlocks(x-2,y+10, z-3, x+2, y+10, z+5,wool2)
    
def boat (mc, x, y, z):
    #wool_BLOCK 35,14 IRON_BLOCK  35,7  wool_block2  35,15
    wool_block = 35,14
    iron_block = 35,8
    wool_block2 = 35,15
    air = 0
    mc.setBlocks(x, y, z+2, x, y, z+48, wool_block) # 0  46 ROW 0
    mc.setBlocks(x, y+1, z+1, x, y+1, z+47, wool_block) # 1   46 ROW 1
    mc.setBlocks(x+1, y+1, z+3, x-1, y+1, z+44, wool_block) # 1    ROW 1
    mc.setBlocks(x, y+2, z+4, x, y+2, z+50, iron_block)  # 2  48 ROW 2
    mc.setBlocks(x, y+3, z+3, x, y+3, z+50, iron_block)  # 3  49 ROW 3
    mc.setBlocks(x-1, y+3, z+4, x+1, y+3, z+52, iron_block)  # 3  49 ROW 3
    mc.setBlocks(x, y+4, z+2, x, y+4, z+52, iron_block)  # 4 52
    mc.setBlocks(x-2, y+4, z+3, x+2, y+4, z+52, iron_block)  # 4 52
    mc.setBlocks(x, y+5, z+1, x, y+5, z+8, iron_block)  # 5 
    mc.setBlocks(x-2, y+5, z+3, x+2, y+5, z+8, iron_block)  # 5 
    mc.setBlocks(x, y+6, z, x, y+6, z+6, iron_block)  # 6
    mc.setBlocks(x-2, y+6, z+2, x+2, y+6, z+6, iron_block)  # 6
    mc.setBlock(x-2,y+6,z+2, air)
    mc.setBlock(x+2,y+6,z+2, air)
    mc.setBlock(x-2,y+5,z+3, air)
    mc.setBlock(x+2,y+5,z+3, air)
    mc.setBlock(x-2,y+4,z+3, air)
    mc.setBlock(x+2,y+4,z+3, air)
    mc.setBlock(x-2,y+4,z+4, air)
    mc.setBlock(x+2,y+4,z+4, air)
#main  
def main():  
    mc = init()
    mc.player.setPos(0, 30, 0)
    x, y, z = mc.player.getPos()  
    mc.player.setPos(x-30, y, z+30)
    clear_with_air(mc, x,y,z)
    boat(mc, x,y,z)
    fin_a(mc,x,y,z)
    fin_b(mc,x,y+2,z+50)
    fin_c(mc,x,y+5,z+50)
    bridge(mc,x,y+5,z+20)
    #mc.player.setPos(-17,30, 20)
    #mc.player.setPos(-5,21, -3)
    #mc.player.setPos(-17,35,23)
    #mc.player.setPos(0,35,23)

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
redwool              35,14
blackwool            35,15
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

