import cv2
import serial
import time
import tryinglens as ocr
 
def cameraclick():
	"""This function opens video frames from camera and waits from input from arduino serial monitor.
	If the capture button is pressed on the arduino, existing frame is captured. It sends the image as argument
	to detect document function that processes the photo and converts it into text. This text is returned as key.
	"""

	cam = cv2.VideoCapture(1)

	cv2.namedWindow("test")
	
	key = ""

	while True:
		ret, frame = cam.read()
		cv2.imshow("test", frame)
		arduiOp=0
		ArduinoSerial=serial.Serial("/dev/ttyACM0", 9600)

		try:
			arduiOp=int(str(ArduinoSerial.readline().strip("\n")))
			print (arduiOp)
		except:
			pass

		if not ret:
			break

		k = cv2.waitKey(1)

		if arduiOp==2:
			print ("clicked")
			img_name="camera1.jpg"
			cv2.imwrite(img_name, frame)
			key=ocr.detect_document(img_name)
			break
			

	print(key)
	print("Key Printed")
	cam.release()
	cv2.destroyAllWindows()
	return key

# cameraclick()