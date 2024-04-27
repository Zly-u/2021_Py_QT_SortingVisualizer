from PyQt5.QtGui import QColor
from classes.iteration import Iteration


class Sort:
    def __init__(self):
        # Sort Info
        self.__name__ = "Selection Sort"
        self.__iterations__ = 0
        self.__reads__ = 0
        self.__writes__ = 0

        # Visualizing Vars
        self.color_write = QColor()
        self.color_write.setHsv(0, 255, 255 * 0.7)

        self.color_select = QColor()
        self.color_select.setRgbF(1, 1, 1, 1)

        self.color_read = QColor()
        self.color_read.setHsv(60*3, 255, 255 * 0.7)

    def sort(self, ul, *args):
        _len = len(ul)
        for i in range(_len):
            minID = i
            for j in range(i+1, _len):
                if ul[minID] > ul[j]:
                    self.__reads__ += 1
                    minID = j
                self.__iterations__ += 1

                yield [
                    Iteration(j, self.color_select),
                    Iteration(minID, self.color_read),
                    Iteration(i, self.color_write),
                ]

            self.__writes__ += 1
            ul[i], ul[minID] = ul[minID], ul[i]