import numpy as np
class Interpolation:
    __image = None

    def __init__(self, image):
        """"""

        self.__image = image

    def NearestNeighbor(self, xScale, yScale):
        """Call to perform nearest neighbor interpolation on an image.
           No parameters are required."""
        (h, w) = self.__image.shape
        newHeight = h * yScale
        newWidth = w * xScale
        newImage = np.zeros((int(newHeight), int(newWidth), 1), np.uint8)

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

                newImage[i,j] = self.__image[mappedY, mappedX]

        return newImage


    def linear_interpolation(self, pt1, pt2, unknown):
        """helper function to perform linear interpolation."""
        I1 = float(pt1[1])
        I2 = float(pt2[1])

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


    def Bilinear(self, xScale, yScale):
        """Call to perform bi-linear interpolation."""
        import math

        (h, w) = self.__image.shape

        newHeight = h * float(yScale)
        newWidth = w * float(xScale)

        hRatio = h / (newHeight + 1)
        wRatio = w / (newWidth + 1)

        newImage = np.zeros((int(newHeight), int(newWidth), 1), np.uint8)

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
                    newImage[i, j] = self.__image[y1, x1]
                elif y1 == y2:
                    """"""
                    newImage[i, j] = self.linear_interpolation((x1, self.__image[y1, x1]), (x2, self.__image[y1, x2]), ((wRatio * j), 0))[1]
                elif x1 == x2:
                    """"""
                    newImage[i, j] = self.linear_interpolation((y1, self.__image[y1, x1]), (y2, self.__image[y2, x1]), ((hRatio * i), 0))[1]
                else:
                    pt1 = (y1, x1, self.__image[y1, x1])
                    pt2 = (y1, x2, self.__image[y1, x2])
                    pt3 = (y2, x1, self.__image[y2, x1])
                    pt4 = (y2, x2, self.__image[y2, x2])

                    unknown = ((hRatio * i), (wRatio * j), 0)

                    newImage[i, j] = self.bilinear_interpolation(pt1, pt2, pt3, pt4, unknown)

        return newImage

    def Cubic(self):
        """Call to perform cubic interpolation."""

    def Lanczos(self):
        """Call to perform Lanczos4 interpolation."""