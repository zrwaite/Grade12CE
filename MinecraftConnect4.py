from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
mc = Minecraft.create()

x, y, z = mc.player.getPos()
gold = 41
diamond = 57
quartz = 155
stone = block.STONE_BRICK.id

def w():
    #------W_Letter----------
    mc.setBlock(2, 13, 9, 42)
    sleep(0.1)
    mc.setBlock(2, 12, 9, 42)
    sleep(0.1)
    mc.setBlock(2, 11, 9, 42)
    sleep(0.1)
    mc.setBlock(2, 10, 9, 42)
    sleep(0.1)
    mc.setBlock(1, 9, 9, 42)
    sleep(0.1)
    mc.setBlock(0.6, 10, 9, 42)
    sleep(0.1)
    mc.setBlock(0.6, 11, 9, 42)
    sleep(0.1)
    mc.setBlock(-0.7, 9, 9, 42)
    sleep(0.1)
    mc.setBlock(-1.5, 10, 9, 42)
    sleep(0.1)
    mc.setBlock(-1.5, 11, 9, 42)
    sleep(0.1)
    mc.setBlock(-1.5, 12, 9, 42)
    sleep(0.1)
    mc.setBlock(-1.5, 13, 9, 42)
    sleep(0.1)
def l():
    mc.setBlock(1, 12, 9, 42)
    sleep(0.1)
    mc.setBlock(1, 11, 9, 42)
    sleep(0.1)
    mc.setBlock(1, 10, 9, 42)
    sleep(0.1)
    mc.setBlock(1, 9, 9, 42)
    sleep(0.1)
    mc.setBlock(0, 9, 9, 42)
    sleep(0.1)
    mc.setBlock(-1, 9, 9, 42)
    sleep(0.1)

def connect():
    c1()
    o()
    n1()
    n2()
    e()
    c2()
    t()
def c1():
    mc.setBlock(13, 19, 9, 44, 1)
    mc.setBlock(13, 18, 9, 24)
    mc.setBlock(13, 17, 9, 24)
    mc.setBlock(12, 19.5, 9, 44, 1)
    mc.setBlock(11, 19.5, 9, 44, 1)
    mc.setBlock(12, 17, 9, 44, 1)
    mc.setBlock(11, 17, 9, 44, 1)
def o():
    mc.setBlock(9, 19, 9, 44, 1)
    mc.setBlock(8, 19, 9, 44, 1)
    mc.setBlock(7, 19, 9, 44, 1)
    mc.setBlock(9, 18, 9, 24)
    mc.setBlock(9, 17, 9, 24)
    mc.setBlock(7, 18, 9, 24)
    mc.setBlock(7, 17, 9, 24)
    mc.setBlock(8, 17, 9, 44, 1)
def n1():
    mc.setBlock(5, 19, 9, 44, 1)
    mc.setBlock(5, 18, 9, 24)
    mc.setBlock(5, 17, 9, 24)
    mc.setBlock(4, 19, 9, 44, 1)
    mc.setBlock(3, 19, 9, 44, 1)
    mc.setBlock(2, 17, 9, 24)
    mc.setBlock(2, 18, 9, 24)
def n2():
    mc.setBlock(0, 19, 9, 44, 1)
    mc.setBlock(0, 18, 9, 24)
    mc.setBlock(0, 17, 9, 24)
    mc.setBlock(-1, 19, 9, 44, 1)
    mc.setBlock(-2, 19, 9, 44, 1)
    mc.setBlock(-3, 17, 9, 24)
    mc.setBlock(-3, 18, 9, 24)
def e():
    mc.setBlock(-5, 19, 9, 44, 1)
    mc.setBlock(-5, 18, 9, 24)
    mc.setBlock(-5, 17, 9, 24)
    mc.setBlock(-6, 19, 9, 44, 1)
    mc.setBlock(-7, 19, 9, 44, 1)
    mc.setBlock(-6, 18, 9, 44, 1)
    mc.setBlock(-6, 17, 9, 44, 1)
    mc.setBlock(-7, 17, 9, 44, 1)               
def c2():
    mc.setBlock(-9, 19, 9, 44, 1)
    mc.setBlock(-9, 18, 9, 24)
    mc.setBlock(-9, 17, 9, 24)
    mc.setBlock(-10, 19.5, 9, 44, 1)
    mc.setBlock(-11, 19.5, 9, 44, 1)
    mc.setBlock(-10, 17, 9, 44, 1)
    mc.setBlock(-11, 17, 9, 44, 1)
def t():
    mc.setBlock(-13, 19, 9, 44, 1)
    mc.setBlock(-14, 19, 9, 44, 1)
    mc.setBlock(-15, 19, 9, 44, 1)
    mc.setBlock(-14, 18, 9, 24)
    mc.setBlock(-14, 17, 9, 24)

def createStage():
    mc.setBlocks(6, 7, 11, -5, 15, 4, 0)
    mc.setBlocks(4, 7, 10, -4, 16, 9, quartz)
    mc.setBlocks(3, 8, 10, -3, 13, 10, stone)
    mc.setBlocks(3, 8, 9, -3, 13, 9, 0)
    mc.setBlocks(3, 14, 9, -3, 14, 9, diamond)
    mc.setBlocks(3, 15, 9, -3, 15, 9, gold)
    mc.setBlock(4, 16, 9, 247)
    mc.setBlock(-4, 16, 9, 103)
    connect()
    four()
def clear():
    x1, y1, z = 3, 8, 9
    x2, y2 = -3, 14
    mc.setBlock(x1, y1, z, 41)
    mc.setBlock(x2, y2, z, 41)
    i = 0
    size = 7
    while(size>=3):
        while(i<size):
            mc.setBlock(x1-i, y1, z, 0)
            mc.setBlock(x1, y1+i, z, 0)
            mc.setBlock(x2+i, y2, z, 0)
            mc.setBlock(x2, y2-i, z, 0)
            i+=1
            sleep(0.1)
        x1 -= 1
        y1 += 1
        x2 += 1
        y2 -= 1
        mc.setBlock(x1, y1, z, 0)
        mc.setBlock(x2, y2, z, 0)
        i = 0
        size-=2
    mc.setBlock(0.7, 11, 9, 0)

def animation(win, lose):
    mc.setBlocks(3, 8, 9, -3, 13, 9, 0)
    x1, y1, z = 3, 8, 9
    x2, y2 = -3, 14
    mc.setBlock(x1, y1, z, win)
    mc.setBlock(x2, y2, z, win)
    i = 0
    size = 7
    while(size>=3):
        while(i<size):
            mc.setBlock(x1-i, y1, z, win)
            mc.setBlock(x1, y1+i, z, win)
            mc.setBlock(x2+i, y2, z, win)
            mc.setBlock(x2, y2-i, z, win)
            i+=1
            sleep(0.1)
        x1 -= 1
        y1 += 1
        x2 += 1
        y2 -= 1
        mc.setBlock(x1, y1, z, win)
        mc.setBlock(x2, y2, z, win)
        i = 0
        size-=2
    mc.setBlock(0.7, 11, 9, win)
    sleep(0.10)

    #------W_Letter----------
    w()

    #Loser clears the screen

    x1, y1, z = 3, 8, 9
    x2, y2 = -3, 14
    mc.setBlock(x1, y1, z, lose)
    mc.setBlock(x2, y2, z, lose)

    i = 0
    size = 7
    while(size>=3):
        while(i<size):
            mc.setBlock(x1-i, y1, z, lose)
            mc.setBlock(x1, y1+i, z, lose)
            mc.setBlock(x2+i, y2, z, lose)
            mc.setBlock(x2, y2-i, z, lose)
            i+=1
            sleep(0.1)
        x1 -= 1
        y1 += 1
        x2 += 1
        y2 -= 1
        mc.setBlock(x1, y1, z, lose)
        mc.setBlock(x2, y2, z, lose)
        i = 0
        size-=2
    mc.setBlock(0.7, 11, 9, lose)
    sleep(0.10)

    l()
    clear()
    createStage()


def clearStage():
    mc.setBlocks(3, 8, 9, -3, 13, 9, 0)

def checkStage():
    mc.postToChat("works")
    blocks = mc.getBlocks(3, 8, 9, -3, 13, 9)
    mc.postToChat(blocks[0])
    mc.postToChat("still works")
    

def dropBlock(bx, by, bz, ID):
    if ID == gold:
        by-=1
    oby = by
    while mc.getBlock(bx, by-1, bz) == 0:
        if by!=oby:
            mc.setBlock(bx, by, bz, 0)
        mc.setBlock(bx, by-1, bz, ID)
        sleep(0.2)
        by-=1

def four():
    mc.setBlocks(3, 19, 12, -3, 25, 12, diamond)
    mc.setBlocks(3, 24, 12, 3, 25, 12, 0)
    mc.setBlock(2, 25, 12, 0)
    mc.setBlocks(-3, 24, 12, -3, 25, 12, 0)
    mc.setBlock(-2, 25, 12, 0)
    mc.setBlocks(3, 19, 12, 3, 20, 12, 0)
    mc.setBlock(2, 19, 12, 0)
    mc.setBlocks(-3, 19, 12, -3, 20, 12, 0)
    mc.setBlock(-2, 19, 12, 0)
    mc.setBlocks(-1, 19, 12, -1, 24, 12, gold)
    mc.setBlocks(1, 22, 12, 1, 24, 12, gold)
    mc.setBlock(0, 22, 12, gold)
    

createStage()
while(True):
    sleep(0.2)
    events = mc.events.pollBlockHits()
    length = len(events)
    if length != 0:
        x, y, z = events[0].pos
        if mc.getBlock(x, y, z) == gold:
            dropBlock(x, y, z, gold)
        if mc.getBlock(x, y, z) == diamond:
            dropBlock(x, y, z, diamond)
        if mc.getBlock(x, y, z) == 247:
            animation(57, 41)
        if mc.getBlock(x, y, z) == 103:
            animation(41, 57)
    mc.events.clearAll()
