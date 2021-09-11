import cv2
import imutils

# read the image using opencv
image = cv2.imread('./dataset/train/friends.jpg')

# images are multidimensional have (height, width, and depth(channel))
# rows X columns X channels
(h, w, d) = image.shape
print(" height: {}\n widh: {}\n depth: {}".format(h, w, d))

# show the image using the opencv library
#cv2.imshow("Image", image)
#cv2.waitKey(0)

# extracting the color value from the image by giving the cordinate x=50,y=100
# we know height is rows and widht is columns so

(B,G,R) = image[100,50] #color (with in 0 -255 only on the x,y cordinate)

print (" R :{}, G:{}, B: {}".format(R,G,B))

# extracting the Region of interest (ROI)