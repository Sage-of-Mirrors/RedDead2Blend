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


from .importing import register as registerImporting, unregister as unregisterImporting
from .exporting import register as registerExporting, unregister as unregisterExporting
from .shaders import register as registerShaders, unregister as unregisterShaders


""" Register function """
def register():
    registerImporting()
    registerExporting()
    registerShaders()
    

""" Unregister function """
def unregister():   
    unregisterShaders()
    unregisterExporting()
    unregisterImporting()


if __name__ == "__main__":
    register()
