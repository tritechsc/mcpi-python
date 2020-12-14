# mcpi-python

Minecraft Python on the Raspberry Pi
Your can clone this version of Minecraft Pi to un on your Desktop
https://github.com/tritechsc/mcpi-app
<hr />
This repository is for using Minecraft to teach and experiment with coding in Python and Networking.

https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/

https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/worksheet/

http://www.stuffaboutcode.com/p/minecraft-api-reference.html

##Screenshots: cd ~/ ;git clone https://github.com/AndrewFromMelbourne/raspi2png;
curl -sL https://raw.githubusercontent.com/AndrewFromMelbourne/raspi2png/master/installer.sh | bash -
Select and copy then pase in tty
<pre>
Partlist:
- Raspberry Pi
- Class 10 mini sd card.
- hdmi cable to hdmi minitor
- Minitor or TV with hdmi 
- Keyboard
- Mouse
<hr />
Python Scripts Created by:
Julian
Nathan
Evan
Grant
Kevin
Brenden

Craig Coleman


API Blocks
=======================
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

Some of the blocks that appear in the inventory screen aren’t listed but here they are :

Non-API Blocks
=======================
PAINTING            321
STONE_STAIRS         67
OAK_STAIRS           53
OAK_STAIRS           59
NETHERRACK           87
TRAPDOOR             96
MELON_SEEDS         105
BRICK_STAIRS        108
SANDSTONE_STAIRS    128
STONE_BRICK_STAIRS  109
NETHER_BRICK        112
NETHER_BRICK_STAIRS 114
QUARTZ_BLOCK        155
QUARTZ_STAIRS       156
STONE_CUTTER        245
BONE_MEAL           351

If you have imported the “block” library at the top of your script like this :

import mcpi.block as block

you can call up the blocks in the “API Block List” using the following syntax :

block.MELON.id

=======================
wool 35,0  WHITE
wool 35,1  ORGANE
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


</pre>
