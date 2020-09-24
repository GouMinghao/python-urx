import urx
import logging
import time

logging.basicConfig(level=logging.WARN)

rob = urx.Robot("192.168.1.102")
#rob = urx.Robot("localhost")
rob.set_tcp((0,0,0.20,0,0,0))
rob.set_payload(0.5, (0,0,0))
l = -0.03
v = 0.05
a = 0.3
pose = rob.getl()
print("before move[0.1, 0.1, 0.1], robot tcp is at: ", pose)

# print("absolute move in base coordinate ")
# pose[2] += l
pose[1] += l
# pose[0] += l

rob.movel(pose, acc=a, vel=v)
time.sleep(2)
print("after move[0.1, 0.1, 0.1], robot tcp is at: ", pose)
# print("relative move in base coordinate ")
# rob.translate((0, 0, -l), acc=a, vel=v)
# print("relative move back and forth in tool coordinate")
# rob.translate_tool((0, 0, -l), acc=a, vel=v)
# rob.translate_tool((0, 0, l), acc=a, vel=v)

rob.close()