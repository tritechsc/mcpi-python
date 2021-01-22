# block-list-0123456789ABCDEF.py
# Documentation https://github.com/raspberrypilearning/getting-started-with-minecraft-pi/blob/master/worksheet.md
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    #ip = "192.168.7.84"
    ip = "127.0.0.1"
    mc = Minecraft.create(ip, 4711)
    #mc.setting("world_immutable",True)
    
    return mc
    
def clearAir(mc,x,y,z):
  # 256×256×128
  x,y,z = 0,0,0
  #mc.setBlocks(x-128-2,y-63,z-128+2,x+127-1,y+127,z+128-1,0)
  mc.setBlocks(x-128+10,y-5,z-64+10,x+127-10,y+127,z+63+10,0)
  #mc.setBlocks(-128,-3,-128,128,64,128,0)

def matrix(mc,x,y,z):
  
  X = ["777777777777777777777777777777777777777777777777777777777777",
       "7777777777777777ffffffffffff77ffffffffffff777777777777777777",
       "777777777777777feeeeeeeeeeef77feeeeeeeeeeef77777777777777777",
       "77777777777777feeeeeeeeeeeef77feeeeeeeeeeeef7777777777777777",
       "7777777777777feeeeeeeeeeeeef77feeeeeeeeeeeeef777777777777777",
       "777777777777feeeeeeeeeeeeeef77feeeeeeeeeeeeeef77777777777777",
       "77777777777feeeeeeeeeeeeeeef77feeeeeeeeeeeeeeef7777777777777",
       "7777777777feeeeeeeeeeeeeeeef77feeeeeeeeeeeeeeeef777777777777",
       "777777777feeeeeeeeeeeeeeeeef77feeeeeeeeeeeeeeeeef77777777777",
       "77777777feeeeeeeeeeeeeeeeef7777feeeeeeeeeeeeeeeeef7777777777",
       "7777777feeeeeeeeeeeeeeeeef777777feeeeeeeeeeeeeeeeef777777777",
       "777777feeeeeeeeeeeeeeeeef77777777feeeeeeeeeeeeeeeeef77777777",
       "77777feeeeeeeeeeeeeeeeef7777777777feeeeeeeeeeeeeeeeef7777777",
       "7777feeeeeeeeeeeeeeeeef777777777777feeeeeeeeeeeeeeeeef777777",
       "777feeeeeeeeeeeeeeeeef77777777777777feeeeeeeeeeeeeeeeef77777",
       "77feeeeeeeeeeeeeeeeef7777777777777777feeeeeeeeeeeeeeeeef7777",
       "7feeeeeeeeeeeeeeeeef777777777777777777feeeeeeeeeeeeeeeef7777",
       "7feeeeeeeeeeeeeeeef77777777777777777777feeeeeeeeeeeeeeef7777",
       "7fffffffffffffffff7777777777777777777777feeeeeeeeeeeeeef7777",
       "7777777777777777777777777777777777777777feeeeeeeeeeeeeef7777",
       "77777777777777777ff777777777777777777777feeeeeeeeeeeeef77777",
       "7777777777777777fef77777777777777777777feeeeeeeeeeeeef777777",
       "777777777777777feef7777777777777777777feeeeeeeeeeeeef777ff77",
       "77777777777777feeef777777777777777777feeeeeeeeeeeeef777fef77",
       "7777777777777feeeef77777777777777777feeeeeeeeeeeeef777feef77",
       "777777777777feeeeef7777777777777777feeeeeeeeeeeeef777feeef77",
       "77777777777feeeeeef777777777777777feeeeeeeeeeeeef777feeeef77",
       "7777777777feeeeeeef77777777777777feeeeeeeeeeeeef777feeeeef77",
       "777777777feeeeeeeef7777777777777feeeeeeeeeeeeef777feeeeeef77",
       "77777777feeeeeeeeef7777777777777feeeeeeeeeeeef777feeeeeeef77",
       "7777777feeeeeeeeeef7777777777777feeeeeeeeeeef777feeeeeeeef77",
       "777777feeeeeeeeeeef7777777777777feeeeeeeeeef777feeeeeeeeef77",
       "77777feeeeeeeeeeeef7777777777777feeeeeeeeeef77feeeeeeeeeef77",
       "7777feeeeeeeeeeeeef7777777777777feeeeeeeeef77feeeeeeeeeeef77",
       "777feeeeeeeeeeeeef77777777777777feeeeeeeef77feeeeeeeeeeeef77",
       "77feeeeeeeeeeeeef777777777777777feeeeeeef77feeeeeeeeeeeef777",
       "7feeeeeeeeeeeeef7777777777777777feeeeeef77feeeeeeeeeeeef7777",
       "feeeeeeeeeeeeef77777777777777777feeeeef77feeeeeeeeeeeef77777",
       "feeeeeeeeeeeef777777777777777777feeeef77feeeeeeeeeeeef777777",
       "feeeeeeeeeeef7777777777777777777feeef77feeeeeeeeeeeef7777777",
       "feeeeeeeeeef77777777777777777777feef77feeeeeeeeeeeef77777777",
       "feeeeeeeeef777777777777777777777fef77feeeeeeeeeeeef777777777",
       "feeeeeeeef7777777777777777777777ff77feeeeeeeeeeeef7777777777",
       "feeeeeeef77777777777777777777777777feeeeeeeeeeeef77777777777",
       "feeeeeef77777777777777777777777777feeeeeeeeeeeef777777777777",
       "feeeeef77777777777777777777777777feeeeeeeeeeeef7777777777777",
       "feeeef77777777777777777777777777feeeeeeeeeeeef77777777777777",
       "feeef777777777777777777777777777feeeeeeeeeeef777777777777777",
       "feef7777777777777777777777777777feeeeeeeeeef7777777777777777",
       "fef77777777777777777777777777777feeeeeeeeef77777777777777777",
       "ff777777777777777777777777777777feeeeeeeef777777777777777777",
       "77777777777777777777777777777777feeeeeeef7777777777777777777",
       "77777777777777777777777777777777feeeeeef77777777777777777777",
       "77777777777777777777777777777777feeeeef777777777777777777777",
       "77777777777777777777777777777777feeeef7777777777777777777777",
       "77777777777777777777777777777777feeef77777777777777777777777",
       "77777777777777777777777777777777feef777777777777777777777777",
       "77777777777777777777777777777777fef7777777777777777777777777",
       "77777777777777777777777777777777ff77777777777777777777777777",
       "77777777777777777777777777777777777777777777777777777777777 ",
       "777777777777777777777777777777777777777777777777777777777777",
       "777777777777777777777777777777777777777777777777777777777777",
       "777777777777777777777777777777777777777777777777777777777777"]
      #"123456789A"
 
  y1 = 60
  for h in range (0,60):
    x1 = 60
    for k  in range (0,60):
      print(X[h][k],end="") # debug
      #print(h,k," ",end="")
      theBlock = X[h][k]
      c = -1 # LOGIC FOR WOOL OR NOT WOOL
      if (theBlock == "0"):
        c = 0 # wool 35,0  WHITE
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
      if (theBlock == "6"):
        c = 6 # wool 35,6  LIGHT PINK
      if (theBlock == "7"):
        c = 7 # wool 35,7  DARK GRAY
      if (theBlock == "8"):
        c = 8 # wool 35,8  LIGHT GRAY  
      if (theBlock == "9"):
        c = 9 # wool 35,9  TEAL OR DARKER BLUE
      if (theBlock == "A"):
        c = 10 # wool 35,10  VIOLET
      if (theBlock == "B"):
        c = 11 # wool 35,11  DARK BLUE
      if (theBlock == "C"):
        c = 12 # wool 35,12  BROWN
      if (theBlock == "D"):
        c = 13 # wool 35,13  DARK GREEN
      if (theBlock == "e"):
        c = 14 # wool 35,14  RED
      if (theBlock == "f"):
        c = 15 # wool 35,15  BLACK
      if c == -1:
        mc.setBlock(x1-x,y1+y,z,0) # set the material with a number
      else:
        mc.setBlock(x1-x,y1+y,z,35,c)
      x1 = x1 - 1
    y1 = y1 - 1
    print()
    
def main():
  mc = init()
  mc.player.setPos(0,0,0)
  x,y,z = mc.player.getPos()
  print(x,y,z)
  clearAir(mc,x,y,z)
  matrix(mc,x,y,z+5)
  #mc.player.setPos(x,y,z-5)
  mc.postToChat("0 20 0")
  mc.player.setPos(0,20,0)
  
if __name__ == "__main__":
  main()

'''
wool 35,0  WHITE
wool 35,1  ORANGE
wool 35,2  DARK PINK 
wool 35,3  LIGHT BLUE 
wool 35,4  YELLOW
wool 35,5  GREEN
wool 35,6  LIGHT PINK
wool 35,7  DARK GRAY
wool 35,8  LIGHT GRAY
wool 35,9  TEAL OR DARKER BLUE 
wool 35,10 VIOLET
wool 35,11  DARK BLUE
wool 35,12  BROWN
wool 35,13  DARK GREEN
wool 35,14  RED
wool 35,15  BLACK

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
#   FLOWER_YELLOW        37
#   FLOWER_CYAN          38
#   MUSHROOM_BROWN       39
#   MUSHROOM_RED         40
#   GOLD_BLOCK           41
#   IRON_BLOCK           42
#   STONE_SLAB_DOUBLE    43
#   STONE_SLAB           44
#   BRICK_BLOCK          45
#   TNT                  46
#   BOOKSHELF            47
#   MOSS_STONE           48
#   OBSIDIAN             49
#   TORCH                50
#   FIRE                 51
#   STAIRS_WOOD          53
#   CHEST                54
#   DIAMOND_ORE          56
#   DIAMOND_BLOCK        57
#   CRAFTING_TABLE       58
#   FARMLAND             60
#   FURNACE_INACTIVE     61
#   FURNACE_ACTIVE       62
#   DOOR_WOOD            64
#   LADDER               65
#   STAIRS_COBBLESTONE   67
#   DOOR_IRON            71
#   REDSTONE_ORE         73
#   SNOW                 78
#   ICE                  79
#   SNOW_BLOCK           80
#   CACTUS               81
#   CLAY                 82
#   SUGAR_CANE           83
#   FENCE                85
#   GLOWSTONE_BLOCK      89
#   BEDROCK_INVISIBLE    95
#   STONE_BRICK          98
#   GLASS_PANE          102
#   MELON               103
#   FENCE_GATE          107
#   GLOWING_OBSIDIAN    246
#   NETHER_REACTOR_CORE 247
'''