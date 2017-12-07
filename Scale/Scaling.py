from . import Interpolation


class Scaling:
    __interpolation = None
    image = None

    def __init__(self, image = None):
        self.__interpolation = Interpolation.Interpolation(image)
        self.image = image

    def resize(self, xScale, yScale, interpolation):
        """Call to perform an image resize.
           Parameters include the image, the x and y factors
           by which the image will be scaled, and the
           interpolation type."""
        self.__interpolation.image = self.image

        if interpolation == "nearest_neighbor":
            print("About to do nn")
            self.__interpolation.NearestNeighbor(xScale, yScale)
        elif interpolation == "bilinear":
            self.__interpolation.Bilinear(xScale, yScale)
        elif interpolation == "cubic":
            self.__interpolation.Cubic(xScale, yScale)
        elif interpolation == "lanczos":
            self.__interpolation.Lanczos(xScale, yScale)
        else:
            print("An invalid interpolation type was given")
