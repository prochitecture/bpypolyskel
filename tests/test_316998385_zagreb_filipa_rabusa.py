import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((23.47800636291504, 1.2245588302612305, 0.0)),
    Vector((24.145246505737305, 4.285847187042236, 0.0)),
    Vector((24.021081924438477, 10.686717987060547, 0.0)),
    Vector((23.656414031982422, 12.779522895812988, 0.0)),
    Vector((22.290861129760742, 16.241554260253906, 0.0)),
    Vector((21.111526489257812, 18.24530029296875, 0.0)),
    Vector((19.722705841064453, 20.093198776245117, 0.0)),
    Vector((18.74510383605957, 20.783376693725586, 0.0)),
    Vector((-2.731078624725342, 11.733075141906738, 0.0)),
    Vector((0.0, 0.0, 15.518122673034668)),
    Vector((23.47800636291504, 1.2245588302612305, 15.518122673034668)),
    Vector((24.145246505737305, 4.285847187042236, 15.518122673034668)),
    Vector((24.021081924438477, 10.686717987060547, 15.518122673034668)),
    Vector((23.656414031982422, 12.779522895812988, 15.518122673034668)),
    Vector((22.290861129760742, 16.241554260253906, 15.518122673034668)),
    Vector((21.111526489257812, 18.24530029296875, 15.518122673034668)),
    Vector((19.722705841064453, 20.093198776245117, 15.518122673034668)),
    Vector((18.74510383605957, 20.783376693725586, 15.518122673034668)),
    Vector((-2.731078624725342, 11.733075141906738, 15.518122673034668))
]
unitVectors = [
    Vector((0.9986425042152405, 0.05208689719438553, 0.0)),
    Vector((0.21296070516109467, 0.9770607352256775, 0.0)),
    Vector((-0.01939442940056324, 0.9998119473457336, 0.0)),
    Vector((-0.1716618537902832, 0.9851559996604919, 0.0)),
    Vector((-0.36692512035369873, 0.9302505254745483, 0.0)),
    Vector((-0.5072311758995056, 0.8618100881576538, 0.0)),
    Vector((-0.6008017063140869, 0.7993980646133423, 0.0)),
    Vector((-0.8169261813163757, 0.5767422914505005, 0.0)),
    Vector((-0.9215171337127686, -0.38833752274513245, 0.0)),
    Vector((0.22670695185661316, -0.9739630222320557, 0.0))
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