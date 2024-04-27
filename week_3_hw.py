import maya.cmds as cmds
import json

def get_curve_transformations():
    # Find all curves in the scene
    curves = cmds.ls(type='nurbsCurve')
    
    # Dictionary to store transformation information of curves
    curve_transformations = {}

    # Iterate through all found curves
    for curve in curves:
        # Get the transform node of the curve
        transform_node = cmds.listRelatives(curve, parent=True)[0]

        # Check if any channels are locked for the curve
        # If locked, skip this curve
        if any(cmds.getAttr(transform_node + '.' + attr, lock=True) for attr in ('tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz')):
            continue

        # Get translation values
        translation = cmds.getAttr(transform_node + '.translate')[0]
        # Get rotation values
        rotation = cmds.getAttr(transform_node + '.rotate')[0]
        # Get scale values
        scale = cmds.getAttr(transform_node + '.scale')[0]

        # Add transformation information to the dictionary
        curve_transformations[curve] = {
            'translation': translation,
            'rotation': rotation,
            'scale': scale
        }

    return curve_transformations

# Get transformation information of all curves in the scene
curve_transformations = get_curve_transformations()

# Path to save the JSON file
json_file_path = r"C:\Users\Rogov\Documents\curve_transformations.json"

# Save data to JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(curve_transformations, json_file, indent=4)

print("Transformation information of curves saved to", json_file_path)
