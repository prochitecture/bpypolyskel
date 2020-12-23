import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((1.4818518161773682, 0.8794242143630981, 0.0)),
    Vector((2.637950897216797, 2.1595988273620605, 0.0)),
    Vector((3.3533263206481934, 3.7292041778564453, 0.0)),
    Vector((3.5768799781799316, 5.443524360656738, 0.0)),
    Vector((3.2766761779785156, 7.135580539703369, 0.0)),
    Vector((2.484652280807495, 8.671789169311523, 0.0)),
    Vector((1.2710685729980469, 9.896303176879883, 0.0)),
    Vector((-0.18523108959197998, 10.085545539855957, 0.0)),
    Vector((-1.4626901149749756, 0.1892433762550354, 0.0)),
    Vector((0.0, 0.0, 3.1444664001464844)),
    Vector((1.4818518161773682, 0.8794242143630981, 3.1444664001464844)),
    Vector((2.637950897216797, 2.1595988273620605, 3.1444664001464844)),
    Vector((3.3533263206481934, 3.7292041778564453, 3.1444664001464844)),
    Vector((3.5768799781799316, 5.443524360656738, 3.1444664001464844)),
    Vector((3.2766761779785156, 7.135580539703369, 3.1444664001464844)),
    Vector((2.484652280807495, 8.671789169311523, 3.1444664001464844)),
    Vector((1.2710685729980469, 9.896303176879883, 3.1444664001464844)),
    Vector((-0.18523108959197998, 10.085545539855957, 3.1444664001464844)),
    Vector((-1.4626901149749756, 0.1892433762550354, 3.1444664001464844))
]
unitVectors = [
    Vector((0.859963059425354, 0.5103562474250793, 0.0)),
    Vector((0.6702263355255127, 0.7421567440032959, 0.0)),
    Vector((0.4147244393825531, 0.9099469780921936, 0.0)),
    Vector((0.12930884957313538, 0.9916043281555176, 0.0)),
    Vector((-0.17469137907028198, 0.9846232533454895, 0.0)),
    Vector((-0.45825091004371643, 0.8888229131698608, 0.0)),
    Vector((-0.7039296627044678, 0.7102696895599365, 0.0)),
    Vector((-0.9916623830795288, 0.12886394560337067, 0.0)),
    Vector((-0.12802228331565857, -0.9917712807655334, 0.0)),
    Vector((0.9917339086532593, -0.128310889005661, 0.0))
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