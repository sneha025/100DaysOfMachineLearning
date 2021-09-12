import cv2
import imutils

image =cv2.imread('../dataset/train/tetris_blocks.png')
#cv2.imshow("Image",image)
#cv2.waitKey(0)

#conver the image into grayscale

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Image",gray)
#cv2.waitKey(0)

# let's detect edges
edges = cv2.Canny(gray,50,150)
#cv2.imshow("Image",edges)
#cv2.waitKey(0)

# thresholding

thresh =cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)[1]
cv2.imshow("thresh",thresh)
cv2.waitKey(0)

# finding the contours

conts =cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

conts= imutils.grab_contours(conts)

output = image.copy()

for c in conts:
    cv2.drawContours(output,[c],-1,(240,0,159),3)
    cv2.imshow("Contours", output)
    cv2.waitKey(0)


text ="I found {} objects".format(len(conts))

cv2.putText(output,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(240,0,159),2)
cv2.imshow("Contours", output)
cv2.waitKey(0)