from mcpi.minecraft import Minecraft
from time import sleep
from random import randrange

mc = Minecraft.create()
x, y, z = mc.player.getPos()

bola = 41

cores = {'white':0,'orange':1,'magenta':2,'cyan':3,'yellow':4,'green':5,
         'pink':6,'dark_gray':7,'light_gray':8,'blue':9,'purple':10,'dark_blue':11,
         'brown':12,'dark_green':13,'red':14,'black':15}

def faz_campo():
    mc.setBlocks(-35, -10, -45,    35, 50, 45,0) #limpa espaco
    mc.setBlocks(-25, 0, -35,    25, -1, 35, 2) #faz campo
    mc.setBlocks(-21, 0, -31,    21, -1, 31, 1) #faz entorno
    mc.setBlocks(-20, 0, -30,    20, -1, 30, 2) #faz campo
    mc.setBlocks(-21, 0, 0,    21, -1, 0, 1) #faz meio campo

    mc.setBlocks(-10, 0, -20,    10, -1, -31, 1) #faz area 1
    mc.setBlocks(-9, 0, -21,    9, -1, -30, 2) #faz area 1

    mc.setBlocks(-10, 0, 20,    10, -1, 31, 1) #faz area 2
    mc.setBlocks(-9, 0, 21,    9, -1, 30, 2) #faz area 2

    mc.setBlocks(-6, 1, 31,    6, 5, 34, 155) #faz gol 1 trave
    mc.setBlocks(-6, 1, 32,    6, 5, 34, 20) #faz gol 1 rede
    mc.setBlocks(-5, 1, 31,    5, 4, 33, 0) #faz gol 1

    mc.setBlocks(-6, 1, -31,    6, 5, -34, 155) #faz gol 2 trave
    mc.setBlocks(-6, 1, -32,    6, 5, -34, 20) #faz gol 2 rede
    mc.setBlocks(-5, 1, -31,    5, 4, -33, 0) #faz gol 2


    mc.setBlocks(0, 1, 0,    0, 1, 0, bola) #bola

def tem_espaco(x,z):
    if (mc.getBlockWithData(x,1,z).id == 0 and
    mc.getBlockWithData(x,0,z).id != 0):
        return True
    else:
        return False

def chuta_bola():
    hits = mc.events.pollBlockHits()
    for hit in hits:
        print(hit.face, mc.getBlockWithData(hit.pos.x,hit.pos.y,hit.pos.z).id)
        if mc.getBlockWithData(hit.pos.x,hit.pos.y,hit.pos.z).id == bola:
            if hit.face ==2 and tem_espaco(hit.pos.x,hit.pos.z+1):
                mc.setBlock(hit.pos.x,1,hit.pos.z,0)
                mc.setBlock(hit.pos.x,1,hit.pos.z+1,bola)
            elif hit.face == 3 and tem_espaco(hit.pos.x,hit.pos.z-1):
                mc.setBlock(hit.pos.x,1,hit.pos.z,0)
                mc.setBlock(hit.pos.x,1,hit.pos.z-1,bola)
            elif hit.face == 4 and tem_espaco(hit.pos.x+1,hit.pos.z):
                mc.setBlock(hit.pos.x,1,hit.pos.z,0)
                mc.setBlock(hit.pos.x+1,1,hit.pos.z,bola)
            elif hit.face == 5 and tem_espaco(hit.pos.x-1,hit.pos.z):
                mc.setBlock(hit.pos.x,1,hit.pos.z,0)
                mc.setBlock(hit.pos.x-1,1,hit.pos.z,bola)
            elif hit.face == 1:
                mc.setBlock(hit.pos.x,1,hit.pos.z,0)
                mc.setBlock(hit.pos.x,2,hit.pos.z,bola)
                sleep(0.2)
                mc.setBlock(hit.pos.x,2,hit.pos.z,0)
                mc.setBlock(hit.pos.x,1,hit.pos.z,bola)

def cria_jogador(a,c1,c2,pos):
    x,y = pos
    mc.setBlock(x,1,y,a,c1)
    mc.setBlock(x,2,y,a,c2)
    #mc.setBlock(x,3,y,44)

def monta_time():
    time1 = []
    time2 = []
    for i in range(3):
        pos = tuple([randrange(-19,19),randrange(1,29)])
        time1.append(pos)
        cria_jogador(35,cores['red'],cores['black'],pos)
        pos = tuple([randrange(-19,19),randrange(-29,-1)])
        time2.append(pos)
        cria_jogador(35,cores['dark_green'],cores['red'],pos)
    return time1,time2

def move(time,c1,c2):
    novo_time = []
    for i in time:
        new_pos = tuple([i[0]+randrange(-1,2),i[1]+randrange(-1,2)])
        if tem_espaco(new_pos[0],new_pos[1]):
            cria_jogador(0,0,0,i)
            i=new_pos
            cria_jogador(35,c1,c2,i)
        novo_time.append(i)
    return novo_time


faz_campo()
   
time1 , time2 = monta_time()

print(time1)
print(time2)
mc.player.setPos(randrange(-10,10),10,randrange(-10,10))

while True:
    chuta_bola()
    time1 = move(time1,cores['red'],cores['black'])
    time2 = move(time2,cores['dark_green'],cores['red'])
