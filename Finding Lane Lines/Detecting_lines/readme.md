# Detecting Lane Lines On Video
 Detecting lane lines is a crucial part of self-driving cars. The aim of this study, detecting lane lines using the OpenCV library to gain some intuition about self-driving cars and computer vision areas.<br>
 <br>Some of the Technologies used in this study:<b>Python,OpenCV,Numpy,Matplotlib</b><br><br>
 The study consistof 5 steps:<br>
 <ul>
 <li>Edge detection with Canny Image Detector</li>
 <li>Apply Region Of Interest to image</li>
 <li>Create Lane Lines using HuoughLinesP method</li>
 <li>Apply to lines Avarage Slope Intercept method</li>
 </ul>
 <br>
 
## Convert Image To Grayscale Image

	   
	   def canny(img):
    	   gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    	   kernel = 5
    	   blur = cv2.GaussianBlur(gray,(kernel, kernel),0)
    	   canny = cv2.Canny(gray, 50, 150)
    	   return canny
       
In this section we've created a method that convert image to canny image in order to detect edges in image. <br>Edge detection is an image processing technique for finding the boundaries of objects within images. It works by detecting discontinuities in brightness.<br>
After  applying canny() method to image i obtained following result.



<p  align="left">
<img  src="Data/test_image.jpg"  width="620" height="350">
</p>

<p  align="right">
<img  src="Results/canny_image.png"  width="620" height="350">
</p>





 
 
