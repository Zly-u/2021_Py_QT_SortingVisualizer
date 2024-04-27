from PyQt5.QtGui import QColor
from classes.iteration import Iteration


class Sort:
    def __init__(self):
        # Sort Info
        self.__name__ = "Bubble Sort"
        self.__iterations__ = 0
        self.__reads__ = 0
        self.__writes__ = 0

        # Visualizing Vars
        self.color_iter = QColor()
        self.color_read = QColor()
        self.color_iter.setHsv(0, 255, 255 * 0.7)
        self.color_read.setHsv(60*3, 255, 255 * 0.7)

    def sort(self, ul, *args):
        _len = len(ul)

        for i in range(_len):
            for j in range(_len-i-1):
                self.__reads__ += 1
                if ul[j] > ul[j+1]:
                    ul[j], ul[j+1] = ul[j+1], ul[j]
                    self.__writes__ += 1

                self.__iterations__ += 1

                yield [
                    Iteration(j, self.color_iter),
                    Iteration(j+1, self.color_read),
                ]