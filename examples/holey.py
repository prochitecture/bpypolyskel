import mathutils 
import random
import matplotlib.pyplot as plt

def examplePoly():
    # clockwise order, seen from top, the polygon is on the right of this contour
    polygon = ( mathutils.Vector((30,100,5)),mathutils.Vector((50, 200,5)),mathutils.Vector((220,240,5)),mathutils.Vector((440,240,5)),\
                mathutils.Vector((430,40,5)),mathutils.Vector((230,30,5)),mathutils.Vector((85,40,5)) )


    # anti-clockwise order, seen from top, the polygon is on the left of this contour
    hole = ( mathutils.Vector((175,85,5)),mathutils.Vector((245,140,5)),mathutils.Vector((315,90,5)),mathutils.Vector((385,160,5)), \
             mathutils.Vector((330,200,5)),mathutils.Vector((165,180,5)) )

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

