from PIL import Image
from mcpi import minecraft, block
from time import sleep


mc = minecraft.Minecraft.create()

while True:
    #Get the block hit events
    sleep(3)
    blockHits = mc.events.pollBlockHits()
    # if a block has been hit
    if blockHits:
        print("q")
        # for each block that has been hit
        for blockHit in blockHits:
            # do something with the block
            print(blockHit.pos.x,blockHit.pos.y,blockHit.pos.z)
            print(blockHit.face)
            print(blockHit.type)
            print(blockHit.entityId)
