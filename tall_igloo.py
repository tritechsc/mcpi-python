
from mcpi.minecraft import Minecraft
from math import ceil

def sphere(mc,px,py,pz,X,Y,Z,block,*extradata):
 edata=list(extradata)
 exdata=[0,0,0,0,1,0]
 for i in range(len(edata)):
  exdata[i]=edata[i]
 bdata=exdata[0]
 hX=exdata[1]
 hY=exdata[2]
 hZ=exdata[3]
 tdist=exdata[4]
 taxis=exdata[5]
 limits=[-int(X),-int(Y),-int(Z),int(X),int(Y),int(Z)]
 limits[taxis]=int(limits[taxis]*2*tdist-limits[taxis])
 for x in range(limits[0],limits[3]):
  for y in range(limits[1],limits[4]):
   for z in range(limits[2],limits[5]):
    if ((x/X)**2)+((y/Y)**2)+((z/Z)**2)<1 and (((x/hX)**2)+((y/hY)**2)+((z/hZ)**2)>1 or abs(x)==hX or abs(y)==hY or abs(z)==hZ):
     mc.setBlock(px+x,py+y,pz+z,block,bdata)

def cylinder(mc,px,py,pz,X,Y,Z,axis,block):
 if axis%3==0:
  for x in range(-int(X),int(X)):
   for y in range(-int(Y),int(Y)):
    if ((x/X)**2)+((y/Y)**2)<1:
     mc.setBlocks(px+x,py+y,pz-Z,px+x,py+y,pz+Z,block)
 elif axis%3==1:
  for x in range(-int(X),int(X)):
   for z in range(-int(Z),int(Z)):
    if ((x/X)**2)+((z/Z)**2)<1:
     mc.setBlocks(px+x,py-Y,pz+z,px+x,py+Y,pz+z,block)
 elif axis%3==2:
  for y in range(-int(Y),int(Y)):
   for z in range(-int(Z),int(Z)):
    if ((y/Y)**2)+((z/Z)**2)<1:
     mc.setBlocks(px-X,py+y,pz+z,px+X,py+y,pz+z,block)

def main(place):
 mc=Minecraft.create(place,4711)
 x,y,z=mc.player.getPos()
 mc.setBlocks(x-5,y,z-20,x+5,y+5,z-8,0)
 sphere(mc,x,y,z-15,5,5,5,80,0,4,4,4,0.5,1)
 cylinder(mc,x,y,z-10,3,3,1,shapes.XY,80)
 cylinder(mc,x,y,z-10,2,2,1,shapes.XY,0)
 height=0
 nx,ny,nz=x,y-1,z-15
 clear=True
 while clear:
  height+=1
  clearpos=0
  pos=[(0,0),(5,5),(-5,5),(-5,-5),(5,-5)]
  for xmod,zmod in pos:
   if mc.getBlock(xmod+nx,ny-height,zmod+nz) in [0,8,9,10,11,31,37,38,39,40,65,78,102,107,]:
    clearpos+=1
  if clearpos==0:
   clear=False
 shapes.cylinder(mc,x,y-1-ceil(height/2),z-15,5,ceil(height/2),5,shapes.XZ,80)
 mc.setBlocks(x-2,y-1-height,z-11,x+2,y-1,z-9,80)
 #mc.setBlocks(x-5,y-1,z-20,x+5,y-1,z-8,80)

if __name__=='__main__':
 main("127.0.0.1")
