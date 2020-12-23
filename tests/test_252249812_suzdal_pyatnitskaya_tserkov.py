import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((-2.5737411975860596, -12.467782020568848, 0.0)),
    Vector((13.447500228881836, -15.684894561767578, 0.0)),
    Vector((13.57064437866211, -15.072637557983398, 0.0)),
    Vector((16.464567184448242, -15.662620544433594, 0.0)),
    Vector((18.71197509765625, -15.66261100769043, 0.0)),
    Vector((20.79928970336914, -14.816573143005371, 0.0)),
    Vector((22.40017318725586, -13.224696159362793, 0.0)),
    Vector((23.26833724975586, -11.154149055480957, 0.0)),
    Vector((23.27448272705078, -8.883231163024902, 0.0)),
    Vector((22.418611526489258, -6.80156135559082, 0.0)),
    Vector((20.836185455322266, -5.198568820953369, 0.0)),
    Vector((18.748868942260742, -4.330286502838135, 0.0)),
    Vector((15.818008422851562, -3.751437187194824, 0.0)),
    Vector((15.928837776184082, -3.1948394775390625, 0.0)),
    Vector((0.0, 0.0, 2.8653392791748047)),
    Vector((-2.5737411975860596, -12.467782020568848, 2.8653392791748047)),
    Vector((13.447500228881836, -15.684894561767578, 2.8653392791748047)),
    Vector((13.57064437866211, -15.072637557983398, 2.8653392791748047)),
    Vector((16.464567184448242, -15.662620544433594, 2.8653392791748047)),
    Vector((18.71197509765625, -15.66261100769043, 2.8653392791748047)),
    Vector((20.79928970336914, -14.816573143005371, 2.8653392791748047)),
    Vector((22.40017318725586, -13.224696159362793, 2.8653392791748047)),
    Vector((23.26833724975586, -11.154149055480957, 2.8653392791748047)),
    Vector((23.27448272705078, -8.883231163024902, 2.8653392791748047)),
    Vector((22.418611526489258, -6.80156135559082, 2.8653392791748047)),
    Vector((20.836185455322266, -5.198568820953369, 2.8653392791748047)),
    Vector((18.748868942260742, -4.330286502838135, 2.8653392791748047)),
    Vector((15.818008422851562, -3.751437187194824, 2.8653392791748047)),
    Vector((15.928837776184082, -3.1948394775390625, 2.8653392791748047))
]
unitVectors = [
    Vector((-0.20216870307922363, -0.979350745677948, 0.0)),
    Vector((0.9804289937019348, -0.1968730241060257, 0.0)),
    Vector((0.19718259572982788, 0.9803667068481445, 0.0)),
    Vector((0.9798446893692017, -0.1997605860233307, 0.0)),
    Vector((1.0, 4.243441253493074e-06, 0.0)),
    Vector((0.9267656803131104, 0.37564000487327576, 0.0)),
    Vector((0.7090986371040344, 0.7051092982292175, 0.0)),
    Vector((0.38667744398117065, 0.922214925289154, 0.0)),
    Vector((0.0027061544824391603, 0.9999963045120239, 0.0)),
    Vector((-0.3802608549594879, 0.924879252910614, 0.0)),
    Vector((-0.7025267481803894, 0.7116573452949524, 0.0)),
    Vector((-0.9233018159866333, 0.38407525420188904, 0.0)),
    Vector((-0.9810492992401123, 0.19375869631767273, 0.0)),
    Vector((0.19528554379940033, 0.9807463884353638, 0.0)),
    Vector((-0.9804731011390686, 0.19665302336215973, 0.0))
]
holesInfo = None
firstVertIndex = 15
numPolygonVerts = 15
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