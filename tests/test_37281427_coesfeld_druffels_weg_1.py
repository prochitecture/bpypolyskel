import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((-3.733499765396118, 0.7347100377082825, 0.0)),
    Vector((-3.108959913253784, 4.007502555847168, 0.0)),
    Vector((-20.74697494506836, 7.39165735244751, 0.0)),
    Vector((-22.016666412353516, 0.8794724941253662, 0.0)),
    Vector((-18.11845588684082, 0.12248430401086807, 0.0)),
    Vector((-18.564563751220703, -2.1929595470428467, 0.0)),
    Vector((-5.277691841125488, -4.7533392906188965, 0.0)),
    Vector((-3.0815157890319824, -9.061405181884766, 0.0)),
    Vector((-2.7864043712615967, -9.528947830200195, 0.0)),
    Vector((-2.4638404846191406, -9.896302223205566, 0.0)),
    Vector((-1.9696999788284302, -10.297052383422852, 0.0)),
    Vector((-1.1186798810958862, -10.708934783935547, 0.0)),
    Vector((-0.26079654693603516, -10.864782333374023, 0.0)),
    Vector((0.5696345567703247, -10.775726318359375, 0.0)),
    Vector((1.3863394260406494, -10.486295700073242, 0.0)),
    Vector((1.8804800510406494, -10.174601554870605, 0.0)),
    Vector((2.2785377502441406, -9.829510688781738, 0.0)),
    Vector((2.8344457149505615, -9.172725677490234, 0.0)),
    Vector((3.1570091247558594, -8.404620170593262, 0.0)),
    Vector((3.2736809253692627, -7.892550945281982, 0.0)),
    Vector((3.3354482650756836, -7.380481243133545, 0.0)),
    Vector((3.294269323348999, -6.823883533477783, 0.0)),
    Vector((3.1501448154449463, -6.144834995269775, 0.0)),
    Vector((1.9971497058868408, -3.862785816192627, 0.0)),
    Vector((2.6285507678985596, -3.52882719039917, 0.0)),
    Vector((2.1206841468811035, -2.538084030151367, 0.0)),
    Vector((1.4824200868606567, -2.872042655944824, 0.0)),
    Vector((0.0, 0.0, 2.912221908569336)),
    Vector((-3.733499765396118, 0.7347100377082825, 2.912221908569336)),
    Vector((-3.108959913253784, 4.007502555847168, 2.912221908569336)),
    Vector((-20.74697494506836, 7.39165735244751, 2.912221908569336)),
    Vector((-22.016666412353516, 0.8794724941253662, 2.912221908569336)),
    Vector((-18.11845588684082, 0.12248430401086807, 2.912221908569336)),
    Vector((-18.564563751220703, -2.1929595470428467, 2.912221908569336)),
    Vector((-5.277691841125488, -4.7533392906188965, 2.912221908569336)),
    Vector((-3.0815157890319824, -9.061405181884766, 2.912221908569336)),
    Vector((-2.7864043712615967, -9.528947830200195, 2.912221908569336)),
    Vector((-2.4638404846191406, -9.896302223205566, 2.912221908569336)),
    Vector((-1.9696999788284302, -10.297052383422852, 2.912221908569336)),
    Vector((-1.1186798810958862, -10.708934783935547, 2.912221908569336)),
    Vector((-0.26079654693603516, -10.864782333374023, 2.912221908569336)),
    Vector((0.5696345567703247, -10.775726318359375, 2.912221908569336)),
    Vector((1.3863394260406494, -10.486295700073242, 2.912221908569336)),
    Vector((1.8804800510406494, -10.174601554870605, 2.912221908569336)),
    Vector((2.2785377502441406, -9.829510688781738, 2.912221908569336)),
    Vector((2.8344457149505615, -9.172725677490234, 2.912221908569336)),
    Vector((3.1570091247558594, -8.404620170593262, 2.912221908569336)),
    Vector((3.2736809253692627, -7.892550945281982, 2.912221908569336)),
    Vector((3.3354482650756836, -7.380481243133545, 2.912221908569336)),
    Vector((3.294269323348999, -6.823883533477783, 2.912221908569336)),
    Vector((3.1501448154449463, -6.144834995269775, 2.912221908569336)),
    Vector((1.9971497058868408, -3.862785816192627, 2.912221908569336)),
    Vector((2.6285507678985596, -3.52882719039917, 2.912221908569336)),
    Vector((2.1206841468811035, -2.538084030151367, 2.912221908569336)),
    Vector((1.4824200868606567, -2.872042655944824, 2.912221908569336))
]
unitVectors = [
    Vector((-0.9811820387840271, 0.19308538734912872, 0.0)),
    Vector((0.18744538724422455, 0.9822749495506287, 0.0)),
    Vector((-0.9820865988731384, 0.18843010067939758, 0.0)),
    Vector((-0.1913682371377945, -0.9815182685852051, 0.0)),
    Vector((0.9816624522209167, -0.19062769412994385, 0.0)),
    Vector((-0.18918690085411072, -0.9819411039352417, 0.0)),
    Vector((0.9819349646568298, -0.18921883404254913, 0.0)),
    Vector((0.4541722238063812, -0.8909139037132263, 0.0)),
    Vector((0.5337619185447693, -0.8456347584724426, 0.0)),
    Vector((0.65981125831604, -0.7514312267303467, 0.0)),
    Vector((0.7766821384429932, -0.6298927068710327, 0.0)),
    Vector((0.9001184105873108, -0.43564534187316895, 0.0)),
    Vector((0.9838964343070984, -0.1787397414445877, 0.0)),
    Vector((0.9942987561225891, 0.10662929713726044, 0.0)),
    Vector((0.9425614476203918, 0.33403271436691284, 0.0)),
    Vector((0.8457937836647034, 0.5335100293159485, 0.0)),
    Vector((0.7555880546569824, 0.6550471186637878, 0.0)),
    Vector((0.6460552215576172, 0.7632907032966614, 0.0)),
    Vector((0.3871907591819763, 0.9219996929168701, 0.0)),
    Vector((0.222150519490242, 0.9750123620033264, 0.0)),
    Vector((0.1197548508644104, 0.9928034543991089, 0.0)),
    Vector((-0.07378166168928146, 0.9972743391990662, 0.0)),
    Vector((-0.20761987566947937, 0.9782095551490784, 0.0)),
    Vector((-0.45095518231391907, 0.8925465941429138, 0.0)),
    Vector((0.8839687705039978, 0.46754592657089233, 0.0)),
    Vector((-0.45616957545280457, 0.8898928761482239, 0.0)),
    Vector((-0.886042594909668, -0.463603675365448, 0.0)),
    Vector((-0.45866137742996216, 0.8886111974716187, 0.0))
]
holesInfo = None
firstVertIndex = 28
numPolygonVerts = 28
faces = bpypolyskel.polygonize(verts, firstVertIndex, numPolygonVerts, holesInfo, 0.0, 0.5, None, unitVectors)
faces = None


@pytest.mark.timeout(10)
def test_polygonize():
    global faces
    faces = bpypolyskel.polygonize(verts, firstVertIndex, numPolygonVerts, holesInfo, 0.0, 0.5, None, unitVectors)


def test_numVertsInFace():
    for face in faces:
        assert len(face) >= 3


def test_duplication():
    for face in faces:
        assert len(face) == len(set(face))