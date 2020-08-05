# 建高塔

from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

time.sleep(5)

x, y, z = mc.player.getTilePos()

mc.setBlocks(x+1, y-1, z+1, x-1, y-1, z-1, 206)
