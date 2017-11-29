import numpy as np
import cv2
import math

img = cv2.imread("pic/lenna_grey.png", 0)

def load_display(input_image):
    #pic = cv2.imread(input_image)
    cv2.namedWindow("Picture", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Picture", input_image)
    cv2.waitKey(0)
    cv2.destroyWindow("Picture")

def translateImage(image, fx, fy):

    # Get height and width of input image
    rows, cols = image.shape

    # Create an empty image to store translated image
    translatedImage = np.zeros([rows, cols, 1], dtype=np.uint8)

    # Move the pixels to new location
    for i in range(cols):
        for j in range(rows):

            # Get new coordinate
            a = i - fy
            b = j + fx

            # Check if index is out of bound
            if (a < cols and a > 0 and b < rows and b > 0):
                translatedImage[a, b] = image[i, j]

    return translatedImage

load_display(translateImage(img, 100, 150))

def calculateInterpolation(img, positionX, positionY):
    outImg = []

    # Get integer and fractional parts of numbers
    x = int(positionX)
    y = int(positionY)
    x_diff = 0
    y_diff = 0
    xPlus = min(x + 1, img.shape[1] - 1)
    yPlus = min(y + 1, img.shape[0] - 1)

    # Get pixels in four corners

    bottomLeft = img[y, x]
    bottomRight = img[y, xPlus]
    topLeft = img[yPlus, x]
    topRight = img[yPlus, xPlus]

    # Calculate interpolation
    bottom = x_diff * bottomRight + (1. - x_diff) * bottomLeft
    top = x_diff * topRight + (1. - x_diff) * topLeft
    pixel = y_diff * top + (1. - y_diff) * bottom

    outImg.append(int(pixel))

    # print(outImg)
    return outImg



def rotateImage(image, angle, fx=None, fy=None):

    # Get input image's width and height
    rows, cols = image.shape[:2]

    # Create an empty image to store rotated image
    rotatedImage = np.zeros([cols, rows, 1], dtype=np.uint8)

    # Convert degree to radian to calculate new coordinate for pixels
    theta = np.deg2rad(-angle)

    # Compute cos and sin of the input degree
    cosine, sine = math.cos(theta), math.sin(theta)

    # Check if user want to shift the rotated image
    if(fx is None):
        fx = 0
    if(fy is None):
        fy = 0

    # Rotate image
    for x in range(2):
        for i in range (cols):
            for j in range (rows):

                # Compute new x and y position of the rotated pixel of (i,j)
                if(x%2 == 0):
                    a = math.floor((i * cosine) - (j * sine))
                    b = math.floor((i * sine) + (j * cosine))
                else:
                    a = math.ceil((i * cosine) - (j * sine))
                    b = math.ceil((i * sine) + (j * cosine))

                # Shift the pixel into the windows
                a = a - fy
                b = b + fx

                # Check if index is out of bound
                if (a < cols and a > 0 and b < rows and b > 0):
                    rotatedImage[a, b] = calculateInterpolation(image, j, i)
                    #rotatedImage[a, b] = image[i, j]

    return rotatedImage

#load_display(rotateImage(img, 45, 250))






