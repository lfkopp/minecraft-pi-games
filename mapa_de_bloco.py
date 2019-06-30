from PIL import Image
from mcpi import minecraft, block
from time import sleep


mc = minecraft.Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    for hit in hits:
        print(mc.getBlockWithData(hit.pos.x,hit.pos.y,hit.pos.z).id)
        print(mc.getBlockWithData(hit.pos.x,hit.pos.y,hit.pos.z).data)
        print(mc.getBlockWithData(hit.pos.x,hit.pos.y,hit.pos.z).withData.__str__)
        mc.setBlocks(hit.pos.x-2,hit.pos.y-2,hit.pos.z-2,
                     hit.pos.x+2,hit.pos.y+2,hit.pos.z+2,0)
        
