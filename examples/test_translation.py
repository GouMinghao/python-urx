import urx
import logging
import time
import numpy as np
import math
from urx import RobotPose
logging.basicConfig(level=logging.WARN)

# Robotiq TCP = [0, 0, 0.16, 0, 0, 0]
# Ready Pose = [-0.5, 0, 0.35, 0, -math.pi, 0]

rob = urx.Robot("192.168.1.102")
try:
    #rob = urx.Robot("localhost")
    rob.set_tcp((0, 0, 0.16, 0, 0, 0))

    rob.set_payload(0, (0, 0, 0))

    v = 0.01
    a = 0.01

    pose = rob.getl()

    joint_pose = rob.getj()

    rpose = RobotPose()
    rpose.set_pose(pose)
    rpose.set_joint_pose(joint_pose)
    print('origin pose:{}'.format(pose))
    print('joint angle:',rpose.get_joint_pose(angle_type='degree'))
    print('pose:', rpose.get_pose(length_unit='inch', angle_unit='pi'))


    pose[0] = -0.5
    pose[1] = 0
    pose[2] = 0.35

    pose[3] = 0
    pose[4] = - math.pi
    pose[5] = 0

    pose[3] = math.pi
    pose[4] = 0
    pose[5] = math.pi / 2
    print('target pose:{}'.format(pose))
    # rob.movel(pose, acc=a, vel=v)

    pose = rob.getl()
    print("after move, robot tcp is at: ", pose)

finally:
    rob.close()