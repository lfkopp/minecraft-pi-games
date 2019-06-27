import mcpi.minecraft as minecraft
import mcpi.block as block
#import mcpi.minecraftstuff as minecraftstuff
import minecraftstuff
import math
import time
def distanceBetweenPoint(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))

horseBlocks = [
   # minecraftstuff.ShapeBlock(-1,-1,0,block.IRON_BLOCK.id), 
    minecraftstuff.ShapeBlock(-1,0,0,block.IRON_BLOCK.id),
    minecraftstuff.ShapeBlock(-1,1,0,block.IRON_BLOCK.id),
    minecraftstuff.ShapeBlock(-1,2,0,block.IRON_BLOCK.id),
    minecraftstuff.ShapeBlock(-1,3,0,block.IRON_BLOCK.id),
    minecraftstuff.ShapeBlock(-1,4,0,block.DIAMOND_BLOCK.id),
    minecraftstuff.ShapeBlock(-1,5,0,block.IRON_BLOCK.id),
    minecraftstuff.ShapeBlock(0,2,0,block.IRON_BLOCK.id),
    minecraftstuff.ShapeBlock(0,3,0,block.SNOW_BLOCK.id),
    minecraftstuff.ShapeBlock(0,4,0,block.SNOW_BLOCK.id),
    minecraftstuff.ShapeBlock(0,5,0,block.IRON_BLOCK.id),
#    minecraftstuff.ShapeBlock(1,-1,0,block.IRON_BLOCK.id),
    minecraftstuff.ShapeBlock(1,0,0,block.IRON_BLOCK.id),
    minecraftstuff.ShapeBlock(1,1,0,block.IRON_BLOCK.id),
    minecraftstuff.ShapeBlock(1,2,0,block.IRON_BLOCK.id),
    minecraftstuff.ShapeBlock(1,3,0,block.IRON_BLOCK.id),
    minecraftstuff.ShapeBlock(1,4,0,block.DIAMOND_BLOCK.id),
    minecraftstuff.ShapeBlock(-2,3,0,block.IRON_BLOCK.id),
    minecraftstuff.ShapeBlock(-3,3,0,block.IRON_BLOCK.id),
    minecraftstuff.ShapeBlock(2,3,0,block.IRON_BLOCK.id),
    minecraftstuff.ShapeBlock(3,3,0,block.IRON_BLOCK.id),
    minecraftstuff.ShapeBlock(3,2,0,block.IRON_BLOCK.id),
    minecraftstuff.ShapeBlock(-3,2,0,block.IRON_BLOCK.id), 
    minecraftstuff.ShapeBlock(1,5,0,block.IRON_BLOCK.id)]

TOO_FAR_AWAY = 15                     
mc = minecraft.Minecraft.create()  
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
blockMood = "happy"                     
horsePos = mc.player.getTilePos()
horsePos.x = horsePos.x + 6
horsePos.y = mc.getHeight(horsePos.x, horsePos.z)
print("horsePos born=("+str(horsePos.x)+","+str(horsePos.y)+","+str(horsePos.z)+")")
horseShape = minecraftstuff.MinecraftShape(mc, horsePos,horseBlocks)

mc.postToChat("<block> Hello IRON friend")
time.sleep(3)
target = horsePos.clone()

while True:
    pos =  mc.player.getTilePos()
    #mc.postToChat("x1="+str(pos.x)+" y1="+str(pos.y)+" z1="+str(pos.z))
    print("pos=("+str(pos.x)+","+str(pos.y)+","+str(pos.z)+")")
    distance = distanceBetweenPoint(pos, horsePos)
    if blockMood =="happy":
        if distance < TOO_FAR_AWAY:
            target = pos.clone()
            target.x = target.x + 4
        elif distance >= TOO_FAR_AWAY:
            blockMood ="sad"                     
            mc.postToChat("<block>YOU are too fast!")
    elif blockMood == "sad":
        if distance <= 10:
            blockMood = "happy"
            mc.postToChat("<block> Thank you steve")

    if horsePos != target:
        #mc.postToChat("horsePos=("+str(horsePos.x)+","+str(horsePos.y)+","+str(horsePos.z)+")")
        print("horsePos=("+str(horsePos.x)+","+str(horsePos.y)+","+str(horsePos.z)+")")
        #mc.postToChat("target=("+str(target.x)+","+str(target.y)+","+str(target.z)+")")
        print("target=("+str(target.x)+","+str(target.y)+","+str(target.z)+")")
        leavesBetween = mcdrawing.getLine(horsePos.x, horsePos.y, horsePos.z,
                                         target.x, target.y, target.z)
        for blockBetween in leavesBetween[:-1]:
            if blockBetween.x == horsePos.x and blockBetween.z == horsePos.z:
                horsePos = blockBetween.clone()
            else:
                horsePos = blockBetween.clone()
                print("horsePosA=("+str(horsePos.x)+","+str(horsePos.y)+","+str(horsePos.z)+")")
                horsePos.y = mc.getHeight(horsePos.x, horsePos.z)
                print("horsePosB=("+str(horsePos.x)+","+str(horsePos.y)+","+str(horsePos.z)+")")
            horseShape.move(horsePos.x, horsePos.y, horsePos.z)
            time.sleep(0.5)
        target = horsePos.clone()
    time.sleep(0.5)
horseShape.clear() 