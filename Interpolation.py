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

    def Linear(self):
        """Call to perform linear interpolation."""

    def Bilinear(self):
        """Call to perform bi-linear interpolation."""

    def Cubic(self):
        """Call to perform cubic interpolation."""

    def Lanczos(self):
        """Call to perform Lanczos4 interpolation."""