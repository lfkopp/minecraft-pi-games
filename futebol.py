from mcpi.minecraft import Minecraft
from time import sleep
from random import randrange
import pygame

pygame.mixer.init()



mc = Minecraft.create()
x, y, z = mc.player.getPos()



cores = {'white':0,'orange':1,'magenta':2,'cyan':3,'yellow':4,'green':5,
         'pink':6,'dark_gray':7,'light_gray':8,'blue':9,'purple':10,'dark_blue':11,
         'brown':12,'dark_green':13,'red':14,'black':15}


def foi_gol(x,z,fla,flu):
    if (-5 <= x <= 5) and (z < -31):
        pygame.mixer.music.load("wav/gol_fla.wav")
        pygame.mixer.music.play()
        fla += 1
        mc.postToChat("ahhhh gol do Flamengo")
        sleep(3)
        mc.postToChat(''.join(["Fluminense ",str(flu)," x ", str(fla), " Flamengo"]))
        mc.player.setPos(randrange(-10,10),10,randrange(-10,10))
        mc.setBlock(x, 1, z, 0) #limpa bola
        mc.setBlock(0, 1, 0, 41) #bola
        return 0,0,fla,flu
    elif (-5 <= x <= 5) and (z > 31):
        if 15 < randrange(0,20) < 18:
            pygame.mixer.music.load("wav/gol_ganso.wav")
        else:
            pygame.mixer.music.load("wav/gol_flu.wav")
        pygame.mixer.music.play()
        flu +=1
        mc.postToChat("gol do Fluminense")
        sleep(3)
        mc.postToChat(''.join(["Fluminense ",str(flu)," x ", str(fla), " Flamengo"]))
        mc.player.setPos(randrange(-10,10),10,randrange(-10,10))
        mc.setBlock(x, 1, z, 0) #limpa bola
        mc.setBlock(0, 1, 0, 41) #bola
        return 0,0,fla,flu
    
    return x,z,fla,flu

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

    
    
    
def tem_espaco(x,z):
    if (mc.getBlockWithData(x,1,z).id == 0 and
    mc.getBlockWithData(x,0,z).id != 0):
        return True
    else:
        return False

def chuta_bola(x,z):
    hits = mc.events.pollBlockHits()
    for hit in hits:
        if 15 < randrange(0,20) < 18:
            pygame.mixer.music.load("wav/emocionante.wav")
        elif 10 < randrange(0,20) < 15:
            pygame.mixer.music.load("wav/toque.wav")
        else:
            pygame.mixer.music.load("wav/chute.wav")
        pygame.mixer.music.play()
        print(hit.face, mc.getBlockWithData(hit.pos.x,hit.pos.y,hit.pos.z).id)
        if mc.getBlockWithData(hit.pos.x,hit.pos.y,hit.pos.z).id == bola:
            jx,jy,jz = mc.player.getPos()
            deltax = (hit.pos.x-jx)/3
            for t in range(randrange(5,10)):
                oldx,oldz = hit.pos.x,hit.pos.z
                if hit.face == 2 and tem_espaco(hit.pos.x+ deltax,hit.pos.z+1):
                    hit.pos.z = hit.pos.z +1
                    hit.pos.x = hit.pos.x + deltax
                elif hit.face == 3 and tem_espaco(hit.pos.x+ deltax,hit.pos.z-1):
                    hit.pos.z = hit.pos.z-1
                    hit.pos.x = hit.pos.x + deltax
                elif hit.face == 4 and tem_espaco(hit.pos.x+1,hit.pos.z):
                    hit.pos.x = hit.pos.x+1
                elif hit.face == 5 and tem_espaco(hit.pos.x-1,hit.pos.z):
                    hit.pos.x = hit.pos.x-1
                mc.setBlock(oldx,1,oldz,0)
                mc.setBlock(hit.pos.x,1,hit.pos.z,bola)
                x,z=hit.pos.x,hit.pos.z
            if hit.face == 1:
                mc.setBlock(hit.pos.x,1,hit.pos.z,0)
                mc.setBlock(hit.pos.x,2,hit.pos.z,bola)
                sleep(0.2)
                mc.setBlock(hit.pos.x,2,hit.pos.z,0)
                mc.setBlock(hit.pos.x,1,hit.pos.z,bola)
    return x,z

def cria_jogador(a,c1,c2,pos):
    x,z = pos
    mc.setBlock(x,1,z,a,c1)
    mc.setBlock(x,2,z,a,c2)
    #mc.setBlock(x,3,z,44)

def monta_time():
    time1 = []
    time2 = []
    for i in range(30):
        pos = tuple([randrange(-19,19),randrange(1,29)])
        time1.append(pos)
        cria_jogador(35,cores['red'],cores['black'],pos)
        pos = tuple([randrange(-19,19),randrange(-29,-1)])
        time2.append(pos)
        cria_jogador(35,cores['dark_green'],cores['red'],pos)
    return time1,time2

def monta_goleiro(pos,lado,cor):
    mc.setBlock(pos, 1, lado, 35,cores[cor])
    mc.setBlock(pos, 2, lado, 35,cores[cor])
    mc.setBlock(pos, 3, lado, 35,cores[cor])
    return pos
    
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

def move_goleiro(pos,lado,cor):
    new_pos = pos+randrange(-1,2)
    if tem_espaco(new_pos,lado):
        mc.setBlocks(pos, 1, lado, pos, 3, lado, 0)
        monta_goleiro(new_pos,lado,cor)
        return new_pos
    else:
        return pos

faz_campo()
bolax, bolaz, bola = 0,0,41
mc.postToChat("Pedro, vamos jogar futebol?")
time1 , time2 = monta_time()
gol1 = monta_goleiro(randrange(-5,5),31,'yellow')
gol2 = monta_goleiro(randrange(-5,5),-31,'orange')
mc.player.setPos(randrange(-10,10),10,randrange(-10,10))
mc.setBlock(bolax, 1, bolaz, bola) #bola

fla,flu = 0,0
pygame.mixer.music.load("wav/comeco.wav")
pygame.mixer.music.play()
        
while True:
    bolax,bolaz = chuta_bola(bolax,bolaz)
    bolax,bolaz,fla,flu = foi_gol(bolax,bolaz,fla,flu)
    gol1 = move_goleiro(gol1,31,'yellow')
    gol2 = move_goleiro(gol2,-31,'orange')
    #time1 = move(time1,cores['red'],cores['black'])
    #time2 = move(time2,cores['dark_green'],cores['red'])
    
