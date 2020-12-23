import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((10.749798774719238, -0.7124329209327698, 0.0)),
    Vector((11.122574806213379, 3.8182711601257324, 0.0)),
    Vector((11.630918502807617, 3.818272352218628, 0.0)),
    Vector((11.942695617675781, 7.224649429321289, 0.0)),
    Vector((11.407238960266113, 7.291440010070801, 0.0)),
    Vector((11.786791801452637, 11.911199569702148, 0.0)),
    Vector((1.0234647989273071, 12.846269607543945, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((10.749798774719238, -0.7124329209327698, 5.341334819793701)),
    Vector((11.122574806213379, 3.8182711601257324, 5.341334819793701)),
    Vector((11.630918502807617, 3.818272352218628, 5.341334819793701)),
    Vector((11.942695617675781, 7.224649429321289, 5.341334819793701)),
    Vector((11.407238960266113, 7.291440010070801, 5.341334819793701)),
    Vector((11.786791801452637, 11.911199569702148, 5.341334819793701)),
    Vector((1.0234647989273071, 12.846269607543945, 5.341334819793701)),
    Vector((0.0, 0.0, 5.341334819793701))
]
unitVectors = [
    Vector((0.08200063556432724, 0.9966322779655457, 0.0)),
    Vector((1.0, 2.3450529624824412e-06, 0.0)),
    Vector((0.09114649891853333, 0.9958374500274658, 0.0)),
    Vector((-0.9923101663589478, 0.12377654016017914, 0.0)),
    Vector((0.08188267797231674, 0.996641993522644, 0.0)),
    Vector((-0.9962475895881653, 0.08654956519603729, 0.0)),
    Vector((-0.07941854745149612, -0.9968413710594177, 0.0)),
    Vector((0.9978110194206238, -0.06612899899482727, 0.0))
]
holesInfo = None
firstVertIndex = 8
numPolygonVerts = 8
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