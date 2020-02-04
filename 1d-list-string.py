# Base project format.
# Documentation https://github.com/raspberrypilearning/getting-started-with-minecraft-pi/blob/master/worksheet.md
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    #ip = "192.168.7.84"
    ip = "127.0.0.1"
    mc = Minecraft.create(ip, 4711)
    #mc.setting("world_immutable",True)
    #x, y, z = mc.player.getPos()        
    return mc
    
def clearAir(mc,x,y,z):
    mc.setBlocks(x-10,y-5,z-20,x+10,y+20,z+20,0)
    
def output2d(mc,mList,x,y,z):
     for k in range (0,10):
        for l  in range (0,10):
            #print(mList[k][l],end="")
            theBlock = mList[k][l]
            if (theBlock == "1"):
                theBlock = 79
            if (theBlock == "0"):
                theBlock = 1
            mc.setBlock(x,9+y-k,z+l,35,theBlock)
    #print()

def main():
  CLR = ["0000000000",
          "0000000000",
          "0000000000",
          "0000000000",
          "0000000000",
          "0000000000",
          "0000000000",
          "0000000000",
          "0000000000",
          "0000000000"]
          
  L =["0011000000",
         "0011111100",
         "0011001100",
         "0011001100",
         "0011001100",
         "0011001100",
         "0011001100",
         "0011001100",
         "0011111100",
         "0011111000"]
         
  D = ["0011111000",
         "0011111100",
         "0011001100",
         "0011001100",
         "0011001100",
         "0011001100",
         "0011001100",
         "0011001100",
         "0011111100",
         "0011111000"]
         
  I =  ["0011111100",
          "0011111100",
          "0000110000",
          "0000110000",
          "0000110000",
          "0000110000",
          "0000110000",
          "0000110000",
          "0011111100",
          "0011111100"]
          
  K =  ["0011000100",
          "0011001100",
          "0011011000",
          "0011110000",
          "0011000000",
          "0011100000",
          "0011110000",
          "0011011000",
          "0011001100",
          "0011000100"]
  mc = init()
  x,y,z = mc.player.getPos()
  clearAir(mc,x,y,z)
  output2d(mc,I,x,y+17,z) 
  output2d(mc,D,x,y+6,z)
  output2d(mc,K,x,y-5,z)
  mc.player.setPos(x-7,y+5,z+5)
  x = x -20
    #matrixY(mc,x,y,z)

if __name__ == "__main__":
    main()

'''
AIR                   0
ICE                  79
WOOL                35
'''
