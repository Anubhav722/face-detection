import cv2


# Loading the cascades. xml files

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Define functions that will do the detections.

# will take input of images coming from the webcam.
# NOTE: Cascades work o black and white image.
# So accepting the image here in black and white (gray)
# and also the original image
def detect(gray, frame):
	# Get the coordinates of the rectangle which detect the face.

	# x, y are the coordiantes on the upper left corner.
	# w and h are the width and height respectively.
	# x, y, w, h = 

	# detectMultiScale method takes the gray image.and 
	# other arguments include the factor by which image size is going to be reduced.
	# min. no. neighbours.

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	print (faces) # tuples (x,y,w,h)

	for (x,y,w,h) in faces:
		# Draw the rectangle for the faces.
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

		# Eyes will be detected where we have found our face.
		# So we will perform our tests on the face's referential frame in order to save the computational time.

		# We will be taking to region of interest. The gray scale image and the colored image.

		roi_gray = gray(y:y+h, x:x+w)
		roi_color = frame(y:y+h, x:x+w)

		# Detecting the eyes.
		eyes = eye_cascade.detectMultiScale(rot_gray, 1.1, 3)

		for (ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)

	return frame



