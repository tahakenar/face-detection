import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
font = cv2.FONT_HERSHEY_SIMPLEX
images = []

def read_image(filename):
	#read image and resize it
	img = cv2.imread(filename)
	h = int(img.shape[0]/2)
	w = int(img.shape[1]/2)
	img = cv2.resize(img,(w,h))
	return img

def detect_faces(image):
	#makes the grayscale image and detect faces (haar_cascades)
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,1.1,9)
	return faces

def show_faces(image,faces):
	count = 0
	#gets position values from each face detected and draws rectangle around them
	for (x,y,w,h) in faces:
		count += 1
		cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)
	cv2.rectangle(image,(0,0),(140,30),(0,0,0),-1)
	cv2.putText(image,f"Total faces: {count}",(10,20),font,0.5,(0,255,0),1,cv2.LINE_AA)
	print("Press esc to close the image...")
	cv2.imshow("Face detector",image)
	k = cv2.waitKey(0)
	if k == 27:         # wait for ESC key to exit
		cv2.destroyWindow("Face detector")
		cv2.waitKey(1)

#gets only the files with desired extension in the current directory
#then add them to the global 'images' list
def get_images():
	global images
	temp = []
	exts = ['png','jpg','jpeg']
	path = "/Users/emirkenar/Desktop/ImageManipulation"
	dirs = os.listdir(path)
	for file in dirs:
		split = file.split('.')
		if (len(split) < 2) or (split[1] not in exts):
			pass
		else:
			temp.append(file)
	images = images + temp


def get_filename(images):
	while True:
		inp = input("name of the file? ")
		if inp not in images:
			print(f"No file named {inp}. Try again\n")
			continue
		else:
			break
	return inp


def menu():
	print("Welcome to the face detection app\nSelect your operation:\n1. Print files in the directory\n2. Detect faces with known file name\n3. Quit")
	get_images()
	while True:
		slc = input("\nWrite only the number of desired operation and press enter: ")
		if slc == '1':
			for i in images:
				print(i)
			continue
		elif slc == '2':
			filename = get_filename(images)
			image = read_image(filename)
			face = detect_faces(image)
			show_faces(image,face)
			continue
		elif slc == '3':
			break
		else:
			print("Invalid input...")
			continue
menu()






