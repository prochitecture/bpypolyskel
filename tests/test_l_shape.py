import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((-4.888134002685547, -7.435404300689697, 0.0)),
    Vector((6.6646647453308105, -15.030360221862793, 0.0)),
    Vector((8.631254196166992, -12.03894329071045, 0.0)),
    Vector((0.604164183139801, -6.761839866638184, 0.0)),
    Vector((3.5257041454315186, -2.3178412914276123, 0.0)),
    Vector((0.0, 0.0, 14.989067077636719)),
    Vector((-4.888134002685547, -7.435404300689697, 14.989067077636719)),
    Vector((6.6646647453308105, -15.030360221862793, 14.989067077636719)),
    Vector((8.631254196166992, -12.03894329071045, 14.989067077636719)),
    Vector((0.604164183139801, -6.761839866638184, 14.989067077636719)),
    Vector((3.5257041454315186, -2.3178412914276123, 14.989067077636719))
]
unitVectors = [
    Vector((-0.5493357181549072, -0.8356017470359802, 0.0)),
    Vector((0.8356019854545593, -0.5493353009223938, 0.0)),
    Vector((0.5493342280387878, 0.8356027603149414, 0.0)),
    Vector((-0.835602343082428, 0.5493348240852356, 0.0)),
    Vector((0.549335241317749, 0.8356021046638489, 0.0)),
    Vector((-0.8356021642684937, 0.5493351221084595, 0.0))
]
holesInfo = None
firstVertIndex = 6
numPolygonVerts = 6
faces = []

bpypolyskel.debugOutputs["skeleton"] = 1


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


@pytest.mark.dependency(depends=["test_polygonize"])
def test_edgeCrossing():
    assert not bpypolyskel.checkEdgeCrossing(bpypolyskel.debugOutputs["skeleton"])