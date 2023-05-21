#!/usr/bin/env python3

""" Plugin info """
bl_info = {
    "name": "RedDeadBlend2",
    "author": "Gamma AKA Sage of Mirrors",
    "version": (0, 0, 1),
    "blender": (3, 0, 0),
    "location": "File > Import/Export > RDR2",
    "description": "Import and export model files from RDR2 (.ydr, .ydd, .yft)",
    "wiki_url": "https://github.com/Sage-of-Mirrors/RedDeadBlend2",
    "warning": "Work in Progress",
    "tracker_url": "https://github.com/Sage-of-Mirrors/RedDeadBlend2/issues",
    "category": "Import-Export",
}

__version__ = '.'.join([str(s) for s in bl_info['version']])


import logging.config
import io, os
import bpy

from .importing import ImportYdr, ImportYdd, ImportYft
from .exporting import ExportYdr, ExportYdd, ExportYft
from .ui import TOPBAR_MT_file_import_reddead2, TOPBAR_MT_file_export_reddead2


""" Register function """
def register():
    bpy.utils.register_class(ImportYdr)
    bpy.utils.register_class(ImportYdd)
    bpy.utils.register_class(ImportYft)
    
    bpy.utils.register_class(ExportYdr)
    bpy.utils.register_class(ExportYdd)
    bpy.utils.register_class(ExportYft)

    bpy.utils.register_class(TOPBAR_MT_file_import_reddead2)
    bpy.types.TOPBAR_MT_file_import.append(TOPBAR_MT_file_import_reddead2.menu_draw)
    
    #bpy.utils.register_class(TOPBAR_MT_file_export_reddead2)
    #bpy.types.TOPBAR_MT_file_export.append(TOPBAR_MT_file_export_reddead2.menu_draw)


""" Unregister function """
def unregister():
    #bpy.types.TOPBAR_MT_file_export.remove(TOPBAR_MT_file_export_reddead2.menu_draw)
    #bpy.utils.unregister_class(TOPBAR_MT_file_export_reddead2)
    
    bpy.types.TOPBAR_MT_file_import.remove(TOPBAR_MT_file_import_reddead2.menu_draw)
    bpy.utils.unregister_class(TOPBAR_MT_file_import_reddead2)
    
    bpy.utils.unregister_class(ExportYft)
    bpy.utils.unregister_class(ExportYdd)
    bpy.utils.unregister_class(ExportYdr)
    
    bpy.utils.unregister_class(ImportYft)
    bpy.utils.unregister_class(ImportYdd)
    bpy.utils.unregister_class(ImportYdr)


if __name__ == "__main__":
    register()
