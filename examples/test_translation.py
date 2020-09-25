import urx
import logging
import time
import numpy as np
import math
from urx import RobotPose
from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper

logging.basicConfig(level=logging.WARN)

# Robotiq TCP = [0, 0, 0.16, 0, 0, 0]
# Ready Pose = [-0.5, 0, 0.35, 0, -math.pi, 0]

rob = urx.Robot("192.168.1.102")
robotiqgrip = Robotiq_Two_Finger_Gripper(rob)
try:
    #rob = urx.Robot("localhost")
    rob.set_tcp((0, 0, 0.16, 0, 0, 0))

    rob.set_payload(0, (0, 0, 0))

    v = 0.1
    a = 0.1

    pose = rob.getl()

    joint_pose = rob.getj()

    rpose = RobotPose()
    rpose.set_pose(pose)
    rpose.set_joint_pose(joint_pose)
    print('origin pose:{}'.format(pose))


    # pose[0] = -0.5
    # pose[1] = 0
    # pose[2] = 0.35

    # pose[3] = 0
    # pose[4] = - math.pi
    # pose[5] = 0

    pose[0] = -0.45 + 0.079 - 0.077
    pose[1] = 0 - 0.136 
    pose[2] = 0.45 - 0.035 - 0.40 + 0.16
    # pose[2] = 0.45 

    pose[3] = 2.2214415
    pose[4] = 2.2214415
    pose[5] = 0

    rob.movel(pose, acc=a, vel=v)

    # pose[0] = -0.5
    # pose[1] = 0
    # pose[2] = 0.23

    # pose[3] = 0
    # pose[4] = - math.pi
    # pose[5] = 0


    # rob.movel(pose, acc=a, vel=v)
    robotiqgrip.close_gripper()

    # pose[0] = -0.45
    # pose[1] = 0
    # pose[2] = 0.45

    # pose[3] = 2.2214415
    # pose[4] = 2.2214415
    # pose[5] = 0

    # rob.movel(pose, acc=a, vel=v)
    
    pose[0] = -0.45
    pose[1] = 0
    pose[2] = 0.45

    pose[3] = 2.2214415
    pose[4] = 2.2214415
    pose[5] = 0

    rob.movel(pose, acc=a, vel=v)
    robotiqgrip.open_gripper()

    pose = rob.getl()
    print('actual pose:{}'.format(pose))

finally:
    rob.close()