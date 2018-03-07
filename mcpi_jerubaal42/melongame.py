#A minigame with multiplayer support. Right click melons - First to 50 melons wins!

from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi import event
from random import randint

def init():
	mc = Minecraft.create("127.0.0.1", 4711)
	return mc

def melon(mc):
	global meloncount
	entityIds=mc.getPlayerEntityIds()
	while meloncount<(len(entityIds)*50):
		x=randint(-128,128)
		z=randint(-128,128)
		y=mc.getHeight(x,z)
		mc.setBlock(x,y,z,103)
		meloncount=meloncount+1
		print meloncount

def checkBlock(mc,score):
	global meloncount
	entityIds=mc.getPlayerEntityIds()
	for each in entityIds:
		if each not in score:
			score.update({each:0})
			mc.setting("world_immutable",True)
			melon(mc)
	blockEvent=mc.events.pollBlockHits()
	for each in blockEvent:
		x=each.pos.x
		y=each.pos.y
		z=each.pos.z
		if mc.getBlock(x,y,z)==103:
			mc.setBlock(x,y,z,0)
			meloncount=meloncount-1
			playerId=each.entityId
			score[playerId]=score[playerId]+1
			if (score[playerId])%10==0:
				mc.postToChat("Player {0} has {1} points!".format(playerId,score[playerId]))
			if score[playerId]>=50:
				mc.postToChat("Player {0} wins!".format(playerId))
				exit()
	
def main():
	global meloncount
	mc=init()
	mc.postToChat("Welcome to Melon Grabber Minigame!")
	mc.setting("world_immutable",True)
	score={}
	meloncount=0
	melon(mc)
	mc.postToChat("Melons have spawned!")
	mc.events.clearAll()
	while True:
		checkBlock(mc,score)

main()
