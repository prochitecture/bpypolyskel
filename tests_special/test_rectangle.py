import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 10.0, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((20.0, 0.0, 0.0)),
    Vector((20.0, 10.0, 0.0))
]

unitVectors = None

holesInfo = None
firstVertIndex = 0
numPolygonVerts = 4
faces = []


@pytest.mark.dependency()
@pytest.mark.timeout(10)
def test_polygonize():
    global faces
    faces = bpypolyskel.polygonize(verts, firstVertIndex, numPolygonVerts, holesInfo, 0.0, 0.5, None, unitVectors)


@pytest.mark.dependency(depends=["test_polygonize"])
def test_numVertsInFace():
    for face in faces:
        assert len(face) >= 3


@pytest.mark.dependency(depends=["test_polygonize"])
def test_duplication():
    for face in faces:
        assert len(face) == len(set(face))


def plot_chart():
    import matplotlib.pyplot as plt
    
    global faces
    faces = bpypolyskel.polygonize(verts, firstVertIndex, numPolygonVerts, holesInfo, 0.0, 0.5, faces, unitVectors)

    # plot the hipped roof in 3D
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    for face in faces:
        for edge in zip(face, face[1:] + face[:1]):
            p1 = verts[edge[0]]
            p2 = verts[edge[1]]
            ax.plot([p1.x,p2.x],[p1.y,p2.y],[p1.z,p2.z],'k')
    plt.show()

#plot_chart()