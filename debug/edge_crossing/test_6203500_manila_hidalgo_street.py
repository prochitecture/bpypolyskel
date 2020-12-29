import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((-18.79814338684082, -7.079912185668945, 0.0)),
    Vector((-3.404139280319214, -47.92304229736328, 0.0)),
    Vector((3.985858917236328, -45.140052795410156, 0.0)),
    Vector((0.8510344624519348, -36.802223205566406, 0.0)),
    Vector((4.750710964202881, -35.33280563354492, 0.0)),
    Vector((7.8855366706848145, -43.65950393676758, 0.0)),
    Vector((15.394030570983887, -40.83198547363281, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((-18.79814338684082, -7.079912185668945, 6.395418167114258)),
    Vector((-3.404139280319214, -47.92304229736328, 6.395418167114258)),
    Vector((3.985858917236328, -45.140052795410156, 6.395418167114258)),
    Vector((0.8510344624519348, -36.802223205566406, 6.395418167114258)),
    Vector((4.750710964202881, -35.33280563354492, 6.395418167114258)),
    Vector((7.8855366706848145, -43.65950393676758, 6.395418167114258)),
    Vector((15.394030570983887, -40.83198547363281, 6.395418167114258)),
    Vector((0.0, 0.0, 6.395418167114258)),
    Vector((-4.933842182159424, -21.05051612854004, 0.0)),
    Vector((-1.1418935060501099, -19.63675880432129, 0.0)),
    Vector((1.4435261487960815, -26.56083106994629, 0.0)),
    Vector((-2.348423480987549, -27.97458839416504, 0.0)),
    Vector((-4.933842182159424, -21.05051612854004, 6.395418167114258)),
    Vector((-1.1418935060501099, -19.63675880432129, 6.395418167114258)),
    Vector((1.4435261487960815, -26.56083106994629, 6.395418167114258)),
    Vector((-2.348423480987549, -27.97458839416504, 6.395418167114258))
]
unitVectors = [
    Vector((0.3526862561702728, -0.935741662979126, 0.0)),
    Vector((0.9358394742012024, 0.35242652893066406, 0.0)),
    Vector((-0.3519243001937866, 0.9360284209251404, 0.0)),
    Vector((0.935772716999054, 0.35260382294654846, 0.0)),
    Vector((0.35233649611473083, -0.9358733296394348, 0.0)),
    Vector((0.9358434081077576, 0.35241615772247314, 0.0)),
    Vector((-0.3527710735797882, 0.9357096552848816, 0.0)),
    Vector((-0.9358272552490234, -0.35245898365974426, 0.0)),
    Vector((0.9369955062866211, 0.3493412733078003, 0.0)),
    Vector((0.3498055338859558, -0.9368222951889038, 0.0)),
    Vector((-0.9369955062866211, -0.34934118390083313, 0.0)),
    Vector((-0.34980544447898865, 0.9368224143981934, 0.0))
]
holesInfo = [
    (20, 4)
]
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