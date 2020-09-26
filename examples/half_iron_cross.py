import mathutils 
import random
import matplotlib.pyplot as plt

def examplePoly():
    # counterclockwise order, seen from top, the polygon is on the left of this contour
    polygon = [
        mathutils.Vector((300, 50, 5)),
        mathutils.Vector((250, 150, 5)),
        mathutils.Vector((350, 100, 5)),
        mathutils.Vector((350, 350, 5)),
        mathutils.Vector((50,  350, 5)),
        mathutils.Vector((50,  100, 5)),
        mathutils.Vector((150, 150, 5)),
        mathutils.Vector((100, 50, 5))
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

