################# The getHeight function #################
def getHeight(heightArray):
    for x in range(-128,128):
        for z in range(-128,128):
        # scanert world and fill empty array #
            heightArray.append(mc.getHeight(x, z))
#####################################################
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create("127.0.0.1", 4711)
heightArray = [] # initinalize an empty array #
getHeight(heightArray) # call function and pass empty array as funct argument #
globalMax = max(heightArray)
mc.postToChat("This Minecraft World's highest point is : %s" % (globalMax))
print (globalMax)
