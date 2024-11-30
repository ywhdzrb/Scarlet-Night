from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

width = 800
height = 500

def br_show():
    global win
    label = QLabel(win)
    pixmap = QPixmap("assets/background/image/br.png")
    pixmap_resized = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    label.setPixmap(pixmap_resized)
    # 调整图片
    label.setScaledContents(True)

    label.show()

def main():
    global win
    app = QApplication(sys.argv)
    win = QWidget()
    win.setGeometry(width, height, width, height)
    win.setWindowTitle("Scarlet Night")  
    win.setFixedSize(800, 500)
    win.show()

    br_show()

    sys.exit(app.exec_())

main()