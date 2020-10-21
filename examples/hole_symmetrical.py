import mathutils 
import random

def examplePoly():
    # counterclockwise order, seen from top, the polygon is on the left of this contour
    verts = [
        0,
        0,
        # polygon contour in clockwise order, seen from top, 
        # the polygon is on the right of this contour
        mathutils.Vector((400, 0, 0)),
        mathutils.Vector((400, 200, 0)),
        mathutils.Vector((0, 200, 0)),
        mathutils.Vector((0, 0, 0)),
        0,
        0,
        0,
        mathutils.Vector((50, 150, 0)),
        mathutils.Vector((350, 150, 0)),
        mathutils.Vector((350, 50, 0)),
        mathutils.Vector((50, 50, 0))
    ]

    unitVectors = None

    firstVertIndex = 2
    numPolygonVerts = 4
    holesInfo = [
        (9,4)
    ]
    return verts, numPolygonVerts, firstVertIndex, holesInfo, unitVectors

