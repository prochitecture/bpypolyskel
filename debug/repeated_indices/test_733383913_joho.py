import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((0.20979124307632446, -5.310866191265973e-10, 0.0)),
    Vector((0.20979124307632446, -0.10018754005432129, 0.0)),
    Vector((0.6624986529350281, -0.10018754750490189, 0.0)),
    Vector((0.6624986529350281, -4.425721567002938e-09, 0.0)),
    Vector((0.8170816898345947, -6.727096657499487e-09, 0.0)),
    Vector((0.8170816898345947, 0.04452779144048691, 0.0)),
    Vector((0.861248254776001, 0.04452778771519661, 0.0)),
    Vector((0.8170816898345947, 0.6345210671424866, 0.0)),
    Vector((0.011041645891964436, 0.5677294135093689, 0.0)),
    Vector((0.0, 0.0, 0.05000000074505806)),
    Vector((0.20979124307632446, -5.310866191265973e-10, 0.05000000074505806)),
    Vector((0.20979124307632446, -0.10018754005432129, 0.05000000074505806)),
    Vector((0.6624986529350281, -0.10018754750490189, 0.05000000074505806)),
    Vector((0.6624986529350281, -4.425721567002938e-09, 0.05000000074505806)),
    Vector((0.8170816898345947, -6.727096657499487e-09, 0.05000000074505806)),
    Vector((0.8170816898345947, 0.04452779144048691, 0.05000000074505806)),
    Vector((0.861248254776001, 0.04452778771519661, 0.05000000074505806)),
    Vector((0.8170816898345947, 0.6345210671424866, 0.05000000074505806)),
    Vector((0.011041645891964436, 0.5677294135093689, 0.05000000074505806))
]
unitVectors = [
    Vector((1.0, -2.531500342684012e-09, 0.0)),
    Vector((0.0, -1.0, 0.0)),
    Vector((0.9999999403953552, -1.645782710113508e-08, 0.0)),
    Vector((0.0, 1.0, 0.0)),
    Vector((1.0, -1.4887630683801945e-08, 0.0)),
    Vector((0.0, 0.9999999403953552, 0.0)),
    Vector((1.0, -8.434638942844686e-08, 0.0)),
    Vector((-0.07465056329965591, 0.9972098469734192, 0.0)),
    Vector((-0.9965842962265015, -0.08258090168237686, 0.0)),
    Vector((-0.019445106387138367, -0.9998109936714172, 0.0))
]
holesInfo = None
firstVertIndex = 10
numPolygonVerts = 10
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