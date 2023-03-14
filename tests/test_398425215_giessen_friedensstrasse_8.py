import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 7.081154551613622e-10, 0.0)),
    Vector((-6.283901214599609, -5.810873508453369, 0.0)),
    Vector((-4.014913082122803, -8.271037101745605, 0.0)),
    Vector((-4.72176456451416, -9.028008460998535, 0.0)),
    Vector((-5.061053276062012, -9.517813682556152, 0.0)),
    Vector((-5.2024245262146, -10.130070686340332, 0.0)),
    Vector((-5.0681233406066895, -10.820252418518066, 0.0)),
    Vector((-4.820725917816162, -11.221002578735352, 0.0)),
    Vector((-4.248176574707031, -11.65514850616455, 0.0)),
    Vector((-3.5837364196777344, -11.799864768981934, 0.0)),
    Vector((-2.891021966934204, -11.644018173217773, 0.0)),
    Vector((-2.403294324874878, -11.298927307128906, 0.0)),
    Vector((-1.8166075944900513, -10.675539016723633, 0.0)),
    Vector((0.4029053747653961, -13.04664421081543, 0.0)),
    Vector((6.686808109283447, -7.235762596130371, 0.0)),
    Vector((0.0, 7.081154551613622e-10, 5.718061923980713)),
    Vector((-6.283901214599609, -5.810873508453369, 5.718061923980713)),
    Vector((-4.014913082122803, -8.271037101745605, 5.718061923980713)),
    Vector((-4.72176456451416, -9.028008460998535, 5.718061923980713)),
    Vector((-5.061053276062012, -9.517813682556152, 5.718061923980713)),
    Vector((-5.2024245262146, -10.130070686340332, 5.718061923980713)),
    Vector((-5.0681233406066895, -10.820252418518066, 5.718061923980713)),
    Vector((-4.820725917816162, -11.221002578735352, 5.718061923980713)),
    Vector((-4.248176574707031, -11.65514850616455, 5.718061923980713)),
    Vector((-3.5837364196777344, -11.799864768981934, 5.718061923980713)),
    Vector((-2.891021966934204, -11.644018173217773, 5.718061923980713)),
    Vector((-2.403294324874878, -11.298927307128906, 5.718061923980713)),
    Vector((-1.8166075944900513, -10.675539016723633, 5.718061923980713)),
    Vector((0.4029053747653961, -13.04664421081543, 5.718061923980713)),
    Vector((6.686808109283447, -7.235762596130371, 5.718061923980713))
]
unitVectors = [
    Vector((-0.7342004776000977, -0.6789327263832092, 0.0)),
    Vector((0.6779683828353882, -0.7350911498069763, 0.0)),
    Vector((-0.6824962496757507, -0.7308892011642456, 0.0)),
    Vector((-0.5694286823272705, -0.8220407366752625, 0.0)),
    Vector((-0.2249821424484253, -0.9743627905845642, 0.0)),
    Vector((0.19100557267665863, -0.9815889596939087, 0.0)),
    Vector((0.5253011584281921, -0.8509163856506348, 0.0)),
    Vector((0.7968264818191528, -0.6042081713676453, 0.0)),
    Vector((0.9770930409431458, -0.2128126323223114, 0.0)),
    Vector((0.9756140112876892, 0.21949322521686554, 0.0)),
    Vector((0.8163266181945801, 0.5775905251502991, 0.0)),
    Vector((0.6853450536727905, 0.7282184362411499, 0.0)),
    Vector((0.683384120464325, -0.7300590872764587, 0.0)),
    Vector((0.734200119972229, 0.6789332032203674, 0.0)),
    Vector((-0.6786987781524658, 0.734416663646698, 0.0))
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