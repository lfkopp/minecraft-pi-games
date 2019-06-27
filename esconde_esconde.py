import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
import math


def roundVec3(vec3):
    return minecraft.Vec3(int(vec3.x), int(vec3.y), int(vec3.z))

def distanceBetweenPoints(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))


def verticaldistance(point1, point2):
    yd = point2.y - point1.y
    if yd < 0:
        return "pra baixo " + str(int(abs(yd)))
    else:
        return "pra cima " + str(int(abs(yd)))

                
if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    mc.postToChat("oi Pedro!! Vamos brincar???")
    time.sleep(2)
    mc.postToChat("eu escondi um diamante, voce consegue encontrar?")
    time.sleep(2)
    while True:
        playerPos = mc.player.getPos()
        randomBlockPos = roundVec3(playerPos)
        randomBlockPos.x = random.randrange(max(-127,randomBlockPos.x - 50), min(127,randomBlockPos.x + 50))
        randomBlockPos.y = random.randrange(randomBlockPos.y - 5, randomBlockPos.y + 5)
        randomBlockPos.z = random.randrange(max(-127,randomBlockPos.x - 50), min(127,randomBlockPos.x + 50))
        print(randomBlockPos)
        mc.setBlocks(randomBlockPos.x-1, randomBlockPos.y-1, randomBlockPos.z-1,randomBlockPos.x+1, randomBlockPos.y+1, randomBlockPos.z+1, block.DIAMOND_BLOCK)
        mc.postToChat("Pronto! Pode ir procurar!")
        seeking = True
        lastPlayerPos = playerPos
        lastDistanceFromBlock = distanceBetweenPoints(randomBlockPos, lastPlayerPos)
        timeStarted = time.time()
        while (seeking == True):
            playerPos = mc.player.getPos()
            if lastPlayerPos != playerPos:
                distanceFromBlock = distanceBetweenPoints(randomBlockPos, playerPos)
                if distanceFromBlock < 14:
                    mc.postToChat(verticaldistance(randomBlockPos, playerPos))
                    if distanceFromBlock < 5:
                        seeking = False
                else:
                    if distanceFromBlock < lastDistanceFromBlock:
                        mc.postToChat("Ta quente " + str(int(distanceFromBlock)))
                    if distanceFromBlock > lastDistanceFromBlock:
                        mc.postToChat("Ta frio " + str(int(distanceFromBlock)))
                    lastDistanceFromBlock = distanceFromBlock
            time.sleep(2)
        timeTaken = time.time() - timeStarted
        mc.postToChat("Muito bem, cara!! Demorou so - " + str(int(timeTaken)) + " segundos.")
        time.sleep(5)
        mc.setBlocks(randomBlockPos.x-2, randomBlockPos.y-2, randomBlockPos.z-2,randomBlockPos.x+2, randomBlockPos.y+2, randomBlockPos.z+2, 0)
        
