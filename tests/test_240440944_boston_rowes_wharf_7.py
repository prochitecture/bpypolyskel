import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((-45.66310501098633, -0.16683021187782288, 0.0)),
    Vector((-45.58098602294922, -21.85186767578125, 0.0)),
    Vector((0.08226129412651062, -21.68503761291504, 0.0)),
    Vector((0.06580900400876999, -18.044889450073242, 0.0)),
    Vector((11.615288734436035, -18.00035285949707, 0.0)),
    Vector((11.607059478759766, -16.219240188598633, 0.0)),
    Vector((12.495479583740234, -15.128307342529297, 0.0)),
    Vector((13.137114524841309, -13.837000846862793, 0.0)),
    Vector((13.5237398147583, -12.590221405029297, 0.0)),
    Vector((13.754067420959473, -11.109671592712402, 0.0)),
    Vector((13.75406551361084, -9.75157356262207, 0.0)),
    Vector((13.523730278015137, -8.014989852905273, 0.0)),
    Vector((12.816282272338867, -6.467650890350342, 0.0)),
    Vector((11.565910339355469, -4.83125638961792, 0.0)),
    Vector((11.557682037353516, -3.3284432888031006, 0.0)),
    Vector((0.016452215611934662, -3.3729805946350098, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((-45.66310501098633, -0.16683021187782288, 22.350650787353516)),
    Vector((-45.58098602294922, -21.85186767578125, 22.350650787353516)),
    Vector((0.08226129412651062, -21.68503761291504, 22.350650787353516)),
    Vector((0.06580900400876999, -18.044889450073242, 22.350650787353516)),
    Vector((11.615288734436035, -18.00035285949707, 22.350650787353516)),
    Vector((11.607059478759766, -16.219240188598633, 22.350650787353516)),
    Vector((12.495479583740234, -15.128307342529297, 22.350650787353516)),
    Vector((13.137114524841309, -13.837000846862793, 22.350650787353516)),
    Vector((13.5237398147583, -12.590221405029297, 22.350650787353516)),
    Vector((13.754067420959473, -11.109671592712402, 22.350650787353516)),
    Vector((13.75406551361084, -9.75157356262207, 22.350650787353516)),
    Vector((13.523730278015137, -8.014989852905273, 22.350650787353516)),
    Vector((12.816282272338867, -6.467650890350342, 22.350650787353516)),
    Vector((11.565910339355469, -4.83125638961792, 22.350650787353516)),
    Vector((11.557682037353516, -3.3284432888031006, 22.350650787353516)),
    Vector((0.016452215611934662, -3.3729805946350098, 22.350650787353516)),
    Vector((0.0, 0.0, 22.350650787353516))
]
unitVectors = [
    Vector((0.0037868693470954895, -0.9999929070472717, 0.0)),
    Vector((0.9999932646751404, 0.003653462277725339, 0.0)),
    Vector((-0.004519629757851362, 0.9999897480010986, 0.0)),
    Vector((0.9999926090240479, 0.0038561271503567696, 0.0)),
    Vector((-0.004620240069925785, 0.99998939037323, 0.0)),
    Vector((0.631464421749115, 0.7754048705101013, 0.0)),
    Vector((0.4449827969074249, 0.8955391049385071, 0.0)),
    Vector((0.2961851954460144, 0.9551305174827576, 0.0)),
    Vector((0.1537199467420578, 0.9881144762039185, 0.0)),
    Vector((-1.4044263707546634e-06, 1.0, 0.0)),
    Vector((-0.1314854621887207, 0.9913181662559509, 0.0)),
    Vector((-0.41580498218536377, 0.9094537496566772, 0.0)),
    Vector((-0.6071471571922302, 0.7945893406867981, 0.0)),
    Vector((-0.005475184414535761, 0.9999850392341614, 0.0)),
    Vector((-0.9999925494194031, -0.0038589450996369123, 0.0)),
    Vector((-0.004877591039985418, 0.9999881386756897, 0.0)),
    Vector((-0.9999933242797852, -0.003653476946055889, 0.0))
]
holesInfo = None
firstVertIndex = 17
numPolygonVerts = 17
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