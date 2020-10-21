import mathutils 
import random
import matplotlib.pyplot as plt

def examplePoly():
    verts = [
        0,
        0,
        0,
        # polygon contour in clockwise order, seen from top, 
        # the polygon is on the right of this contour
        mathutils.Vector((520, 40,5)),
        mathutils.Vector((520, 310,5)),
        mathutils.Vector((40, 310,5)),
        mathutils.Vector((40, 40,5))
    ]

    unitVectors = None

    firstVertIndex = 3
    numPolygonVerts = 4
    holesInfo = None
    return verts, numPolygonVerts, firstVertIndex, holesInfo, unitVectors