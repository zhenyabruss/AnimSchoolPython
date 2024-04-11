import maya.cmds as cmds

mySphere = cmds.ls(cmds.polySphere())[0]
cmds.move(-10,0,0,mySphere)
cmds.setKeyframe(mySphere, time=1)
last_frame = cmds.playbackOptions(q=True, maxTime=True)
cmds.setKeyframe(mySphere,attribute='translateX', time=last_frame, value = 10)

myBox = cmds.ls(cmds.polyCube())[0]
cmds.move(-10,0,10)
cmds.currentTime(1)
constraint = cmds.parentConstraint(mySphere, myBox, maintainOffset=True)
start_frame = cmds.playbackOptions(q=True, minTime=True)
end_frame = cmds.playbackOptions(q=True, maxTime=True)
cmds.bakeResults(myBox, simulation=True, t=(start_frame, end_frame))
cmds.delete(constraint)