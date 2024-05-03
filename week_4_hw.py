import maya.cmds as cmds # type: ignore

def createObject(*args):
    
    # Reading object type, name and group checkbox
    n = cmds.textField("textfld01_id", q=1, text=1)
    selected_button = cmds.radioButtonGrp("radiogrp01_id", query=True, select=True)
    checkbox_value = cmds.checkBox("checkbox01_id", query=True, value=True)

    # Creating choosen object
    if selected_button == 1:
        newObject = cmds.polySphere(name=n)
    elif selected_button == 2:
        newObject = cmds.polyCone(name=n)
    elif selected_button == 3:
        newObject = cmds.polyCube(name=n)

    if checkbox_value:
        cmds.group(newObject, name="myGroup")

def cancelCreation(*args):
    cmds.deleteUI("MyWindow")

# delete "MyWindow" if exists already
if cmds.window("MyWindow", exists = 1):
    cmds.deleteUI("MyWindow")
    
# delete "MyWindow"  prefs if exists 
if cmds.windowPref("MyWindow", exists = 1):
    cmds.windowPref("MyWindow", remove = 1)

#create and show window 
cmds.window("MyWindow", title="Object Creator", width = 285, height = 90, tlb = 1)
cmds.showWindow("MyWindow")

mainLayout  = cmds.columnLayout()

# Type name field
nameLayout  = cmds.columnLayout(parent=mainLayout)
textField = cmds.textField("textfld01_id", parent = nameLayout, width = 280, placeholderText = 'Object Name')

# Choose object type radio buttons
chooseTypeLayout = cmds.rowLayout(parent=mainLayout)
radio_group = cmds.radioButtonGrp("radiogrp01_id", parent = chooseTypeLayout, numberOfRadioButtons=3, labelArray3=["Sphere", "Cone", "Cube"])

# Checkbox to put object into group
optionsLayout  = cmds.columnLayout(parent=mainLayout, adjustableColumn=True, rowSpacing=15)
group_checkbox = cmds.checkBox("checkbox01_id", label="Add object to group upon creation", parent=optionsLayout)

# 'Create' and 'Cancel' buttons create
button_layout = cmds.rowLayout(numberOfColumns=2, parent=mainLayout)
create_button = cmds.button(label="Create", w=140, command = createObject)
cancel_button = cmds.button(label="Cancel", w=140, command = cancelCreation)



     