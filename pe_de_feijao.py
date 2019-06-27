from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create()
x,y,z = mc.player.getPos()

for i in range(20):
    sleep(1)
    mc.setBlock(x+5,y+1,z, block.LEAVES.id)