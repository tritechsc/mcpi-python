from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
from random import randint
def init(): 
	# change 192.168.1.13 to 127.0.0.1 or your ip
	mc = Minecraft.create("127.0.0.1", 4711)
	x, y, z = mc.player.getPos()  
	return mc

#main  
def main():
	mc = init()
	#mc.player.setPos(0, 0, 0)
	x, y, z = mc.player.getPos()  
	mc.setBlocks(x-1, y, z+1, x+3, y+30, z+5, 4)
	mc.setBlock(x+1, y+0, z+1, 0)
	mc.setBlock(x+1, y+1, z+1, 0)
	mc.setBlocks(x+0, y, z+2, x+2, y+29, z+4, 0)
	mc.setBlock(x+1, y+1, z+5, 20)
	mc.setBlock(x+1, y+3, z+5, 20)
	mc.setBlock(x+1, y+5, z+5, 20)
	mc.setBlock(x+1, y+7, z+5, 20)
	mc.setBlock(x+1, y+9, z+5, 20)
	mc.setBlock(x+1, y+11, z+5, 20)
	mc.setBlock(x+1, y+13, z+5, 20)
	mc.setBlock(x+1, y+15, z+5, 20)
	mc.setBlock(x+1, y+17, z+5, 20)
	mc.setBlock(x+1, y+19, z+5, 20)
	mc.setBlock(x+1, y+21, z+5, 20)
	mc.setBlock(x+1, y+23, z+5, 20)
	mc.setBlock(x+1, y+25, z+5, 20)
	mc.setBlock(x+1, y+27, z+5, 20)
	mc.setBlock(x+1, y+29, z+5, 20)
	mc.setBlock(x-1, y+31, z+5, 50)
	mc.setBlock(x+3, y+31, z+1, 50)
	mc.setBlock(x-1, y+31, z+1, 50)
	mc.setBlock(x+3, y+31, z+5, 50)
	mc.setBlock(x+3, y+29, z+3, 20)
	mc.setBlock(x+3, y+27, z+3, 20)
	mc.setBlock(x+3, y+25, z+3, 20)
	mc.setBlock(x+3, y+23, z+3, 20)
	mc.setBlock(x+3, y+21, z+3, 20)
	mc.setBlock(x+3, y+19, z+3, 20)
	mc.setBlock(x+3, y+17, z+3, 20)
	mc.setBlock(x+3, y+15, z+3, 20)
	mc.setBlock(x+3, y+13, z+3, 20)
	mc.setBlock(x+3, y+11, z+3, 20)
	mc.setBlock(x+3, y+9, z+3, 20)
	mc.setBlock(x+3, y+7, z+3, 20)
	mc.setBlock(x+3, y+5, z+3, 20)
	mc.setBlock(x+3, y+3, z+3, 20)
	mc.setBlock(x+3, y+1, z+3, 20)
	mc.setBlock(x-1, y+29, z+3, 20)
	mc.setBlock(x-1, y+27, z+3, 20)
	mc.setBlock(x-1, y+25, z+3, 20)
	mc.setBlock(x-1, y+23, z+3, 20)
	mc.setBlock(x-1, y+21, z+3, 20)
	mc.setBlock(x-1, y+19, z+3, 20)
	mc.setBlock(x-1, y+17, z+3, 20)
	mc.setBlock(x-1, y+15, z+3, 20)
	mc.setBlock(x-1, y+13, z+3, 20)
	mc.setBlock(x-1, y+11, z+3, 20)
	mc.setBlock(x-1, y+9, z+3, 20)
	mc.setBlock(x-1, y+7, z+3, 20)
	mc.setBlock(x-1, y+5, z+3, 20)
	mc.setBlock(x-1, y+3, z+3, 20)
	mc.setBlock(x-1, y+1, z+3, 20)
	mc.setBlock(x+1, y+31, z+3, 17)
	mc.setBlock(x+1, y+32, z+3, 17)
	mc.setBlock(x+1, y+33, z+3, 17)
	mc.setBlock(x+1, y+34, z+3, 18)
	mc.setBlock(x+1, y+34, z+3, 18)
	mc.setBlock(x+2, y+34, z+3, 18)
	mc.setBlock(x+0, y+34, z+3, 18)
	mc.setBlock(x+1, y+34, z+3, 18)
	mc.setBlock(x+1, y+34, z+4, 18)
	mc.setBlock(x-0, y+34, z+4, 18)
	mc.setBlock(x+2, y+34, z+4, 18)
	mc.setBlock(x+2, y+34, z+2, 18)
	mc.setBlock(x+1, y+34, z+2, 18)
	mc.setBlock(x+0, y+34, z+2, 18)
	mc.setBlock(x+1, y+31, z+1, 50)
	mc.setBlock(x+1, y+31, z+5, 50)
	mc.setBlock(x-1, y+31, z+3, 50)
	mc.setBlock(x+3, y+31, z+3, 50)
	mc.setBlock(x+0, y+2, z+0, 50)
	mc.setBlock(x+2, y+2, z+0, 50)
	mc.setBlock(x+1, y+36, z+3, 18)
	mc.setBlock(x+2, y+36, z+3, 18)
	mc.setBlock(x+0, y+36, z+3, 18)
	mc.setBlock(x+1, y+36, z+3, 18)
	mc.setBlock(x+1, y+36, z+4, 18)
	mc.setBlock(x-0, y+36, z+4, 18)
	mc.setBlock(x+2, y+36, z+4, 18)
	mc.setBlock(x+2, y+36, z+2, 18)
	mc.setBlock(x+1, y+36, z+2, 18)
	mc.setBlock(x+0, y+36, z+2, 18)
	mc.setBlock(x+1, y+35, z+3, 18)
	mc.setBlock(x+2, y+35, z+3, 18)
	mc.setBlock(x+0, y+35, z+3, 18)
	mc.setBlock(x+1, y+35, z+3, 18)
	mc.setBlock(x+1, y+35, z+4, 18)
	mc.setBlock(x-0, y+35, z+4, 18)
	mc.setBlock(x+2, y+35, z+4, 18)
	mc.setBlock(x+2, y+35, z+2, 18)
	mc.setBlock(x+1, y+35, z+2, 18)
	mc.setBlock(x+1, y+35, z+2, 18)
	mc.setBlock(x+0, y+35, z+2, 18)
	
	for x in range(3, 5):
		x = 5



main()



While Loop


from mcpi.minecraft import Minecraft
from mcpi import block    
from time import sleep
from random import randint

def init(): 
    mc = Minecraft.create("127.0.0.1", 4711)
    x, y, z = mc.player.getPos()  
    return mc

def make_poles(mc,x,y,z,k,h):
        m = 41
        for n in range(0,k):
                if n > (k -2):
                        m = 10
                mc.setBlock(x, y+k,z,m,)

def main():
        mc = init()
        x, y, z = mc.player.getPos()  
        count = 0
        while count < 1000:
                x1 = randint(-100,100)
                z1 = randint(-100,100)
                h = randint(3,15)
                make_poles(mc,x1,0,z1,35, h%16)
                count = count + 1

main()



  
