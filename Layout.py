import cv2
import tryinglens as ocr
import serial
import time
from PIL import Image, ImageFilter
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from camera import cameraclick
from imageopen import photoback



count = 0

def Assign():
	print("assign")
	key = cameraclick()
	global count
	count+=1
	path =""

	cam2 = cv2.VideoCapture(2)
	cv2.namedWindow("testInfo")
	file = open("KeynInfo.txt", "a+")
	img_name = ""

	while(True):
		retI, frameI = cam2.read()
		
		cv2.imshow("testInfo", frameI)
		arduiOp=0
		ArduinoSerial=serial.Serial("/dev/ttyACM0", 9600)

		try:
			arduiOp=int(str(ArduinoSerial.readline().strip("\n")))
		except:
			pass

		if not retI:
			break

		k = cv2.waitKey(1)

		if arduiOp==3:
			print ("clicked")
			img_name="camera_info" + str(count) + ".jpg"
			cv2.imwrite(img_name, frameI)
			break

	file.write(key+";"+img_name)
	return


def Recall():
	print("recall")
	photoback()
	return





def func():
	
	ArduinoSerial=serial.Serial("/dev/ttyACM0", 9600)
	while True:
		arduiOp=0
		try:
			arduiOp=int(str(ArduinoSerial.readline().strip("\n")))
			print (arduiOp)
		except:
			print ("blah")
			pass
			
		if (arduiOp==1):
			# var=1
			Assign()
		elif (arduiOp==4):
			# var=4
			Recall()

func()