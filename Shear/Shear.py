import numpy as np
import cv2
class Shear:

    def horizontal(self, image, coef, direction):
        """use for horizontal shearing. Give a coefficient used to skew image. small numbers. direction either right or left"""

        (h,w) = image.shape

        newW = int(w + coef*h)

        newImage = np.zeros((h, newW), dtype=np.uint8)

        if direction == "right":
            for i in range(h):
                for j in range(w):
                    newJ = int(j + coef*i)
                    newImage[i,newJ] = image[i,j]
        elif direction == "left":
            for i in range(h):
                for j in range(w):
                    newJ = int(j + -coef*i + (newW-w-1))
                    newImage[i, newJ] = image[i,j]

        # cv2.namedWindow("window_name")
        # cv2.imshow("window_name", newImage)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows();

        return newImage

    def vertical(self, image, coef, direction):
        """Use for vertical shearing."""
        (h,w) = image.shape
        newH = int(h + coef*w)

        newImage = np.zeros((newH, w), dtype=np.uint8)


        if direction == "down":
            for i in range(h):
                for j in range(w):
                    newI = int(i + coef*j)
                    newImage[newI, j] = image[i,j]
        elif direction == "up":
            for i in range(h):
                for j in range(w):
                    newI = int(i + -coef * j + (newH-h-1))
                    newImage[newI, j] = image[i, j]

        # cv2.namedWindow("window_name")
        # cv2.imshow("window_name", newImage)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows();

        return newImage