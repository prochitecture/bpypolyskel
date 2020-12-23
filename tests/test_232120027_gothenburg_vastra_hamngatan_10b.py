import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((2.8132400512695312, -24.35670280456543, 0.0)),
    Vector((6.923063278198242, -21.42899513244629, 0.0)),
    Vector((9.712503433227539, -18.28978157043457, 0.0)),
    Vector((11.175613403320312, -14.73868465423584, 0.0)),
    Vector((11.26481819152832, -11.198724746704102, 0.0)),
    Vector((9.962274551391602, -6.189351558685303, 0.0)),
    Vector((7.5534796714782715, -3.061278820037842, 0.0)),
    Vector((3.889742612838745, -0.8348942995071411, 0.0)),
    Vector((0.0, 0.0, 15.0)),
    Vector((2.8132400512695312, -24.35670280456543, 15.0)),
    Vector((6.923063278198242, -21.42899513244629, 15.0)),
    Vector((9.712503433227539, -18.28978157043457, 15.0)),
    Vector((11.175613403320312, -14.73868465423584, 15.0)),
    Vector((11.26481819152832, -11.198724746704102, 15.0)),
    Vector((9.962274551391602, -6.189351558685303, 15.0)),
    Vector((7.5534796714782715, -3.061278820037842, 15.0)),
    Vector((3.889742612838745, -0.8348942995071411, 15.0))
]
unitVectors = [
    Vector((0.11473887413740158, -0.9933957457542419, 0.0)),
    Vector((0.814471423625946, 0.5802035927772522, 0.0)),
    Vector((0.6642345786094666, 0.7475242614746094, 0.0)),
    Vector((0.3809487521648407, 0.9245961904525757, 0.0)),
    Vector((0.025191383436322212, 0.9996827244758606, 0.0)),
    Vector((-0.25165313482284546, 0.967817485332489, 0.0)),
    Vector((-0.6101220846176147, 0.7923074960708618, 0.0)),
    Vector((-0.8545833230018616, 0.5193143486976624, 0.0)),
    Vector((-0.9777314066886902, 0.20986025035381317, 0.0))
]
holesInfo = None
firstVertIndex = 9
numPolygonVerts = 9
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