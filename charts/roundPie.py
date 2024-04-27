from classes.utils import *

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen


class Chart:
    def __init__(self, sortAlg=None, segments=60):
        self.initialChart = generateSegments(segments)
        self.shuffledChart = shuffleAsCopy(self.initialChart)
        # self.shuffledChart = self.initialChart

        self.sortAlg = sortAlg()

        self.isDoneSorting = False
        self.tableOfIterToHighlight = None

        # put a sort function into a courontuna
        self.coSort = self.sortAlg.sort(self.shuffledChart, self.initialChart)

    def drawSegments(self, painter: QPainter, x: float, y: float, radX: float, radY: float):
        _chart = self.shuffledChart
        segments = len(_chart)
        angleStep = 360 / segments
        for i in range(segments):
            angle = angleStep * i

            # drawing manipulations
            color = QColor()

            if self.isDoneSorting:
                color.setHsv(_chart[i] * angleStep, 255, 255 * 0.7)
                painter.setPen(color)
            else:
                color.setHsv(_chart[i] * angleStep, 255 * 0.5, 255 * 0.4)
                painter.setPen(color)


            painter.setBrush(color)
            painter.drawPie(x-radX, y-radY, radX*2, radY*2, -angle*16, angleStep*16)

    def drawIterSegment(self, painter: QPainter, x: float, y: float, radX: float, radY: float):
        _chart = self.shuffledChart
        segments = len(_chart)
        angleStep = 360 / segments
        if not self.isDoneSorting:
            pen = QPen()
            pen.setWidth(2)

            color = QColor()
            if self.tableOfIterToHighlight:
                for segment in self.tableOfIterToHighlight:
                    angle = angleStep * segment.pos

                    # fill
                    color.setHsv(_chart[segment.pos] * angleStep, 255, 255 * 0.8)
                    painter.setBrush(color)
                    painter.drawPie(x - radX, y - radY, radX * 2, radY * 2, -angle * 16, angleStep * 16)

                    # outline
                    pen.setColor(segment.color)
                    painter.setPen(pen)
                    painter.drawPie(x - radX, y - radY, radX * 2, radY * 2, -angle * 16, angleStep * 16)

    def drawSegmentsOutline(self, painter: QPainter, x: float, y: float, radX: float, radY: float):
        pen = QPen()
        pen.setColor(Qt.white)
        pen.setWidth(6)
        painter.setPen(pen)
        painter.drawEllipse(x - radX, y - radY, radX * 2, radY * 2)

    def sortUpdate(self):
        if not self.isDoneSorting:
            try:
                self.tableOfIterToHighlight = next(self.coSort)
            except StopIteration:
                self.isDoneSorting = True

        return self.isDoneSorting

    def draw(self, painter: QPainter, geometry):
        # Size of the window
        size = geometry()

        rad = 500
        params = [painter, size.width() / 2, size.height() / 2, rad, rad / 2]
        self.drawSegmentsOutline(*params)
        self.drawSegments(*params)
        self.drawIterSegment(*params)