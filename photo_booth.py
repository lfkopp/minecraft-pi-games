from PIL import Image
from mcpi import minecraft, block

mc = minecraft.Minecraft.create()
mc.postToChat('Sou tricolor de coracao!!')

player_pos = mc.player.getPos()

im = Image.open('flu.png')
pixels = im.load()
for i in range(im.size[0]):
    print(" ")
    for j in range(im.size[1]):
        pixel = pixels[i,j]
        print(pixel,",",end="")
        if pixel > 14:
            type = block.STONE
        else:
            type = block.GLASS
        mc.setBlock(player_pos.x + 20 , player_pos.y +im.size[1]/2 - j, player_pos.z + i, type)        

