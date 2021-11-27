from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from random import randint


class Ui_Form(object):
    @staticmethod
    def setupUi(self):
        self.resize(400, 300)
        self.button = QtWidgets.QPushButton(self)
        self.button.setGeometry(QtCore.QRect(160, 260, 75, 23))
        self.button.setObjectName("button")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 251))
        self.label.setText("")
        self.label.setObjectName("label")

        QtCore.QMetaObject.connectSlotsByName(self)


class Test(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button.clicked.connect(self.circle)

        canvas = QPixmap(380, 250)
        self.label.setPixmap(canvas)

    def circle(self):
        x, y = randint(0, 300), randint(0, 200)
        w = randint(10, 100)
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, w)
        painter.end()
        self.update()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())