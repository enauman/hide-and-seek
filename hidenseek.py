import math
import sys
from random import *
from mcpi import minecraft
from mcpi import block
import time
mc = minecraft.Minecraft.create("localhost", 4711,name="erik")
# pos = mc.player.getPos()

def distanceBetweenPoints(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))

def makeBuilding(seekerID):
	pos = mc.entity.getPos(seekerID)
	mc.setBlocks(pos.x+3, pos.y-1, pos.z-5, pos.x-3, pos.y+2, pos.z+5, block.GLOWSTONE_BLOCK.id)
	mc.setBlocks(pos.x+2, pos.y, pos.z-4, pos.x-2, pos.y+1, pos.z+4, block.WOOD_PLANKS.id)
	mc.setBlocks(pos.x+1, pos.y-1, pos.z-5, pos.x-1, pos.y-1, pos.z+3, block.GLOWSTONE_BLOCK.id)
	mc.setBlocks(pos.x+2, pos.y+2, pos.z-4, pos.x-2, pos.y+2, pos.z+4, block.WOOD_PLANKS.id)
	mc.setBlocks(pos.x+1, pos.y, pos.z-1, pos.x-1, pos.y+1, pos.z+1, block.WOOD_PLANKS.id)
	mc.setBlocks(pos.x, pos.y, pos.z, pos.x, pos.y+1, pos.z, block.AIR.id)
	mc.setBlock(pos.x, pos.y-1, pos.z, block.GOLD_BLOCK.id)

	time.sleep(30)

	mc.setBlocks(pos.x+1, pos.y, pos.z-3, pos.x-1, pos.y+1, pos.z+3, block.AIR.id)
	mc.setBlocks(pos.x, pos.y, pos.z-5, pos.x, pos.y+1, pos.z-4, block.AIR.id)
	
	mc.setBlock(pos.x, pos.y-1, pos.z-5, block.DIAMOND_BLOCK.id)


entityIds = mc.getPlayerEntityIds() #creates a list of player IDs
entityPositions = []

seekerIndex = randint(0, (len(entityIds)-1))
seekerID = entityIds[seekerIndex]
seeking = True

hiderIDs = []
lastHiderPositions = []
currentHiderPositions = []

distanceFromHider = []


# makeBuilding()

# for entityId in entityIds:  # loops thru the list to print the list of IDs in game
#     print entityId
#     print len(entityIds)
# while True:
# 	#every 5 seconds print each player's ID and tile position
# 	for player in entityIds:
# 		print player
# 		print mc.entity.getTilePos(player)
# 	time.sleep(5)


# lastDistanceFromBlock = distanceBetweenPoints(randomBlockPos, lastPlayerPos)


# .APPEND add items to list
# mylist.remove('two')
# mylist.pop()
# del mylist[1:3]

for x in range(0, (len(entityIds))):
	entityPositions.append(mc.entity.getPos(entityIds[x]))
	if entityIds[x] != seekerID:
		hiderIDs.append(entityIds[x])
	print entityIds[x]

print " "

for x in range(0, (len(entityPositions))):
	print (str(entityIds[x]) + " - " + str(entityPositions[x]))


mc.postToChat("Welcome to multiplayer hide and seek. There are " + str(len(entityIds)) + " players in this game.")
time.sleep(1)
mc.postToChat("Game will start in: 3")
time.sleep(1)
mc.postToChat("2")
time.sleep(1)
mc.postToChat("1")
time.sleep(1)
mc.postToChat("Get hiding!")


makeBuilding(seekerID)

for x in range(0, (len(hiderIDs))):
	lastHiderPositions.append(mc.entity.getPos(hiderIDs[x]))
	lastHiderPositions[x].y = lastHiderPositions[x].y-1
	mc.setBlock(lastHiderPositions[x].x, lastHiderPositions[x].y, lastHiderPositions[x].z, block.IRON_BLOCK.id)


timeStarted = time.time()
while seeking:

	seekerPos = mc.entity.getPos(seekerID)

	for x in range(0, (len(hiderIDs))):
		currentHiderPositions.append(mc.entity.getPos(hiderIDs[x]))
		currentHiderPositions[x].y = currentHiderPositions[x].y-1
		if lastHiderPositions[x] != currentHiderPositions[x]:
			mc.entity.setPos(hiderIDs[x], lastHiderPositions[x].x, lastHiderPositions[x].y+1, lastHiderPositions[x].z)

	currentHiderPositions = []

	for x in range(0, (len(hiderIDs))):
		distanceFromHider.append(distanceBetweenPoints(seekerPos, lastHiderPositions[x]))

	minDistance = sys.maxint
	# maxDistance = (-sys.maxint - 1)

	for x in range(0, (len(distanceFromHider))):
		# if int(distanceFromHider[x]) > maxDistance:
		# 	maxDistance = int(distanceFromHider[x])
		if int(distanceFromHider[x]) < minDistance:
			minDistance = int(distanceFromHider[x])

	if minDistance < 2:
		seeking = False
	else:
		mc.postToChat("The closest hider is " + str(minDistance) + " blocks away")

	distanceFromHider = []

	time.sleep(2)

timeTaken = time.time() - timeStarted

mc.postToChat("Good game! It took you " + str(int(timeTaken)) + " seconds to find someone.")
