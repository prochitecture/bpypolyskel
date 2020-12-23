import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((-3.24507737159729, -5.68281364440918, 0.0)),
    Vector((8.30772876739502, -13.277770042419434, 0.0)),
    Vector((10.27431869506836, -10.286351203918457, 0.0)),
    Vector((10.900666236877441, -2.708956480026245, 0.0)),
    Vector((5.716447830200195, 1.8445731401443481, 0.0)),
    Vector((0.0, 0.0, 15.129359245300293)),
    Vector((-3.24507737159729, -5.68281364440918, 15.129359245300293)),
    Vector((8.30772876739502, -13.277770042419434, 15.129359245300293)),
    Vector((10.27431869506836, -10.286351203918457, 15.129359245300293)),
    Vector((10.900666236877441, -2.708956480026245, 15.129359245300293)),
    Vector((5.716447830200195, 1.8445731401443481, 15.129359245300293))
]
unitVectors = [
    Vector((-0.4958803355693817, -0.8683908581733704, 0.0)),
    Vector((0.8356021046638489, -0.5493350625038147, 0.0)),
    Vector((0.5493340492248535, 0.835602879524231, 0.0)),
    Vector((0.0823790580034256, 0.9966011047363281, 0.0)),
    Vector((-0.7513300776481628, 0.6599266529083252, 0.0)),
    Vector((-0.9516814947128296, -0.30708688497543335, 0.0))
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