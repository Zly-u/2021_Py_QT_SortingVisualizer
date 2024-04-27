from PyQt5.QtGui import QColor
from random import sample
from classes.iteration import Iteration


class Sort:
    def __init__(self):
        # Sort Info
        self.__name__ = "Bogo Sort"
        self.__iterations__ = 0
        self.__reads__ = 0
        self.__writes__ = 0

        # Visualizing Vars
        self.color_iter = QColor()
        self.color_iter.setHsv(0, 255, 255 * 0.7)

    def sort(self, ul, sl):
        _len = range(len(ul))
        while ul != sl:
            i, j = sample(_len, k=2)
            ul[i], ul[j] = ul[j], ul[i]
            self.__writes__ += 1
            self.__iterations__ += 1

            yield [
                Iteration(i, self.color_iter),
                Iteration(j, self.color_iter)
            ]