import math, random
from panda3d.core import *


def Cloud(radius = 1):
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1
    z = 2 * random.random() - 1

    unitVec = vec3(x, y, z)
    unitVec.normalize()
    return unitVec * radius
    