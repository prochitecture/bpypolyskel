import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((-9.559392929077148, -2.471283435821533, 0.0)),
    Vector((0.730660080909729, -41.76707458496094, 0.0)),
    Vector((10.03980541229248, -39.01747131347656, 0.0)),
    Vector((8.138724327087402, -31.603595733642578, 0.0)),
    Vector((8.774667739868164, -31.42548370361328, 0.0)),
    Vector((7.962820053100586, -28.28627586364746, 0.0)),
    Vector((7.326877117156982, -28.475521087646484, 0.0)),
    Vector((3.0782251358032227, -11.95571231842041, 0.0)),
    Vector((3.727696657180786, -11.777600288391113, 0.0)),
    Vector((2.868497848510742, -8.471412658691406, 0.0)),
    Vector((2.2325572967529297, -8.694051742553711, 0.0)),
    Vector((0.0, 0.0, 10.825926780700684)),
    Vector((-9.559392929077148, -2.471283435821533, 10.825926780700684)),
    Vector((0.730660080909729, -41.76707458496094, 10.825926780700684)),
    Vector((10.03980541229248, -39.01747131347656, 10.825926780700684)),
    Vector((8.138724327087402, -31.603595733642578, 10.825926780700684)),
    Vector((8.774667739868164, -31.42548370361328, 10.825926780700684)),
    Vector((7.962820053100586, -28.28627586364746, 10.825926780700684)),
    Vector((7.326877117156982, -28.475521087646484, 10.825926780700684)),
    Vector((3.0782251358032227, -11.95571231842041, 10.825926780700684)),
    Vector((3.727696657180786, -11.777600288391113, 10.825926780700684)),
    Vector((2.868497848510742, -8.471412658691406, 10.825926780700684)),
    Vector((2.2325572967529297, -8.694051742553711, 10.825926780700684))
]
unitVectors = [
    Vector((-0.9681708216667175, -0.2502904236316681, 0.0)),
    Vector((0.25332018733024597, -0.9673824906349182, 0.0)),
    Vector((0.9590408802032471, 0.28326788544654846, 0.0)),
    Vector((-0.24838604032993317, 0.9686610698699951, 0.0)),
    Vector((0.962945282459259, 0.2696971595287323, 0.0)),
    Vector((-0.2503781020641327, 0.9681481719017029, 0.0)),
    Vector((-0.9584617614746094, -0.28522104024887085, 0.0)),
    Vector((-0.24907958507537842, 0.968483030796051, 0.0)),
    Vector((0.9643921852111816, 0.26447635889053345, 0.0)),
    Vector((-0.25152143836021423, 0.9678517580032349, 0.0)),
    Vector((-0.943830668926239, -0.3304296135902405, 0.0)),
    Vector((-0.2487216740846634, 0.9685749411582947, 0.0))
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