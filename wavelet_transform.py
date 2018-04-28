
import os
import cv2
import glob
import cv2
import pywt






# Getting the path where the original images are located
TEST_IMAGE_PATHS = glob.glob("./object_detection/*.jpg")

newpath = './wavelet/' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

newpath2 = './original/' 
if not os.path.exists(newpath2):
    os.makedirs(newpath2)

count = 0;
list=[]
i = 0


# applying wavelets to each image
for image_path in TEST_IMAGE_PATHS:

	#grabbing the image
	img = cv2.imread(image_path)

	name2 = './original/' + str(count) + '.jpg'
	print ('Creating...' + name2);
	cv2.imwrite(name2, img)

	# turning it to gray scale
	gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	#applying the wavelet to the image
	(cA, (cH, cV, cD)) = pywt.wavedec2(gray_image, 'haar', level=1)

	#saveing the LL image as a png to a new folder
	name = './wavelet/' + str(count) + '.png'
	print ('Creating...' + name);
	cv2.imwrite(name, cA)




	count = count + 1

# When everything done, release the capture
cv2.destroyAllWindows()

