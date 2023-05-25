""" Contains types for importing RDR2 model files. """

import io, os, sys
import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty, IntProperty, PointerProperty
from bpy.types import Operator
from mathutils import Matrix, Vector, Quaternion

from . import pylibdrawable


""" YDR import class """
class ImportYdr(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "import_mesh.ydr"
    bl_label = "Import YDR"

    filename_ext = ".ydr"

    filter_glob: StringProperty(
        default="*.ydr",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )
    
    def execute(self, context):
        retcode = 'FINISHED'
        
        ydrModel = pylibdrawable.ImportYdr(self.filepath)
        
        ydrObj = bpy.data.objects.new(ydrModel.FileName.split(".")[0], None)
        ydrObj.empty_display_size = 2
        ydrObj.empty_display_type = 'PLAIN_AXES'
            
        bpy.context.collection.objects.link(ydrObj)
        
        # Load skeleton data
        arma = None
        if ydrModel.Skeleton is not None:
            skel = ydrModel.Skeleton
            
            arma = bpy.data.armatures.new(ydrModel.FileName.split(".")[0] + "_bones")
            armaObj = bpy.data.objects.new(ydrModel.FileName.split(".")[0] + "_armature", arma)
            bpy.context.collection.objects.link(armaObj)
            bpy.context.view_layer.update()
            
            act_bk = bpy.context.view_layer.objects.active
            bpy.context.view_layer.objects.active = armaObj
            
            bpy.ops.object.mode_set(mode='EDIT')
            
            for jntIdx, jnt in enumerate(skel.FlatSkeleton):
                arma.edit_bones.new(jnt.Name)
            
            self.build_joint_transforms_recursive(arma, skel.Root, Matrix.Identity(4))
                  
            bpy.context.view_layer.update()
            bpy.ops.object.mode_set(mode='OBJECT')
            
            bpy.context.view_layer.objects.active = act_bk
        
        # Load model data
        lodNames = ["lod_hi", "lod_med", "lod_low", "lod_vlow"]
        for lodIdx, lod in enumerate(ydrModel.Lods):
            if lod is None:
                continue
            
            # Create empty parent for this LOD
            lodObj = bpy.data.objects.new(lodNames[lodIdx] + "__" + ydrObj.name, None)
            lodObj.empty_display_size = 2
            lodObj.empty_display_type = 'PLAIN_AXES'
            
            lodObj.parent = ydrObj
            
            for modelIdx, model in enumerate(lod.Models):
                # Create empty parent for this model
                modelName = "model" + str(modelIdx) + "__" + lodObj.name
                modelObj = bpy.data.objects.new(modelName, None)
                modelObj.empty_display_size = 2
                modelObj.empty_display_type = 'PLAIN_AXES'
                modelObj.parent = lodObj
                
                bpy.context.collection.objects.link(modelObj)
                
                for geomIdx, geom in enumerate(model.Geometries):
                    if len(geom.Vertices) == 0:
                        continue
                        
                    verts = geom.GetVertexPositionArray()
                    indices = geom.GetIndexArray()
                        
                    # Create mesh for this geometry
                    geomName = "geometry" + str(geomIdx) + "__" + modelObj.name
                    geomMesh = bpy.data.meshes.new(geomName)
                    
                    geomObj = bpy.data.objects.new(geomName, geomMesh)
                    geomObj.parent = modelObj
                    
                    geomMesh.from_pydata(verts, [], indices)
                    
                    if arma is not None:
                        mod = geomObj.modifiers.new('Armature', type='ARMATURE')
                        mod.object = armaObj
                        
                        for i in range(len(arma.bones)):
                            geomObj.vertex_groups.new(name=arma.bones[i].name)
                            
                        blend_indices = geom.GetVertexBlendIndexArray()
                        blend_weights = geom.GetVertexBlendWeightArray()
                        
                        for i in range(len(blend_indices)):
                            for n in range(4):
                                if blend_weights[i][n] == 0:
                                    continue
                                    
                                jnt_index = blend_indices[i][n]
                                geomObj.vertex_groups[jnt_index].add([i], blend_weights[i][n], 'ADD')
                    
                    geomMesh.update()
                    bpy.context.collection.objects.link(geomObj)
                    
            bpy.context.collection.objects.link(lodObj)
        
        return {retcode}
    
    def build_joint_transforms_recursive(self, armature, cur_joint, parent_mtx):
        realJnt = armature.edit_bones[cur_joint.Name]
        
        # Try to set joint parent
        if cur_joint.Parent is not None:
            realJnt.parent = armature.edit_bones[cur_joint.Parent.Name]
        
        # Set joint position
        realJnt.head.xyz = parent_mtx @ Vector(cur_joint.GetTranslation())
        realJnt.tail.xyz = realJnt.head.xyz + Vector((0, 0, 0.01))
        
        # Grab translation and scale for current joint
        jntTrans = Vector(cur_joint.GetTranslation())
        jntScale = Vector(cur_joint.GetScale())
        
        # Blender expects quaternions in (w, x, y, z) order, ensure w is first in the constructor
        jntRot = cur_joint.GetRotation()
        correctedRot = Quaternion((jntRot[3], jntRot[0], jntRot[1], jntRot[2]))
        
        # calculate new parent matrix
        transMtx = Matrix.LocRotScale(jntTrans, correctedRot, jntScale)
        new_mtx = parent_mtx @ transMtx
        
        # Recurse down the hierarchy
        for child in cur_joint.Children:
            self.build_joint_transforms_recursive(armature, child, new_mtx)
    
    def draw(self, context):
        pass


""" YDD import class """      
class ImportYdd(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "import_mesh.ydd"
    bl_label = "Import YDD"

    filename_ext = ".ydd"

    filter_glob: StringProperty(
        default="*.ydd",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )
    
    def execute(self, context):
        retcode = 'FINISHED'
        
        # TODO
        
        return {retcode}
        
    def draw(self, context):
        pass


""" YFT import class """  
class ImportYft(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "import_mesh.yft"
    bl_label = "Import YFT"

    filename_ext = ".yft"

    filter_glob: StringProperty(
        default="*.yft",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )
    
    def execute(self, context):
        retcode = 'FINISHED'
        
        # TODO
        
        return {retcode}
        
    def draw(self, context):
        pass
