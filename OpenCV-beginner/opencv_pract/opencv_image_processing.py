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

# manual extraction
# for extracting the roi we need the cordinates which create a rectangle (ymin : ymax , xmin:xmax)
# image[startY:endY, startX:endX]
roi = image[160:260, 320:420]
#cv2.imshow("ROI",roi)
#cv2.waitKey(0)

# resize the image in 200X200 pixels

resize = cv2.resize(image, (200,200))
#cv2.imshow("resized" ,resize)
#cv2.waitKey(0)

# instead of fixed ratio , we going to set aspect ratio

r = 300.0/w
dim = (300, int(h*r))  # dimension are in the form of the (widht X height)

# we created a aspect ratio r of new width  , we wanna to have 300px to be our width
# then we need the  new height with related to the 300 widht = h*r


new_resize = cv2.resize(image,dim)
cv2.imshow("resized" ,new_resize)
cv2.waitKey(0)