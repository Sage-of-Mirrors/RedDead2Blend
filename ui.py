""" Contains types for modifying Blender's UI. """

import bpy

from .importing import ImportYdr, ImportYdd, ImportYft
from .exporting import ExportYdr, ExportYdd, ExportYft


""" Import menu class """
class TOPBAR_MT_file_import_reddead2(bpy.types.Menu):
    bl_label = "Red Dead Redemption 2"
    
    def draw(self, context):
        self.layout.operator(ImportYdr.bl_idname, text="Drawable (*.ydr)")
        #self.layout.operator(ImportYdd.bl_idname, text="Drawable Dictionary (*.ydd)")
        #self.layout.operator(ImportYft.bl_idname, text="Fragment (*.yft)")
        
    def menu_draw(self, context):
        self.layout.menu("TOPBAR_MT_file_import_reddead2")


""" Export menu class """
class TOPBAR_MT_file_export_reddead2(bpy.types.Menu):
    bl_label = "Red Dead Redemption 2"
    
    def draw(self, context):
        self.layout.operator(ExportYdr.bl_idname, text="Drawable (*.ydr)")
        #self.layout.operator(ImportYdd.bl_idname, text="Drawable Dictionary (*.ydd)")
        #self.layout.operator(ImportYft.bl_idname, text="Fragment (*.yft)")
        
    def menu_draw(self, context):
        self.layout.menu("TOPBAR_MT_file_export_reddead2")
