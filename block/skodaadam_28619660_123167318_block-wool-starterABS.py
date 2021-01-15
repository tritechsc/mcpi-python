from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
# set player to 0,0,0
mc.player.setPos(-9,0,14)
# CLEAR AN AREA WITH AIR TO BUILD
air = 0
mc.setBlocks(-24,0,-36,24,64,36,air) # clear some air                                               
x, y, z = mc.player.getPos()
xyzString = str(x)+" , "+str(y)+" , "+str(z)
print(xyzString)
# mc.setBlock (x,y,z, material_number) 

# Lay blocks flat on ground
mc.setBlock(0,0,0,35,0) 	# WHITE   0,  0,  0
mc.setBlock(1,0,1,35,1) 	# ORANGE  2,  0,  2
mc.setBlock(-1,0,1,35,6) 	# PINK   -2,  0,  2
mc.setBlock(-1,0,-1,35,3) 	# BLUE   -2,  0, -2
mc.setBlock(1,0,-1,35,4)  	# YELLOW  2,  0, -2
mc.setBlock(1,1,1,35,2)		# PURPLE
mc.setBlock(3,2,2,35,4)		# YELLOW
mc.setBlock(5,4,5,35,2)		# PURPLE
mc.setBlock(8,5,8,35,2)		# PURPLE


#  Lay block in the air 
mc.setBlock(0,2,2,35,0) 	# WHITE   0,  0,  0
mc.setBlock(1,3,2,35,1) 	# ORANGE  2,  0,  2
mc.setBlock(-1,3,2,35,6) 	# PINK   -2,  0,  2
mc.setBlock(-1,1,2,35,3) 	# BLUE   -2,  0, -2
mc.setBlock(1,1,2,35,4)  	# YELLOW  2,  0, -2
mc.setBlock(1,1,5,35,3)  	# BLUE 
mc.setBlock(1,0,4,35,3)  	# BLUE   

mc.player.setPos(0,0,-5)