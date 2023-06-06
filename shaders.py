""" Contains types for handling RDR2 shaders. """

import os
import json
import bpy


""" Class representing a uniform (parameter) in an RDR2 shader """
class RDR2ShaderUniformPropertyGroup(bpy.types.PropertyGroup):
    data: bpy.props.FloatVectorProperty(name="Data", size=[8, 8])


""" Class representing an RDR2 shader """
class RDR2ShaderPropertyGroup(bpy.types.PropertyGroup):
    uniforms: bpy.props.CollectionProperty(
        type=RDR2ShaderUniformPropertyGroup,
        name="Uniforms"
    )


""" Class representing the UI panel that shaders and uniforms are displayed on """
class OBJECT_PT_shader_view_panel(bpy.types.Panel):
    bl_label = "Red Dead Redemption 2"
    bl_idname = "OBJECT_PT_shader_view_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"
    bl_order = 100
    
    def __init__(self):
        scn = bpy.context.scene
        if len(scn.rdr2_shader_templates) == 0:
            data_path = os.path.dirname(__file__) + "/data/shaders"
            shader_files = os.listdir(data_path)
            
            for p in shader_files:
                shader_json = []
                with open(data_path + "/" + p, encoding="utf-8") as f:
                      shader_json = json.load(f)
            
                shader_item = scn.rdr2_shader_templates.add()
                shader_item.name = shader_json["name"]
                
                for u in shader_json["uniforms"]:
                    uniform_item = shader_item.uniforms.add()
                    uniform_item.name = u["name"]
                    
    @classmethod
    def poll(cls, context):
        return (context.material is not None)
        
    def draw(self, context):
        if len(context.scene.rdr2_shader_templates) == 0:
            return
        
        # Configure panel layout to mimic Blender's native formatting
        layout = self.layout
        split = layout.split(factor=0.4)
        
        col_right = split.column(align=True)
        col_right.alignment = "RIGHT"
        
        col_left = split.column(align=True)
        layout.use_property_split = True
        
        # Draw shader selection combobox
        col_right.label(text="Shader")
        col_left.prop(context.material, "rdr2_shader_template_enum", text="")
        
        # Put space between combobox and shader uniforms
        col_right.separator()
        col_left.separator()
         
        # Draw controls for editing the shader uniforms in the current material
        for u in context.scene.rdr2_shader_templates[2].uniforms:
            col_right.label(text=u["name"])
            col_left.label(text="placeholder")
 
            
""" Module registration """
def register():
    # Register uniform and shader property group classes
    bpy.utils.register_class(RDR2ShaderUniformPropertyGroup)
    bpy.utils.register_class(RDR2ShaderPropertyGroup)
    
    # Register shader UI panel
    bpy.utils.register_class(OBJECT_PT_shader_view_panel)
    
    # Add shader template collection property to the Scene type
    bpy.types.Scene.rdr2_shader_templates = bpy.props.CollectionProperty(
        type=RDR2ShaderPropertyGroup,
        name="RDR2 Shader Templates Collection"
    )
    
    # Add current RDR2 shader template enum property to the Material type
    bpy.types.Material.rdr2_shader_template_enum = bpy.props.EnumProperty(
        name="Red Dead Redemption 2 Shaders",
        items=(lambda self, context: [(shader.name, shader.name, "") for shader in context.scene.rdr2_shader_templates])
    )
    bpy.types.Material.rdr2_shader_pointer = bpy.props.PointerProperty(
        type=RDR2ShaderPropertyGroup,
        name="Red Dead Redemption 2 Shader"
    )
    

""" Module unregistration """   
def unregister():
    # Remove custom properties from native Blender types
    del bpy.types.Material.rdr2_shader_pointer
    del bpy.types.Material.rdr2_shader_template_enum
    del bpy.types.Scene.rdr2_shader_templates
    
    # Clear shader UI panel
    bpy.utils.unregister_class(OBJECT_PT_shader_view_panel)
    
    # Clear uniform and shader property group classes
    bpy.utils.unregister_class(RDR2ShaderUniformPropertyGroup)
    bpy.utils.unregister_class(RDR2ShaderPropertyGroup)
    