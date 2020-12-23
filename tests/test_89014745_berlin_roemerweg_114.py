import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((-0.5761287212371826, -0.7235766649246216, 0.0)),
    Vector((-3.748225450515747, -0.45640847086906433, 0.0)),
    Vector((-4.1277971267700195, -5.688424110412598, 0.0)),
    Vector((-6.411979675292969, -5.510310649871826, 0.0)),
    Vector((-6.615324974060059, -9.562339782714844, 0.0)),
    Vector((5.951082706451416, -10.664403915405273, 0.0)),
    Vector((6.628870010375977, -1.3358293771743774, 0.0)),
    Vector((3.5109963417053223, -1.068665862083435, 0.0)),
    Vector((3.205986499786377, -0.16697818040847778, 0.0)),
    Vector((0.0, 0.0, 5.411919116973877)),
    Vector((-0.5761287212371826, -0.7235766649246216, 5.411919116973877)),
    Vector((-3.748225450515747, -0.45640847086906433, 5.411919116973877)),
    Vector((-4.1277971267700195, -5.688424110412598, 5.411919116973877)),
    Vector((-6.411979675292969, -5.510310649871826, 5.411919116973877)),
    Vector((-6.615324974060059, -9.562339782714844, 5.411919116973877)),
    Vector((5.951082706451416, -10.664403915405273, 5.411919116973877)),
    Vector((6.628870010375977, -1.3358293771743774, 5.411919116973877)),
    Vector((3.5109963417053223, -1.068665862083435, 5.411919116973877)),
    Vector((3.205986499786377, -0.16697818040847778, 5.411919116973877))
]
unitVectors = [
    Vector((-0.622891902923584, -0.7823078632354736, 0.0)),
    Vector((-0.9964718818664551, 0.08392732590436935, 0.0)),
    Vector((-0.07235772162675858, -0.9973787665367126, 0.0)),
    Vector((-0.9969736933708191, 0.07774091511964798, 0.0)),
    Vector((-0.05012050271034241, -0.9987432360649109, 0.0)),
    Vector((0.9961764812469482, -0.08736389875411987, 0.0)),
    Vector((0.07246609032154083, 0.9973708987236023, 0.0)),
    Vector((-0.9963489770889282, 0.08537488430738449, 0.0)),
    Vector((-0.32042956352233887, 0.9472723603248596, 0.0)),
    Vector((-0.9986463785171509, 0.052012745290994644, 0.0))
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