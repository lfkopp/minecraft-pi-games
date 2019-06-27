from PIL import Image
from mcpi import minecraft, block

mc = minecraft.Minecraft.create()
mc.postToChat('Sou tricolor de coracao!!')

player_pos = mc.player.getPos()

img = Image.open('flu.png')
baseheight = 40
hpercent = (baseheight / float(img.size[1]))
wsize = int((float(img.size[0]) * float(hpercent)))
img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
img.save(‘resized_img.bmp')

img = Image.open(‘resized_img.bmp')
pixels = img.load()

for i in range(im.size[0]):
    for j in range(im.size[1]):
        pixel = pixels[i,j]
        mc.postToChat(str(pixel))
        if pixel[0] > 100:
            type = block.STONE
        else:
            type = block.GLASS
        mc.setBlock(player_pos.x + 2 , player_pos.y - j, player_pos.z + i, type)        
print (pixel)