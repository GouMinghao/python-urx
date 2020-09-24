import urx
import logging
import time
import numpy as np
import math
from urx import RobotPose
logging.basicConfig(level=logging.WARN)

rob = urx.Robot("192.168.1.102")
#rob = urx.Robot("localhost")
rob.set_tcp((0,0,0,0,0,0))
rob.set_payload(0, (0,0,0))
l = -0.03
v = 0.05
a = 0.01
pose = rob.getl()
# print("before move[0.1, 0.1, 0.1], robot tcp is at: ", pose)
joint_pose = rob.getj()
# print(type(joint_pose))
# print("joint pose:{}".format(np.array(joint_pose) / math.pi * 180))
rpose = RobotPose()
rpose.set_pose(pose)
rpose.set_joint_pose(joint_pose)
print('joint angle:',rpose.get_joint_pose(angle_type='degree'))
print('pose:', rpose.get_pose(length_unit='inch', angle_unit='rad'))

# print("absolute move in base coordinate ")
# pose[2] += l
# pose[1] += l
# pose[0] += l
pose[0] = -0.5
pose[1] = 0
pose[2] = 0.55
pose[3] = - math.pi / 4 * 3
pose[4] = - math.pi / 2
pose[5] = 0
rob.movel(pose, acc=a, vel=v)
time.sleep(2)
pose = rob.getl()
print("after move[0.1, 0.1, 0.1], robot tcp is at: ", pose)
# print("relative move in base coordinate ")
# rob.translate((0, 0, -l), acc=a, vel=v)
# print("relative move back and forth in tool coordinate")
# rob.translate_tool((0, 0, -l), acc=a, vel=v)
# rob.translate_tool((0, 0, l), acc=a, vel=v)

rob.close()