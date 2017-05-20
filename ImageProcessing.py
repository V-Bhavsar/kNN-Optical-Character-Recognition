import numpy as np
import cv2

def capture_image():

	# Starting webcam capture -> Webcam port on my MacBook is port 0
	camera = cv2.VideoCapture(0)

	while(1):
		ret_val, frame = camera.read()
		cv2.imshow("Image Capture", frame)

		key = cv2.waitKey(30)

		if key == 27:
			#Escape hit: exit
			break
		elif key == 32:
			#Spacebar hit: capture current frame
			image_name = "OriginalImage.png"

			#Saving Image
			cv2.imwrite(image_name, frame)
			print "The original image has been saved as " + image_name
			break

	camera.release()
	cv2.destroyAllWindows()

def process_image():
	original_image = cv2.imread("OriginalImage.png")

	#Image Processing (blur and converting to black and white)
	image_grayscale = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
	image_blur = cv2.GaussianBlur(image_grayscale, (5,5), 0)
	threshold, image_b_and_w = cv2.threshold(image_blur, 70, 255, cv2.THRESH_BINARY_INV)

	cv2.imshow("Preview", image_b_and_w)
	print "Displaying the image after processing"

	#Saving the image
	image_name = "ProcessedImage.png"
	cv2.imwrite(image_name, image_b_and_w)
	print "The processed image has been saved as " + image_name

	#Resizing the image to 20x20
	dimensions = (20,20)

	resized_image = cv2.resize(image_b_and_w, dimensions, interpolation = cv2.INTER_AREA)

	cv2.imshow("Preview", resized_image)
	print "Displaying the resized image"

	#Saving the image
	image_name = "ResizedImage.png"
	cv2.imwrite(image_name, resized_image)
	print "The processed image has been saved as " + image_name

def run():
	capture_image()
	process_image()





