import mathutils 
import random

def examplePoly():
    # counterclockwise order, seen from top, the polygon is on the left of this contour
    polygon = [
        mathutils.Vector((-5, -3, 0)),
        mathutils.Vector((5, -3, 0)),
        mathutils.Vector((5, -1.5, 0)),
        mathutils.Vector((8, -1.5, 0)),
        mathutils.Vector((8, 2.5, 0)),
        mathutils.Vector((5, 2.5, 0)),
        mathutils.Vector((5, 3, 0)),
        mathutils.Vector((-5, 3, 0)),
    ]

    verts = []

    # create a random number of vertices before the polygon
    firstVertIndex = random.randrange(100)
    for i in range(firstVertIndex):
        verts.append(mathutils.Vector((0,0,0)))

    verts.extend(polygon)
 
    numVerts = len(polygon)
    numVertsHoles = []
    return verts, numVerts, firstVertIndex, numVertsHoles

