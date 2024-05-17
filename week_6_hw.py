

import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore

class MyDialog(QtWidgets.QDialog):

    def __init__(self):
        super(MyDialog, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.initUI()
        
    def initUI(self):
        self.setObjectName('myTestWindow')
        self.setWindowTitle('Poly Creation Tool')
        self.setMinimumSize(300, 150)  # Width, Height in pixels
        
        # create main layout
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)

        # Add name input
        self.name_label = QtWidgets.QLabel("Object Name")
        self.mainLayout.addWidget(self.name_label)

        self.name_input = QtWidgets.QLineEdit(self)
        self.mainLayout.addWidget(self.name_input)

        # group for radio buttons
        self.radio_group = QtWidgets.QGroupBox()
        self.radio_group.setMaximumHeight(50)  # group height
 
        # create layout to radio group
        self.radio_groupLayout = QtWidgets.QHBoxLayout()

        # create radio buttons
        self.radio_Sphere = QtWidgets.QRadioButton('Sphere')
        self.radio_Cube = QtWidgets.QRadioButton('Cube')
        self.radio_Cone = QtWidgets.QRadioButton('Cone')
        
        # put them to layout
        self.radio_groupLayout.addWidget(self.radio_Sphere)
        self.radio_groupLayout.addWidget(self.radio_Cube)
        self.radio_groupLayout.addWidget(self.radio_Cone)
        
        # set layout to group
        self.radio_group.setLayout(self.radio_groupLayout)
        
        # put group to main layout
        self.mainLayout.addWidget(self.radio_group)
        
        # make default radio button
        self.radio_Sphere.setChecked(True)

        # Add slider
        self.slider_label = QtWidgets.QLabel("X Position")
        self.mainLayout.addWidget(self.slider_label)

        slider_layout = QtWidgets.QHBoxLayout()
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.slider.setRange(0, 10)
        self.slider.setValue(0)
        self.slider.valueChanged.connect(self.update_slider_value)
        slider_layout.addWidget(self.slider)

        self.slider_value = QtWidgets.QLineEdit("0", self)
        self.slider_value.setReadOnly(True)
        slider_layout.addWidget(self.slider_value)

        self.mainLayout.addLayout(slider_layout)

        # create buttons
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.setSpacing(2)
        self.buttonsLayout.setContentsMargins(0,0,0,0)  # Left Top Right Bottom
        
        self.button_Create = QtWidgets.QPushButton('Create')
        self.button_Apply = QtWidgets.QPushButton('Apply')
        self.button_Close = QtWidgets.QPushButton('Close')
        
        # put these buttons in layout
        self.buttonsLayout.addWidget(self.button_Create)
        self.buttonsLayout.addWidget(self.button_Apply)
        self.buttonsLayout.addWidget(self.button_Close)
        
        # buttons layout to main to main layout
        self.mainLayout.addLayout(self.buttonsLayout)

        # buttons func
        self.button_Create.clicked.connect(self.create)
        self.button_Apply.clicked.connect(self.apply)
        self.button_Close.clicked.connect(self.close)

    def update_slider_value(self, value):
        self.slider_value.setText(str(value))

    def create(self):
        # create object
        self.apply()
        self.close()
        
    def apply(self):
        # create object
        object_name = self.name_input.text()
        x_position = self.slider.value()

        if object_name:
            if self.radio_Sphere.isChecked():
                new_object = cmds.polySphere(name=object_name)[0]
            elif self.radio_Cube.isChecked():
                new_object = cmds.polyCube(name=object_name)[0]
            else:
                new_object = cmds.polyCone(name=object_name)[0]
            
            # Move x position
            cmds.move(x_position, 0, 0, new_object)
        else:
            cmds.warning("Please enter a name for the object.")

# Kill window if it already exists
if cmds.window('myTestWindow', q=1, exists=1):
    cmds.deleteUI('myTestWindow')
    
# Kill preferences if they exist
if cmds.windowPref('myTestWindow', exists=1):
    cmds.windowPref('myTestWindow', remove=1)

# Show UI
myUI = MyDialog()
myUI.show()

