import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, -5.911065101623535, 0.0)),
    Vector((-10.528433799743652, -5.911051273345947, 0.0)),
    Vector((-10.528467178344727, -18.74618911743164, 0.0)),
    Vector((0.0, -18.74620246887207, 0.0)),
    Vector((0.0, -22.063522338867188, 0.0)),
    Vector((20.33598518371582, -22.063472747802734, 0.0)),
    Vector((20.335874557495117, 5.116134343552403e-05, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((0.0, -5.911065101623535, 2.0)),
    Vector((-10.528433799743652, -5.911051273345947, 2.0)),
    Vector((-10.528467178344727, -18.74618911743164, 2.0)),
    Vector((0.0, -18.74620246887207, 2.0)),
    Vector((0.0, -22.063522338867188, 2.0)),
    Vector((20.33598518371582, -22.063472747802734, 2.0)),
    Vector((20.335874557495117, 5.116134343552403e-05, 2.0)),
    Vector((0.0, 0.0, 2.0))
]
unitVectors = [
    Vector((-1.0, 1.3134221035215887e-06, 0.0)),
    Vector((-2.6005641302617732e-06, -0.9999999403953552, 0.0)),
    Vector((1.0, -1.2681276757575688e-06, 0.0)),
    Vector((0.0, -1.0, 0.0)),
    Vector((1.0, 2.438586761854822e-06, 0.0)),
    Vector((-5.013986537960591e-06, 1.0, 0.0)),
    Vector((-1.0, -2.5158171865768963e-06, 0.0)),
    Vector((0.0, -1.0, 0.0))
]
holesInfo = None
firstVertIndex = 8
numPolygonVerts = 8
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