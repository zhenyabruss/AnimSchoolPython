import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore, QtGui
from shiboken2 import wrapInstance

def get_maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

class SelectionSetButton(QtWidgets.QPushButton):
    def __init__(self, name, parent=None):
        super(SelectionSetButton, self).__init__(name, parent)
        self.setText(name)
        self.name = name
        self.selected_objects = []

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.select_objects()
        super(SelectionSetButton, self).mousePressEvent(event)

    def select_objects(self):
        cmds.select(self.selected_objects)

class SelectionSetTool(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(SelectionSetTool, self).__init__(parent)
        self.setWindowTitle('Selection Sets Tool')
        self.setFixedSize(250, 400)

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.add_button = QtWidgets.QPushButton('+')
        self.add_button.clicked.connect(self.add_selection_set)
        self.layout.addWidget(self.add_button)

    def add_selection_set(self):
        selected_objects = cmds.ls(selection=True)
        if not selected_objects:
            cmds.warning("No objects selected!")
            return

        button_name = f'Selection Set {self.layout.count()}'
        selection_button = SelectionSetButton(button_name)
        selection_button.selected_objects = selected_objects
        self.layout.insertWidget(self.layout.count() - 1, selection_button)

def show_selection_set_tool():
    try:
        for widget in QtWidgets.QApplication.allWidgets():
            if isinstance(widget, SelectionSetTool):
                widget.close()
                widget.deleteLater()
    except:
        pass

    main_window = get_maya_main_window()
    tool_window = SelectionSetTool(parent=main_window)
    tool_window.show()

show_selection_set_tool()
