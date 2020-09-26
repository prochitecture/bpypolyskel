import mathutils 
import random
import matplotlib.pyplot as plt

def examplePoly():
    # counterclockwise order, seen from top, the polygon is on the left of this contour
    polygon = [
        mathutils.Vector((520, 40,5)),
        mathutils.Vector((520, 310,5)),
        mathutils.Vector((40, 310,5)),
        mathutils.Vector((40, 40,5))
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

