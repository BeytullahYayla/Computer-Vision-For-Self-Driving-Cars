import cv2
import numpy as np
import matplotlib.pyplot as plt

def make_coordinates(image,line_parameters):
    slope,intercept=line_parameters
    y1=image.shape[0]
    y2=int(y1*(3/5))
    x1=int((y1-intercept)/slope)
    x2=int((y2-intercept)/slope)

    return np.array([x1,y1,x2,y2])

def avarage_slope_intercept(image,lines):
    left_fit=[]
    right_fit=[]
    for line in lines:
        x1,y1,x2,y2=line.reshape(4)
        parameters=np.polyfit((x1,x2),(y1,y2),1)
        slope=parameters[0]
        intercept=parameters[1]
        if slope<0:
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))
        left_fit_avarage=np.average(left_fit,axis=0)
        right_fit_avarage=np.average(right_fit,axis=0)
        #avaraging process will be done across the rows
        left_line=make_coordinates(image,left_fit_avarage)
        right_line=make_coordinates(image,right_fit_avarage)

        return np.array([left_line,right_line])

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

avaraged_line=avarage_slope_intercept(lane_image,line)
line_image_with_avarage_slope_intercept=display_lines(lane_image,avaraged_line)
cv2.imshow("Lines on the image",line_image)
#combo_image=cv2.addWeighted(lane_image,0.8,line_image,1,1)
#cv2.imshow("Image with lines",combo_image)
print(lane_image.shape)#(704,1279,3)
cv2.waitKey(0)