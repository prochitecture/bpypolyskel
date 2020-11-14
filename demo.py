"""
This module demontrates the funcion polygonize() of bpypolyskel.

It cannot be used in Blender and is thought to be used by an interpreter
where the library mathutils is installed as standalone library.

Use 'pip install mathutils'
"""
import matplotlib.pyplot as plt
import mathutils
from bpypolyskel import bpypolyskel

def runDemo():
	#Define vertices of a polygon and a hole
	verts = [
		# polygon contour in counterclockwise order, seen from top, 
		# the polygon is on the left of this contour
		mathutils.Vector((0, 0, 0)),
		mathutils.Vector((10, 0, 0)),
		mathutils.Vector((10, 5, 0)),
		mathutils.Vector((45, 5, 0)),
		mathutils.Vector((45, 20, 0)),
		mathutils.Vector((10, 20, 0)),
		mathutils.Vector((10, 25, 0)),
		mathutils.Vector((0, 25, 0)),
		# hole contour in clockwise order, seen from top, 
		# the polygon is on the left of this contour
		mathutils.Vector((5, 16, 0)),
		mathutils.Vector((35, 16, 0)),
		mathutils.Vector((35, 9, 0)),
		mathutils.Vector((5, 9, 0))
	]

	# Define indices and lengths of polygon and hole
	firstVertIndex = 0
	numVerts = 8
	holesInfo = [
		(8,4)
	]

	# We let polygonize() compute the unit vectors
	# and have no faces yet
	unitVectors = None
	faces = None

	faces = bpypolyskel.polygonize(verts, firstVertIndex, numVerts, holesInfo, 0.0, 0.5, faces, unitVectors)

	# plot the hipped roof in 3D
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	for face in faces:
		for edge in zip(face, face[1:] + face[:1]):
			p1 = verts[edge[0]]
			p2 = verts[edge[1]]
			ax.plot([p1.x,p2.x],[p1.y,p2.y],[p1.z,p2.z],'k')
	plt.show()

if __name__ == "__main__":
    # execute only if run as a script
    runDemo()