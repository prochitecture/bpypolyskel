import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((-13.019964218139648, 8.659543709654827e-06, 0.0)),
    Vector((-13.057278633117676, -6.378598213195801, 0.0)),
    Vector((-13.896678924560547, -8.56045913696289, 0.0)),
    Vector((-13.066610336303711, -9.918558120727539, 0.0)),
    Vector((-12.898740768432617, -17.187721252441406, 0.0)),
    Vector((-10.893515586853027, -19.380718231201172, 0.0)),
    Vector((-7.246799468994141, -19.39185333251953, 0.0)),
    Vector((-7.246800422668457, -20.605234146118164, 0.0)),
    Vector((-0.009326641447842121, -20.616369247436523, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((-13.019964218139648, 8.659543709654827e-06, 4.0)),
    Vector((-13.057278633117676, -6.378598213195801, 4.0)),
    Vector((-13.896678924560547, -8.56045913696289, 4.0)),
    Vector((-13.066610336303711, -9.918558120727539, 4.0)),
    Vector((-12.898740768432617, -17.187721252441406, 4.0)),
    Vector((-10.893515586853027, -19.380718231201172, 4.0)),
    Vector((-7.246799468994141, -19.39185333251953, 4.0)),
    Vector((-7.246800422668457, -20.605234146118164, 4.0)),
    Vector((-0.009326641447842121, -20.616369247436523, 4.0)),
    Vector((0.0, 0.0, 4.0))
]
unitVectors = [
    Vector((-0.005849831737577915, -0.9999828934669495, 0.0)),
    Vector((-0.35906219482421875, -0.9333136677742004, 0.0)),
    Vector((0.5215045213699341, -0.8532485365867615, 0.0)),
    Vector((0.02308722957968712, -0.9997335076332092, 0.0)),
    Vector((0.674805760383606, -0.737995445728302, 0.0)),
    Vector((0.9999954104423523, -0.0030534458346664906, 0.0)),
    Vector((-7.859645734242804e-07, -1.0, 0.0)),
    Vector((0.9999988079071045, -0.0015385323204100132, 0.0)),
    Vector((0.0004523900570347905, 0.9999999403953552, 0.0)),
    Vector((-1.0, 6.650973887190048e-07, 0.0))
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