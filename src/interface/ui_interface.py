# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(725, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(725, 550))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #040f13;\n"
"}\n"
"#side_menu{\n"
"	background-color: #071e26;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: #040f13;\n"
"	border-radius: 5px;\n"
"}\n"
"#main_screen{\n"
"	background-color: #071e26;\n"
"	border-radius: 10px;\n"
"}")
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy1)
        self.header.setMinimumSize(QSize(700, 50))
        self.header.setMaximumSize(QSize(16777215, 16777215))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAcceptDrops(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.header, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(700, 0))
        self.frame_2.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setBold(False)
        self.frame_2.setFont(font2)
        self.frame_2.setMouseTracking(False)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QWidget(self.frame_2)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setEnabled(True)
        self.horizontalLayout_6 = QHBoxLayout(self.side_menu)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 10, 5, 0)
        self.items_menu = QFrame(self.side_menu)
        self.items_menu.setObjectName(u"items_menu")
        self.items_menu.setMinimumSize(QSize(125, 0))
        self.items_menu.setMaximumSize(QSize(125, 16777215))
        self.items_menu.setFrameShape(QFrame.StyledPanel)
        self.items_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.items_menu)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dashboard_btn = QPushButton(self.items_menu)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        self.dashboard_btn.setEnabled(True)
        self.dashboard_btn.setCheckable(True)

        self.verticalLayout_3.addWidget(self.dashboard_btn)

        self.diagnostic_btn = QPushButton(self.items_menu)
        self.diagnostic_btn.setObjectName(u"diagnostic_btn")
        self.diagnostic_btn.setEnabled(True)
        self.diagnostic_btn.setCheckable(False)

        self.verticalLayout_3.addWidget(self.diagnostic_btn)

        self.settings_btn = QPushButton(self.items_menu)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setCheckable(True)

        self.verticalLayout_3.addWidget(self.settings_btn)


        self.horizontalLayout_6.addWidget(self.items_menu, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.side_menu)

        self.main_screen = QWidget(self.frame_2)
        self.main_screen.setObjectName(u"main_screen")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_screen.sizePolicy().hasHeightForWidth())
        self.main_screen.setSizePolicy(sizePolicy3)
        self.horizontalLayout_5 = QHBoxLayout(self.main_screen)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_screen)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.verticalLayout_2 = QVBoxLayout(self.dashboard)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dashboard_label = QLabel(self.dashboard)
        self.dashboard_label.setObjectName(u"dashboard_label")
        self.dashboard_label.setEnabled(True)
        sizePolicy.setHeightForWidth(self.dashboard_label.sizePolicy().hasHeightForWidth())
        self.dashboard_label.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setKerning(True)
        self.dashboard_label.setFont(font3)
        self.dashboard_label.setAutoFillBackground(False)
        self.dashboard_label.setScaledContents(False)
        self.dashboard_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.dashboard_label)

        self.stackedWidget.addWidget(self.dashboard)
        self.diagnostic = QWidget()
        self.diagnostic.setObjectName(u"diagnostic")
        self.verticalLayout = QVBoxLayout(self.diagnostic)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.diagnostic)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setPointSize(12)
        self.label_2.setFont(font4)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.diagnostic)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.verticalLayout_4 = QVBoxLayout(self.settings)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.settings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.settings)

        self.horizontalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.main_screen)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.toggled.connect(self.side_menu.setHidden)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"BMS", None))
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.diagnostic_btn.setText(QCoreApplication.translate("MainWindow", u"DIAGNOSTIC", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.dashboard_label.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Diagnostic", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

