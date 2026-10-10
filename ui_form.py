# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setToolTipDuration(-2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleBar = QWidget(self.centralwidget)
        self.titleBar.setObjectName(u"titleBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleBar.sizePolicy().hasHeightForWidth())
        self.titleBar.setSizePolicy(sizePolicy)
        self.titleBar.setMinimumSize(QSize(0, 40))
        self.titleBar.setMaximumSize(QSize(16777215, 40))
        self.titleBar.setToolTipDuration(2)
        self.horizontalLayout = QHBoxLayout(self.titleBar)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 4, 0)
        self.label = QLabel(self.titleBar)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnMinimize = QPushButton(self.titleBar)
        self.btnMinimize.setObjectName(u"btnMinimize")
        self.btnMinimize.setMinimumSize(QSize(32, 32))
        self.btnMinimize.setMaximumSize(QSize(32, 32))
        self.btnMinimize.setStyleSheet(u"QPushButton#btnClose,\n"
"QPushButton#btnMinimize {\n"
"    border: none;\n"
"    outline: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    qproperty-iconSize: 24px 24px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../../../../assets/minimize-normal.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMinimize.setIcon(icon)
        self.btnMinimize.setIconSize(QSize(24, 24))
        self.btnMinimize.setFlat(True)

        self.horizontalLayout.addWidget(self.btnMinimize)

        self.btnClose = QPushButton(self.titleBar)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(32, 32))
        self.btnClose.setMaximumSize(QSize(32, 32))
        self.btnClose.setStyleSheet(u"QPushButton#btnClose,\n"
"QPushButton#btnMinimize {\n"
"    border: none;\n"
"    outline: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    qproperty-iconSize: 24px 24px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../../../../assets/close-normal.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnClose.setIcon(icon1)
        self.btnClose.setIconSize(QSize(24, 24))
        self.btnClose.setFlat(True)

        self.horizontalLayout.addWidget(self.btnClose)


        self.verticalLayout.addWidget(self.titleBar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Stormworks XML Editor", None))
        self.btnMinimize.setText("")
        self.btnClose.setText("")
    # retranslateUi

