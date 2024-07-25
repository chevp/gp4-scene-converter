import bpy
import json
import sys
import os

def convert_blend_to_json(input_filepath, output_filepath, gltf_dir):
    # Open the .blend file
    bpy.ops.wm.open_mainfile(filepath=input_filepath)
       
    # Prepare a data structure to store the collected information
    data = {
       'objects': []
    }
       
    # Ensure the GLTF directory exists
    os.makedirs(gltf_dir, exist_ok=True)
       
    for obj in bpy.data.objects:
        obj_data = {
            'name': obj.name,
            'location': list(obj.location),
            'rotation': list(obj.rotation_euler),
            'scale': list(obj.scale)
        }
           
        # Export each object as GLTF
        gltf_path = os.path.join(gltf_dir, f"{obj.name}.gltf")
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.ops.export_scene.gltf(filepath=gltf_path, use_selection=True)
           
        obj_data['gltf_file'] = gltf_path
        data['objects'].append(obj_data)
       
    # Write the collected data to the output JSON file
    with open(output_filepath, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    input_filepath = sys.argv[-3]
    output_filepath = sys.argv[-2]
    gltf_dir = sys.argv[-1]
    convert_blend_to_json(input_filepath, output_filepath, gltf_dir)