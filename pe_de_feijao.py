from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import random


mc = Minecraft.create()
x,y,z = mc.player.getPos()

for i in range(50):
    sleep(.5)
    dx = random.randrange(-1,1)        
    dz = random.randrange(-1,1)  
    dy = i/2
    mc.setBlock(x+dx,y+dy,z+dz, block.LEAVES.id)
