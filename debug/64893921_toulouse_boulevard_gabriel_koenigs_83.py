import mathutils
#import matplotlib.pyplot as plt
from bpypolyskel import bpypolyskel
from collections import Counter

verts = [
    mathutils.Vector((14.40660285949707,-2.298732042312622,0.0)),
    mathutils.Vector((15.019295692443848,2.688382625579834,0.0)),
    mathutils.Vector((12.665223121643066,3.5232739448547363,0.0)),
    mathutils.Vector((12.850645065307617,4.291378498077393,0.0)),
    mathutils.Vector((12.939324378967285,5.070615291595459,0.0)),
    mathutils.Vector((12.923198699951172,6.016830921173096,0.0)),
    mathutils.Vector((12.713587760925293,7.063233852386475,0.0)),
    mathutils.Vector((12.254057884216309,8.1318998336792,0.0)),
    mathutils.Vector((11.601044654846191,9.044718742370605,0.0)),
    mathutils.Vector((11.109269142150879,9.59018325805664,0.0)),
    mathutils.Vector((10.359513282775879,10.18017578125,0.0)),
    mathutils.Vector((9.174416542053223,10.770167350769043,0.0)),
    mathutils.Vector((8.408537864685059,10.9594087600708,0.0)),
    mathutils.Vector((7.682968616485596,11.070727348327637,0.0)),
    mathutils.Vector((6.900966644287109,11.070727348327637,0.0)),
    mathutils.Vector((5.949665069580078,10.926011085510254,0.0)),
    mathutils.Vector((-15.019291877746582,4.046480178833008,0.0)),
    mathutils.Vector((-8.078027725219727,-11.070718765258789,0.0)),
    mathutils.Vector((14.40660285949707,-2.298732042312622,16.648548126220703)),
    mathutils.Vector((15.019295692443848,2.688382625579834,16.648548126220703)),
    mathutils.Vector((12.665223121643066,3.5232739448547363,16.648548126220703)),
    mathutils.Vector((12.850645065307617,4.291378498077393,16.648548126220703)),
    mathutils.Vector((12.939324378967285,5.070615291595459,16.648548126220703)),
    mathutils.Vector((12.923198699951172,6.016830921173096,16.648548126220703)),
    mathutils.Vector((12.713587760925293,7.063233852386475,16.648548126220703)),
    mathutils.Vector((12.254057884216309,8.1318998336792,16.648548126220703)),
    mathutils.Vector((11.601044654846191,9.044718742370605,16.648548126220703)),
    mathutils.Vector((11.109269142150879,9.59018325805664,16.648548126220703)),
    mathutils.Vector((10.359513282775879,10.18017578125,16.648548126220703)),
    mathutils.Vector((9.174416542053223,10.770167350769043,16.648548126220703)),
    mathutils.Vector((8.408537864685059,10.9594087600708,16.648548126220703)),
    mathutils.Vector((7.682968616485596,11.070727348327637,16.648548126220703)),
    mathutils.Vector((6.900966644287109,11.070727348327637,16.648548126220703)),
    mathutils.Vector((5.949665069580078,10.926011085510254,16.648548126220703)),
    mathutils.Vector((-15.019291877746582,4.046480178833008,16.648548126220703)),
    mathutils.Vector((-8.078027725219727,-11.070718765258789,16.648548126220703))
]
unitVectors = [
    mathutils.Vector((0.12193838506937027,0.9925376772880554,0.0)),
    mathutils.Vector((-0.9424813985824585,0.3342588245868683,0.0)),
    mathutils.Vector((0.23466134071350098,0.9720771908760071,0.0)),
    mathutils.Vector((0.11307293176651001,0.9935867190361023,0.0)),
    mathutils.Vector((-0.017039813101291656,0.9998547434806824,0.0)),
    mathutils.Vector((-0.1964137703180313,0.9805210828781128,0.0)),
    mathutils.Vector((-0.39503031969070435,0.9186681509017944,0.0)),
    mathutils.Vector((-0.5818278193473816,0.8133119344711304,0.0)),
    mathutils.Vector((-0.669609546661377,0.7427133321762085,0.0)),
    mathutils.Vector((-0.7858604788780212,0.6184037327766418,0.0)),
    mathutils.Vector((-0.895198404788971,0.4456678628921509,0.0)),
    mathutils.Vector((-0.9708034992218018,0.2398764044046402,0.0)),
    mathutils.Vector((-0.9884345531463623,0.15164801478385925,0.0)),
    mathutils.Vector((-1.0,0.0,0.0)),
    mathutils.Vector((-0.9886261224746704,-0.1503942459821701,0.0)),
    mathutils.Vector((-0.9501696825027466,-0.31173330545425415,0.0)),
    mathutils.Vector((0.417277991771698,-0.9087789058685303,0.0)),
    mathutils.Vector((0.9316127896308899,0.3634524941444397,0.0))
]
holesInfo = None
firstVertIndex = 18
numPolygonVerts = 18
faces = bpypolyskel.polygonize(verts, firstVertIndex, numPolygonVerts, holesInfo, 0.0, 0.5, None, unitVectors)
#fig = plt.figure()
#ax = fig.gca(projection='3d')
for face in faces:
    if len(face) < 3:
        raise Exception("Less than 3 verts in a face")
    if len(face) != len(set(face)):
        raise Exception("Duplicated indices")
    #for edge in zip(face, face[1:] + face[:1]):
    #    p1 = verts[edge[0]]
    #    p2 = verts[edge[1]]
    #    ax.plot([p1.x,p2.x],[p1.y,p2.y],[p1.z,p2.z])
#plt.show()