  
# Importing Image from PIL package  
from PIL import Image 
      
# creating a image object 
def ColorThreshold(InputImage):
	image = Image.open(InputImage)  
  
	width, height = image.size 

	i=0
	k=0
	for x in range(height): 
		for y in range(width): 
			cordinate = x1, y1 = y,x
			r,g,b=image.getpixel(cordinate)
			k=k+1
			if not(abs(r-b)<10 and (r-g)<10 and (b-g)<10):
				image.putpixel((y, x), (0, 0, 0, 255) ) 
			else:
				i=i+1
  
	if float(i)/float(k)*100>50:
		return 0
	else:
		return 1
	#image.show() 
	#im1 = image.save("geeks.bmp") 
