# Original code from:
# http://code.activestate.com/recipes/578590-mandelbrot-fractal-using-tkinter/

import tkinter
import random 
from tkinter import *

'''This was my first picture I created. I tried to keep it simple to make sure I 
understood all of the concepts, but I wanted to play around with different colors
and fading with random.random().'''
def mandelbrot(z, c, count):
	z = z ** 2 + c
	count += 1 
	if abs(z) > 2 or count > maxIt - 1: 
		return count
	return mandelbrot(z,c,count)
'''part of the original code'''
WIDTH = 640 
HEIGHT = 640
xmin = -.4207407407 
xmax = -.0007407407
ymin =-1.3116666 
ymax = -.891666666
maxIt = 255 
'''I used the website ( http://atopon.org/mandel/ (Links to an external site.))
to find a specific zoom I liked. '''
window = Tk()

'''this caused me trouble in the last step where I was putting all of the three pictures 
on the same  file. I tried originally to do all three with Tk() and renaming varaibles
but this did not work. As a result, when I went to extra help I was told about the function 
toplevel(). Then I tried to use this three times which produced 4 windows, (three top levels). 
As a result, I had to find the right balance and use toplevel twice and this function 
just once.'''
canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = "#000000")


img = PhotoImage(width = WIDTH, height = HEIGHT)
canvas.create_image((0, 0), image = img, state = "normal", anchor = tkinter.NW)


for row in range(HEIGHT):
    for col in range(WIDTH):
    	
        c = complex(xmin + (xmax - xmin) * col / WIDTH, ymin + (ymax - ymin) * row / HEIGHT)
        z = complex(0.0, 0.0)
        r = mandelbrot(z, c, 0)

      
        if r < 5:
	        gr = hex((int(abs(random.random() * 150 - (20 * r)))) % 255)[2:].zfill(2)
        else:
            gr = hex((int(abs(150 - (20 * r)))) % 255)[2:].zfill(2)
        rd = hex(int(abs(r)))[2:].zfill(2)
        bl = hex(int(abs(10 - r)))[2:].zfill(2)
        
        img.put("#" + rd + gr + bl, (col, row))
'''when I first put in the random.random() I did it to all of the image. As a result, I
had a super blurry not very cool photo. So, I decided to try to limit where r would
be random.random(). So I decided I wanted the boundries to be further away from the center. 
To do this I decided that the R values would be smaller further away from the center. So 
I put a restriction on r values less than 5 to make them more blurry past a certain border. 
This was nice because I could have a clear cetner but a blurry outside. This was super cool 
for me, because I was able to produce somethingthing cool and show it to other people. 
I am proud of the fact that it got to print and that it looks cool.'''
canvas.pack()



#--------------------------------------------------------------------

def mandelbrot(z, c, count):
	z = z ** 2 + c
	count += 1 
	if abs(z) > 2 or count > maxIt - 1: 
		return count
	return mandelbrot(z,c,count)

WIDTH = 900 
'''I decided to change the width because I thought it was cool to have it stretched out
instead of being in a square. '''
HEIGHT = 640
xmin2 = -.74760813 
xmax2 = -.7445458
ymin2 = -.1101870
ymax2 = -.113311
maxIt = 255 

window2 = Toplevel()
'''I originally had a few problems renaming the varaible because I did not know
which variables had to be renamed and which ones should remain constant. However,
I asked the other kids in my class and asked for help and I figured out which varaibles 
needed to be numbered and which ones did not. I understand that xmin and max and y 
min and max don't need to be renamed, but I liked renaming them for organization 
purposes for myself.'''

canvas2 = Canvas(window2, width = WIDTH, height = HEIGHT, bg = "#000000")

img2 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas2.create_image((0, 0), image = img2, state = "normal", anchor = tkinter.NW)

for row in range(HEIGHT):
    for col in range(WIDTH):
    	
        c = complex(xmin2 + (xmax2 - xmin2) * col / WIDTH, ymin2 + (ymax2 - ymin2) * row / HEIGHT)
        
        z = complex(0.0, 0.0)

        
        r = mandelbrot(z, c, 0)

       
        if r % 7 == 0:
            gr = hex(0)[2:].zfill(2)
            rd = hex((255))[2:].zfill(2)
            bl = hex(0)[2:].zfill(2)
        elif r % 7 == 1:
            gr = hex(165) [2:].zfill(2)
            rd = hex(255 - (int(random.random() *10)))[2:].zfill(2)
            bl = hex(0)[2:].zfill(2)
        elif r % 7 == 2:
            gr = hex(255)[2:].zfill(2)
            rd = hex(255)[2:].zfill(2)
            bl = hex(0)[2:].zfill(2)
        elif r % 7 == 4:
            gr = hex(255)[2:].zfill(2)
            rd = hex(0)[2:].zfill(2)
            bl = hex(0)[2:].zfill(2)
        elif r % 7 == 5:
            gr = hex(0)[2:].zfill(2)
            rd = hex(0)[2:].zfill(2)
            bl = hex(255)[2:].zfill(2)

        elif r % 7 == 6:
            gr = hex(0)[2:].zfill(2)
            rd = hex(128)[2:].zfill(2)
            bl = hex(128)[2:].zfill(2)
        
        else: 
            gr = hex(int(abs(r - 100 )))[2:].zfill(2)
            rd = hex((int(abs(150 - (20 * r)))) % 255)[2:].zfill(2)
            bl = hex(int(abs(10 - r)))[2:].zfill(2)



        
        bl = hex(int(abs(10 - r)))[2:].zfill(2)
        
        
        img2.put("#" + rd + gr + bl, (col, row))
'''This one made me very proud because I felt that I created something really 
visually interesting and it was satisfying to see something created. I had seen 
pictures of this when I was researching mandlebrot set and for this reason knew 
where to look for this cool spiral.'''
'''For this I originally tried to limit my r values like I did in the first one using
a bunch of inequalities. However, this did not work because I could not determine the r 
values of the center. So as a result i did this % to have remainders and be able to
evaluate all r values no matter how big or how small they were.'''
'''lastly. To change up the colors I decided to google the different colors of the rainbow 
in hex and then For all the different remainders set them equal to different colors to create
the rainbow effect in the picture.'''
canvas2.pack()
#--------------------------------------------------------------------
def mandelbrot(z, c, count):
    z = z ** 2 + c
    count += 1 
    if abs(z) > 2 or count > maxIt - 1: 
        return count
    return mandelbrot(z,c,count)

WIDTH = 640
HEIGHT = 640
xmin3 = - .5
xmax3 = .5
ymin3 = -.5
ymax3 = .5
maxIt = 255 

window3 = Toplevel()

canvas3 = Canvas(window3, width = WIDTH, height = HEIGHT, bg = "#000000")

img3 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas3.create_image((0, 0), image = img3, state = "normal", anchor = tkinter.NW)

#c = complex(random.random(), random.random())
'''I used this code to find different c values to find different julias set and 
pick which one I liked best. To do this i randomized and had the c value printed and 
once i got the value i wanted i commented out the random and set the c values as permenant.'''
c = complex(0.3724468662935161, 0.4750530534430848)
'''This was what I needed to change until i found the c value i wanted. And this is 
the final c value i wanted.'''

for row in range(HEIGHT):
    for col in range(WIDTH):
        
        z = complex(xmin3 + (xmax3 - xmin3) * col / WIDTH, ymin3 + (ymax3 - ymin3) * row / HEIGHT)
        
        r = mandelbrot(z, c, 0)

       

        
        if r % 5 == 0:
            gr = hex(127)[2:].zfill(2)
            rd = hex(255)[2:].zfill(2)
            bl = hex(80)[2:].zfill(2)
        elif r % 5 == 1:
            gr = hex(99) [2:].zfill(2)
            rd = hex(255)[2:].zfill(2)
            bl = hex(71)[2:].zfill(2)
        elif r % 5 == 2:
            gr = hex(215)[2:].zfill(2)
            rd = hex(255)[2:].zfill(2)
            bl = hex(0)[2:].zfill(2)
        elif r % 5 == 3:
            gr = hex(165)[2:].zfill(2)
            rd = hex(255)[2:].zfill(2)
            bl = hex(0)[2:].zfill(2)
        elif r % 5 == 4:
            gr = hex(140)[2:].zfill(2)
            rd = hex(255)[2:].zfill(2)
            bl = hex(0)[2:].zfill(2)
        
        
        
        
        img3.put("#" + rd + gr + bl, (col, row))
'''this last one I put the most time into researching. At first I went through a bunch 
of mandlebrot to julias set reading and a bunch of mandlebrot to julias set videos. finally, 
I came to extra help and I got help and found out how to turn the c values.'''
'''Finally I changed this to different shades of my favorite color orange like I had in
the previous picture and changed the zoom so i would get a cool zoomed in picture of the Julias set.'''
canvas3.pack()

mainloop()

'''some of the many sources I used
https://www.youtube.com/watch?v=mg4bp7G0D3s Links to an external site.
https://www.youtube.com/watch?v=2JUAojvFpCo Links to an external site.
https://www.youtube.com/watch?v=0YaYmyfy9Z4 Links to an external site.
mandelbrot_reading.pdf
http://www.rapidtables.com/web/color/orange-color.htm
google for other rainbow colors.
https://batchloaf.wordpress.com/2013/02/10/creating-julia-set-images-in-python/
https://batchloaf.wordpress.com/2013/02/10/creating-julia-set-images-in-python/
'''
'''I am really proud of the final turn outs of this project because I have three different 
things that all have change in code and all different colors and all appealing to my eye
and I feel that I put a lot of time into this project and it payed off to have a finished 
result that in my eyes is very succesful.'''
