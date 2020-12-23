import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((0.8498885631561279, -5.732954025268555, 0.0)),
    Vector((1.7316479682922363, -5.632766246795654, 0.0)),
    Vector((2.5602893829345703, -5.232016086578369, 0.0)),
    Vector((3.2189531326293945, -4.586363315582275, 0.0)),
    Vector((3.6545212268829346, -3.751467227935791, 0.0)),
    Vector((3.813875436782837, -2.8052515983581543, 0.0)),
    Vector((3.6757688522338867, -1.8701677322387695, 0.0)),
    Vector((3.2614481449127197, -1.0241395235061646, 0.0)),
    Vector((2.6027843952178955, -0.356222540140152, 0.0)),
    Vector((1.7953901290893555, 0.055659666657447815, 0.0)),
    Vector((0.8923832774162292, 0.17811116576194763, 0.0)),
    Vector((0.0, 0.0, 2.0)),
    Vector((0.8498885631561279, -5.732954025268555, 2.0)),
    Vector((1.7316479682922363, -5.632766246795654, 2.0)),
    Vector((2.5602893829345703, -5.232016086578369, 2.0)),
    Vector((3.2189531326293945, -4.586363315582275, 2.0)),
    Vector((3.6545212268829346, -3.751467227935791, 2.0)),
    Vector((3.813875436782837, -2.8052515983581543, 2.0)),
    Vector((3.6757688522338867, -1.8701677322387695, 2.0)),
    Vector((3.2614481449127197, -1.0241395235061646, 2.0)),
    Vector((2.6027843952178955, -0.356222540140152, 2.0)),
    Vector((1.7953901290893555, 0.055659666657447815, 2.0)),
    Vector((0.8923832774162292, 0.17811116576194763, 2.0))
]
unitVectors = [
    Vector((0.14664354920387268, -0.9891893863677979, 0.0)),
    Vector((0.993606686592102, 0.1128961592912674, 0.0)),
    Vector((0.9002467393875122, 0.43538016080856323, 0.0)),
    Vector((0.7141249179840088, 0.7000183463096619, 0.0)),
    Vector((0.4625410735607147, 0.8865978717803955, 0.0)),
    Vector((0.1660734862089157, 0.986113429069519, 0.0)),
    Vector((-0.14610934257507324, 0.98926842212677, 0.0)),
    Vector((-0.4398157000541687, 0.8980880379676819, 0.0)),
    Vector((-0.7021574378013611, 0.7120217680931091, 0.0)),
    Vector((-0.8907858729362488, 0.4544233977794647, 0.0)),
    Vector((-0.9909306168556213, 0.13437432050704956, 0.0)),
    Vector((-0.9806578159332275, -0.19572992622852325, 0.0))
]
holesInfo = None
firstVertIndex = 12
numPolygonVerts = 12
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