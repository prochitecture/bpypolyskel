import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((9.351438522338867, -7.963322162628174, 0.0)),
    Vector((17.75308609008789, 5.041026592254639, 0.0)),
    Vector((9.570586204528809, 10.95870304107666, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((9.351438522338867, -7.963322162628174, 8.969878196716309)),
    Vector((17.75308609008789, 5.041026592254639, 8.969878196716309)),
    Vector((9.570586204528809, 10.95870304107666, 8.969878196716309)),
    Vector((0.0, 0.0, 8.969878196716309)),
    Vector((5.150627136230469, 0.7305461764335632, 0.0)),
    Vector((9.89939022064209, 5.7715535163879395, 0.0)),
    Vector((13.771469116210938, 2.4474222660064697, 0.0)),
    Vector((9.31493854522705, -2.6301190853118896, 0.0)),
    Vector((5.150627136230469, 0.7305461764335632, 8.969878196716309)),
    Vector((9.89939022064209, 5.7715535163879395, 8.969878196716309)),
    Vector((13.771469116210938, 2.4474222660064697, 8.969878196716309)),
    Vector((9.31493854522705, -2.6301190853118896, 8.969878196716309))
]
unitVectors = [
    Vector((0.5426624417304993, 0.8399508595466614, 0.0)),
    Vector((-0.8102986812591553, 0.5860171318054199, 0.0)),
    Vector((-0.6577927470207214, -0.7531989812850952, 0.0)),
    Vector((0.7613524198532104, -0.6483381986618042, 0.0)),
    Vector((0.6856927275657654, 0.7278910875320435, 0.0)),
    Vector((0.7587522864341736, -0.6513793468475342, 0.0)),
    Vector((-0.6596508622169495, -0.7515721917152405, 0.0)),
    Vector((-0.7781984210014343, 0.6280184984207153, 0.0))
]
holesInfo = [
    (12, 4)
]
firstVertIndex = 4
numPolygonVerts = 4
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