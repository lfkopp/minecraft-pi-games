from PIL import Image
from mcpi import minecraft, block

mc = minecraft.Minecraft.create()
mc.postToChat('Sou tricolor de coracao!!')

player_pos = mc.player.getPos()

img = Image.open('flu.png')
baseheight = 40
hpercent = (baseheight / float(img.size[1]))
wsize = int((float(img.size[0]) * float(hpercent)))
img = img.resize((wsize, baseheight), Image.ANTIALIAS)
img.save('resized_img.bmp')
img = Image.open('resized_img.bmp')
pixels = img.load()


for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixel = pixels[i,j]
        if pixel == 15:
            type = 155
        elif pixel == 11:
            type = 18
        elif pixel == 1:
            type = 45
        else:
            type = block.AIR
        mc.setBlock(player_pos.x + 5 , player_pos.y + img.size[1]- j, player_pos.z + i, type)        

