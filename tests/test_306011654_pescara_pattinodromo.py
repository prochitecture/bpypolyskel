import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((-3.1037802696228027, -8.51594066619873, 0.0)),
    Vector((-2.6685965061187744, -15.117186546325684, 0.0)),
    Vector((-0.45982012152671814, -21.284286499023438, 0.0)),
    Vector((4.384716510772705, -26.57196044921875, 0.0)),
    Vector((11.873231887817383, -32.30490493774414, 0.0)),
    Vector((20.084325790405273, -35.221458435058594, 0.0)),
    Vector((27.728853225708008, -35.38841247558594, 0.0)),
    Vector((33.67367172241211, -32.96162033081055, 0.0)),
    Vector((38.13226318359375, -28.141462326049805, 0.0)),
    Vector((69.00550079345703, 15.25111198425293, 0.0)),
    Vector((70.67227172851562, 21.874637603759766, 0.0)),
    Vector((70.67219543457031, 29.366439819335938, 0.0)),
    Vector((67.59300231933594, 35.75614929199219, 0.0)),
    Vector((64.28392791748047, 40.153236389160156, 0.0)),
    Vector((58.33912658691406, 44.56143569946289, 0.0)),
    Vector((50.850677490234375, 47.42228698730469, 0.0)),
    Vector((43.583946228027344, 47.867515563964844, 0.0)),
    Vector((35.873836517333984, 45.885986328125, 0.0)),
    Vector((30.29037857055664, 41.321861267089844, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((-3.1037802696228027, -8.51594066619873, 6.0)),
    Vector((-2.6685965061187744, -15.117186546325684, 6.0)),
    Vector((-0.45982012152671814, -21.284286499023438, 6.0)),
    Vector((4.384716510772705, -26.57196044921875, 6.0)),
    Vector((11.873231887817383, -32.30490493774414, 6.0)),
    Vector((20.084325790405273, -35.221458435058594, 6.0)),
    Vector((27.728853225708008, -35.38841247558594, 6.0)),
    Vector((33.67367172241211, -32.96162033081055, 6.0)),
    Vector((38.13226318359375, -28.141462326049805, 6.0)),
    Vector((69.00550079345703, 15.25111198425293, 6.0)),
    Vector((70.67227172851562, 21.874637603759766, 6.0)),
    Vector((70.67219543457031, 29.366439819335938, 6.0)),
    Vector((67.59300231933594, 35.75614929199219, 6.0)),
    Vector((64.28392791748047, 40.153236389160156, 6.0)),
    Vector((58.33912658691406, 44.56143569946289, 6.0)),
    Vector((50.850677490234375, 47.42228698730469, 6.0)),
    Vector((43.583946228027344, 47.867515563964844, 6.0)),
    Vector((35.873836517333984, 45.885986328125, 6.0)),
    Vector((30.29037857055664, 41.321861267089844, 6.0)),
    Vector((0.0, 0.0, 6.0))
]
unitVectors = [
    Vector((0.06578169763088226, -0.9978340268135071, 0.0)),
    Vector((0.3371811807155609, -0.9414398074150085, 0.0)),
    Vector((0.6755353212356567, -0.7373275756835938, 0.0)),
    Vector((0.794028639793396, -0.6078804135322571, 0.0)),
    Vector((0.9423213005065918, -0.33470943570137024, 0.0)),
    Vector((0.9997616410255432, -0.0218344759196043, 0.0)),
    Vector((0.9258294105529785, 0.3779418170452118, 0.0)),
    Vector((0.6790375113487244, 0.7341036200523376, 0.0)),
    Vector((0.5797269940376282, 0.8148108124732971, 0.0)),
    Vector((0.24403591454029083, 0.9697661995887756, 0.0)),
    Vector((-1.0183657650486566e-05, 1.0, 0.0)),
    Vector((-0.434120774269104, 0.9008547067642212, 0.0)),
    Vector((-0.6013085842132568, 0.7990168929100037, 0.0)),
    Vector((-0.8032570481300354, 0.5956325531005859, 0.0)),
    Vector((-0.9341508150100708, 0.35687848925590515, 0.0)),
    Vector((-0.9981282353401184, 0.06115476414561272, 0.0)),
    Vector((-0.9685252904891968, -0.248914897441864, 0.0)),
    Vector((-0.7742397785186768, -0.6328922510147095, 0.0)),
    Vector((-0.5912072658538818, -0.8065195679664612, 0.0)),
    Vector((-0.34243232011795044, -0.9395424723625183, 0.0))
]
holesInfo = None
firstVertIndex = 20
numPolygonVerts = 20
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