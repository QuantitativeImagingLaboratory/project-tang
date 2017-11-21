class Interpolation:
    __image = None

    def __init__(self, image):
        """"""

        self.__image = image

    def NearestNeighbor(self, newImage):
        """Call to perform nearest neighbor interpolation on an image.
           No parameters are required."""

        return newImage

    def Linear(self):
        """Call to perform linear interpolation."""

    def Bilinear(self):
        """Call to perform bi-linear interpolation."""

    def Cubic(self):
        """Call to perform cubic interpolation."""

    def Lanczos(self):
        """Call to perform Lanczos4 interpolation."""