import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((-4.180785179138184, -6.519289970397949, 0.0)),
    Vector((7.414609432220459, -13.955343246459961, 0.0)),
    Vector((11.704358100891113, -7.266115665435791, 0.0)),
    Vector((8.433736801147461, -5.168692111968994, 0.0)),
    Vector((5.771400451660156, -9.320208549499512, 0.0)),
    Vector((0.37277403473854065, -5.858105659484863, 0.0)),
    Vector((2.926142454147339, -1.8765164613723755, 0.0)),
    Vector((0.0, 0.0, 15.962427139282227)),
    Vector((-4.180785179138184, -6.519289970397949, 15.962427139282227)),
    Vector((7.414609432220459, -13.955343246459961, 15.962427139282227)),
    Vector((11.704358100891113, -7.266115665435791, 15.962427139282227)),
    Vector((8.433736801147461, -5.168692111968994, 15.962427139282227)),
    Vector((5.771400451660156, -9.320208549499512, 15.962427139282227)),
    Vector((0.37277403473854065, -5.858105659484863, 15.962427139282227)),
    Vector((2.926142454147339, -1.8765164613723755, 15.962427139282227))
]
unitVectors = [
    Vector((-0.5398265719413757, -0.8417763113975525, 0.0)),
    Vector((0.8417765498161316, -0.539825975894928, 0.0)),
    Vector((0.5398250818252563, 0.8417772650718689, 0.0)),
    Vector((-0.8417772650718689, 0.5398250818252563, 0.0)),
    Vector((-0.5398253202438354, -0.8417770266532898, 0.0)),
    Vector((-0.8417767286300659, 0.5398257970809937, 0.0)),
    Vector((0.5398260951042175, 0.8417766094207764, 0.0)),
    Vector((-0.8417766094207764, 0.539825975894928, 0.0))
]
holesInfo = None
firstVertIndex = 8
numPolygonVerts = 8
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