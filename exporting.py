""" Contains types for exporting RDR2 model files. """

import io, os
import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty, IntProperty, PointerProperty
from bpy.types import Operator


""" YDR export class """
class ExportYdr(Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "export_mesh.ydr"
    bl_label = "Export YDR"

    filename_ext = ".ydr"

    filter_glob: StringProperty(
        default="*.ydr",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )
    
    def execute(self, context):
        retcode = 'FINISHED'
        
        # TODO
        
        return {retcode}
        
    def draw(self, context):
        pass


""" YDD export class """      
class ExportYdd(Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "export_mesh.ydd"
    bl_label = "Export YDD"

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


""" YFT export class """  
class ExportYft(Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "export_mesh.yft"
    bl_label = "Export YFT"

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


""" Export menu class """
class TOPBAR_MT_file_export_reddead2(bpy.types.Menu):
    bl_label = "Red Dead Redemption 2"
    
    def draw(self, context):
        self.layout.operator(ExportYdr.bl_idname, text="Drawable (*.ydr)")
        #self.layout.operator(ImportYdd.bl_idname, text="Drawable Dictionary (*.ydd)")
        #self.layout.operator(ImportYft.bl_idname, text="Fragment (*.yft)")
        
    def menu_draw(self, context):
        self.layout.menu("TOPBAR_MT_file_export_reddead2")


""" Module registration """
def register():
    # Register export operators
    bpy.utils.register_class(ExportYdr)
    bpy.utils.register_class(ExportYdd)
    bpy.utils.register_class(ExportYft)
    
    # Register import menu class and add it to the import menu
    #bpy.utils.register_class(TOPBAR_MT_file_export_reddead2)
    #bpy.types.TOPBAR_MT_file_export.append(TOPBAR_MT_file_export_reddead2.menu_draw)
    

""" Module unregistration """   
def unregister():
    # Clear import menu class and remove it from the import menu
    #bpy.types.TOPBAR_MT_file_export.remove(TOPBAR_MT_file_export_reddead2.menu_draw)
    #bpy.utils.unregister_class(TOPBAR_MT_file_export_reddead2)
    
    # Clear import operators
    bpy.utils.unregister_class(ExportYft)
    bpy.utils.unregister_class(ExportYdd)
    bpy.utils.unregister_class(ExportYdr)
