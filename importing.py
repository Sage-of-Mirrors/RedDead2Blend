""" Contains types for importing RDR2 model files. """

import io, os
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty, IntProperty, PointerProperty
from bpy.types import Operator


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
        
        # TODO
        
        return {retcode}
        
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
