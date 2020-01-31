# Cyber Minecraft Pi Project
# Base project format.
# Documentation https://github.com/raspberrypilearning/getting-started-with-minecraft-pi/blob/master/worksheet.md
# Use the following format to create a Minecraft object that looks like something we see in the world or universe.
# You can not use any pre-existing project code in the "project" directory. 
#   ( https://github.com/tritechsc/mcpi-python/tree/master/projects)
# Communicate what you are making prior to starting with Mr. Coleman
# Use 5 total functions. One of the functions may clear the area with air.
# Use 1 or more mc.setBlock(x,y, z, block.IRON_BLOCK.id) commands.
# wool = 35; n = 5 (This is an example of how to use wool.)
# Use 1 or more mc.setBlocks(x,y, z,h,k,l, wool,n) commands.
# Use 1 for loop, 1 while loop and 1 if condition.
# Change the skin your your char.png in your ~/Desktop/mcpi-1234567 directory using gimp.
# Then export the file as a char.png
# Example char-turtle-DON.xcf  will be exported as char.png
# Upload your gimp file 
# Example /home/pi/Desktop/mcpi-icebowl/data/images/mob  (icebowl is my 7 character name)
# Code must be posted somewhere on your github site.
# Modify mincraft-pi to display a unique 7 charater name as follows:
'''copy minecraft-pi to a location to edit cp -fR mcpi-app mcpi-1234567
hexdump -ve '1/1 "%.2X"' minecraft-pi > mcpi.txt;
sed -i "s/53746576655069/496365426f776c/g" mcpi.txt;
xxd -r -p mcpi.txt > minecraft-pi.bin;
cp minecraft-pi.bin minecraft-pi;
chown pi:pi minecraft-pi;
'''
# Modify p3-mcpi-start.sh or p4-mcpi-start.sh so it works with your unique mcpi-1234567 directory
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    ipString = "192.168.1.73"
    #mc = Minecraft.create("127.0.0.1", 4711)
    mc = Minecraft.create(ipString, 4711)
    mc.setting("world_immutable",True)
    #x, y, z = mc.player.getPos()        
    return mc

def one(mc,x,y,z):
    print("FUNCTION ONE")
    mc.setBlock(x,y, z, block.IRON_BLOCK.id)

def two(mc,x,y,z):
    print("FUNCTION TWO")
    mc.setBlocks(x-10,y,z+1,x+10,y+10,z+1+10,35,7)
def three(mc,x,y,z):
    print("FUNCTION THREE")
    mc.setBlocks(x-10,y,z+1,x+10,y+10,z+1+10,35,3)
    mc.setBlocks(x-10,y,z+1,x+10,y+10,z+1+10,35,9)
    
def main():
    mc = init()
    x,y,z = mc.player.getPos()
    mc.player.setPos(x,y,z)
    one(mc,x,y,z)
    two(mc,x,y+5,z)
    three(mc,x,y+10,z)

if __name__ == "__main__":
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
