import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((-4.619345664978027, -11.432509422302246, 0.0)),
    Vector((-1.7068554162979126, -12.59023380279541, 0.0)),
    Vector((-1.4697920083999634, -12.00024127960205, 0.0)),
    Vector((5.411818027496338, -14.783225059509277, 0.0)),
    Vector((6.820651531219482, -14.783223152160645, 0.0)),
    Vector((15.192383766174316, -17.521663665771484, 0.0)),
    Vector((17.772960662841797, -9.885138511657715, 0.0)),
    Vector((17.481708526611328, -8.783076286315918, 0.0)),
    Vector((17.183683395385742, -8.14855670928955, 0.0)),
    Vector((16.926300048828125, -7.72554349899292, 0.0)),
    Vector((16.52667808532715, -7.224606990814209, 0.0)),
    Vector((15.944178581237793, -6.690275192260742, 0.0)),
    Vector((15.178802490234375, -6.211604118347168, 0.0)),
    Vector((0.0, 0.0, 11.647357940673828)),
    Vector((-4.619345664978027, -11.432509422302246, 11.647357940673828)),
    Vector((-1.7068554162979126, -12.59023380279541, 11.647357940673828)),
    Vector((-1.4697920083999634, -12.00024127960205, 11.647357940673828)),
    Vector((5.411818027496338, -14.783225059509277, 11.647357940673828)),
    Vector((6.820651531219482, -14.783223152160645, 11.647357940673828)),
    Vector((15.192383766174316, -17.521663665771484, 11.647357940673828)),
    Vector((17.772960662841797, -9.885138511657715, 11.647357940673828)),
    Vector((17.481708526611328, -8.783076286315918, 11.647357940673828)),
    Vector((17.183683395385742, -8.14855670928955, 11.647357940673828)),
    Vector((16.926300048828125, -7.72554349899292, 11.647357940673828)),
    Vector((16.52667808532715, -7.224606990814209, 11.647357940673828)),
    Vector((15.944178581237793, -6.690275192260742, 11.647357940673828)),
    Vector((15.178802490234375, -6.211604118347168, 11.647357940673828))
]
unitVectors = [
    Vector((-0.37462833523750305, -0.927174985408783, 0.0)),
    Vector((0.9292745590209961, -0.3693896532058716, 0.0)),
    Vector((0.37283605337142944, 0.9278972148895264, 0.0)),
    Vector((0.927060604095459, -0.37491148710250854, 0.0)),
    Vector((1.0, 1.3538495977627463e-06, 0.0)),
    Vector((0.9504441618919373, -0.3108955919742584, 0.0)),
    Vector((0.3201405704021454, 0.9473701119422913, 0.0)),
    Vector((-0.25550705194473267, 0.9668072462081909, 0.0)),
    Vector((-0.4251285493373871, 0.9051330089569092, 0.0)),
    Vector((-0.5197952389717102, 0.8542909026145935, 0.0)),
    Vector((-0.6236218214035034, 0.7817261815071106, 0.0)),
    Vector((-0.7369184494018555, 0.6759816408157349, 0.0)),
    Vector((-0.8478434085845947, 0.5302466750144958, 0.0)),
    Vector((-0.9255021810531616, 0.3787422180175781, 0.0))
]
holesInfo = None
firstVertIndex = 14
numPolygonVerts = 14
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