from . import Interpolation
import numpy as np

class Scaling:
    __interpolation = None
    __image = None

    def __init__(self, image):
        self.__interpolation = Interpolation.Interpolation(image)
        self.__image = image

    def resize(self, xScale, yScale, interpolation):
        """Call to perform an image resize.
           Parameters include the image, the x and y factors
           by which the image will be scaled, and the
           interpolation type."""

        if interpolation == "nearest_neighbor":
            self.__interpolation.NearestNeighbor(xScale, yScale)
        elif interpolation == "bilinear":
            self.__interpolation.Bilinear()
        elif interpolation == "cubic":
            self.__interpolation.Cubic()
        elif interpolation == "lanczos":
            self.__interpolation.Lanczos()
        else:
            print("An invalid interpolation type was given")
