import sys
import time

from naoqi import ALProxy


def main(robotIP, port):
	try:
		ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)
	except Exception, e:
		print("Could not create a proxy to ALTextToSpeech")

	#ttsProxy.say("WIPE FOREHEAD")

	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([0.433333, 1.03333, 2.06667, 2.63333, 3.1, 3.56667, 4])
	keys.append([[-0.0261199, [3, -0.144444, 0], [3, 0.2, 0]], [0.427944, [3, -0.2, 0], [3, 0.344444, 0]], [0.308291, [3, -0.344444, 0.0680287], [3, 0.188889, -0.0373061]], [0.11194, [3, -0.188889, 0.0588857], [3, 0.155556, -0.0484941]], [-0.013848, [3, -0.155556, 0], [3, 0.155556, 0]], [0.061318, [3, -0.155556, 0], [3, 0.144444, 0]], [0.00806209, [3, -0.144444, 0], [3, 0, 0]]])

	names.append("HeadYaw")
	times.append([0.433333, 1.03333, 2.06667, 2.63333, 3.1, 3.56667, 4])
	keys.append([[-0.234743, [3, -0.144444, 0], [3, 0.2, 0]], [-0.622845, [3, -0.2, 0], [3, 0.344444, 0]], [-0.113558, [3, -0.344444, -0.132755], [3, 0.188889, 0.072801]], [-0.00617796, [3, -0.188889, 0], [3, 0.155556, 0]], [-0.027654, [3, -0.155556, 0.00511335], [3, 0.155556, -0.00511335]], [-0.036858, [3, -0.155556, 0], [3, 0.144444, 0]], [-0.0048461, [3, -0.144444, 0], [3, 0, 0]]])

	names.append("LElbowRoll")
	times.append([0.3, 0.9, 1.93333, 2.5, 2.96667, 3.43333, 4])
	keys.append([[-0.866668, [3, -0.1, 0], [3, 0.2, 0]], [-0.868202, [3, -0.2, 0], [3, 0.344444, 0]], [-0.822183, [3, -0.344444, 0], [3, 0.188889, 0]], [-0.992455, [3, -0.188889, 0], [3, 0.155556, 0]], [-0.966378, [3, -0.155556, 0], [3, 0.155556, 0]], [-0.990923, [3, -0.155556, 0.00628889], [3, 0.188889, -0.00763651]], [-1.00815, [3, -0.188889, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([0.3, 0.9, 1.93333, 2.5, 2.96667, 3.43333, 4])
	keys.append([[-0.957257, [3, -0.1, 0], [3, 0.2, 0]], [-0.823801, [3, -0.2, 0], [3, 0.344444, 0]], [-1.00788, [3, -0.344444, 0], [3, 0.188889, 0]], [-0.925044, [3, -0.188889, 0], [3, 0.155556, 0]], [-1.24412, [3, -0.155556, 0], [3, 0.155556, 0]], [-0.960325, [3, -0.155556, 0], [3, 0.188889, 0]], [-1.38648, [3, -0.188889, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([0.9, 1.93333, 2.5, 3.43333, 4])
	keys.append([[0.132026, [3, -0.3, 0], [3, 0.344444, 0]], [0.132026, [3, -0.344444, 0], [3, 0.188889, 0]], [0.132026, [3, -0.188889, 0], [3, 0.311111, 0]], [0.132026, [3, -0.311111, 0], [3, 0.188889, 0]], [0.247252, [3, -0.188889, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([0.3, 0.9, 1.93333, 2.5, 2.96667, 3.43333, 4])
	keys.append([[0.863599, [3, -0.1, 0], [3, 0.2, 0]], [0.858999, [3, -0.2, 0], [3, 0.344444, 0]], [0.888144, [3, -0.344444, -0.0151908], [3, 0.188889, 0.00833043]], [0.929562, [3, -0.188889, -0.0235543], [3, 0.155556, 0.0193977]], [1.017, [3, -0.155556, 0], [3, 0.155556, 0]], [0.977116, [3, -0.155556, 0], [3, 0.188889, 0]], [1.39654, [3, -0.188889, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([0.3, 0.9, 1.93333, 2.5, 2.96667, 3.43333, 4])
	keys.append([[0.286815, [3, -0.1, 0], [3, 0.2, 0]], [0.230059, [3, -0.2, 0.0103309], [3, 0.344444, -0.0177921]], [0.202446, [3, -0.344444, 0], [3, 0.188889, 0]], [0.406468, [3, -0.188889, 0], [3, 0.155556, 0]], [0.360449, [3, -0.155556, 0.0145729], [3, 0.155556, -0.0145729]], [0.31903, [3, -0.155556, 0.00802848], [3, 0.188889, -0.00974887]], [0.307117, [3, -0.188889, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([0.9, 1.93333, 2.5, 3.43333, 4])
	keys.append([[0.386526, [3, -0.3, 0], [3, 0.344444, 0]], [0.386526, [3, -0.344444, 0], [3, 0.188889, 0]], [0.386526, [3, -0.188889, 0], [3, 0.311111, 0]], [0.386526, [3, -0.311111, 0], [3, 0.188889, 0]], [0.00105499, [3, -0.188889, 0], [3, 0, 0]]])

	names.append("RElbowRoll")
	times.append([0.166667, 0.766667, 1.8, 2.36667, 2.83333, 3.3, 4])
	keys.append([[1.28093, [3, -0.0555556, 0], [3, 0.2, 0]], [1.39752, [3, -0.2, -0.0356889], [3, 0.344444, 0.0614643]], [1.57239, [3, -0.344444, 0], [3, 0.188889, 0]], [1.24105, [3, -0.188889, 0.0186267], [3, 0.155556, -0.0153397]], [1.22571, [3, -0.155556, 0.0153397], [3, 0.155556, -0.0153397]], [0.840674, [3, -0.155556, 0], [3, 0.233333, 0]], [1.00454, [3, -0.233333, 0], [3, 0, 0]]])

	names.append("RElbowYaw")
	times.append([0.166667, 0.766667, 1.8, 2.36667, 2.83333, 3.3, 4])
	keys.append([[-0.128898, [3, -0.0555556, 0], [3, 0.2, 0]], [-0.285367, [3, -0.2, 0], [3, 0.344444, 0]], [-0.15651, [3, -0.344444, -0.128857], [3, 0.188889, 0.0706633]], [0.754686, [3, -0.188889, -0.242834], [3, 0.155556, 0.199981]], [1.17193, [3, -0.155556, 0], [3, 0.155556, 0]], [0.677985, [3, -0.155556, 0], [3, 0.233333, 0]], [1.38418, [3, -0.233333, 0], [3, 0, 0]]])

	names.append("RHand")
	times.append([0.766667, 1.8, 2.36667, 3.3, 4])
	keys.append([[0.166571, [3, -0.255556, 0], [3, 0.344444, 0]], [0.166208, [3, -0.344444, 0], [3, 0.188889, 0]], [0.166571, [3, -0.188889, 0], [3, 0.311111, 0]], [0.166208, [3, -0.311111, 0], [3, 0.233333, 0]], [0.25, [3, -0.233333, 0], [3, 0, 0]]])

	names.append("RShoulderPitch")
	times.append([0.166667, 0.766667, 1.8, 2.36667, 2.83333, 3.3, 4])
	keys.append([[0.0767419, [3, -0.0555556, 0], [3, 0.2, 0]], [-0.59515, [3, -0.2, 0.11552], [3, 0.344444, -0.19895]], [-0.866668, [3, -0.344444, 0], [3, 0.188889, 0]], [-0.613558, [3, -0.188889, -0.253109], [3, 0.155556, 0.208443]], [0.584497, [3, -0.155556, -0.249275], [3, 0.155556, 0.249275]], [0.882091, [3, -0.155556, -0.108169], [3, 0.233333, 0.162253]], [1.39576, [3, -0.233333, 0], [3, 0, 0]]])

	names.append("RShoulderRoll")
	times.append([0.166667, 0.766667, 1.8, 2.36667, 2.83333, 3.3, 4])
	keys.append([[-0.019984, [3, -0.0555556, 0], [3, 0.2, 0]], [-0.019984, [3, -0.2, 0], [3, 0.344444, 0]], [-0.615176, [3, -0.344444, 0.175025], [3, 0.188889, -0.0959815]], [-0.833004, [3, -0.188889, 0], [3, 0.155556, 0]], [-0.224006, [3, -0.155556, -0.00920487], [3, 0.155556, 0.00920487]], [-0.214801, [3, -0.155556, 0], [3, 0.233333, 0]], [-0.297251, [3, -0.233333, 0], [3, 0, 0]]])

	names.append("RWristYaw")
	times.append([0.766667, 1.8, 2.36667, 3.3, 4])
	keys.append([[-0.058334, [3, -0.255556, 0], [3, 0.344444, 0]], [-0.0521979, [3, -0.344444, 0], [3, 0.188889, 0]], [-0.067538, [3, -0.188889, 0], [3, 0.311111, 0]], [-0.038392, [3, -0.311111, -0.0121571], [3, 0.233333, 0.00911784]], [-0.00371307, [3, -0.233333, 0], [3, 0, 0]]])

	try:
		motion = ALProxy("ALMotion",robotIP,port)
		motion.angleInterpolationBezier(names, times, keys)
	except BaseException, err:
		print err
  
  
if __name__ == "__main__":
	robotIP = "127.0.0.1"
	port = 9559

	if len(sys.argv) <= 1:
		print "(robotIP default: 127.0.0.1)"
	elif len(sys.argv) <= 2:
		robotIP = sys.argv[1]
	else:
		port = int(sys.argv[2])
		robotIP = sys.argv[1]

	start = time.time()
	main(robotIP, port)
	end = time.time()
	print ("%.2f seconds elapsed" % (end-start))
