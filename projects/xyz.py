from mcpi.minecraft import Minecraft
from mcpi import block	  

mc = Minecraft.create()
                                            
x, y, z = mc.player.getPos()  
zz = z + 1

mc.setBlock(x,y, zz, block.IRON_BLOCK.id)
mc.setBlock(x,y+1,zz, block.SANDSTONE	.id)
mc.setBlock(x,y+2,zz, block.GOLD_ORE.id)
mc.setBlock(x,y+3,zz, block.STONE.id)
