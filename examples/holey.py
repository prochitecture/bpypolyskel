import mathutils 
import random

def examplePoly():
    verts = [
        0,
        0,
        0,
        # polygon contour in clockwise order, seen from top, 
        # the polygon is on the right of this contour
        mathutils.Vector((85,40,5)),
        mathutils.Vector((230,30,5)),
        mathutils.Vector((430,40,5)),
        mathutils.Vector((440,240,5)),
        mathutils.Vector((220,240,5)),
        mathutils.Vector((50, 200,5)),
        mathutils.Vector((30,100,5)),
        0,
        0,
        0,
        0,
        # Hole contour in anti-clockwise order, seen from top, 
        # the polygon is on the left of this contour
        mathutils.Vector((165,180,5)),
        mathutils.Vector((330,200,5)),
        mathutils.Vector((385,160,5)),
        mathutils.Vector((315,90,5)),
        mathutils.Vector((245,140,5)),
        mathutils.Vector((175,85,5))
    ]

    unitVectors = None

    firstVertIndex = 3
    numPolygonVerts = 7
    holesInfo = [
        (14,6)
    ]
    return verts, numPolygonVerts, firstVertIndex, holesInfo, unitVectors

