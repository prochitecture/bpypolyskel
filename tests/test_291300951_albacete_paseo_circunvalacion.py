import pytest
from mathutils import Vector
from bpypolyskel import bpypolyskel


verts = [
    Vector((0.0, 0.0, 0.0)),
    Vector((-7.078081130981445, -6.63463830947876, 0.0)),
    Vector((-17.401018142700195, -12.523423194885254, 0.0)),
    Vector((-25.41362953186035, -15.918645858764648, 0.0)),
    Vector((-35.27797317504883, -18.790651321411133, 0.0)),
    Vector((-45.83454895019531, -19.87039566040039, 0.0)),
    Vector((-57.20448684692383, -19.169008255004883, 0.0)),
    Vector((-65.45071411132812, -17.632736206054688, 0.0)),
    Vector((-61.98085403442383, -12.990740776062012, 0.0)),
    Vector((-91.45248413085938, 5.110095500946045, 0.0)),
    Vector((-104.89936065673828, -15.305731773376465, 0.0)),
    Vector((-104.8993911743164, -17.854948043823242, 0.0)),
    Vector((-77.27938842773438, -31.091154098510742, 0.0)),
    Vector((-69.38793182373047, -33.640445709228516, 0.0)),
    Vector((-58.94384765625, -35.49956512451172, 0.0)),
    Vector((-49.66789627075195, -36.18981170654297, 0.0)),
    Vector((-37.12977600097656, -35.499698638916016, 0.0)),
    Vector((-17.2885684967041, -30.078508377075195, 0.0)),
    Vector((-5.338858604431152, -24.82424545288086, 0.0)),
    Vector((4.1793622970581055, -18.556957244873047, 0.0)),
    Vector((13.117818832397461, -9.885159492492676, 0.0)),
    Vector((12.884185791015625, -7.5697150230407715, 0.0)),
    Vector((0.0, 0.0, 15.496682167053223)),
    Vector((-7.078081130981445, -6.63463830947876, 15.496682167053223)),
    Vector((-17.401018142700195, -12.523423194885254, 15.496682167053223)),
    Vector((-25.41362953186035, -15.918645858764648, 15.496682167053223)),
    Vector((-35.27797317504883, -18.790651321411133, 15.496682167053223)),
    Vector((-45.83454895019531, -19.87039566040039, 15.496682167053223)),
    Vector((-57.20448684692383, -19.169008255004883, 15.496682167053223)),
    Vector((-65.45071411132812, -17.632736206054688, 15.496682167053223)),
    Vector((-61.98085403442383, -12.990740776062012, 15.496682167053223)),
    Vector((-91.45248413085938, 5.110095500946045, 15.496682167053223)),
    Vector((-104.89936065673828, -15.305731773376465, 15.496682167053223)),
    Vector((-104.8993911743164, -17.854948043823242, 15.496682167053223)),
    Vector((-77.27938842773438, -31.091154098510742, 15.496682167053223)),
    Vector((-69.38793182373047, -33.640445709228516, 15.496682167053223)),
    Vector((-58.94384765625, -35.49956512451172, 15.496682167053223)),
    Vector((-49.66789627075195, -36.18981170654297, 15.496682167053223)),
    Vector((-37.12977600097656, -35.499698638916016, 15.496682167053223)),
    Vector((-17.2885684967041, -30.078508377075195, 15.496682167053223)),
    Vector((-5.338858604431152, -24.82424545288086, 15.496682167053223)),
    Vector((4.1793622970581055, -18.556957244873047, 15.496682167053223)),
    Vector((13.117818832397461, -9.885159492492676, 15.496682167053223)),
    Vector((12.884185791015625, -7.5697150230407715, 15.496682167053223))
]
unitVectors = [
    Vector((-0.7295918464660645, -0.6838828325271606, 0.0)),
    Vector((-0.868606686592102, -0.49550220370292664, 0.0)),
    Vector((-0.9207497239112854, -0.3901537358760834, 0.0)),
    Vector((-0.9601331949234009, -0.2795429527759552, 0.0)),
    Vector((-0.9948098659515381, -0.10175082832574844, 0.0)),
    Vector((-0.9981026649475098, 0.06157084181904793, 0.0)),
    Vector((-0.9830852746963501, 0.18314877152442932, 0.0)),
    Vector((0.5987141728401184, 0.8009627461433411, 0.0)),
    Vector((-0.8521168231964111, 0.5233516693115234, 0.0)),
    Vector((-0.5500564575195312, -0.8351275324821472, 0.0)),
    Vector((-1.1971356798312627e-05, -1.0, 0.0)),
    Vector((0.9017953872680664, -0.4321632385253906, 0.0)),
    Vector((0.9515795707702637, -0.30740252137184143, 0.0)),
    Vector((0.984523594379425, -0.1752520203590393, 0.0)),
    Vector((0.99724280834198, -0.07420731335878372, 0.0)),
    Vector((0.9984886646270752, 0.054958004504442215, 0.0)),
    Vector((0.9646408557891846, 0.263567715883255, 0.0)),
    Vector((0.915416955947876, 0.402506947517395, 0.0)),
    Vector((0.8352034687995911, 0.5499411225318909, 0.0)),
    Vector((0.7177317142486572, 0.6963198184967041, 0.0)),
    Vector((-0.10039226710796356, 0.9949479699134827, 0.0)),
    Vector((-0.8622037172317505, 0.506561815738678, 0.0))
]
holesInfo = None
firstVertIndex = 22
numPolygonVerts = 22
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