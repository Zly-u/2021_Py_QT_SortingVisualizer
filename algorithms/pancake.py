from PyQt5.QtGui import QColor
from random import sample
from classes.iteration import Iteration


class Sort:
    def __init__(self):
        # Sort Info
        self.__name__ = "Pancake Sort"
        self.__iterations__ = 0
        self.__reads__ = 0
        self.__writes__ = 0

        # Visualizing Vars
        self.maxID = 0

        # Visualizing Vars
        self.color_max = QColor()
        self.color_max.setHsv(60*3, 255, 255 * 0.7)

        self.color_read = QColor()
        self.color_read.setRgbF(1, 1, 1, 1)

        self.color_size = QColor()
        self.color_size.setHsv(60*5, 255, 255 * 0.7)

        self.color_flipStartEnd = QColor()
        self.color_flipStartEnd.setHsv(60 * 4.2, 255, 255 * 0.7)



    def findMax(self, ul, curSize):
        for i in range(curSize):
            self.__reads__ += 1
            if ul[self.maxID] < ul[i]:
                self.maxID = i

            self.__iterations__ += 1
            yield [
                Iteration(i, self.color_read),
                Iteration(curSize-1, self.color_size),
                Iteration(self.maxID, self.color_max)
            ]

    def flip(self, ul, flipEnd):
        flipStart = 0
        while flipStart < flipEnd:
            self.__writes__ += 1
            ul[flipStart], ul[flipEnd] = ul[flipEnd], ul[flipStart]
            flipStart += 1
            flipEnd -= 1

            self.__iterations__ += 1
            yield [
                Iteration(flipStart, self.color_flipStartEnd),
                Iteration(flipEnd, self.color_flipStartEnd)
            ]

    def sort(self, ul, sl):
        curSize = len(ul)
        while ul != sl:
            # Find pos of a max value in a current checking range
            self.maxID = 0
            coFindMax = self.findMax(ul, curSize)
            while True:
                try:
                    yield next(coFindMax)
                except StopIteration:
                    break

            # Check if max number is already in the needed place
            if self.maxID != curSize-1:
                # Flip to maximum value
                coFlipToMax = self.flip(ul, self.maxID)
                while True:
                    try:
                        yield next(coFlipToMax)
                    except StopIteration:
                        break

                # Flip da boi entirely to the currentchecking range
                coFlipAll = self.flip(ul, curSize-1)
                while True:
                    try:
                        yield next(coFlipAll)
                    except StopIteration:
                        break

            # pp short
            curSize -= 1

        '''
        curSize = len(ul)
        while ul != sl:
            # find max
            maxID = 0
            for i in range(curSize):
                self.__reads__ += 1
                if ul[maxID] < ul[i]:
                    maxID = i
                self.__iterations__ += 1
                yield [
                    Iteration(i, self.color_read),
                    Iteration(curSize-1, self.color_size),
                    Iteration(maxID, self.color_max)
                ]

            # Flips
            # if the maxID is not already at the end
            self.__reads__ += 1
            if maxID != curSize-1:
                flipStart = 0
                flipEnd = maxID
                while flipStart < flipEnd:
                    self.__writes__ += 1
                    ul[flipStart], ul[flipEnd] = ul[flipEnd], ul[flipStart]
                    flipStart += 1
                    flipEnd -= 1
                    self.__iterations__ += 1
                    yield [
                        Iteration(flipStart, self.color_flipStartEnd),
                        Iteration(flipEnd, self.color_flipStartEnd)
                    ]

                flipStart = 0
                flipEnd = curSize-1
                while flipStart < flipEnd:
                    self.__writes__ += 1
                    ul[flipStart], ul[flipEnd] = ul[flipEnd], ul[flipStart]
                    flipStart += 1
                    flipEnd -= 1
                    self.__iterations__ += 1
                    yield [
                        Iteration(flipStart, self.color_flipStartEnd),
                        Iteration(flipEnd, self.color_flipStartEnd)
                    ]

            curSize -= 1
            # '''
