import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((9.276623725891113, -8.660648345947266, 0.0)),
    Vector((16.893871307373047, -0.7792097330093384, 0.0)),
    Vector((33.06544876098633, -15.885189056396484, 0.0)),
    Vector((41.905723571777344, -7.1131510734558105, 0.0)),
    Vector((23.559825897216797, 9.45107650756836, 0.0)),
    Vector((21.00643539428711, 10.230302810668945, 0.0)),
    Vector((17.895164489746094, 10.564249992370605, 0.0)),
    Vector((14.447734832763672, 10.564239501953125, 0.0)),
    Vector((11.222029685974121, 9.673675537109375, 0.0)),
    Vector((8.110761642456055, 8.449155807495117, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((9.276623725891113, -8.660648345947266, 11.988847732543945)),
    Vector((16.893871307373047, -0.7792097330093384, 11.988847732543945)),
    Vector((33.06544876098633, -15.885189056396484, 11.988847732543945)),
    Vector((41.905723571777344, -7.1131510734558105, 11.988847732543945)),
    Vector((23.559825897216797, 9.45107650756836, 11.988847732543945)),
    Vector((21.00643539428711, 10.230302810668945, 11.988847732543945)),
    Vector((17.895164489746094, 10.564249992370605, 11.988847732543945)),
    Vector((14.447734832763672, 10.564239501953125, 11.988847732543945)),
    Vector((11.222029685974121, 9.673675537109375, 11.988847732543945)),
    Vector((8.110761642456055, 8.449155807495117, 11.988847732543945)),
    Vector((0.0, 0.0, 11.988847732543945))
]
unitVectors = [
    Vector((0.6949524879455566, 0.719055712223053, 0.0)),
    Vector((0.7307732701301575, -0.6826202273368835, 0.0)),
    Vector((0.7098410725593567, 0.7043619155883789, 0.0)),
    Vector((-0.742228627204895, 0.6701468229293823, 0.0)),
    Vector((-0.9564537405967712, 0.29188403487205505, 0.0)),
    Vector((-0.994288980960846, 0.1067216619849205, 0.0)),
    Vector((-1.0, -3.042967819055775e-06, 0.0)),
    Vector((-0.9639378786087036, -0.266127347946167, 0.0)),
    Vector((-0.9305237531661987, -0.3662315905094147, 0.0)),
    Vector((-0.6925128102302551, -0.721405565738678, 0.0)),
    Vector((0.7309583425521851, -0.6824221014976501, 0.0))
]
holesInfo = None
firstVertIndex = 11
numPolygonVerts = 11
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