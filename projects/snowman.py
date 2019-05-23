# Brenden Cooper
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
from random import randint

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    x,y,z = mc.player.getPos()
    return mc
    
def clear_with_air(mc,x,y,z,h,k,l):
    air = 0
    mc.setBlocks(x-h,y-k,z-l,x+h,y+k,z+l, air)
    
def bottom_ball(mc,x,y,z):
    snow = 80
    mc.setBlocks(x-6,y,z-6,x+6,y+6,z+6, snow)
    
def center_ball(mc,x,y,z):
    snow = 80
    mc.setBlocks(x-4,y,z-4,x+4,y+12,z+4, snow)
    
def head_ball(mc,x,y,z):
    snow = 80
    mc.setBlocks(x-2,y,z-2,x+2,y+17,z+2, snow)
    
def hat(mc,x,y,z):
    wool = 35,15
    mc.setBlocks(x-3,y,z-3,x+3,y,z+3, wool)
    mc.setBlocks(x-2,y,z-2,x+2,y+5,z+2, wool)
    
def nose(mc,x,y,z):
    wool = 35,1
    mc.setBlocks(x+4,y,z,x,y,z, wool)
    
def hatbuckle(mc,x,y,z):
    r = randint(0,2)
    if r == 0:
        wool = 35,5
    if r == 1: 
        wool = 35,6
    if r == 2: 
        wool = 35,4
    mc.setBlocks(x,y,z,x,y,z, wool)
    
def lefteye(mc,x,y,z):
    wool = 35,15
    mc.setBlocks(x,y,z,x,y,z, wool)
    
def righteye(mc,x,y,z):
    wool = 35,15
    mc.setBlocks(x,y,z,x,y,z, wool)

def mouth(mc,x,y,z):
    wool = 35,15
    mc.setBlocks(x,y,z,x,y,z+1, wool)
    
def topbutton(mc,x,y,z):
    wool = 35,15
    mc.setBlocks(x,y,z,x,y,z, wool)
    
def midbutton(mc,x,y,z):
    wool = 35,15
    mc.setBlocks(x,y,z,x,y,z, wool)
    
def botbutton(mc,x,y,z):
    wool = 35,15
    mc.setBlocks(x,y,z,x,y,z, wool)
    
def leftarm(mc,x,y,z):
    wood = 5
    mc.setBlocks(x,y,z+6,x,y,z, wood)
    
def lefthand(mc,x,y,z):
    wood = 5
    mc.setBlocks(x+1,y-1,z,x-1,y,z, wood)
    
def rightarm(mc,x,y,z):
    wood = 5
    mc.setBlocks(x,y,z-6,x,y,z, wood)
    
def righthand(mc,x,y,z):
    wood = 5
    mc.setBlocks(x+1,y-1,z,x-1,y,z, wood)
    
def pipea(mc,x,y,z):
    wood = 5
    mc.setBlocks(x,y,z,x,y,z, wood)
    
def pipeb(mc,x,y,z):
    wood = 5
    mc.setBlocks(x,y,z,x,y,z, wood)
    
def pipec(mc,x,y,z):
    wood = 5
    mc.setBlocks(x,y,z,x,y+1,z, wood)
    
def pipesmoke(mc,x1,y1,z1):
    cobweb = 30
    h = 3
    k = 3
    for n in range (0,2):
        h = randint(0,3)
        k = randint(0,1)
        mc.setBlock(x1+h,y1+h,z1+h, cobweb) 
    while True:
        for n in range (0,2):
            h = randint(0,3)
            k = randint(0,1)
            mc.setBlock(x1+h,y1+h,z1+h, cobweb)
        break
        
def main():
    mc = init()
    x1,y1,z1 = 0,5,0
    mc.player.setPos(x1,y1,z1)
    x,y,z = mc.player.getPos()
    h,k,l = 25,25,25
    clear_with_air(mc,x,y,z,h,k,l)
    bottom_ball(mc,x,y,z)
    center_ball(mc,x,y,z)
    head_ball(mc,x,y,z)
    hat(mc,x1,y1+18,z1)
    nose(mc,x1,y1+15,z1)
    hatbuckle(mc,x1+2,y1+20,z1)
    lefteye(mc,x1+2,y1+16,z1+1)
    righteye(mc,x1+2,y1+16,z1-1)
    mouth(mc,x1+2,y1+14,z1)
    topbutton(mc,x1+4,y1+11,z1)
    midbutton(mc,x1+4,y1+8,z1)
    botbutton(mc,x1+6,y1+5,z1)
    leftarm(mc,x1,y1+10,z1+3)
    lefthand(mc,x1,y1+10,z1+9)
    rightarm(mc,x1,y1+10,z1-3)
    righthand(mc,x1,y1+10,z1-9)
    #pipea(mc,x1+2,y1+14,z1-1)
    #pipeb(mc,x1+3,y1+14,z1-2)
    #pipec(mc,x1+4,y1+14,z1-3)
    #pipesmoke(mc,x1+4,y1+15,z1-3)
    mc.player.setPos(x1,y1+31,z1)
    
main()
