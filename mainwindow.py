# This Python file uses the following encoding: utf-8
import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QPoint
from PySide6.QtUiTools import loadUiType


Ui_MainWindow, _ = loadUiType("form.ui")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # === ПРОЗРАЧНОСТЬ И FRAMELESS — ДО setupUi ===
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setupUi(self)

        self.resize(1024, 720)
        self.move(100, 100)

        self._drag_pos = QPoint()

        # === ПОДКЛЮЧЕНИЕ КНОПОК ===
        self.btnClose.clicked.connect(self.close)
        self.btnMinimize.clicked.connect(self.showMinimized)

        # === ПЕРЕТАСКИВАНИЕ ОКНА ЗА titleBar ===
        self.titleBar.mousePressEvent = self.titleBar_mouse_press
        self.titleBar.mouseMoveEvent = self.titleBar_mouse_move

        # === QSS ===
        qss_path = "assets/styles/main.qss"
        if os.path.exists(qss_path):
            with open(qss_path, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
            print("QSS загружен:", qss_path)
        else:
            print("QSS НЕ найден:", qss_path)

    # === ПЕРЕТАСКИВАНИЕ ===
    def titleBar_mouse_press(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def titleBar_mouse_move(self, event):
        if event.buttons() & Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self._drag_pos)
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())