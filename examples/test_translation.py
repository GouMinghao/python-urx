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
    pose1 = [-0.4501261531239667, -0.0023859654539026224, 0.45003161756996024, 2.2081439212952785, 2.225572199626629, -0.009125868294844316]
    pose2 = [-0.2505051406239682, -0.16642448523251233, 0.4611523200244381, -2.334997723233874, -1.421990779312004, 0.21876017710873752]
    pose3 = [-0.48834440414013297, -0.22143727734986757, 0.2502714286579647, -2.4654997332480106, -1.4102560009938265, -0.389548157172141]
    pose4 = [-0.5771443004744404, -0.12262917911993643, 0.32882353573713, 2.199571926718644, 1.9672870075125797, 0.6090958596544539]
    pose5 = [-0.5523154015889571, 0.04452485315732912, 0.3287748571922589, 2.578911733170794, 1.1665357042470843, 0.27767387780270314]
    pose6 = [-0.46468879864865104, 0.11694284446956853, 0.3287852543351126, 2.6973597739268804, -0.20731046897776595, 0.02558677251098468]
    rob.movel(pose1, acc=a, vel=v)

    # pose[0] = -0.5
    # pose[1] = 0
    # pose[2] = 0.23

    # pose[3] = 0
    # pose[4] = - math.pi
    # pose[5] = 0


    # rob.movel(pose, acc=a, vel=v)
    # robotiqgrip.close_gripper()

    # pose[0] = -0.45
    # pose[1] = 0
    # pose[2] = 0.45

    # pose[3] = 2.2214415
    # pose[4] = 2.2214415
    # pose[5] = 0

    # rob.movel(pose, acc=a, vel=v)
    
    # pose[0] = -0.45
    # pose[1] = 0
    # pose[2] = 0.45

    # pose[3] = 2.2214415
    # pose[4] = 2.2214415
    # pose[5] = 0

    # rob.movel(pose, acc=a, vel=v)
    # robotiqgrip.open_gripper()

    # pose = rob.getl()
    # print('actual pose:{}'.format(pose))

finally:
    rob.close()