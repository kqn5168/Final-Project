
import os
import cv2
import glob
import cv2
import pywt






# Getting the path where the original images are located
TEST_IMAGE_PATHS = glob.glob("./object_detection/*.jpg")

newpath = './original/' 
if not os.path.exists(newpath):
    os.makedirs(newpath)


count = 0;
list=[]
i = 0


# applying wavelets to each image
for image_path in TEST_IMAGE_PATHS:

	#grabbing the image
	img = cv2.imread(image_path)

	# # turning it to gray scale
	# gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# #applying the wavelet to the image
	# (cA, (cH, cV, cD)) = pywt.wavedec2(gray_image, 'haar', level=1)

	#saveing the LL image as a png to a new folder
	name = './original/' + str(count) + '.jpg'
	print ('Creating...' + name);
	cv2.imwrite(name, img)


	count = count + 1


# When everything done, release the capture
cv2.destroyAllWindows()

