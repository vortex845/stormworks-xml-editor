# This Python file uses the following encoding: utf-8
TEXTS = {
    "ru": {
        "title": "Stormworks XML Editor",
        "info_title": """<html><head/><body><p align="center"><span style=" font-size:16pt;">Информация</span></p></body></html>""",
        "info_text": """<html><head/><body><p align="justify"><span style=" font-size:12pt;">Используйте &lt;Открыть Папку&gt; чтобы выбрать XML папку с сохранёнными постройками</span></p></body></html>""",
        "open_btn": "Открыть Папку",
        "open_btn_size": "14px",
        "select_folder": "Выберите папку...",
        "no_files": "В этой папке нет XML-файлов."
    },
    "en": {
        "title": "Stormworks XML Editor",
        "info_title": """<html><head/><body><p align="center"><span style=" font-size:16pt;">Information</span></p></body></html>""",
        "info_text": """<html><head/><body><p align="justify"><span style=" font-size:12pt;">Use &lt;Open Folder&gt; to select XML folder with vehicle saves</span></p></body></html>""",
        "open_btn": "Open Folder",
        "open_btn_size": "16px",
        "select_folder": "Select folder...",
        "no_files": "No XML files in this folder."

    }
}

import sys
import os
import glob

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGraphicsDropShadowEffect, QFileDialog
from PySide6.QtGui import QDesktopServices, QIcon, QFontDatabase, QColor
from PySide6.QtCore import Qt, QPoint, QUrl, QPropertyAnimation, QEasingCurve
from PySide6.QtUiTools import loadUiType

Ui_MainWindow, _ = loadUiType("form.ui")

class ShadowContainer(QWidget):
    def __init__(self, inner_widget, parent=None):
        super().__init__(parent)
        # Делаем фон контейнера прозрачным
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Создаем Layout с отступами (чтобы тени было куда рисоваться)
        lay = QVBoxLayout(self)
        lay.setContentsMargins(5, 5, 5, 5) # Отступы для тени
        lay.addWidget(inner_widget)

        # Создаем тень и применяем её к ВНУТРЕННЕМУ виджету
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(25)
        shadow.setColor(QColor(0, 0, 0, 150)) # Черная полупрозрачная
        shadow.setOffset(0, 5) # Смещение вниз
        inner_widget.setGraphicsEffect(shadow)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        QFontDatabase.addApplicationFont("assets/fonts/Inter_18pt-Regular.ttf")
        QFontDatabase.addApplicationFont("assets/fonts/Inter_18pt-SemiBold.ttf")

        self.current_lang = "en"

        # === ПРОЗРАЧНОСТЬ И FRAMELESS — ДО setupUi ===
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setupUi(self)

        self.btnLanguage.setText("EN")

        self.setFixedSize(1024, 720)
        self.move(100, 100)

        self.panelContainer = ShadowContainer(self.infoPanel, self.centralwidget)
        self.panelContainer.setGeometry(1000, 1000, 300, 200)
        self.panelContainer.raise_()
        self.infoPanel_x = 1024

        # Создаем анимацию для свойства "pos" (позиция)
        self.anim = QPropertyAnimation(self.panelContainer, b"pos")
        self.anim.setDuration(300) # Длительность в миллисекундах (0.3 сек)
        self.anim.setEasingCurve(QEasingCurve.InOutQuad) # Плавное начало и конец

        self._drag_pos = QPoint()

        # === ПОДКЛЮЧЕНИЕ КНОПОК ===
        self.btnInfo.clicked.connect(self.toggle_btnInfo)
        self.btnGithub.clicked.connect(self.open_github)
        self.btnClose.clicked.connect(self.close)
        self.btnMinimize.clicked.connect(self.showMinimized)

        self.btnOpenFolder.clicked.connect(self.open_folder_and_load_xml)

        self.btnLanguage.clicked.connect(self.toggle_language)

        # === ПЕРЕТАСКИВАНИЕ ОКНА ЗА titleBar ===
        self.titleBar.mousePressEvent = self.titleBar_mouse_press
        self.titleBar.mouseMoveEvent = self.titleBar_mouse_move

        # === QSS ===
        qss_path = "assets/styles/main.qss"
        with open(qss_path, "r", encoding="utf-8") as f:
            self.setStyleSheet(f.read())

    def toggle_language(self):
        # Переключаем язык
        if self.current_lang == "en":
            self.current_lang = "ru"
            self.btnLanguage.setText("RU")
        else:
            self.current_lang = "en"
            self.btnLanguage.setText("EN")

        # Применяем новые тексты
        self.apply_language()

    def apply_language(self):
        texts = TEXTS[self.current_lang]

        self.btnOpenFolder.setText(texts["open_btn"])
        self.btnOpenFolder.setStyleSheet(f"font-size: {texts['open_btn_size']};")

        # Текст у Label'ов
        self.infoLabel.setText(texts["info_title"])
        self.infoLabel_2.setText(texts["info_text"])

        # Заголовок окна
        self.setWindowTitle(texts["title"])

    def open_github(self):
        QDesktopServices.openUrl(QUrl("https://github.com/vortex845/stormworks-xml-editor"))

    def toggle_btnInfo(self):
        if self.infoPanel_x == 1024:
            self.anim.setStartValue(QPoint(1024, 80))
            self.anim.setEndValue(QPoint(734, 80))
            self.infoPanel_x = 734
        else:
            self.anim.setStartValue(QPoint(734, 80))
            self.anim.setEndValue(QPoint(1024, 80))
            self.infoPanel_x = 1024
        self.anim.start()

    def open_folder_and_load_xml(self):
        # 1. Открываем проводник для выбора папки
        folder_path = QFileDialog.getExistingDirectory(
            self,
            TEXTS[self.current_lang]["select_folder"],
            TEXTS[self.current_lang]["select_folder"],
            QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog  # Чтобы окно было поверх
        )

        # Если пользователь закрыл окно, ничего не делаем
        if not folder_path:
            return

        # 2. Очищаем список от старых файлов
        self.listWidget.clear()

        # 3. Ищем XML-файлы
        search_pattern = os.path.join(folder_path, "*.xml")
        xml_files = glob.glob(search_pattern)

        if not xml_files:
            self.listWidget.addItem(TEXTS[self.current_lang]["no_files"])
            return

        # 4. Заполняем список
        for file_path in xml_files:
            file_name = os.path.basename(file_path)
            self.listWidget.addItem(file_name)

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
    import ctypes

    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("vortex845.stormworks.xmleditor")

    app = QApplication(sys.argv)

    # === УСТАНОВКА ИКОНКИ ПРИЛОЖЕНИЯ ===
    icon_path = "assets/icons/app_icon.ico"
    app.setWindowIcon(QIcon(icon_path))

    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())