import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((22.110103607177734, -24.17854881286621, 0.0)),
    Vector((34.44038772583008, -12.757105827331543, 0.0)),
    Vector((31.2120361328125, -9.250561714172363, 0.0)),
    Vector((67.92565155029297, 25.203149795532227, 0.0)),
    Vector((48.80339050292969, 45.69686508178711, 0.0)),
    Vector((36.305660247802734, 34.175201416015625, 0.0)),
    Vector((44.139644622802734, 25.69271469116211, 0.0)),
    Vector((20.00393295288086, 3.272829294204712, 0.0)),
    Vector((12.053353309631348, 11.566108703613281, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((22.110103607177734, -24.17854881286621, 14.622499465942383)),
    Vector((34.44038772583008, -12.757105827331543, 14.622499465942383)),
    Vector((31.2120361328125, -9.250561714172363, 14.622499465942383)),
    Vector((67.92565155029297, 25.203149795532227, 14.622499465942383)),
    Vector((48.80339050292969, 45.69686508178711, 14.622499465942383)),
    Vector((36.305660247802734, 34.175201416015625, 14.622499465942383)),
    Vector((44.139644622802734, 25.69271469116211, 14.622499465942383)),
    Vector((20.00393295288086, 3.272829294204712, 14.622499465942383)),
    Vector((12.053353309631348, 11.566108703613281, 14.622499465942383)),
    Vector((0.0, 0.0, 14.622499465942383))
]
unitVectors = [
    Vector((0.7336267232894897, 0.6795525550842285, 0.0)),
    Vector((-0.6773213744163513, 0.7356873154640198, 0.0)),
    Vector((0.7291932702064514, 0.6843078136444092, 0.0)),
    Vector((-0.6822189688682556, 0.7311478853225708, 0.0)),
    Vector((-0.7352343797683716, -0.677812933921814, 0.0)),
    Vector((0.6784669756889343, -0.7346309423446655, 0.0)),
    Vector((-0.7326701283454895, -0.6805840730667114, 0.0)),
    Vector((-0.6920347809791565, 0.7218641042709351, 0.0)),
    Vector((-0.7215401530265808, -0.6923726201057434, 0.0)),
    Vector((0.674835741519928, -0.7379679679870605, 0.0))
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