import cv2
import numpy as np
R = np.array([[0,1,0],[1,0,0],[0,0,-1]],dtype=np.float32)
# R = np.zeros((3, 3), dtype=np.float64)
print(R)
rvecs = cv2.Rodrigues(R)
print(rvecs)
# rvecs = np.zeros((1, 1, 3), dtype=np.float64)
# rvecs,_ = cv2.Rodrigues(R, rvecstmp)