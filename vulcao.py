from mcpi.minecraft import Minecraft
from time import sleep

# from https://projects.raspberrypi.org/en/projects/getting-started-with-minecraft-pi/8
mc = Minecraft.create()

x, y, z = mc.player.getPos()

lava = 10
water = 8
air = 0

mc.setBlock(x+3, y+3, z, lava)
sleep(20)
mc.setBlock(x+3,y+5, z, water)
sleep(4)
mc.setBlock(x+3, y+5, z, air)