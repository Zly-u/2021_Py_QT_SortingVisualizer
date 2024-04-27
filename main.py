# -*- coding: utf-8 -*-
# Python stuff
import sys

#######################################
#######################################
#######################################
# PyQt5 stuff
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget
from PyQt5.QtGui import QPainter, QColor, QFont

#######################################
#######################################
#######################################
# sorting algorithms stuff
from algorithms.pancake import Sort
from charts.roundPie import Chart


class MainWindow(QWidget):
    def __init__(self, chart=None, sortAlg=None, segments=60, speed:float=0):
        super().__init__()

        self.setWindowTitle("Sorting Visualizer")

        self.setStyleSheet("QWidget{background: #000000}")

        # Dimensions of the window
        self.setGeometry(0, 0, 1280, 720)

        # Centers the application on the screen
        self.center()

        # Basically starts an "update" function
        # 60 FPS 1/60 = 0.0166
        # update in ms so 0.0166 -> 16
        # Qt.PreciseTimer - Timer up to ms
        self.timer = self.startTimer(16, timerType=Qt.PreciseTimer)

        # Chart itself
        self.segments = segments

        self.speed = 1 if (speed == 0 or not speed) else speed
        self.delay = abs(self.speed)

        self.chart = chart(sortAlg, segments)
        self.sortAlg = self.chart.sortAlg

        self.isDoneSorting = False
        self.iteration = 0
        self.reads = 0
        self.writes = 0

    def center(self):
        desktop = QDesktopWidget()
        # Size of the screen, not application's window
        screen = desktop.screenGeometry()

        # Size of the window
        size = self.geometry()

        # Centers the application on the screen
        self.move(int((screen.width() - size.width()) / 2),
                  int((screen.height() - size.height()) / 2))

    def draw(self, painter):
        self.chart.draw(painter, self.geometry)

        textFont = QFont()
        fontSize = 11*2
        textFont.setPixelSize(fontSize)
        painter.setFont(textFont)

        textColor = QColor()
        textColor.setRgbF(1, 1, 1, 1)
        painter.setPen(textColor)

        textParams = [
            ("Name", self.sortAlg.__name__),
            ("Segments", self.segments),
            ("Iteration", self.sortAlg.__iterations__),
            ("Writes", self.sortAlg.__writes__),
            ("Reads", self.sortAlg.__reads__),
            ("Is Done", self.isDoneSorting)
        ]
        for i, param in enumerate(textParams, 1):
            painter.drawText(2, fontSize*i - 1, param[0]+": "+str(param[1]))

    def _update(self):

        if self.speed < 0:
            if self.delay > 0:
                self.delay -= 1
            else:
                self.isDoneSorting = self.chart.sortUpdate()
                self.delay = abs(self.speed)

        elif self.speed > 0:
            for i in range(self.speed):
                self.isDoneSorting = self.chart.sortUpdate()

        if not self.isDoneSorting:
            self.iteration += 1

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QPainter()

        # starts the painter process
        painter.begin(self)

        # Sets rendering quality to g00d one
        painter.setRenderHint(painter.Antialiasing)

        # disables outline
        painter.setPen(Qt.NoPen)

        # Custom drawing function
        self.draw(painter)

    # Basically an update function
    def timerEvent(self, event):
        # QT's draw update
        self.repaint()

        # Custom update function
        self._update()



def main():
    app = QApplication(sys.argv)
    window = MainWindow(chart=Chart, sortAlg=Sort, segments=60, speed=0)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
