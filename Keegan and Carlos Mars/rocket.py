from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init(): 
	# change 192.168.1.13 to 127.0.0.1 or your ip
	mc = Minecraft.create("10.183.4.122", 4711)
	x, y, z = mc.player.getPos()  
	return mc

#main  
def main():
	mc = Minecraft.create("10.183.4.122", 4711)
	mc = init()
	#mc.player.setPos(0, 0, 0)
	x, y, z = mc.player.getPos()				
	mc.postToChat("Houston we have a problem")
	# window
	mc.setBlock(-91.7,43.0,-17.6,20)
	mc.setBlock(-92.7,43.0,-17.6,20) 
	mc.setBlock(-90.7,43.0,-17.6,20) 
	mc.setBlock(-91.7,44.0,-17.6,20) 
	mc.setBlock(-92.7,44.0,-17.6,20) 
	mc.setBlock(-90.7,44.0,-17.6,20) 
	mc.setBlock(-91.4,45.0,-11.3,20) 
	# rocket fins
	mc.setBlock(-85.7,42.0,-14.5,35,14)  
	mc.setBlock(-86.7,42.0,-14.5,35,14) 
	mc.setBlock(-86.7,43.0,-14.5,35,14)  
	mc.setBlock(-87.7,42.0,-14.5,35,14) 
	mc.setBlock(-87.7,43.0,-14.5,35,14)  
	mc.setBlock(-87.7,44.0,-14.5,35,14)  
	mc.setBlock(-97.7,42.0,-14.5,35,14)   
	mc.setBlock(-96.7,42.0,-14.5,35,14)  
	mc.setBlock(-96.7,43.0,-14.5,35,14)    
	mc.setBlock(-95.7,42.0,-14.5,35,14)      
	mc.setBlock(-95.7,43.0,-14.5,35,14)   
	mc.setBlock(-95.7,44.0,-14.5,35,14)  
	# staircase  
	mc.setBlock(-91.5,40.0,-12.3,42) 
	mc.setBlock(-91.7,39.0,-13.3,42)     
	# light
	mc.setBlock(-91.7,46.2,-14.3,89) 
	# rocket nose
	mc.setBlock(-92.5,47,-12.7,35,14)
	mc.setBlock(-91.5,47,-12.7,35,14)
	mc.setBlock(-90.5,47,-12.7,35,14)
	mc.setBlock(-89.5,47,-14.3,35,14)
	mc.setBlock(-89.5,47,-15.7,35,14)
	mc.setBlock(-89.7,47,-13.7,35,14)
	mc.setBlock(-90.5,47,-16.3,35,14)
	mc.setBlock(-91.5,47,-16.3,35,14)
	mc.setBlock(-92.5,47,-16.3,35,14)
	mc.setBlock(-93.5,47,-15.3,35,14)
	mc.setBlock(-93.5,47,-14.3,35,14)
	mc.setBlock(-93.5,47,-13.3,35,14)
	mc.setBlock(-92.4,48,-15.6,35,14)
	mc.setBlock(-92.5,48,-14.3,35,14)
	mc.setBlock(-92.5,48,-13.3,35,14)
	mc.setBlock(-91.5,48,-13.3,35,14)
	mc.setBlock(-90.5,48,-13.7,35,14)
	mc.setBlock(-90.7,48,-14.8,35,14)
	mc.setBlock(-90.6,48,-15.3,35,14)
	mc.setBlock(-91.5,48,-15.3,35,14)
	mc.setBlock(-91.5,49,-14.3,35,14)
	# lighting inside the mars caves
	mc.setBlock(-91.7,22.0,3.7,89)
	mc.setBlock(-91.7,22.2,-32.3,89)
	mc.setBlock(-73.3,23.2,-14.3,89)
	mc.setBlock(-109.7,22.2,-14.3,89)
	#rocket interior 
	mc.setBlock(-93.6,39.2,-16.7,62)
	mc.setBlock(-93.7,39.2,-15.6,58)
	# air for shaping the roof of the rocket
	mc.setBlock(-94.4,46,-16.6,0) 
	mc.setBlock(-93.4,46,-17.6,0) 
	mc.setBlock(-89.4,46,-17.6,0) 
	mc.setBlock(-88.4,46,-16.6,0) 
	mc.setBlock(-88.4,46,-12.6,0) 
	mc.setBlock(-89.4,46,-11.6,0) 
	mc.setBlock(-93.4,46,-11.6,0) 
	mc.setBlock(-94.4,46,-12.6,0) 
	
	sphere(mc,-92,22,-15,10,10,10,79)	
	
def sphere(mc,px,py,pz,X,Y,Z,block):
	for x in range(-X,X):
		for y in range(-Y,Y):
			for z in range(-Z,Z):
				if ((x/X)**2)+((y/Y)**2)+((z/Z)**2)<1:
					mc.setBlock(px+x,py+y,pz+z,block)

main()
