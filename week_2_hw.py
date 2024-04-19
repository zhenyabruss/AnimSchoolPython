import maya.cmds as cmds
import random

# Clear scene func
def clear_scene():
    all_transforms = cmds.ls(transforms=True)
    standard_objects = ['persp', 'top', 'front', 'side']
    for transform in all_transforms:
        if transform not in standard_objects:
            shapes = cmds.listRelatives(transform, shapes=True)
            if shapes:
                for shape in shapes:
                    cmds.delete(shape)
            cmds.delete(transform)

# Create planet system func
def create_planet_system (planet_name='Earth', planet_radius_min=5, planet_radius_max=6, number_of_moons_min=5, number_of_moons_max = 15, moon_radius_min=0.4, moon_radius_max=2.0):

    # Planet create
    planet_radius = random.uniform(planet_radius_min, planet_radius_max)
    planet = cmds.polySphere(name=planet_name,radius=planet_radius)[0]
    planet_pivot = cmds.xform(planet, query=True, translation=True, worldSpace=True)

    # Planet shader
    planet_shader = cmds.shadingNode('lambert', asShader=True)
    cmds.hyperShade(assign=planet_shader)

    planet_R_color = random.uniform(0,1)
    planet_G_color = random.uniform(0,1)
    planet_B_color = random.uniform(0,1)
    color = (planet_R_color, planet_G_color, planet_B_color)  
    cmds.setAttr(planet_shader + ".color", *color)
    cmds.select(planet_name)
    cmds.hyperShade(assign=planet_shader)
    
    # Moons create
    number_of_moons = random.randint(number_of_moons_min, number_of_moons_max)
    moon_pivot_list = []


    for moon in range(number_of_moons):
        
        moon_radius = random.uniform(moon_radius_min, moon_radius_max)  
        
        if moon == 0:
            moon_x_position = planet_radius + moon_radius

        moon_x_position = moon_x_position + moon_radius
        current_moon = cmds.polySphere(name='Moon{}'.format(moon+1), radius=moon_radius)[0]
        cmds.xform (current_moon, translation = [moon_x_position, 0, 0])
        current_moon_pivot = cmds.group (current_moon, name = "{}_pivot".format(current_moon))
        
        cmds.xform(current_moon_pivot, pivots = planet_pivot)
        cmds.xform(current_moon_pivot, rotation = (0,random.uniform(0, 360),random.uniform(-45, 45)))

        moon_pivot_list.append(current_moon_pivot)

        moon_x_position = moon_x_position + (moon_radius*2)

        #Moon shader
        moon_shader = cmds.shadingNode('lambert', asShader=True)
        
        moon_R_color = random.uniform(planet_R_color - 0.2, planet_R_color + 0.2)
        if moon_R_color < 0:
            moon_R_color = 0
        elif moon_R_color > 1:
            moon_R_color = 1

        moon_G_color = random.uniform(planet_G_color - 0.2, planet_G_color + 0.2)
        if moon_G_color < 0:
            moon_G_color = 0
        elif moon_G_color > 1:
            moon_G_color = 1

        moon_B_color = random.uniform(planet_B_color - 0.2, planet_B_color + 0.2)
        if moon_B_color < 0:
            moon_B_color = 0
        elif moon_B_color > 1:
            moon_B_color = 1
        
        moon_color = (moon_R_color, moon_G_color, moon_B_color)  
        cmds.setAttr(moon_shader + ".color", *moon_color)
        
        print(current_moon)
        cmds.select(current_moon)
        cmds.hyperShade(assign=moon_shader)

    # Animation

    # Planet animation
    planet_y_angle = 360

    start_frame = cmds.playbackOptions(query=True, minTime=True)
    end_frame = cmds.playbackOptions(query=True, maxTime=True)

    cmds.setKeyframe(planet, attribute='rotateY', t=start_frame, value=0, inTangentType='linear', outTangentType='linear')
    cmds.setKeyframe(planet, attribute='rotateY', t=end_frame, value=planet_y_angle, inTangentType='linear', outTangentType='linear')
    
    # Moon animation
    for pivot in moon_pivot_list:
        moon_y_angle = planet_y_angle * random.uniform(2,5) * 2
        
        cmds.setKeyframe(pivot, attribute='rotateY', t=start_frame, value = 0, inTangentType='linear', outTangentType='linear')
        cmds.setKeyframe(pivot, attribute='rotateY', t=end_frame, value = moon_y_angle,inTangentType='linear', outTangentType='linear')
    
    cmds.select(clear=True)
    cmds.play(state=True)


clear_scene()
create_planet_system(   planet_name = 'Pluto', 
                        planet_radius_min = 3, 
                        planet_radius_max = 6,  
                        number_of_moons_min = 2, 
                        number_of_moons_max = 7, 
                        moon_radius_min = 0.4, 
                        moon_radius_max = 2.0)

