import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((-5.2588725090026855, -8.304431915283203, 0.0)),
    Vector((0.30509504675865173, -11.82213020324707, 0.0)),
    Vector((3.05094838142395, -7.480669021606445, 0.0)),
    Vector((4.905604839324951, -8.66065502166748, 0.0)),
    Vector((-0.321152925491333, -16.90943145751953, 0.0)),
    Vector((13.343921661376953, -25.5700740814209, 0.0)),
    Vector((16.73207664489746, -20.226730346679688, 0.0)),
    Vector((10.453526496887207, -16.25263786315918, 0.0)),
    Vector((12.292121887207031, -13.347195625305176, 0.0)),
    Vector((20.923118591308594, -18.81296157836914, 0.0)),
    Vector((23.436128616333008, -14.84997844696045, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((-5.2588725090026855, -8.304431915283203, 2.9766452312469482)),
    Vector((0.30509504675865173, -11.82213020324707, 2.9766452312469482)),
    Vector((3.05094838142395, -7.480669021606445, 2.9766452312469482)),
    Vector((4.905604839324951, -8.66065502166748, 2.9766452312469482)),
    Vector((-0.321152925491333, -16.90943145751953, 2.9766452312469482)),
    Vector((13.343921661376953, -25.5700740814209, 2.9766452312469482)),
    Vector((16.73207664489746, -20.226730346679688, 2.9766452312469482)),
    Vector((10.453526496887207, -16.25263786315918, 2.9766452312469482)),
    Vector((12.292121887207031, -13.347195625305176, 2.9766452312469482)),
    Vector((20.923118591308594, -18.81296157836914, 2.9766452312469482)),
    Vector((23.436128616333008, -14.84997844696045, 2.9766452312469482)),
    Vector((0.0, 0.0, 2.9766452312469482))
]
unitVectors = [
    Vector((0.8452410101890564, -0.5343853831291199, 0.0)),
    Vector((0.5345325469970703, 0.8451478481292725, 0.0)),
    Vector((0.8437129259109497, -0.5367945432662964, 0.0)),
    Vector((-0.535237193107605, -0.8447018265724182, 0.0)),
    Vector((0.8446487188339233, -0.5353209376335144, 0.0)),
    Vector((0.5355074405670166, 0.8445305228233337, 0.0)),
    Vector((-0.8449602723121643, 0.5348289012908936, 0.0)),
    Vector((0.5347369313240051, 0.8450185656547546, 0.0)),
    Vector((0.8448426723480225, -0.5350149273872375, 0.0)),
    Vector((0.5355265736579895, 0.84451824426651, 0.0)),
    Vector((-0.8447034955024719, 0.5352346897125244, 0.0)),
    Vector((-0.535008430480957, -0.8448467254638672, 0.0))
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