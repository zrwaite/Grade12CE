from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
from math import floor

mc = Minecraft.create()

def fall():
    k = 0
    x, y, z = mc.player.getPos()
    i = mc.getBlock(x, y-1, z)
    
    while k<1:
        x, y, z = mc.player.getPos()
        mc.setBlocks(x+1, y, z+1, x-1, y-15, z-1, 0)
        sleep(0.6)
        mc.setBlocks(x+1, y-1, z+1, x-1, y-1, z-1, i)
        if i==2:
            i=3
        mc.setBlocks(x+1, y-2, z+1, x-1, y-5, z-1, i)
        mc.setBlocks(x+1, y-6, z+1, x-1, y-6, z-1, 1)
        mc.setBlock(x, y-15, z, 50)
        k+=1
    sleep(1)
    

def tunnel():
    blocks = []
    k = 1
    while k<2:
        print(len(blocks))
        x, y, z = mc.player.getPos()
        mc.setBlocks(x-2, y, z-2, x+2, y+2, z+2, 0)
        if mc.getBlock(x, y+3, z) != 0:
            mc.setBlock(x, y +3, z, 50, 2)
        q = [floor(x), floor(y), floor(z)]
        if q not in blocks:
            blocks.append(q)
        length = len(blocks)
        i = 0
        while i <length:
            if mc.getBlock(blocks[i][0],blocks[i][1],blocks[i][2])!=0:
                del blocks[i]
                length -= 1
                continue
            i += 1
        i = 0
        length = len(blocks)
        while i < length:      
            if x+5<blocks[i][0] or x-5>blocks[i][0] or y+5<blocks[i][1] or y-5>blocks[i][1] or z+5<blocks[i][2] or z-5>blocks[i][2]:
                mc.setBlocks(blocks[i][0]-2, blocks[i][1], blocks[i][2]-2, blocks[i][0]+2, blocks[i][1]+2, blocks[i][2]+2, 1)
                del blocks[i]
                length -=1
                continue
            i += 1

fall()
tunnel()


