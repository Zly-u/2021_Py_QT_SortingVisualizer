from PyQt5.QtGui import QColor
from classes.iteration import Iteration


class Sort:
    def __init__(self):
        # Sort Info
        self.__name__ = "Binary Insertion Sort"
        self.__iterations__ = 0
        self.__reads__ = 0
        self.__writes__ = 0

        # Visualizing Vars
        self.color_iter = QColor()
        self.color_check = QColor()
        self.color_iter.setHsv(60 * 3, 255, 255 * 0.7)
        self.color_check.setHsv(0, 255, 255 * 0.7)

    def binarySearch(self, ul, value, start, end):
        for _ in range(120):
            midPos = (end - start) // 2

            yield [
                Iteration(midPos, self.color_iter)
            ]

    def sort(self, ul, *args):
        _len = len(ul)
        # Pick element to think where to paste in
        for i in range(1, _len):
            # Binary search its place
            coBin = self.binarySearch(ul, 43, 0, _len)
            while True:
                try:
                    yield next(coBin)
                except StopIteration:
                    break

            # '''
            yield [
                #Iteration(j, self.color_iter),
                #Iteration(pos, self.color_check)
            ]
            # '''