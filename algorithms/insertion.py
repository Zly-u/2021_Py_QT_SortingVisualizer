from PyQt5.QtGui import QColor
from classes.iteration import Iteration


class Sort:
    def __init__(self):
        # Sort Info
        self.__name__ = "Insertion Sort"
        self.__iterations__ = 0
        self.__reads__ = 0
        self.__writes__ = 0

        # Visualizing Vars
        self.color_iter = QColor()
        self.color_check = QColor()
        self.color_iter.setHsv(60 * 3, 255, 255 * 0.7)
        self.color_check.setHsv(0, 255, 255 * 0.7)

    def sort(self, ul, *args):
        _len = len(ul)
        for i in range(1, _len):
            for j in range(i):
                self.__reads__ += 1
                if ul[j] < ul[i]:
                    self.__writes__ += 1
                    ul[j], ul[i] = ul[i], ul[j]
                    self.__iterations__ += 1
                    continue
                self.__iterations__ += 1

                yield [
                    Iteration(j, self.color_iter),
                    Iteration(i, self.color_check)
                ]