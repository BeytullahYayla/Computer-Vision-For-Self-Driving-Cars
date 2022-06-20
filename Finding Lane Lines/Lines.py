import cv2
import numpy as np
import matplotlib.pyplot as plt
def canny(image):
    gray_image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blurred=cv2.GaussianBlur(gray_image,(5,5),0)
    Canny=cv2.Canny(blurred,50,150)
    return Canny
def region_of_interest(image):
    height=image.shape[0]#Height of our image
    polygons=np.array(
        [[(200,height),(1100,height),(550,255)]]
        )#Triangle for region of interest
    mask=np.zeros_like(image)#creates an array with zeros
    cv2.fillPoly(mask,polygons,255)
    masked_image=cv2.bitwise_and(image,mask)
    ##Take a triangle whose boundaries we defined and apply it on the mask such that area bounded by the polygonial contour will be completely white
    return masked_image
def display_lines(image,lines):
    line_image=np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2=line.reshape(4)
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
    return line_image   
    
    

lane_image=cv2.imread('test_image.jpg')
canny_image=canny(lane_image)
cropped_image=region_of_interest(canny_image)
line=cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
line_image=display_lines(lane_image,line)
cv2.imshow("Lines on the image",line_image)
combo_image=cv2.addWeighted(line_image,0.8,lane_image,1,1)
cv2.imshow("Image with lines",combo_image)


cv2.waitKey(0)