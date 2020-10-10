import pyrealsense2 as rs
import numpy as np
import cv2
from multiprocessing import Process, Queue
import time
# from UR import UR5

    

# def show(pipeline, j):
#     # Start streaming
#     pipeline.start(config)
    

#     # get intrinsic matrix
#     cfg = pipeline.start(config) # Start pipeline and get the configuration it found
#     profile = cfg.get_stream(rs.stream.depth) # Fetch stream profile for depth stream
#     intr = profile.as_video_stream_profile().get_intrinsics() # Downcast to video_stream_profile and fetch intrinsics
#     print(intr)

#     time.sleep(1)

    # u.movel([-0.64271175, -0.23282238,  0.07831567, -1.1972846,   2.87400969,  0.05793196] ,t=3)
    # p = u.getTcpPose()
    # print("[{},{},{},{},{},{}]".format(*p))
    # j = u.getJoint()
    # print("[{},{},{},{},{},{}]".format(*j))

    
    # if j ==4:
    # # while True:
    #     k=0
    #     while(1):
    #         frames = pipeline.wait_for_frames()
    #         depth_frame = frames.get_depth_frame()
    #         color_frame = frames.get_color_frame()
    #         # Convert images to numpy arrays
    #         depth_image = np.asanyarray(depth_frame.get_data())
    #         # print(depth_image)
    #         color_image = np.asanyarray(color_frame.get_data())
    #         # cv2.namedWindow("Image") 
    #         # cv2.imshow('depth',depth_image)
    #         # cv2.imshow('color',color_image)
    #         cv2.imwrite('/Users/newuhe/Code/UR5_control/UR5_control/'+str(j)+'/'+str(k)+'color.png',color_image)
    #         cv2.imwrite('/Users/newuhe/Code/UR5_control/UR5_control/'+str(j)+'/'+str(k)+'depth.png',depth_image)
    #         k=k+1
    # else:
    #     for i in range(10):
    #         frames = pipeline.wait_for_frames()
    #         depth_frame = frames.get_depth_frame()
    #         color_frame = frames.get_color_frame()
    #         # Convert images to numpy arrays
    #         depth_image = np.asanyarray(depth_frame.get_data())
    #         # print(depth_image)
    #         color_image = np.asanyarray(color_frame.get_data())
    #         # cv2.namedWindow("Image") 
    #         # cv2.imshow('depth',depth_image)
    #         # cv2.imshow('color',color_image)
    #         cv2.imwrite('/Users/newuhe/Code/UR5_control/UR5_control/'+str(j)+'/'+str(i)+'color.png',color_image)
    #         cv2.imwrite('/Users/newuhe/Code/UR5_control/UR5_control/'+str(j)+'/'+str(i)+'depth.png',depth_image)


def get_cam(q1, q2):
    # Configure depth and color streams
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

    # Start streaming
    pipeline.start(config)

    while True:
        key = q1.get(True)
        if key == 1:
            frames = pipeline.wait_for_frames()
            depth_frame = frames.get_depth_frame()
            color_frame = frames.get_color_frame()
            if not depth_frame or not color_frame:
                continue
            # Convert images to numpy arrays
            depth_image = np.asanyarray(depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())

            q2.put( (color_image, depth_image) )
            # cd = np.concatenate((c, d), axis=1)



if __name__ == '__main__':
    import os
    q1 = Queue()
    q2 = Queue()
    cam = Process(target=get_cam, args=(q1, q2))
    cam.start()
    ## take picture
    q1.put(1)
    pic, depth = q2.get(True)
    # cv2.imshow(pic)
    scene_num = 'test_scene_0002'
    rgb_dir = os.path.join(scene_num,'rbg')
    depth_dir = os.path.join(scene_num,'depth')
    depth_vis_dir = os.path.join(scene_num,'depth_vis')
    if not os.path.exists(rgb_dir):
        os.makedirs(rgb_dir)
    if not os.path.exists(depth_dir):
        os.makedirs(depth_dir)
    if not os.path.exists(depth_vis_dir):
        os.makedirs(depth_vis_dir)
    image_num = 0
    depth_vis = depth.astype(np.float32)
    depth_vis = (depth_vis / depth_vis.max() * 255.0).astype(np.int32)
    print(depth_vis)
    while os.path.exists(os.path.join(rgb_dir, '%04d.png' % image_num)):
        image_num += 1
    cv2.imwrite(os.path.join(rgb_dir,'%04d.png' % image_num), pic)
    cv2.imwrite(os.path.join(depth_dir, '%04d.png' % image_num), depth)
    cv2.imwrite(os.path.join(depth_vis_dir, '%04d.png' % image_num), depth_vis)
    # u = UR5("192.168.2.147")
    # pipeline = rs.pipeline()
    # config = rs.config()
    # config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    # config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    # print('initialize')

    # # get intrinsic matrix
    # cfg = pipeline.start(config) # Start pipeline and get the configuration it found
    # profile = cfg.get_stream(rs.stream.depth) # Fetch stream profile for depth stream
    # intr = profile.as_video_stream_profile().get_intrinsics() # Downcast to video_stream_profile and fetch intrinsics
    # print(intr)
    # time.sleep(1)

    # u.movej([-0.39803249, -1.9321478,   2.06931114,  0.34823608, -5.01261551,  1.81272268],t=3)
    # time.sleep(1)
    # show(pipeline,0)
    
    # u.movej([ 0.26108533, -0.98936397,  1.34889364, -0.47466642, -2.63877088,  1.81122577],t=3)
    # time.sleep(1)
    # show(pipeline,1)
    
    # u.movej([-0.27609331, -0.92839986,  0.97532511, -0.55726511, -1.64107496,  1.81153738],t=3)
    # time.sleep(1)
    # show(pipeline,2)
    
    # u.movej([-0.92148906, -1.33882076,  1.8098917,  -0.59490663, -0.66457636,  1.92021477],t=3)
    # time.sleep(1)
    # show(pipeline,3)
    
    # u.movej([-0.39803249, -1.9321478,   2.06931114,  0.34823608, -5.01261551,  1.81272268],t=3)
    # time.sleep(1)
    # show(pipeline,4)


    # # Configure depth and color streams
    # pipeline = rs.pipeline()
    # config = rs.config()
    # config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    # config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

    # # Start streaming
    # pipeline.start(config)

    # try:
    #     while True:

    #         # Wait for a coherent pair of frames: depth and color
    #         frames = pipeline.wait_for_frames()
    #         depth_frame = frames.get_depth_frame()
    #         color_frame = frames.get_color_frame()
    #         if not depth_frame or not color_frame:
    #             continue

    #         # Convert images to numpy arrays
    #         depth_image = np.asanyarray(depth_frame.get_data())
    #         color_image = np.asanyarray(color_frame.get_data())

    #         # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
    #         depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

    #         # Stack both images horizontally
    #         images = np.hstack((color_image, depth_colormap))
    #         print(images.shape)

    #         # Show images
    #         cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
    #         cv2.imshow('RealSense', images)
    #         cv2.waitKey(1)

    # finally:

    #     # Stop streaming
    #     pipeline.stop()


      
