import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((-7.868995189666748, -9.629130363464355, 0.0)),
    Vector((13.926976203918457, -27.440235137939453, 0.0)),
    Vector((16.103065490722656, -27.55154800415039, 0.0)),
    Vector((18.20895767211914, -26.994943618774414, 0.0)),
    Vector((20.034061431884766, -25.814950942993164, 0.0)),
    Vector((21.41692352294922, -24.122888565063477, 0.0)),
    Vector((22.210134506225586, -22.09687042236328, 0.0)),
    Vector((22.33647918701172, -19.915008544921875, 0.0)),
    Vector((21.795957565307617, -17.811073303222656, 0.0)),
    Vector((0.0, 0.0, 0.0)),
    Vector((-7.868995189666748, -9.629130363464355, 4.0)),
    Vector((13.926976203918457, -27.440235137939453, 4.0)),
    Vector((16.103065490722656, -27.55154800415039, 4.0)),
    Vector((18.20895767211914, -26.994943618774414, 4.0)),
    Vector((20.034061431884766, -25.814950942993164, 4.0)),
    Vector((21.41692352294922, -24.122888565063477, 4.0)),
    Vector((22.210134506225586, -22.09687042236328, 4.0)),
    Vector((22.33647918701172, -19.915008544921875, 4.0)),
    Vector((21.795957565307617, -17.811073303222656, 4.0)),
    Vector((0.0, 0.0, 4.0))
]
unitVectors = [
    Vector((0.7743395566940308, -0.632770299911499, 0.0)),
    Vector((0.9986943006515503, -0.05108591914176941, 0.0)),
    Vector((0.9668002724647522, 0.2555331587791443, 0.0)),
    Vector((0.8397709131240845, 0.5429409146308899, 0.0)),
    Vector((0.6328121423721313, 0.7743054032325745, 0.0)),
    Vector((0.36456725001335144, 0.931177020072937, 0.0)),
    Vector((0.057809971272945404, 0.9983275532722473, 0.0)),
    Vector((-0.24882930517196655, 0.9685472846031189, 0.0)),
    Vector((-0.7743399143218994, 0.6327698826789856, 0.0)),
    Vector((-0.6327856183052063, -0.7743269801139832, 0.0))
]
holesInfo = None
firstVertIndex = 10
numPolygonVerts = 10
faces = []


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