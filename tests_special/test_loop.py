import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel

verts = [
    Vector((183.2800, 143.3600, 0.0)), # This causes an infinite loop in _LAV 
    Vector((220.2800, 143.3600, 0.0)),
    Vector((220.2800, -2.0800, 0.0)),
    Vector((493.6000, -2.0800, 0.0)),
    Vector((493.6000, 271.2400, 0.0)),
    Vector((326.5600, 271.2400, 0.0)),
    Vector((326.5600, 330.5600, 0.0)),
    Vector((390.6400, 330.5600, 0.0)),
    Vector((390.6400, 557.1800, 0.0)),
    Vector((340.4800, 573.8100, 0.0)),
    Vector((340.4800, 646.4000, 0.0)),
    Vector((390.6400, 646.4000, 0.0)),
    Vector((390.6400, 709.6000, 0.0)),
    Vector((119.3600, 709.6000, 0.0)),
    Vector((119.3600, 493.8400, 0.0)),
    Vector((10.8800, 493.8400, 0.0)),
    Vector((10.8800, 143.3600, 0.0))    
]

unitVectors = None

holesInfo = None
firstVertIndex = 0
numPolygonVerts = len(verts)
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
    try:
        faces = bpypolyskel.polygonize(verts, firstVertIndex, numPolygonVerts, holesInfo, 0.0, 0.5, faces, unitVectors)
    except RuntimeError as e:
        print(e)

    # plot the hipped roof in 3D
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    for face in faces:
        for edge in zip(face, face[1:] + face[:1]):
            p1 = verts[edge[0]]
            p2 = verts[edge[1]]
            ax.plot([p1.x,p2.x],[p1.y,p2.y],[p1.z,p2.z],'k')
    plt.show()

# plot_chart()