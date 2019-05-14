#Juan Barraza
mc = Minecraft.create("10.183.0.2", 4711)
from mcpi.minecraft import Minecraft
from mcpi import block    

mc = Minecraft.create()
                                            
x, y, z = mc.player.getPos()  
zz = z + 1

mc.setBlock(x,y, zz, 7)
mc.setBlock(x+1,y,zz, 7)
mc.setBlock(x+2,y,zz, 7)
mc.setBlock(x+3,y,zz, 7)
mc.setBlock(x+4,y,zz, 7)
mc.setBlock(x-1,y,zz, 7)
mc.setBlock(x-2,y,zz, 7)
mc.setBlock(x-3,y,zz, 7)
mc.setBlock(x-4,y,zz, 7)
mc.setBlock(x-4,y,zz+1, 7)
mc.setBlock(x-4,y,zz+2, 7)
mc.setBlock(x-4,y,zz+3, 7)
mc.setBlock(x-4,y,zz+4, 7)
mc.setBlock(x-4,y,zz+5, 7)
mc.setBlock(x-4,y,zz+6, 7)
mc.setBlock(x+4,y,zz+1, 7)
mc.setBlock(x+4,y,zz+2, 7)
mc.setBlock(x+4,y,zz+3, 7)
mc.setBlock(x+4,y,zz+4, 7)
mc.setBlock(x+4,y,zz+5, 7)
mc.setBlock(x+4,y,zz+6, 7)
mc.setBlock(x,y,zz+6, 7)

#Side Walls
mc.setBlock(x+1,y,zz+6, 7)
mc.setBlock(x+2,y,zz+6, 7)
mc.setBlock(x+3,y,zz+6, 7)
mc.setBlock(x+4,y,zz+6, 7)
mc.setBlock(x-1,y,zz+6, 7)
mc.setBlock(x-2,y,zz+6, 7)
mc.setBlock(x-3,y,zz+6, 7)
mc.setBlock(x-4,y,zz+6, 7)
mc.setBlock(x-3,y,zz+1, 7)
mc.setBlock(x-3,y,zz+2, 7)
mc.setBlock(x-3,y,zz+3, 7)
mc.setBlock(x-3,y,zz+4, 7)
mc.setBlock(x-3,y,zz+5, 7)
mc.setBlock(x-2,y,zz+1, 7)
mc.setBlock(x-2,y,zz+2, 7)
mc.setBlock(x-2,y,zz+3, 7)
mc.setBlock(x-2,y,zz+4, 7)
mc.setBlock(x-2,y,zz+5, 7)
mc.setBlock(x-1,y,zz+1, 7)
mc.setBlock(x-1,y,zz+2, 7)
mc.setBlock(x-1,y,zz+3, 7)
mc.setBlock(x-1,y,zz+4, 7)
mc.setBlock(x-1,y,zz+5, 7)
mc.setBlock(x,y,zz+1, 7)
mc.setBlock(x,y,zz+2, 7)
mc.setBlock(x,y,zz+3, 7)
mc.setBlock(x,y,zz+4, 7)
mc.setBlock(x,y,zz+5, 7)
mc.setBlock(x+1,y,zz+1, 7)
mc.setBlock(x+1,y,zz+2, 7)
mc.setBlock(x+1,y,zz+3, 7)
mc.setBlock(x+1,y,zz+4, 7)
mc.setBlock(x+1,y,zz+5, 7)
mc.setBlock(x+2,y,zz+1, 7)
mc.setBlock(x+2,y,zz+2, 7)
mc.setBlock(x+2,y,zz+3, 7)
mc.setBlock(x+2,y,zz+4, 7)
mc.setBlock(x+2,y,zz+5, 7)
mc.setBlock(x+3,y,zz+1, 7)
mc.setBlock(x+3,y,zz+2, 7)
mc.setBlock(x+3,y,zz+3, 7)
mc.setBlock(x+3,y,zz+4, 7)
mc.setBlock(x+3,y,zz+5, 7)

#Corner Towers
mc.setBlock(x-4, y+1,zz, 7)
mc.setBlock(x-4, y+2,zz, 7)
mc.setBlock(x-4, y+3,zz, 7)
mc.setBlock(x-4, y+4,zz, 7)
mc.setBlock(x-4, y+5,zz, 7)
mc.setBlock(x+4, y+1,zz, 7)
mc.setBlock(x+4, y+2,zz, 7)
mc.setBlock(x+4, y+3,zz, 7)
mc.setBlock(x+4, y+5,zz, 7)
mc.setBlock(x-4, y+1,zz+1, 7)
mc.setBlock(x-4, y+1,zz+2, 7)
mc.setBlock(x-4, y+1,zz+3, 7)
mc.setBlock(x-4, y+1,zz+4, 7)
mc.setBlock(x-4, y+1,zz+5, 7)
mc.setBlock(x-4, y+1,zz+6, 7)
mc.setBlock(x+4, y+1,zz+1, 7)
mc.setBlock(x+4, y+1,zz+2, 7)
mc.setBlock(x+4, y+1,zz+3, 7)
mc.setBlock(x+4, y+1,zz+4, 7)
mc.setBlock(x+4, y+1,zz+5, 7)
mc.setBlock(x+4, y+1,zz+6, 7)
mc.setBlock(x+4, y+2,zz+6, 7)
mc.setBlock(x+4, y+3,zz+6, 7)
mc.setBlock(x+4, y+4,zz+6, 7)
mc.setBlock(x+4, y+5,zz+6, 7)
mc.setBlock(x-4, y+2,zz+6, 7)
mc.setBlock(x-4, y+3,zz+6, 7)
mc.setBlock(x-4, y+4,zz+6, 7)
mc.setBlock(x-4, y+5,zz+6, 7)

#tower connecters
mc.setBlock(x-3, y+4,zz+6, 7)
mc.setBlock(x-2, y+4,zz+6, 7)
mc.setBlock(x-1, y+4,zz+6, 7)
mc.setBlock(x, y+4,zz+6, 7)
mc.setBlock(x+3, y+4,zz+6, 7)
mc.setBlock(x+2, y+4,zz+6, 7)
mc.setBlock(x+1, y+4,zz+6, 7)
mc.setBlock(x+4, y+4,zz+1, 7)
mc.setBlock(x+4, y+4,zz+2, 7)
mc.setBlock(x+4, y+4,zz+3, 7)
mc.setBlock(x+4, y+4,zz+4, 7)
mc.setBlock(x+4, y+4,zz+5, 7)
mc.setBlock(x-4, y+4,zz+1, 7)
mc.setBlock(x-4, y+4,zz+2, 7)
mc.setBlock(x-4, y+4,zz+3, 7)
mc.setBlock(x-4, y+4,zz+4, 7)
mc.setBlock(x-4, y+4,zz+5, 7)
mc.setBlock(x+4, y+4,zz, 7)
mc.setBlock(x+3, y+4,zz, 7)
mc.setBlock(x+2, y+4,zz, 7)
mc.setBlock(x+1, y+4,zz, 7)
mc.setBlock(x, y+4,zz, 7)
mc.setBlock(x-4, y+4,zz, 7)
mc.setBlock(x-3, y+4,zz, 7)
mc.setBlock(x-2, y+4,zz, 7)
mc.setBlock(x-1, y+4,zz, 7)

#Walls and Glass
mc.setBlock(x, y+1, zz+6, 7)
mc.setBlock(x+1, y+1, zz+6, 7)
mc.setBlock(x+2, y+1, zz+6, 7)
mc.setBlock(x+3, y+1, zz+6, 7)
mc.setBlock(x+4, y+1, zz+6, 7)
mc.setBlock(x-1, y+1, zz+6, 7)
mc.setBlock(x-2, y+1, zz+6, 7)
mc.setBlock(x-3, y+1, zz+6, 7)
mc.setBlock(x-4, y+1, zz+6, 7)
mc.setBlock(x-4, y+1, zz+6, 7)



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
