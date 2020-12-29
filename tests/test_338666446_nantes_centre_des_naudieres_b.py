import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((-0.46157968044281006, -0.22263896465301514, 0.0)),
    Vector((-1.0290957689285278, -0.6233890652656555, 0.0)),
    Vector((-1.513376235961914, -1.1020628213882446, 0.0)),
    Vector((-1.8690197467803955, -1.6809240579605103, 0.0)),
    Vector((-2.0279245376586914, -2.2931811809539795, 0.0)),
    Vector((-1.9144214391708374, -2.9165704250335693, 0.0)),
    Vector((-1.6420137882232666, -3.495431900024414, 0.0)),
    Vector((-1.233402132987976, -3.851654291152954, 0.0)),
    Vector((-0.665885865688324, -4.152216911315918, 0.0)),
    Vector((0.007566885091364384, -4.296932220458984, 0.0)),
    Vector((0.7037202715873718, -4.107689380645752, 0.0)),
    Vector((2.0884599685668945, -3.462035894393921, 0.0)),
    Vector((0.0, 0.0, 2.0)),
    Vector((-0.46157968044281006, -0.22263896465301514, 2.0)),
    Vector((-1.0290957689285278, -0.6233890652656555, 2.0)),
    Vector((-1.513376235961914, -1.1020628213882446, 2.0)),
    Vector((-1.8690197467803955, -1.6809240579605103, 2.0)),
    Vector((-2.0279245376586914, -2.2931811809539795, 2.0)),
    Vector((-1.9144214391708374, -2.9165704250335693, 2.0)),
    Vector((-1.6420137882232666, -3.495431900024414, 2.0)),
    Vector((-1.233402132987976, -3.851654291152954, 2.0)),
    Vector((-0.665885865688324, -4.152216911315918, 2.0)),
    Vector((0.007566885091364384, -4.296932220458984, 2.0)),
    Vector((0.7037202715873718, -4.107689380645752, 2.0)),
    Vector((2.0884599685668945, -3.462035894393921, 2.0))
]
unitVectors = [
    Vector((-0.900698721408844, -0.43444421887397766, 0.0)),
    Vector((-0.8168658018112183, -0.5768277645111084, 0.0)),
    Vector((-0.7112118005752563, -0.7029778361320496, 0.0)),
    Vector((-0.5234794020652771, -0.8520383834838867, 0.0)),
    Vector((-0.2512161433696747, -0.9679309725761414, 0.0)),
    Vector((0.17912925779819489, -0.9838256239891052, 0.0)),
    Vector((0.4257999062538147, -0.9048173427581787, 0.0)),
    Vector((0.7537755966186523, -0.6571319103240967, 0.0)),
    Vector((0.8837152719497681, -0.46802496910095215, 0.0)),
    Vector((0.9776820540428162, -0.2100898176431656, 0.0)),
    Vector((0.9649806618690491, 0.26232102513313293, 0.0)),
    Vector((0.9063230752944946, 0.4225853383541107, 0.0)),
    Vector((-0.5165380835533142, 0.8562641739845276, 0.0))
]
holesInfo = None
firstVertIndex = 13
numPolygonVerts = 13
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