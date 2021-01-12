from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import random

def init():
    ip = "127.0.0.1"
    mc = Minecraft.create(ip, 4711)
    mc.setting("world_immutable",True)
    x, y, z = mc.player.getPos()        
    return mc
    
def clearAir(mc,x,y,z):
  mc.setBlocks(x,y,z,x+10,y+10,z+10,0)

def matrix(mc,x,y,z):
  
  X = ["0004444400",
  "0044444440",
  "0444444444",
  "4444444000",
  "4444000000",
  "4444444000",
  "0444444444",
  "0044444440",
  "0004444400",
  "0000000000"]
      #"123456789A"
 
  y1 = 10
  for h in range (0,10):
    x1 = 10
    for k  in range (0,10):
      print(X[h][k],end="") # debug
      #print(h,k," ",end="")
      theBlock = X[h][k]
      c = 0  # wool 35,0  WHITE
      if (theBlock == "1"):
        c = 1 # wool 35,1  ORANGE
      if (theBlock == "2"):
        c = 2 # wool 35,2  DARK PINK 
      if (theBlock == "3"):
        c = 3 # wool 35,3  LIGHT BLUE 
      if (theBlock == "4"):
        c = 4 # wool 35,4  YELLOW
      if (theBlock == "5"):
        c = 5 # wool 35,5  GREEN
      mc.setBlock(x1-x,y1+y,z,35,c)
      x1 = x1 - 1
    y1 = y1 - 1
    print()
    
def main():
  mc = init()
  x,y,z = mc.player.getPos()
  clearAir(mc,x,y,z)
  matrix(mc,x,y,z)
  mc.player.setPos(x,y,z-5)

if __name__ == "__main__":
  main()

'''
PACMAN

  "0004444400",
  "0044444440",
  "0444444444",
  "4444444000",
  "4444000000",
  "4444444000",
  "0444444444",
  "0044444440",
  "0004444400"

'''
