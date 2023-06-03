import bpy

# Clear all mesh objects
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Create a new mesh object
mesh = bpy.data.meshes.new(name="PyramidMesh")
obj = bpy.data.objects.new("Pyramid", mesh)

# Link the object to the scene
scene = bpy.context.scene
scene.collection.objects.link(obj)

# Create a pyramid
verts = [(1, 1, 0), (1, -1, 0), (-1, -1, 0), (-1, 1, 0), (0, 0, 2)]  # 5 vertices
faces = [(0, 1, 4), (1, 2, 4), (2, 3, 4), (3, 0, 4)]  # 4 faces

# Update the mesh with the new data
mesh.from_pydata(verts, [], faces)

# Center the pyramid in the scene
obj.location = (0, 0, 0)

# Update the scene
bpy.context.view_layer.update()

