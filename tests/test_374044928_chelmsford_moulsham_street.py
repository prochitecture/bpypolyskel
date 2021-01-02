import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((-0.248225599527359, -0.24490287899971008, 0.0)),
    Vector((1.3583461046218872, -1.7031880617141724, 0.0)),
    Vector((1.5858861207962036, -1.3469655513763428, 0.0)),
    Vector((1.6824182271957397, -1.0018751621246338, 0.0)),
    Vector((1.6548374891281128, -0.6345208287239075, 0.0)),
    Vector((1.5100390911102295, -0.30056241154670715, 0.0)),
    Vector((1.2824989557266235, -0.044527631253004074, 0.0)),
    Vector((0.9860071539878845, 0.1224515363574028, 0.0)),
    Vector((0.6481446027755737, 0.18924318253993988, 0.0)),
    Vector((0.31028199195861816, 0.14471535384655, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((-0.248225599527359, -0.24490287899971008, 11.0)),
    Vector((1.3583461046218872, -1.7031880617141724, 11.0)),
    Vector((1.5858861207962036, -1.3469655513763428, 11.0)),
    Vector((1.6824182271957397, -1.0018751621246338, 11.0)),
    Vector((1.6548374891281128, -0.6345208287239075, 11.0)),
    Vector((1.5100390911102295, -0.30056241154670715, 11.0)),
    Vector((1.2824989557266235, -0.044527631253004074, 11.0)),
    Vector((0.9860071539878845, 0.1224515363574028, 11.0)),
    Vector((0.6481446027755737, 0.18924318253993988, 11.0)),
    Vector((0.31028199195861816, 0.14471535384655, 11.0)),
    Vector((0.0, 0.0, 11.0))
]
unitVectors = [
    Vector((0.7404524683952332, -0.6721087694168091, 0.0)),
    Vector((0.5383110046386719, 0.8427462577819824, 0.0)),
    Vector((0.26938873529434204, 0.963031530380249, 0.0)),
    Vector((-0.07486867159605026, 0.9971933960914612, 0.0)),
    Vector((-0.3977995812892914, 0.9174723029136658, 0.0)),
    Vector((-0.6642882823944092, 0.7474765181541443, 0.0)),
    Vector((-0.8713211417198181, 0.49071332812309265, 0.0)),
    Vector((-0.9810142517089844, 0.1939355432987213, 0.0)),
    Vector((-0.9914268851280212, -0.13066282868385315, 0.0)),
    Vector((-0.9062759280204773, -0.4226866066455841, 0.0)),
    Vector((-0.7118551731109619, -0.7023263573646545, 0.0))
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