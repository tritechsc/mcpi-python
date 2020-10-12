from mcpi.minecraft import Minecraft
from mcpi import block	  

mc = Minecraft.create()

mc.postToChat("Hello world")
x, y, z = mc.player.getTilePos()                                                  
#x, y, z = mc.player.getPos()

mc.postToChat("LEAVES")
mc.setBlock(x+1, y, z, 18)
mc.postToChat("WOOD")
mc.setBlock(x, y+1, z, 17)
mc.postToChat("COAL_ORE")
mc.setBlock(x, y, z+1, 16)

#COAL_ORE             16
#WOOD                 17
#LEAVES               18
