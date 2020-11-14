bl_info = {
    "name": "Demo bpypolyskel",
    "author": "polarkernel",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New bpypolykel Demo Object",
    "description": "Add a bpypolykel Demo Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector
from itertools import *

from .bpypolyskel import bpypolyskel

def _iterCircularPrevThis(lst):
    prevs, this = tee(lst)
    prevs = islice(cycle(prevs), len(lst) - 1, None)
    return zip(prevs,this)

def add_object(self, context):
    scale_x = self.scale.x
    scale_y = self.scale.y
    scale_z = self.scale.z

    # Define vertices for the base footprint of the building at height 0.0
    # counterclockwise order
    verts = [
        Vector((7.710012435913086*scale_x,-6.9630279541015625*scale_y,0.0)),
        Vector((8.055673599243164*scale_x,4.447220325469971*scale_y,0.0)),
        Vector((0.4236260652542114*scale_x,4.58079719543457*scale_y,0.0)),
        Vector((0.38295790553092957*scale_x,5.0149431228637695*scale_y,0.0)),
        Vector((0.3016217052936554*scale_x,5.426825046539307*scale_y,0.0)),
        Vector((0.13217128813266754*scale_x,5.81644344329834*scale_y,0.0)),
        Vector((-0.10505922883749008*scale_x,6.172665596008301*scale_y,0.0)),
        Vector((-0.40329185128211975*scale_x,6.462096691131592*scale_y,0.0)),
        Vector((-0.7557485699653625*scale_x,6.7069993019104*scale_y,0.0)),
        Vector((-1.1488733291625977*scale_x,6.873978614807129*scale_y,0.0)),
        Vector((-1.5623321533203125*scale_x,6.951902389526367*scale_y,0.0)),
        Vector((-1.989346981048584*scale_x,6.963034629821777*scale_y,0.0)),
        Vector((-2.409583806991577*scale_x,6.885111331939697*scale_y,0.0)),
        Vector((-2.8094866275787354*scale_x,6.740396022796631*scale_y,0.0)),
        Vector((-3.1687216758728027*scale_x,6.517757415771484*scale_y,0.0)),
        Vector((-3.4805104732513428*scale_x,6.228326797485352*scale_y,0.0)),
        Vector((-3.731297254562378*scale_x,5.883236408233643*scale_y,0.0)),
        Vector((-3.9075260162353516*scale_x,5.493618488311768*scale_y,0.0)),
        Vector((-4.009196758270264*scale_x,5.0817365646362305*scale_y,0.0)),
        Vector((-4.049864768981934*scale_x,4.658722400665283*scale_y,0.0)),
        Vector((-4.436212062835693*scale_x,4.680986404418945*scale_y,0.0)),
        Vector((-4.503993988037109*scale_x,2.86647891998291*scale_y,0.0)),
        Vector((-7.865891456604004*scale_x,2.7996914386749268*scale_y,0.0)),
        Vector((-8.055685997009277*scale_x,-3.2004287242889404*scale_y,0.0)),
        Vector((-4.693784236907959*scale_x,-3.2226970195770264*scale_y,0.0)),
        Vector((-4.809013843536377*scale_x,-6.695865154266357*scale_y,0.0))
    ]

    # We construct the footprint of the roof with
    # same shape as the base footprint, but at height 5.0*scale_z.
    roof  = [v + Vector((0.0,0.0,5.0*scale_z)) for v in verts]
    verts.extend(roof)

    # The footprint of the roof starts at index 26 and has 26 vertices.
    holesInfo = None        # we have no holes
    unitVectors = None      # we have no unit vectors, let them compute by polygonize()
    firstVertIndex = 26
    numVerts = 26

    # In order to have already some faces, we construct those of the sidewalls
    # in counterclockwise order
    faces = []
    for prev, this in _iterCircularPrevThis([i for i in range(numVerts)]):
        faces.append([prev,this,this+firstVertIndex, prev+firstVertIndex])

    # Let us use a tangent of the roof pitch angle of 0.6 instead of the roof's height
    height = 0.0
    tan = 0.6

    # now extend 'faces' by faces of straight polygon
    faces = bpypolyskel.polygonize(verts, firstVertIndex, numVerts, holesInfo, height, tan, faces, unitVectors)

    # construct the mesh for this building and we are done.
    edges = []
    mesh = bpy.data.meshes.new(name="Building_with_Roof")
    mesh.from_pydata(verts, edges, faces)
    object_data_add(context, mesh, operator=self)



class OBJECT_OT_add_object(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_object"
    bl_label = "Add a bpypolykel Demo Object"
    bl_options = {'REGISTER', 'UNDO'}

    scale: FloatVectorProperty(
        name="scale",
        default=(1.0, 1.0, 1.0),
        subtype='TRANSLATION',
        description="scaling",
    )

    def execute(self, context):

        add_object(self, context)

        return {'FINISHED'}


# Registration
def add_object_button(self, context):
    self.layout.operator(
        OBJECT_OT_add_object.bl_idname,
        text="Add bpypolykel Demo Object",
        icon='PLUGIN')


# This allows you to right click on a button and link to documentation
def add_object_manual_map():
    url_manual_prefix = "https://docs.blender.org/manual/en/latest/"
    url_manual_mapping = (
        ("bpy.ops.mesh.add_object", "scene_layout/object/types.html"),
    )
    return url_manual_prefix, url_manual_mapping


def register():
    bpy.utils.register_class(OBJECT_OT_add_object)
    bpy.utils.register_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.append(add_object_button)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_object)
    bpy.utils.unregister_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_object_button)


if __name__ == "__main__":
    register()
