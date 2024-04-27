import maya.cmds as cmds
import json

def apply_curve_transformations(json_file_path):
    # Load data from JSON file
    with open(json_file_path, 'r') as json_file:
        curve_transformations = json.load(json_file)

    # Iterate through the dictionary and apply transformations
    for curve, transformations in curve_transformations.items():
        # Check if the transform node exists for the curve
        transform_node = cmds.listRelatives(curve, parent=True, fullPath=True)
        if transform_node:
            # Apply translation
            cmds.setAttr(transform_node[0] + '.translateX', transformations['translation'][0])
            cmds.setAttr(transform_node[0] + '.translateY', transformations['translation'][1])
            cmds.setAttr(transform_node[0] + '.translateZ', transformations['translation'][2])
            
            # Apply rotation
            cmds.setAttr(transform_node[0] + '.rotateX', transformations['rotation'][0])
            cmds.setAttr(transform_node[0] + '.rotateY', transformations['rotation'][1])
            cmds.setAttr(transform_node[0] + '.rotateZ', transformations['rotation'][2])
            
            # Apply scale
            cmds.setAttr(transform_node[0] + '.scaleX', transformations['scale'][0])
            cmds.setAttr(transform_node[0] + '.scaleY', transformations['scale'][1])
            cmds.setAttr(transform_node[0] + '.scaleZ', transformations['scale'][2])
        else:
            print("Transform node not found for curve:", curve)

# Path to the JSON file
json_file_path = r"C:\Users\Rogov\Documents\curve_transformations.json"

# Apply curve transformations
apply_curve_transformations(json_file_path)
