import sys
import urx
from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper
import time

rob = urx.Robot("192.168.1.102")
robotiqgrip = Robotiq_Two_Finger_Gripper(rob)

if(len(sys.argv) != 2):
    print("false")
    sys.exit()

if(sys.argv[1] == "close") :
    robotiqgrip.close_gripper()
if(sys.argv[1] == "open") :
    robotiqgrip.open_gripper()
else:
    robotiqgrip.gripper_action(int(sys.argv[1]))
# for i in range(25):
#     print(i)
#     robotiqgrip.gripper_action(i  * 10)
#     time.sleep(0.01)

rob.close()