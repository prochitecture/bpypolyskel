import mathutils 
import random

def examplePoly():
    verts = [
        0,
        0,
        0,
        0,
        0,
        # polygon contour in clockwise order, seen from top, 
        # the polygon is on the right of this contour
        mathutils.Vector((-5, -3, 0)),
        mathutils.Vector((5, -3, 0)),
        mathutils.Vector((5, -1.5, 0)),
        mathutils.Vector((8, -1.5, 0)),
        mathutils.Vector((8, 2.5, 0)),
        mathutils.Vector((5, 2.5, 0)),
        mathutils.Vector((5, 3, 0)),
        mathutils.Vector((-5, 3, 0)),
    ]

    unitVectors = None

    firstVertIndex = 5
    numPolygonVerts = 8
    holesInfo = None
    return verts, numPolygonVerts, firstVertIndex, holesInfo, unitVectors
