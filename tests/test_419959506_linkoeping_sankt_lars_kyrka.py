import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((2.361597776412964, 0.7013134956359863, 0.0)),
    Vector((4.315016746520996, 1.892433762550354, 0.0)),
    Vector((5.6503376960754395, 3.206005334854126, 0.0)),
    Vector((6.670778274536133, 4.731083869934082, 0.0)),
    Vector((7.242223262786865, 6.044654846191406, 0.0)),
    Vector((7.697044849395752, 8.204254150390625, 0.0)),
    Vector((7.615405082702637, 10.45290756225586, 0.0)),
    Vector((7.020630359649658, 12.523448944091797, 0.0)),
    Vector((6.134302139282227, 14.148712158203125, 0.0)),
    Vector((4.495765209197998, 15.952085494995117, 0.0)),
    Vector((2.454885244369507, 17.2545223236084, 0.0)),
    Vector((0.09329728037118912, 17.978097915649414, 0.0)),
    Vector((-2.1225130558013916, 18.05602264404297, 0.0)),
    Vector((0.0, 0.0, 10.0)),
    Vector((2.361597776412964, 0.7013134956359863, 10.0)),
    Vector((4.315016746520996, 1.892433762550354, 10.0)),
    Vector((5.6503376960754395, 3.206005334854126, 10.0)),
    Vector((6.670778274536133, 4.731083869934082, 10.0)),
    Vector((7.242223262786865, 6.044654846191406, 10.0)),
    Vector((7.697044849395752, 8.204254150390625, 10.0)),
    Vector((7.615405082702637, 10.45290756225586, 10.0)),
    Vector((7.020630359649658, 12.523448944091797, 10.0)),
    Vector((6.134302139282227, 14.148712158203125, 10.0)),
    Vector((4.495765209197998, 15.952085494995117, 10.0)),
    Vector((2.454885244369507, 17.2545223236084, 10.0)),
    Vector((0.09329728037118912, 17.978097915649414, 10.0)),
    Vector((-2.1225130558013916, 18.05602264404297, 10.0))
]
unitVectors = [
    Vector((0.9586231708526611, 0.284678190946579, 0.0)),
    Vector((0.8537940382957458, 0.5206109881401062, 0.0)),
    Vector((0.7128886580467224, 0.7012773156166077, 0.0)),
    Vector((0.556103527545929, 0.8311131000518799, 0.0)),
    Vector((0.3989182114601135, 0.9169865846633911, 0.0)),
    Vector((0.20608384907245636, 0.9785343408584595, 0.0)),
    Vector((-0.036282166838645935, 0.999341607093811, 0.0)),
    Vector((-0.27609050273895264, 0.9611316323280334, 0.0)),
    Vector((-0.47877758741378784, 0.8779361844062805, 0.0)),
    Vector((-0.6724720001220703, 0.7401225566864014, 0.0)),
    Vector((-0.8429694771766663, 0.5379613041877747, 0.0)),
    Vector((-0.9561273455619812, 0.2929513454437256, 0.0)),
    Vector((-0.9993822574615479, 0.035145875066518784, 0.0)),
    Vector((0.1167476549744606, -0.9931615591049194, 0.0))
]
holesInfo = None
firstVertIndex = 14
numPolygonVerts = 14
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