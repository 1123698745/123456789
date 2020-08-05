# Disco舞廳

from mcpi.minecraft import Minecraft
import time
import random

mc = Minecraft.create()

time.sleep(5)
x, y, z = mc.player.getTilePos()



while True:
    x, y, z = mc.player.getTilePos()


    mc.setBlocks(x-25, y-1, z-25, x+25, y-1, z+25, 46)
    
    time.sleep(1)