@rem Execute the Script via Command Line: Open Command Prompt and run the 
@rem following command, replacing input.blend with the path to your 
@rem .blend file and output.json with the desired output path for the JSON file:

Call "C:\Program Files\Blender Foundation\Blender 3.5\blender.exe" --background --python convert_to_json.py -- input.blend dist/output.json

pause