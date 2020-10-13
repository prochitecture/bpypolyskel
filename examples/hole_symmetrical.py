import mathutils 
import random

def examplePoly():
    # counterclockwise order, seen from top, the polygon is on the left of this contour
    polygon = [
        mathutils.Vector((400, 0, 0)),
        mathutils.Vector((400, 200, 0)),
        mathutils.Vector((0, 200, 0)),
        mathutils.Vector((0, 0, 0)),
    ]

    # clockwise order, seen from top, the polygon is on the right of this contour
    hole = [
        mathutils.Vector((50, 150, 0)),
        mathutils.Vector((350, 150, 0)),
        mathutils.Vector((350, 50, 0)),
        mathutils.Vector((50, 50, 0))
    ]

    verts = []

    # create a random number of vertices before the polygon
    firstVertIndex = random.randrange(100)
    for i in range(firstVertIndex):
        verts.append(mathutils.Vector((0,0,0)))

    verts.extend(polygon)
    verts.extend(hole)

    numVerts = len(polygon)
    numVertsHoles = []
    numVertsHoles.append(len(hole))
    return verts, numVerts, firstVertIndex, numVertsHoles

