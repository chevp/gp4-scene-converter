import bpy
import json
import sys

def convert_blend_to_json(input_filepath, output_filepath):
    bpy.ops.wm.open_mainfile(filepath=input_filepath)
    
    # Collect data from the blend file. Example: names of all objects
    data = {}
    data['objects'] = [obj.name for obj in bpy.data.objects]
    
    # Convert the collected data to JSON and write to output file
    with open(output_filepath, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    input_filepath = sys.argv[-2]
    output_filepath = sys.argv[-1]
    convert_blend_to_json(input_filepath, output_filepath)