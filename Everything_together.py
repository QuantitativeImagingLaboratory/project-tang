from tkinter import *
from tkinter import Label, Tk, READABLE, WRITABLE, EXCEPTION
from PIL import Image, ImageTk
from tkinter import filedialog
from datetime import datetime
from functools import partial
import numpy as np
import cv2
import math
import PIL
from tkinter import messagebox



class Window(Frame):
    def __init__(self, master=None):
        # super().__init__(im)


        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Creation of init_window
    def init_window(self):
        myx = StringVar()
        myy = StringVar()
        mydegree = StringVar()
        xscale=StringVar()
        yscale = StringVar()
        xscaleB = StringVar()
        yscaleB = StringVar()
        xscaleC = StringVar()
        yscaleC = StringVar()
        coefh = StringVar()
        directionh = StringVar()
        coefv = StringVar()
        directionv = StringVar()
        xscaleL = StringVar()
        yscaleL = StringVar()

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand="true")
        # path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg')])
        top = Frame(master=None, width=1100, height=54, bg="LightBlue1", relief=SUNKEN)
        top.place(x=102, y=0)
        down = Frame(master=None, width=1400, height=54, bg="LightBlue1", relief=SUNKEN)
        down.place(x=0, y=605)
        labelinfo = Label(top, font=('arial', 20, 'bold'), text="Image Geometric Transformation", fg="green", bd=10,
                          anchor='w')
        labelinfo.place(x=300, y=0)
        # creating a button instance
        uploadButton = Button(self, text="Select an image", height=3, width=13, bg="dark green", fg="white",
                              font=('arial', 9, 'bold'), command=self.client_upload)

        # placing the button on my window
        uploadButton.place(x=0, y=0)

        rotate = Button(self, text="Rotate image",bg= "powder blue", command=lambda: self.rotateImage(mydegree))
        rotate.place(x=0, y=400)
        labelrotatedeg = Label(self, text="Degree° = ")
        labelrotatedeg.place(x=115, y=400)
        rotatedegree = Entry(self, textvariable=mydegree, width=5)
        rotatedegree.place(x=175, y=400)
        Translateimage = Button(self, text="Translate Image",bg="linen", command=lambda: self.translateImage(myx, myy))
        Translateimage.place(x=0, y=425)
        labelentryx = Label(self, text="x=")
        labelentryx.place(x=150, y=425)
        labelentryy = Label(self, text="y=")
        labelentryy.place(x=225, y=425)
        transentryx = Entry(self, textvariable=myx, width=5)
        transentryx.place(x=175, y=425)
        transentryy = Entry(self, textvariable=myy, width=5)
        transentryy.place(x=250, y=425)
        NearestNeighbor = Button(self,text = "Nearest Neighbor",bg="powder blue",command = lambda:self.NearestNeighbor(xscale,yscale))
        NearestNeighbor.place(x=0,y=450)
        labelentryx = Label(self, text="x=")
        labelentryx.place(x=150, y=450)
        labelentryy = Label(self, text="y=")
        labelentryy.place(x=225, y=450)
        nearestentryx = Entry(self, textvariable=xscale, width=5)
        nearestentryx.place(x=175, y=450)
        nearestentryy = Entry(self, textvariable=yscale, width=5)
        nearestentryy.place(x=250, y=450)
        Bilinear = Button(self,text="Bilinear",bg="linen",command= lambda:self.Bilinear(xscaleB,yscaleB))
        Bilinear.place(x=0,y=475)
        labelentryx = Label(self, text="x=")
        labelentryx.place(x=150, y=475)
        labelentryy = Label(self, text="y=")
        labelentryy.place(x=225, y=475)
        bilinearentryx = Entry(self, textvariable=xscaleB, width=5)
        bilinearentryx.place(x=175, y=475)
        bilinearentryy = Entry(self, textvariable=yscaleB, width=5)
        bilinearentryy.place(x=250, y=475)
        cubic= Button(self,text= "Cubic",bg="powder blue",command=lambda:self.Cubic(xscaleC,yscaleC))
        cubic.place(x=0,y=500)
        labelentryx = Label(self, text="x=")
        labelentryx.place(x=150, y=500)
        labelentryy = Label(self, text="y=")
        labelentryy.place(x=225, y=500)
        cubicentryx = Entry(self, textvariable=xscaleC, width=5)
        cubicentryx.place(x=175, y=500)
        cubicentryy = Entry(self, textvariable=yscaleC, width=5)
        cubicentryy.place(x=250, y=500)
        lanczos = Button(self,text = "Lanczos",bg="linen",command=lambda: self.Lanczos(xscaleL,xscaleL))
        lanczos.place(x=0,y=525)
        labelentryx = Label(self, text="x=")
        labelentryx.place(x=150, y=525)
        labelentryy = Label(self, text="y=")
        labelentryy.place(x=225, y=525)
        lanczosentryx = Entry(self, textvariable=xscaleL, width=5)
        lanczosentryx.place(x=175, y=525)
        lanczosentryy = Entry(self, textvariable=yscaleL, width=5)
        lanczosentryy.place(x=250, y=525)
        horizontalshearing = Button(self,text= "Horizontal Shearing",bg="powder blue",command = lambda:self.horizontal(coefh,directionh))
        horizontalshearing.place(x=0,y=550)
        labelentrycoef = Label(self, text="coef")
        labelentrycoef.place(x=150, y=550)
        labelentrydirection = Label(self, text="Direction (right or left)")
        labelentrydirection.place(x=225, y=550)
        shearingcentrycoef = Entry(self, textvariable=coefh, width=5)
        shearingcentrycoef.place(x=180, y=550)
        shearingdirection = Entry(self, textvariable=directionh, width=8)
        shearingdirection.place(x=350, y=550)
        verticalshearing= Button(self,text="Vertical Shearing",bg="linen",command = lambda:self.vertical(coefv,directionv))
        verticalshearing.place(x=0,y=575)
        labelentrycoefv = Label(self, text="coef")
        labelentrycoefv.place(x=150, y=580)
        labelentrydirection = Label(self, text="Direction (up or down)")
        labelentrydirection.place(x=225, y=580)
        shearingcentrycoefv = Entry(self, textvariable=coefv, width=5)
        shearingcentrycoefv.place(x=180, y=580)
        shearingdirectionv = Entry(self, textvariable=directionv, width=8)
        shearingdirectionv.place(x=350, y=580)
        quit = Button(self, text="QUIT", height=3, width=9, bg="dark green", fg="white", command=self.quit)
        quit.place(x=1200, y=0)

        #quit = Button (self,text = "QUIT",command = self.quit)
        #quit.place(x=1200,y=0)






        # translateBtn = Button(self, text="Translate image",command=lambda:self.translateImage(45, 45))
        # translateBtn.place(x=100, y=400)
    #def quit(self):
        #result = messagebox.askyes("Continue?", "Do you wish to close this window :( ?")

        #exit()
    def quit(self):
        result = messagebox.askyesno("Continue?", "Do you wish to close this window :( ?" )
        if result is True:
         exit()
        else:
            pass

    def client_upload(self):
        path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg')])
        self.resultPanel = Label(root, border=25)
        self.im = Image.open(path)

        self.im = self.im.resize((300, 300), Image.ANTIALIAS)  # this works yayyy resizes the image
        self.tkimage = ImageTk.PhotoImage(
            self.im)  # HAD TO MAKE THIS SELF.TKIMAGE SO THAT THE IMAGE IS ASSOCIATED WITH THE OBJECT!!
        myvar = Label(self, image=self.tkimage)  # first param used to be root, changed it to self
        myvar.image = self.tkimage  # these references are necessary so that garbage collection doesn't destroy the image
        myvar.place(x=10, y=60)  # i added this this works and it moves the image u can change it to (40,100)
        # myvar.pack()#this was original and running
        # self.init_window(im)


        return self.tkimage  # pretty sure should return tkimage. It was returning im before


    def resize(self, xScale, yScale, interpolation):  # from Scaling.py
        """Call to perform an image resize.
           Parameters include the image, the x and y factors
           by which the image will be scaled, and the
           interpolation type."""
        self.__interpolation.image = self.im

        if interpolation == "nearest_neighbor":
            print("About to do nn")
            self.__interpolation.NearestNeighbor(xScale, yScale)
        elif interpolation == "bilinear":
            self.__interpolation.Bilinear(xScale, yScale)
        elif interpolation == "cubic":
            self.__interpolation.Cubic(xScale, yScale)
        elif interpolation == "lanczos":
            self.__interpolation.Lanczos()
        else:
            print("An invalid interpolation type was given")






    def NearestNeighbor(self, xScale, yScale):  # beginning of interpolation.py functions
        """Call to perform nearest neighbor interpolation on an image.
           No parameters are required."""
        xScale = float(xScale.get())
        yScale = float(yScale.get())
        print("At nn")
        (w,h) = self.im.size #orginal (h,w) = self.im.shape
        #h= self.im.size
        data = np.array(self.im)

        print("Height: ",h)
        print("width: ", w)
        newHeight = h * yScale
        newWidth = w * xScale
        newImage = np.zeros((int(newHeight), int(newWidth),3), dtype = np.uint8)


        heightRatio = h / newImage.shape[0]
        widthRatio = w / newImage.shape[1]

        for i in range(newImage.shape[0]):
            for j in range(newImage.shape[1]):
                mappedY = round(heightRatio * i, None)
                mappedX = round(widthRatio * j, None)

                if (mappedY == h):
                    mappedY = h - 1
                if (mappedX == w):
                    mappedX = w - 1
                #print("i: ", i, "  j: ",j, "   Mapped i: ", mappedY, "  Mapped j:", mappedX)
            #if (mappedY < newHeight and mappedY > 0 and mappedX < newWidth and mappedX > 0):
                newImage[i,j] = data[mappedY, mappedX] #newImage[i,j] = self.im[mappedY, mappedX] #orginal
                #newImage[i,0] = data[mappedY]
               # newImage[0,j]= data[mappedX]
        print("finished nn")
        # img = Image.fromarray(newImage)
        # self.tkimage = ImageTk.PhotoImage(img)
        # myvar = Label(self, image=self.tkimage)
        # myvar.image = self.tkimage
        # myvar.place(x=700, y=60)
        #myvar = Label(self, image = self.tkimage)

        self.im_converter(newImage)

        #img = Image.fromarray(newImage)  # CONVERT NUMPY ARRAY TO IMAGE OBJECT
        #tkimage = ImageTk.PhotoImage(img)  # THINK I NEED TO CONVERT rotatedImage TO AN IMAGE OBJECT TO MAKE THIS LINE WORK
        #myvar = Label(self, image=tkimage)
        # myvar.image = tkimage
        # myvar.place(x=700, y=60)
        # cv2.namedWindow("window_name")
        # cv2.imshow("window_name", newImage)
        # cv2.waitKey(0)

        return newImage




    def linear_interpolation(self, pt1, pt2, unknown):  #from interpolation.py
        """helper function to perform linear interpolation."""
        I1 = (pt1[1])
        I2 = (pt2[1])

        x1 = pt1[0]
        x2 = pt2[0]

        x = unknown[0]

        i = (I1 * (x2 - x) / (x2 - x1)) + (I2 * (x - x1) / (x2 - x1))

        return (x, i)



    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """helper function to perform bilinear interpolation"""
        newPt1 = (pt1[1], pt1[2])
        newPt2 = (pt2[1], pt2[2])
        newPt3 = (pt3[1], pt3[2])
        newPt4 = (pt4[1], pt4[2])

        r1 = self.linear_interpolation(newPt1, newPt2, (unknown[1], unknown[2]))
        r2 = self.linear_interpolation(newPt3, newPt4, (unknown[1], unknown[2]))

        newR1 = (pt1[0], r1[1])
        newR2 = (pt3[0], r2[1])

        p = self.linear_interpolation(newR1, newR2, (unknown[0], unknown[2]))

        return p[1]



    def Bilinear(self, xScaleB, yScaleB):
        """Call to perform bi-linear interpolation."""
        #import math
        xScaleB = float(xScaleB.get())
        yScaleB = float(yScaleB.get())
        data = np.array(self.im)

        (w, h) = self.im.size  # MAY NEED TO BE W,H SINCE CHANGED TO .SIZE

        newHeight = h * float(yScaleB)
        newWidth = w * float(xScaleB)

        hRatio = h / (newHeight + 1)
        wRatio = w / (newWidth + 1)

        newImage = np.zeros((int(newHeight), int(newWidth), 3),dtype =  np.uint8)

        for i in range(newImage.shape[0]):
            for j in range(newImage.shape[1]):

                y1 = math.floor(hRatio * i)
                y2 = math.ceil(hRatio * i)

                x1 = math.floor(wRatio * j)
                x2 = math.ceil(wRatio * j)

                if (y2 == h):
                    y2 = h - 1
                    y1 = h - 2

                if (x2 == w):
                    x2 = w - 1
                    x1 = w - 2

                if y1 == y2 and x1 == x2:
                    newImage[i, j] = data[y1, x1]
                elif y1 == y2:
                    newImage[i, j] = self.linear_interpolation((x1, data[y1, x1]), (x2, data[y1, x2]),((wRatio * j), 0))[1]
                elif x1 == x2:
                    newImage[i, j] = self.linear_interpolation((y1, data[y1, x1]), (y2, data[y2, x1]),((hRatio * i), 0))[1]
                else:
                    pt1 = (y1, x1, data[y1, x1])
                    pt2 = (y1, x2, data[y1, x2])
                    pt3 = (y2, x1, data[y2, x1])
                    pt4 = (y2, x2, data[y2, x2])

                    unknown = ((hRatio * i), (wRatio * j), 0)

                    newImage[i, j] = self.bilinear_interpolation(pt1, pt2, pt3, pt4, unknown)

        output_image_name = "image_name" + "Bilinear" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
        # img = Image.fromarray(newImage)
        # self.tkimage = ImageTk.PhotoImage(img)
        # myvar = Label(self, image=self.tkimage)
        # myvar.image = self.tkimage
        # myvar.place(x=700, y=60)
        # cv2.imwrite(output_image_name, newImage)
        #
        # cv2.namedWindow("window_name")
        # cv2.imshow("window_name", newImage)
        # cv2.waitKey(0)

        #return newImage
        self.im_converter(newImage)






    def linear_cubic(self, pt1, pt2, pt3, pt4, unknown):
        """helper function for Cubic interpolation"""
        I1 = float(pt1[1])
        I2 = float(pt2[1])
        I3 = float(pt3[1])
        I4 = float(pt4[1])

        x2 = pt2[0]
        x3 = pt3[0]

        x = unknown[0]

        mu = (x - x2) / (x3 - x2)
        mu2 = mu * mu

        a1 = (-0.5*I1) + (1.5*I2) - (1.5*I3) + (0.5*I4)
        a2 = I1 - 2.5*I2 + 2*I3 - 0.5*I4
        a3 = -0.5*I1 + 0.5*I3
        a4 = I2

        i = a1*mu*mu2+a2*mu2+a3*mu+a4
        #print(i)
        if i>255:


            i = 255
        if i<0:

            i = 0

        return (x, i)




    def bi_cubic(self, pt1, pt2, pt3, pt4, pt5,  pt6, pt7, pt8,pt9, pt10, pt11, pt12, pt13, pt14, pt15, pt16, unknown, y1, y4):
        """helper function for cubic interpolation"""
        newPt1 = (pt1[1], pt1[2])
        newPt2 = (pt2[1], pt2[2])
        newPt3 = (pt3[1], pt3[2])
        newPt4 = (pt4[1], pt4[2])

        newPt5 = (pt5[1], pt5[2])
        newPt6 = (pt6[1], pt6[2])
        newPt7 = (pt7[1], pt7[2])
        newPt8 = (pt8[1], pt8[2])

        newPt9 = (pt9[1], pt9[2])
        newPt10 = (pt10[1], pt10[2])
        newPt11 = (pt11[1], pt11[2])
        newPt12 = (pt12[1], pt12[2])

        newPt13 = (pt13[1], pt13[2])
        newPt14 = (pt14[1], pt14[2])
        newPt15 = (pt15[1], pt15[2])
        newPt16 = (pt16[1], pt16[2])

        r1 = self.linear_cubic(newPt1, newPt2, newPt3, newPt4, (unknown[1], unknown[2]))
        r2 = self.linear_cubic(newPt5, newPt6, newPt7, newPt8, (unknown[1], unknown[2]))

        r3 = self.linear_cubic(newPt9, newPt10, newPt11, newPt12, (unknown[1], unknown[2]))
        r4 = self.linear_cubic(newPt13, newPt14, newPt15, newPt16, (unknown[1], unknown[2]))



        newR1 = (pt1[0], r1[1])
        newR2 = (pt5[0], r2[1])
        newR3 = (pt9[0], r3[1])
        newR4 = (pt13[0], r4[1])

        #p = self.linear_interpolation(newR1, newR2, (unknown[0], unknown[2]))
        #print("Finding final I")
        p = self.linear_cubic(newR1, newR2, newR3, newR4, (unknown[0], unknown[2]))

        return p[1]




    def Cubic(self, xScaleC, yScaleC):
        """Call to perform cubic interpolation."""
        xScaleC = float(xScaleC.get())
        yScaleC = float(yScaleC.get())
        img = self.im.convert("L")

        data = np.array(img, dtype= np.uint8)

        (w, h) = self.im.size  # THIS MAY NEED TO BE W,H SINCE USING .SIZE

        newHeight = h * float(yScaleC)
        newWidth = w * float(xScaleC)

        hRatio = h / (newHeight + 1)
        wRatio = w / (newWidth + 1)

        newImage = np.zeros((int(newHeight), int(newWidth), 3),dtype= np.uint8)


        for i in range(newImage.shape[0]):
            for j in range(newImage.shape[1]):

                x2 = math.floor(wRatio * j)
                x1 = x2 - 1
                x3 = math.ceil(wRatio * j)
                x4 = x3 + 1

                y2 = math.floor(hRatio * i)
                y1 = y2 - 1
                y3 = math.ceil(hRatio * i)
                y4 = y3 + 1

                if x2 == 0:
                    x1 = 0
                if x3 == w-1 or x3 == w:
                    x3 = w-1
                    x4 = w - 1

                if y2 == 0:
                    y1 = 0
                if y3 == h-1 or y3 == w:
                    y3 = h-1
                    y4 = h-1

                if x2 == x3 and y2 == y3:
                    newImage[i,j] = data[y2,x2]
                elif y2 == y3:
                    """"""
                    pt1 = (x1, data[y2,x1])
                    pt2 = (x2, data[y2,x2])
                    pt3 = (x3, data[y2,x3])
                    pt4 = (x4, data[y2,x4])
                    unknown = (wRatio*j,0)
                    newImage[i,j] = self.linear_cubic(pt1, pt2, pt3, pt4, unknown)[1]
                elif x2 == x3:
                    """"""
                    pt1 = (y1, data[y1,x2])
                    pt2 = (y2, data[y2,x2])
                    pt3 = (y3, data[y3,x2])
                    pt4 = (y4, data[y4,x2])
                    unknown = (hRatio*i, 0)
                    newImage[i, j] = self.linear_cubic(pt1, pt2, pt3, pt4, unknown)[1]

                else:
                    """"""
                    pt1 = (y1, x1, data[y1, x1])
                    pt2 = (y1, x2, data[y1, x2])
                    pt3 = (y1, x3, data[y1, x3])
                    pt4 = (y1, x4, data[y1, x4])

                    pt5 = (y2, x1, data[y2, x1])
                    pt6 = (y2, x2, data[y2, x2])
                    pt7 = (y2, x3, data[y2, x3])
                    pt8 = (y2, x4, data[y2, x4])

                    pt9 = (y3, x1, data[y3, x1])
                    pt10 = (y3, x2, data[y3, x2])
                    pt11 = (y3, x3, data[y3, x3])
                    pt12 = (y3, x4, data[y3, x4])

                    pt13 = (y4, x1, data[y4, x1])
                    pt14 = (y4, x2, data[y4, x2])
                    pt15 = (y4, x3, data[y4, x3])
                    pt16 = (y4, x4, data[y4, x4])

                    unknown = (hRatio*i, wRatio*j, 0)

                    newImage[i, j] = self.bi_cubic(pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8,pt9, pt10, pt11, pt12, pt13, pt14, pt15, pt16, unknown,y1,y4)

        output_image_name = "image_name" + "Cubic" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
        # cv2.imwrite(output_image_name, newImage)
        #
        # cv2.namedWindow("window_name")
        # cv2.imshow("window_name", newImage)
        # cv2.waitKey(0)
        self.im_converter(newImage)


        #return newImage







    def translateImage(self, fx, fy):
        # fx= int(self.myx.get("1.0"))
        # fy=int(self.myy.get())
        # print(fx.get(), fy.get())
        fx = int(fx.get())
        fy = int(fy.get())
        # Get height and width of input image
        cols, rows = self.im.size
        newcol, newrow = cols * 2, rows * 2

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
        self.im_converter(translatedImage)
        # Convert numpy array to PIL image for display
        # img = Image.fromarray(translatedImage)
        # self.tkimage = ImageTk.PhotoImage(img)
        # myvar = Label(self, image=self.tkimage)
        # myvar.image = self.tkimage
        # myvar.place(x=700, y=60)

    def rotateImage(self, angle, fx=None, fy=None):
        angle = int(angle.get())
        # Get input image's width and height
        cols, rows = self.im.size
        newcol, newrow = cols * 2, rows * 2

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
            # else:
            # fx = int(fx.get())
        if (fy is None):
            fy = 0
            # else:
            # fy = int(fy.get())

        # Rotate image
        for x in range(2):
            for i in range(cols):
                for j in range(rows):

                    pivotX = i - np.round(rows / 2)
                    pivotY = j - np.round(rows / 2)

                    # Compute new x and y position of the rotated pixel of (i,j)
                    if (x % 2 == 0):
                        a = math.floor((pivotX * cosine) - (pivotY * sine))
                        b = math.floor((pivotX * sine) + (pivotY * cosine))
                    else:
                        a = math.ceil((pivotX * cosine) - (pivotY * sine))
                        b = math.ceil((pivotX * sine) + (pivotY * cosine))

                    # Shift the pixel into the windows
                    a = math.floor(a + rows / 2)
                    b = math.floor(b + rows / 2)

                    # Check if index is out of bound
                    if (a < cols and a > 0 and b < rows and b > 0):
                        rotatedImage[a, b] = data[i, j]

        # Convert numpy array to PIL image for display
        # img = Image.fromarray(rotatedImage)
        # self.tkimage = ImageTk.PhotoImage(img)
        # myvar = Label(self, image=self.tkimage)
        # myvar.image = self.tkimage
        # myvar.place(x=700, y=60)
        self.im_converter(rotatedImage)

    def horizontal(self, coefh, directionh):
        """use for horizontal shearing. Give a coefficient used to skew image. small numbers. direction either right or left"""
        coefh = float(coefh.get())
        directionh = (directionh.get())
        (w, h) = self.im.size
        data = np.array(self.im)

        newW = int(w + coefh * h)

        newImage = np.zeros((h, newW,3), dtype=np.uint8)

        if directionh == "right":
            for i in range(h):
                for j in range(w):
                    newJ = int(j + coefh * i)
                    newImage[i, newJ] = data[i, j]
        elif directionh == "left":
            for i in range(h):
                for j in range(w):
                    newJ = int(j + -coefh * i + (newW - w - 1))
                    newImage[i, newJ] = data[i, j]
        self.im_converter(newImage)
        # cv2.namedWindow("window_name")
        # cv2.imshow("window_name", newImage)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows();

        return newImage

    def vertical(self, coefv, directionv):
        """Use for vertical shearing."""
        coefv = float(coefv.get())
        directionv = (directionv.get())
        (w, h) = self.im.size
        data = np.array(self.im)

        newH = int(h + coefv * w)

        newImage = np.zeros((newH, w,3), dtype=np.uint8)

        if directionv == "down":
            for i in range(h):
                for j in range(w):
                    newI = int(i + coefv * j)
                    newImage[newI, j] = data[i, j]
        elif directionv == "up":
            for i in range(h):
                for j in range(w):
                    newI = int(i + -coefv * j + (newH - h - 1))
                    newImage[newI, j] = data[i, j]

        self.im_converter(newImage)
        # cv2.namedWindow("window_name")
        # cv2.imshow("window_name", newImage)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows();

        return newImage

    def lanczos_window(self, x):
        if x > 0:
            part1 = np.sin(np.pi * x) / (np.pi * x)
            part2 = np.sin(np.pi * x / 4) / (np.pi * x / 4)

            return part1 * part2
        else:
            return 0

    def linear_lanczos(self, points, unknown):
        I = 0
        for i in points:
            I += self.lanczos_window(np.abs(unknown[0] - i[0])) * i[1]

        if I > 255:
            I = 255
        if I < 0:
            I = 0

        return (unknown[0], I)

    def bi_lanczos(self, points, unknown):
        """"""

        horizPoints = {}
        uniqueY = set()
        for i in points:
            uniqueY.add(i[0])

        for i in uniqueY:
            temp = []
            for j in points:

                if j[0] == i:
                    temp.append((j[1], j[2]))
            if len(temp) > 0:
                horizPoints[i] = temp

        intermPoints = []

        for key, value in horizPoints.items():
            tempPoint = self.linear_lanczos(value, (unknown[1], unknown[2]))
            intermPoints.append((key, tempPoint[1]))

        p = self.linear_lanczos(intermPoints, (unknown[0], unknown[2]))

        return p[1]

    def Lanczos(self, xScaleL, yScaleL):
        """Call to perform Lanczos4 interpolation."""
        #import math
        xScaleL = float(xScaleL.get())
        yScaleL = float(yScaleL.get())

        (w, h) = self.im.size
        img = self.im.convert("L")

        data = np.array(img, dtype=np.uint8)

        newHeight = h * float(yScaleL)
        newWidth = w * float(xScaleL)

        hRatio = h / (newHeight + 1)
        wRatio = w / (newWidth + 1)

        newImage = np.zeros((int(newHeight), int(newWidth), 3), dtype=np.uint8)

        for i in range(int(newHeight)):
            for j in range(int(newWidth)):
                x1 = math.floor(wRatio * j)
                x2 = math.ceil(wRatio * j)

                y1 = math.floor(hRatio * i)
                y2 = math.ceil(hRatio * i)

                points = set()
                xValues = []
                yValues = []

                if x1 == x2 and y1 == y2:
                    newImage[i, j] = data[y1, x1]
                elif y1 == y2:
                    xValues = [x1 - 3, x1 - 2, x1 - 1, x1, x2, x2 + 1, x2 + 2, x2 + 3]
                    for k in range(8):
                        if xValues[k] >= 0 and xValues[k] < w:
                            points.add((xValues[k], data[y1, xValues[k]]))
                    newImage[i, j] = self.linear_lanczos(points, (wRatio * j, 0))[1]
                elif x1 == x2:
                    yValues = [y1 - 3, y1 - 2, y1 - 1, y1, y2, y2 + 1, y2 + 2, y2 + 3]
                    for k in range(8):
                        if yValues[k] >= 0 and yValues[k] < h:
                            points.add((yValues[k], data[y1, yValues[k]]))
                    unknown = (hRatio * i, 0)
                    newImage[i, j] = self.linear_lanczos(points, unknown)[1]
                else:

                    xValues = [x1 - 3, x1 - 2, x1 - 1, x1, x2, x2 + 1, x2 + 2, x2 + 3]
                    yValues = [y1 - 3, y1 - 2, y1 - 1, y1, y2, y2 + 1, y2 + 2, y2 + 3]
                    for k in range(8):
                        for l in range(8):
                            if (xValues[k] >= 0 and yValues[l] >= 0 and xValues[k] < w and yValues[l] < h):
                                points.add((yValues[l], xValues[k], data[(yValues[l], xValues[k])]))

                    unknown = (i * hRatio, j * wRatio, 0)
                    newImage[i, j] = self.bi_lanczos(points, unknown)
        # cv2.namedWindow("window_name")
        # cv2.imshow("window_name", newImage)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows();
        self.im_converter(newImage)
        #return newImage




    def im_converter(self, image):
        img = Image.fromarray(image)
        img = ImageTk.PhotoImage(img)

        self.resultPanel.configure(image = img)
        self.resultPanel.image = img
        self.resultPanel.place(x=700, y=60)
        #myvar = Label(self, image=self.tkimage)
        #myvar.image = self.tkimage
        #myvar.place(x=700, y=60)


root = Tk()  # should this line through 'root.mainloop()' line be included in main?


# size of the window
root.geometry("1920x1000")

app = Window(root)
root.mainloop()