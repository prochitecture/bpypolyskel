import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((8.8688325881958, -6.807755470275879, 0.0)),
    Vector((17.987651824951172, 5.0718584060668945, 0.0)),
    Vector((9.118826866149902, 11.879590034484863, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((8.8688325881958, -6.807755470275879, 20.076494216918945)),
    Vector((17.987651824951172, 5.0718584060668945, 20.076494216918945)),
    Vector((9.118826866149902, 11.879590034484863, 20.076494216918945)),
    Vector((0.0, 0.0, 20.076494216918945)),
    Vector((5.004627704620361, 1.589969277381897, 0.0)),
    Vector((9.195164680480957, 6.993898391723633, 0.0)),
    Vector((13.324121475219727, 3.792056083679199, 0.0)),
    Vector((9.133585929870605, -1.611877679824829, 0.0)),
    Vector((5.004627704620361, 1.589969277381897, 20.076494216918945)),
    Vector((9.195164680480957, 6.993898391723633, 20.076494216918945)),
    Vector((13.324121475219727, 3.792056083679199, 20.076494216918945)),
    Vector((9.133585929870605, -1.611877679824829, 20.076494216918945))
]
unitVectors = [
    Vector((0.608898937702179, 0.7932478785514832, 0.0)),
    Vector((-0.7932477593421936, 0.6088988780975342, 0.0)),
    Vector((-0.6088999509811401, -0.7932469844818115, 0.0)),
    Vector((0.7932470440864563, -0.6088999509811401, 0.0)),
    Vector((0.6127992868423462, 0.7902385592460632, 0.0)),
    Vector((0.7902388572692871, -0.6127989292144775, 0.0)),
    Vector((-0.6127988696098328, -0.7902389168739319, 0.0)),
    Vector((-0.7902384996414185, 0.612799346446991, 0.0))
]
holesInfo = [
    (12, 4)
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