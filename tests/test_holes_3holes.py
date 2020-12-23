import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((11.983535766601562, -8.813440322875977, 0.0)),
    Vector((26.341291427612305, 10.708718299865723, 0.0)),
    Vector((14.357771873474121, 19.522106170654297, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((11.983535766601562, -8.813440322875977, 21.477258682250977)),
    Vector((26.341291427612305, 10.708718299865723, 21.477258682250977)),
    Vector((14.357771873474121, 19.522106170654297, 21.477258682250977)),
    Vector((0.0, 0.0, 21.477258682250977)),
    Vector((5.6908488273620605, 0.6323739290237427, 0.0)),
    Vector((9.881379127502441, 6.036295413970947, 0.0)),
    Vector((14.010330200195312, 2.834458351135254, 0.0)),
    Vector((9.819801330566406, -2.5694682598114014, 0.0)),
    Vector((5.6908488273620605, 0.6323739290237427, 21.477258682250977)),
    Vector((9.881379127502441, 6.036295413970947, 21.477258682250977)),
    Vector((14.010330200195312, 2.834458351135254, 21.477258682250977)),
    Vector((9.819801330566406, -2.5694682598114014, 21.477258682250977)),
    Vector((11.974641799926758, 8.6879301071167, 0.0)),
    Vector((16.1651611328125, 14.091849327087402, 0.0)),
    Vector((20.294111251831055, 10.890020370483398, 0.0)),
    Vector((16.103591918945312, 5.486096382141113, 0.0)),
    Vector((11.974641799926758, 8.6879301071167, 21.477258682250977)),
    Vector((16.1651611328125, 14.091849327087402, 21.477258682250977)),
    Vector((20.294111251831055, 10.890020370483398, 21.477258682250977)),
    Vector((16.103591918945312, 5.486096382141113, 21.477258682250977))
]
unitVectors = [
    Vector((0.5924769043922424, 0.8055875301361084, 0.0)),
    Vector((-0.8055875897407532, 0.5924766659736633, 0.0)),
    Vector((-0.5924783945083618, -0.8055863976478577, 0.0)),
    Vector((0.8055863380432129, -0.5924785137176514, 0.0)),
    Vector((0.6127992272377014, 0.790238618850708, 0.0)),
    Vector((0.7902389764785767, -0.6127988696098328, 0.0)),
    Vector((-0.6127987504005432, -0.7902390956878662, 0.0)),
    Vector((-0.790238618850708, 0.612799346446991, 0.0)),
    Vector((0.6127984523773193, 0.7902393341064453, 0.0)),
    Vector((0.790239691734314, -0.6127979755401611, 0.0)),
    Vector((-0.6127980351448059, -0.7902395725250244, 0.0)),
    Vector((-0.7902392148971558, 0.6127985715866089, 0.0))
]
holesInfo = [
    (12, 4),
    (20, 4)
]
firstVertIndex = 4
numPolygonVerts = 4
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