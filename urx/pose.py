import numpy as np
import math
class RobotPose():
    def __init__(self):
        self.pose = np.zeros(6)
        self.joint_pose = np.zeros(6)

    def set_pose(self, pose):
        self.pose = np.array(pose)
    
    def set_joint_pose(self, joint_pose):
        self.joint_pose = np.array(joint_pose)

    def get_translation(self, length_unit = 'meter'):
        if length_unit == 'meter':
            translation = self.pose[:3]
        elif length_unit == 'millimeter':
            translation = self.pose[:3] * 1000
        elif length_unit == 'inch':
            translation = self.pose[:3] * 39.3700787
        else:
            raise ValueError('Unknown length unit:{}'.format(length_unit))
        return translation
    
    def get_rotation(self, angle_type = 'rad'):
        if angle_type == 'rad':
            angle = self.pose[3:]
        elif angle_type == 'pi':
            angle = self.pose[3:] / math.pi
        elif angle_type == 'degree':
            angle = self.pose[3:] / math.pi * 180
        else:
            raise ValueError('Unknown length unit:{}'.format(angle_type))
        return angle

    def get_rotation(self, angle_type = 'rad'):
        if angle_type == 'rad':
            angle = self.pose[3:]
        elif angle_type == 'pi':
            angle = self.pose[3:] / math.pi
        elif angle_type == 'degree':
            angle = self.pose[3:] / math.pi * 180
        else:
            raise ValueError('Unknown length unit:{}'.format(angle_type))
        return angle

    def get_pose(self, length_unit = 'meter', angle_unit = 'rad'):
        tranlation = self.get_translation(length_unit = length_unit)
        angle = self.get_rotation(angle_type = angle_unit)
        return np.concatenate((tranlation, angle))

    def get_joint_pose(self, angle_type = 'rad'):
        if angle_type == 'rad':
            angle = self.joint_pose
        elif angle_type == 'pi':
            angle = self.joint_pose / math.pi
        elif angle_type == 'degree':
            angle = self.joint_pose / math.pi * 180
        else:
            raise ValueError('Unknown length unit:{}'.format(angle_type))
        return angle