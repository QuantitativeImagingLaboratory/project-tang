from tkinter import *
from tkinter import Label, Tk, READABLE, WRITABLE, EXCEPTION
from PIL import Image, ImageTk
from tkinter import filedialog
from functools import partial
import numpy as np
import cv2
import math
import PIL


class Window(Frame):
    # global im
    # global path,tkimage


    # tkimage = ImageTk.PhotoImage(im)
    # myvar = Label(root, image=tkimage)
    # path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg')])
    # def __init__(self, master):


    def __init__(self, master=None):
        # super().__init__(im)


        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Creation of init_window
    def init_window(self):
        myx = StringVar()
        myy= StringVar()
        mydegree=StringVar()


        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand="true")
        # path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg')])

        # creating a button instance
        uploadButton = Button(self, text="Select an image", command=self.client_upload)

        # placing the button on my window
        uploadButton.place(x=0, y=0)



        rotate = Button(self, text="Rotate image",command=lambda:self.rotateImage(mydegree))
        rotate.place(x=0, y=400)
        labelrotatedeg = Label(self,text="Degree° = ")
        labelrotatedeg.place (x=115,y=400)
        rotatedegree= Entry(self,textvariable = mydegree,width= 5)
        rotatedegree.place(x=175,y=400)
        Translateimage = Button(self, text="Translate Image", command=lambda:self.translateImage(myx,myy))
        Translateimage.place(x=0, y=425)
        labelentryx = Label(self, text="x=")
        labelentryx.place(x=150, y=425)
        labelentryy = Label(self, text="y=")
        labelentryy.place(x=225, y=425)
        transentryx = Entry(self, textvariable=myx, width=5)
        transentryx.place(x=175, y=425)
        transentryy = Entry(self, textvariable=myy, width=5)
        transentryy.place(x=250, y=425)
        #translateBtn = Button(self, text="Translate image",command=lambda:self.translateImage(45, 45))
        #translateBtn.place(x=100, y=400)

    def client_upload(self):
        path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg')])
        self.im = Image.open(path)

        self.im = self.im.resize((300, 300), Image.ANTIALIAS)  # this works yayyy resizes the image
        self.tkimage = ImageTk.PhotoImage(self.im)  # HAD TO MAKE THIS SELF.TKIMAGE SO THAT THE IMAGE IS ASSOCIATED WITH THE OBJECT!!
        myvar = Label(self, image=self.tkimage)  # first param used to be root, changed it to self
        myvar.image = self.tkimage  # these references are necessary so that garbage collection doesn't destroy the image
        myvar.place(x=10, y=60)  # i added this this works and it moves the image u can change it to (40,100)
        # myvar.pack()#this was original and running
        # self.init_window(im)


        return self.tkimage  # pretty sure should return tkimage. It was returning im before

    def translateImage(self, fx, fy):
        #fx= int(self.myx.get("1.0"))
        #fy=int(self.myy.get())
       # print(fx.get(), fy.get())
        fx = int(fx.get())
        fy = int(fy.get())
        # Get height and width of input image
        cols, rows = self.im.size
        newcol,newrow = cols*2,rows*2

        # Convert input image to numpy array
        data = np.array(self.im)
        # Create an empty image to store translated image
        translatedImage = np.zeros([cols, rows, 3], dtype=np.uint8)

        # Move the pixels to new location
        for i in range(cols):
            for j in range(rows):
                 # Get new coordinate
                a = i - fy
                b = j + fx

                 # Check if index is out of bound
                if (a < cols and a > 0 and b < rows and b > 0):
                    translatedImage[a, b] = data[i, j]

        # Convert numpy array to PIL image for display
        img = Image.fromarray(translatedImage)
        self.tkimage = ImageTk.PhotoImage(img)
        myvar = Label(self, image=self.tkimage)
        myvar.image = self.tkimage
        myvar.place(x=700, y=60)


    def rotateImage(self, angle, fx=None, fy=None):
        angle= int(angle.get())
        # Get input image's width and height
        cols, rows =  self.im.size
        newcol,newrow = cols*2,rows*2

        # Convert input PIL image to numpy array
        data = np.array(self.im)

        # Create an empty image to store rotated image
        rotatedImage = np.zeros([cols, rows, 3], dtype=np.uint8)

        # Convert degree to radian to calculate new coordinate for pixels
        theta = np.deg2rad(-angle)

        # Compute cos and sin of the input degree
        cosine, sine = np.cos(theta), np.sin(theta)

        # Check if user want to shift the rotated image
        if (fx is None):
            fx = 0
        #else:
            #fx = int(fx.get())
        if (fy is None):
            fy = 0
        #else:
            #fy = int(fy.get())

        # Rotate image
        for x in range(2):
            for i in range(cols):
                for j in range(rows):

                    pivotX = i - np.round(rows/2)
                    pivotY = j - np.round(rows/2)

                    # Compute new x and y position of the rotated pixel of (i,j)
                    if (x % 2 == 0):
                        a = math.floor((pivotX * cosine) - (pivotY * sine))
                        b = math.floor((pivotX * sine) + (pivotY * cosine))
                    else:
                        a = math.ceil((pivotX * cosine) - (pivotY * sine))
                        b = math.ceil((pivotX * sine) + (pivotY * cosine))

                    # Shift the pixel into the windows
                    a = math.floor(a + rows/2)
                    b = math.floor(b + rows/2)

                    # Check if index is out of bound
                    if (a < cols and a > 0 and b < rows and b > 0):
                        rotatedImage[a, b] = data[i, j]

        #Convert numpy array to PIL image for display
        img = Image.fromarray(rotatedImage)
        self.tkimage = ImageTk.PhotoImage(img)
        myvar = Label(self, image=self.tkimage)
        myvar.image = self.tkimage
        myvar.place(x=700, y=60)




root = Tk() # should this line through 'root.mainloop()' line be included in main?

# size of the window
root.geometry("1920x1000")

app = Window(root)
root.mainloop()