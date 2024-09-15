# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_index.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
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
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #8b8d8e;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color: #747678;\n"
"    gridline-color: #747678;\n"
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
        font = QFont()
        font.setPointSize(8)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, 6)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

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
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.label.setFont(font2)
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
        font3 = QFont()
        font3.setBold(False)
        self.frame_2.setFont(font3)
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
        font4 = QFont()
        font4.setPointSize(10)
        self.dashboard_btn.setFont(font4)
        self.dashboard_btn.setCheckable(True)

        self.verticalLayout_3.addWidget(self.dashboard_btn)

        self.diagnostic_btn = QPushButton(self.items_menu)
        self.diagnostic_btn.setObjectName(u"diagnostic_btn")
        self.diagnostic_btn.setEnabled(True)
        self.diagnostic_btn.setFont(font4)
        self.diagnostic_btn.setCheckable(False)

        self.verticalLayout_3.addWidget(self.diagnostic_btn)

        self.settings_btn = QPushButton(self.items_menu)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setFont(font4)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy4)
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.gridLayout_4 = QGridLayout(self.dashboard)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.grid_dashboard = QGridLayout()
        self.grid_dashboard.setObjectName(u"grid_dashboard")
        self.grid_dashboard.setHorizontalSpacing(10)
        self.grid_dashboard.setVerticalSpacing(25)
        self.grid_dashboard.setContentsMargins(0, -1, -1, -1)
        self.cell16_frame = QFrame(self.dashboard)
        self.cell16_frame.setObjectName(u"cell16_frame")
        self.cell16_frame.setFrameShape(QFrame.StyledPanel)
        self.cell16_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.cell16_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.cell16_title = QLabel(self.cell16_frame)
        self.cell16_title.setObjectName(u"cell16_title")
        font5 = QFont()
        font5.setPointSize(13)
        font5.setBold(True)
        self.cell16_title.setFont(font5)
        self.cell16_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.cell16_title)

        self.cell16_voltage = QLabel(self.cell16_frame)
        self.cell16_voltage.setObjectName(u"cell16_voltage")
        self.cell16_voltage.setFont(font1)
        self.cell16_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.cell16_voltage)

        self.cell16_soc = QLabel(self.cell16_frame)
        self.cell16_soc.setObjectName(u"cell16_soc")
        self.cell16_soc.setFont(font1)
        self.cell16_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.cell16_soc)


        self.grid_dashboard.addWidget(self.cell16_frame, 3, 3, 1, 1, Qt.AlignHCenter)

        self.cell2_frame = QFrame(self.dashboard)
        self.cell2_frame.setObjectName(u"cell2_frame")
        self.cell2_frame.setFrameShape(QFrame.StyledPanel)
        self.cell2_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.cell2_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.cell2_title = QLabel(self.cell2_frame)
        self.cell2_title.setObjectName(u"cell2_title")
        self.cell2_title.setFont(font5)
        self.cell2_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.cell2_title)

        self.cell2_voltage = QLabel(self.cell2_frame)
        self.cell2_voltage.setObjectName(u"cell2_voltage")
        self.cell2_voltage.setFont(font1)
        self.cell2_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.cell2_voltage)

        self.cell2_soc = QLabel(self.cell2_frame)
        self.cell2_soc.setObjectName(u"cell2_soc")
        self.cell2_soc.setFont(font1)
        self.cell2_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.cell2_soc)


        self.grid_dashboard.addWidget(self.cell2_frame, 0, 1, 1, 1, Qt.AlignHCenter)

        self.cell8_frame = QFrame(self.dashboard)
        self.cell8_frame.setObjectName(u"cell8_frame")
        self.cell8_frame.setFrameShape(QFrame.StyledPanel)
        self.cell8_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.cell8_frame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.cell8_title = QLabel(self.cell8_frame)
        self.cell8_title.setObjectName(u"cell8_title")
        self.cell8_title.setFont(font5)
        self.cell8_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.cell8_title)

        self.cell8_voltage = QLabel(self.cell8_frame)
        self.cell8_voltage.setObjectName(u"cell8_voltage")
        self.cell8_voltage.setFont(font1)
        self.cell8_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.cell8_voltage)

        self.cell8_soc = QLabel(self.cell8_frame)
        self.cell8_soc.setObjectName(u"cell8_soc")
        self.cell8_soc.setFont(font1)
        self.cell8_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.cell8_soc)


        self.grid_dashboard.addWidget(self.cell8_frame, 1, 3, 1, 1, Qt.AlignHCenter)

        self.cell7_frame = QFrame(self.dashboard)
        self.cell7_frame.setObjectName(u"cell7_frame")
        self.cell7_frame.setFrameShape(QFrame.StyledPanel)
        self.cell7_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.cell7_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.cell7_title = QLabel(self.cell7_frame)
        self.cell7_title.setObjectName(u"cell7_title")
        self.cell7_title.setFont(font5)
        self.cell7_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.cell7_title)

        self.cell7_voltage = QLabel(self.cell7_frame)
        self.cell7_voltage.setObjectName(u"cell7_voltage")
        self.cell7_voltage.setFont(font1)
        self.cell7_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.cell7_voltage)

        self.cell7_soc = QLabel(self.cell7_frame)
        self.cell7_soc.setObjectName(u"cell7_soc")
        self.cell7_soc.setFont(font1)
        self.cell7_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.cell7_soc)


        self.grid_dashboard.addWidget(self.cell7_frame, 1, 2, 1, 1, Qt.AlignHCenter)

        self.cell12_frame = QFrame(self.dashboard)
        self.cell12_frame.setObjectName(u"cell12_frame")
        self.cell12_frame.setFrameShape(QFrame.StyledPanel)
        self.cell12_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.cell12_frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.cell12_title = QLabel(self.cell12_frame)
        self.cell12_title.setObjectName(u"cell12_title")
        self.cell12_title.setFont(font5)
        self.cell12_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.cell12_title)

        self.cell12_voltage = QLabel(self.cell12_frame)
        self.cell12_voltage.setObjectName(u"cell12_voltage")
        self.cell12_voltage.setFont(font1)
        self.cell12_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.cell12_voltage)

        self.cell12_soc = QLabel(self.cell12_frame)
        self.cell12_soc.setObjectName(u"cell12_soc")
        self.cell12_soc.setFont(font1)
        self.cell12_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.cell12_soc)


        self.grid_dashboard.addWidget(self.cell12_frame, 2, 3, 1, 1, Qt.AlignHCenter)

        self.cell1_frame = QFrame(self.dashboard)
        self.cell1_frame.setObjectName(u"cell1_frame")
        self.cell1_frame.setFrameShape(QFrame.StyledPanel)
        self.cell1_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.cell1_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.cell1_title = QLabel(self.cell1_frame)
        self.cell1_title.setObjectName(u"cell1_title")
        self.cell1_title.setFont(font5)
        self.cell1_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.cell1_title)

        self.cell1_voltage = QLabel(self.cell1_frame)
        self.cell1_voltage.setObjectName(u"cell1_voltage")
        self.cell1_voltage.setFont(font1)
        self.cell1_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.cell1_voltage)

        self.cell1_soc = QLabel(self.cell1_frame)
        self.cell1_soc.setObjectName(u"cell1_soc")
        self.cell1_soc.setFont(font1)
        self.cell1_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.cell1_soc)


        self.grid_dashboard.addWidget(self.cell1_frame, 0, 0, 1, 1, Qt.AlignHCenter)

        self.cell14_frame = QFrame(self.dashboard)
        self.cell14_frame.setObjectName(u"cell14_frame")
        self.cell14_frame.setFrameShape(QFrame.StyledPanel)
        self.cell14_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.cell14_frame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.cell14_title = QLabel(self.cell14_frame)
        self.cell14_title.setObjectName(u"cell14_title")
        self.cell14_title.setFont(font5)
        self.cell14_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.cell14_title)

        self.cell14_voltage = QLabel(self.cell14_frame)
        self.cell14_voltage.setObjectName(u"cell14_voltage")
        self.cell14_voltage.setFont(font1)
        self.cell14_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.cell14_voltage)

        self.cell14_soc = QLabel(self.cell14_frame)
        self.cell14_soc.setObjectName(u"cell14_soc")
        self.cell14_soc.setFont(font1)
        self.cell14_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.cell14_soc)


        self.grid_dashboard.addWidget(self.cell14_frame, 3, 1, 1, 1, Qt.AlignHCenter)

        self.cell15_frame = QFrame(self.dashboard)
        self.cell15_frame.setObjectName(u"cell15_frame")
        self.cell15_frame.setStyleSheet(u"")
        self.cell15_frame.setFrameShape(QFrame.StyledPanel)
        self.cell15_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.cell15_frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.cell15_title = QLabel(self.cell15_frame)
        self.cell15_title.setObjectName(u"cell15_title")
        self.cell15_title.setFont(font5)
        self.cell15_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.cell15_title)

        self.cell15_voltage = QLabel(self.cell15_frame)
        self.cell15_voltage.setObjectName(u"cell15_voltage")
        self.cell15_voltage.setFont(font1)
        self.cell15_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.cell15_voltage)

        self.cell15_soc = QLabel(self.cell15_frame)
        self.cell15_soc.setObjectName(u"cell15_soc")
        self.cell15_soc.setFont(font1)
        self.cell15_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.cell15_soc)


        self.grid_dashboard.addWidget(self.cell15_frame, 3, 2, 1, 1, Qt.AlignHCenter)

        self.cell11_frame = QFrame(self.dashboard)
        self.cell11_frame.setObjectName(u"cell11_frame")
        self.cell11_frame.setFrameShape(QFrame.StyledPanel)
        self.cell11_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.cell11_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.cell11_title = QLabel(self.cell11_frame)
        self.cell11_title.setObjectName(u"cell11_title")
        self.cell11_title.setFont(font5)
        self.cell11_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.cell11_title)

        self.cell11_voltage = QLabel(self.cell11_frame)
        self.cell11_voltage.setObjectName(u"cell11_voltage")
        self.cell11_voltage.setFont(font1)
        self.cell11_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.cell11_voltage)

        self.cell11_soc = QLabel(self.cell11_frame)
        self.cell11_soc.setObjectName(u"cell11_soc")
        self.cell11_soc.setFont(font1)
        self.cell11_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.cell11_soc)


        self.grid_dashboard.addWidget(self.cell11_frame, 2, 2, 1, 1, Qt.AlignHCenter)

        self.cell10_frame = QFrame(self.dashboard)
        self.cell10_frame.setObjectName(u"cell10_frame")
        self.cell10_frame.setFrameShape(QFrame.StyledPanel)
        self.cell10_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.cell10_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.cell10_title = QLabel(self.cell10_frame)
        self.cell10_title.setObjectName(u"cell10_title")
        self.cell10_title.setFont(font5)
        self.cell10_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.cell10_title)

        self.cell10_voltage = QLabel(self.cell10_frame)
        self.cell10_voltage.setObjectName(u"cell10_voltage")
        self.cell10_voltage.setFont(font1)
        self.cell10_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.cell10_voltage)

        self.cell10_soc = QLabel(self.cell10_frame)
        self.cell10_soc.setObjectName(u"cell10_soc")
        self.cell10_soc.setFont(font1)
        self.cell10_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.cell10_soc)


        self.grid_dashboard.addWidget(self.cell10_frame, 2, 1, 1, 1, Qt.AlignHCenter)

        self.cell4_frame = QFrame(self.dashboard)
        self.cell4_frame.setObjectName(u"cell4_frame")
        self.cell4_frame.setFrameShape(QFrame.StyledPanel)
        self.cell4_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.cell4_frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.cell4_title = QLabel(self.cell4_frame)
        self.cell4_title.setObjectName(u"cell4_title")
        self.cell4_title.setFont(font5)
        self.cell4_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.cell4_title)

        self.cell4_voltage = QLabel(self.cell4_frame)
        self.cell4_voltage.setObjectName(u"cell4_voltage")
        self.cell4_voltage.setFont(font1)
        self.cell4_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.cell4_voltage)

        self.cell4_soc = QLabel(self.cell4_frame)
        self.cell4_soc.setObjectName(u"cell4_soc")
        self.cell4_soc.setFont(font1)
        self.cell4_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.cell4_soc)


        self.grid_dashboard.addWidget(self.cell4_frame, 0, 3, 1, 1, Qt.AlignHCenter)

        self.cell3_frame = QFrame(self.dashboard)
        self.cell3_frame.setObjectName(u"cell3_frame")
        self.cell3_frame.setFrameShape(QFrame.StyledPanel)
        self.cell3_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.cell3_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cell3_title = QLabel(self.cell3_frame)
        self.cell3_title.setObjectName(u"cell3_title")
        self.cell3_title.setFont(font5)
        self.cell3_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.cell3_title)

        self.cell3_voltage = QLabel(self.cell3_frame)
        self.cell3_voltage.setObjectName(u"cell3_voltage")
        self.cell3_voltage.setFont(font1)
        self.cell3_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.cell3_voltage)

        self.cell3_soc = QLabel(self.cell3_frame)
        self.cell3_soc.setObjectName(u"cell3_soc")
        self.cell3_soc.setFont(font1)
        self.cell3_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.cell3_soc)


        self.grid_dashboard.addWidget(self.cell3_frame, 0, 2, 1, 1, Qt.AlignHCenter)

        self.cell5_frame = QFrame(self.dashboard)
        self.cell5_frame.setObjectName(u"cell5_frame")
        self.cell5_frame.setFrameShape(QFrame.StyledPanel)
        self.cell5_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.cell5_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.cell5_title = QLabel(self.cell5_frame)
        self.cell5_title.setObjectName(u"cell5_title")
        self.cell5_title.setFont(font5)
        self.cell5_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.cell5_title)

        self.cell5_voltage = QLabel(self.cell5_frame)
        self.cell5_voltage.setObjectName(u"cell5_voltage")
        self.cell5_voltage.setFont(font1)
        self.cell5_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.cell5_voltage)

        self.cell5_soc = QLabel(self.cell5_frame)
        self.cell5_soc.setObjectName(u"cell5_soc")
        self.cell5_soc.setFont(font1)
        self.cell5_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.cell5_soc)


        self.grid_dashboard.addWidget(self.cell5_frame, 1, 0, 1, 1, Qt.AlignHCenter)

        self.cell13_frame = QFrame(self.dashboard)
        self.cell13_frame.setObjectName(u"cell13_frame")
        font6 = QFont()
        font6.setStrikeOut(False)
        self.cell13_frame.setFont(font6)
        self.cell13_frame.setAutoFillBackground(False)
        self.cell13_frame.setFrameShape(QFrame.StyledPanel)
        self.cell13_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.cell13_frame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.cell13_title = QLabel(self.cell13_frame)
        self.cell13_title.setObjectName(u"cell13_title")
        self.cell13_title.setFont(font5)
        self.cell13_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.cell13_title)

        self.cell13_voltage = QLabel(self.cell13_frame)
        self.cell13_voltage.setObjectName(u"cell13_voltage")
        self.cell13_voltage.setFont(font1)
        self.cell13_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.cell13_voltage)

        self.cell13_soc = QLabel(self.cell13_frame)
        self.cell13_soc.setObjectName(u"cell13_soc")
        self.cell13_soc.setFont(font1)
        self.cell13_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.cell13_soc)


        self.grid_dashboard.addWidget(self.cell13_frame, 3, 0, 1, 1, Qt.AlignHCenter)

        self.cell6_frame = QFrame(self.dashboard)
        self.cell6_frame.setObjectName(u"cell6_frame")
        self.cell6_frame.setFrameShape(QFrame.StyledPanel)
        self.cell6_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.cell6_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.cell6_title = QLabel(self.cell6_frame)
        self.cell6_title.setObjectName(u"cell6_title")
        self.cell6_title.setFont(font5)
        self.cell6_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.cell6_title)

        self.cell6_voltage = QLabel(self.cell6_frame)
        self.cell6_voltage.setObjectName(u"cell6_voltage")
        self.cell6_voltage.setFont(font1)
        self.cell6_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.cell6_voltage)

        self.cell6_soc = QLabel(self.cell6_frame)
        self.cell6_soc.setObjectName(u"cell6_soc")
        self.cell6_soc.setFont(font1)
        self.cell6_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.cell6_soc)


        self.grid_dashboard.addWidget(self.cell6_frame, 1, 1, 1, 1, Qt.AlignHCenter)

        self.cell9_frame = QFrame(self.dashboard)
        self.cell9_frame.setObjectName(u"cell9_frame")
        self.cell9_frame.setFrameShape(QFrame.StyledPanel)
        self.cell9_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.cell9_frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.cell9_title = QLabel(self.cell9_frame)
        self.cell9_title.setObjectName(u"cell9_title")
        self.cell9_title.setFont(font5)
        self.cell9_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.cell9_title)

        self.cell9_voltage = QLabel(self.cell9_frame)
        self.cell9_voltage.setObjectName(u"cell9_voltage")
        self.cell9_voltage.setFont(font1)
        self.cell9_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.cell9_voltage)

        self.cell9_soc = QLabel(self.cell9_frame)
        self.cell9_soc.setObjectName(u"cell9_soc")
        self.cell9_soc.setFont(font1)
        self.cell9_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.cell9_soc)


        self.grid_dashboard.addWidget(self.cell9_frame, 2, 0, 1, 1, Qt.AlignHCenter)

        self.cell17_frame = QFrame(self.dashboard)
        self.cell17_frame.setObjectName(u"cell17_frame")
        self.cell17_frame.setFrameShape(QFrame.StyledPanel)
        self.cell17_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.cell17_frame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.cell17_title = QLabel(self.cell17_frame)
        self.cell17_title.setObjectName(u"cell17_title")
        self.cell17_title.setFont(font5)
        self.cell17_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.cell17_title)

        self.cell17_voltage = QLabel(self.cell17_frame)
        self.cell17_voltage.setObjectName(u"cell17_voltage")
        self.cell17_voltage.setFont(font1)
        self.cell17_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.cell17_voltage)

        self.cell17_soc = QLabel(self.cell17_frame)
        self.cell17_soc.setObjectName(u"cell17_soc")
        self.cell17_soc.setFont(font1)
        self.cell17_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.cell17_soc)


        self.grid_dashboard.addWidget(self.cell17_frame, 4, 1, 1, 1)

        self.cell18_frame = QFrame(self.dashboard)
        self.cell18_frame.setObjectName(u"cell18_frame")
        self.cell18_frame.setFrameShape(QFrame.StyledPanel)
        self.cell18_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.cell18_frame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.cell18_title = QLabel(self.cell18_frame)
        self.cell18_title.setObjectName(u"cell18_title")
        self.cell18_title.setFont(font5)
        self.cell18_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.cell18_title)

        self.cell18_voltage = QLabel(self.cell18_frame)
        self.cell18_voltage.setObjectName(u"cell18_voltage")
        self.cell18_voltage.setFont(font1)
        self.cell18_voltage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.cell18_voltage)

        self.cell18_soc = QLabel(self.cell18_frame)
        self.cell18_soc.setObjectName(u"cell18_soc")
        self.cell18_soc.setFont(font1)
        self.cell18_soc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.cell18_soc)


        self.grid_dashboard.addWidget(self.cell18_frame, 4, 2, 1, 1)


        self.gridLayout_4.addLayout(self.grid_dashboard, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.dashboard)
        self.diagnostic = QWidget()
        self.diagnostic.setObjectName(u"diagnostic")
        sizePolicy4.setHeightForWidth(self.diagnostic.sizePolicy().hasHeightForWidth())
        self.diagnostic.setSizePolicy(sizePolicy4)
        self.verticalLayout = QVBoxLayout(self.diagnostic)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalFrame = QFrame(self.diagnostic)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy4.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy4)
        self.layout_diagnostic = QHBoxLayout(self.horizontalFrame)
        self.layout_diagnostic.setSpacing(5)
        self.layout_diagnostic.setObjectName(u"layout_diagnostic")
        self.layout_diagnostic.setContentsMargins(0, 0, 0, 0)
        self.diagnostic_table = QTableWidget(self.horizontalFrame)
        if (self.diagnostic_table.columnCount() < 4):
            self.diagnostic_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.diagnostic_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.diagnostic_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.diagnostic_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.diagnostic_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.diagnostic_table.setObjectName(u"diagnostic_table")
        font7 = QFont()
        font7.setPointSize(14)
        self.diagnostic_table.setFont(font7)
        self.diagnostic_table.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.diagnostic_table.setLayoutDirection(Qt.LeftToRight)
        self.diagnostic_table.setAutoFillBackground(False)
        self.diagnostic_table.setStyleSheet(u"")
        self.diagnostic_table.setLineWidth(1)
        self.diagnostic_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.diagnostic_table.setAutoScroll(True)
        self.diagnostic_table.setAutoScrollMargin(16)
        self.diagnostic_table.setAlternatingRowColors(False)
        self.diagnostic_table.setIconSize(QSize(0, 0))
        self.diagnostic_table.setShowGrid(True)
        self.diagnostic_table.setGridStyle(Qt.SolidLine)
        self.diagnostic_table.setSortingEnabled(True)
        self.diagnostic_table.setRowCount(0)
        self.diagnostic_table.horizontalHeader().setCascadingSectionResizes(False)
        self.diagnostic_table.horizontalHeader().setDefaultSectionSize(150)
        self.diagnostic_table.verticalHeader().setVisible(False)
        self.diagnostic_table.verticalHeader().setMinimumSectionSize(30)
        self.diagnostic_table.verticalHeader().setDefaultSectionSize(35)
        self.diagnostic_table.verticalHeader().setProperty("showSortIndicator", True)

        self.layout_diagnostic.addWidget(self.diagnostic_table)

        self.verticalFrame = QFrame(self.horizontalFrame)
        self.verticalFrame.setObjectName(u"verticalFrame")
        sizePolicy4.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy4)
        self.layout_button_diagnostic = QVBoxLayout(self.verticalFrame)
        self.layout_button_diagnostic.setSpacing(10)
        self.layout_button_diagnostic.setObjectName(u"layout_button_diagnostic")
        self.layout_button_diagnostic.setContentsMargins(10, 5, 5, 0)
        self.pause_diagnostic_btn = QPushButton(self.verticalFrame)
        self.pause_diagnostic_btn.setObjectName(u"pause_diagnostic_btn")
        font8 = QFont()
        font8.setPointSize(11)
        self.pause_diagnostic_btn.setFont(font8)
        self.pause_diagnostic_btn.setStyleSheet(u"color: green")
        self.pause_diagnostic_btn.setCheckable(True)
        self.pause_diagnostic_btn.setChecked(False)

        self.layout_button_diagnostic.addWidget(self.pause_diagnostic_btn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.clear_diagnostic_btn = QPushButton(self.verticalFrame)
        self.clear_diagnostic_btn.setObjectName(u"clear_diagnostic_btn")
        self.clear_diagnostic_btn.setFont(font8)
        self.clear_diagnostic_btn.setCheckable(True)

        self.layout_button_diagnostic.addWidget(self.clear_diagnostic_btn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.save_diagnostic_btn = QPushButton(self.verticalFrame)
        self.save_diagnostic_btn.setObjectName(u"save_diagnostic_btn")
        self.save_diagnostic_btn.setFont(font8)
        self.save_diagnostic_btn.setCheckable(True)

        self.layout_button_diagnostic.addWidget(self.save_diagnostic_btn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.layout_diagnostic.addWidget(self.verticalFrame, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout.addWidget(self.horizontalFrame, 0, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.diagnostic)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.verticalLayout_4 = QVBoxLayout(self.settings)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.settings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
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
        self.cell16_title.setText(QCoreApplication.translate("MainWindow", u"Cell 16", None))
        self.cell16_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell16_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell2_title.setText(QCoreApplication.translate("MainWindow", u"Cell 2", None))
        self.cell2_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell2_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell8_title.setText(QCoreApplication.translate("MainWindow", u"Cell 8", None))
        self.cell8_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell8_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell7_title.setText(QCoreApplication.translate("MainWindow", u"Cell 7", None))
        self.cell7_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell7_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell12_title.setText(QCoreApplication.translate("MainWindow", u"Cell 12", None))
        self.cell12_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell12_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell1_title.setText(QCoreApplication.translate("MainWindow", u"Cell 1", None))
        self.cell1_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell1_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell14_title.setText(QCoreApplication.translate("MainWindow", u"Cell 14", None))
        self.cell14_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell14_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell15_title.setText(QCoreApplication.translate("MainWindow", u"Cell 15", None))
        self.cell15_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell15_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell11_title.setText(QCoreApplication.translate("MainWindow", u"Cell 11", None))
        self.cell11_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell11_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell10_title.setText(QCoreApplication.translate("MainWindow", u"Cell 10", None))
        self.cell10_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell10_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell4_title.setText(QCoreApplication.translate("MainWindow", u"Cell 4", None))
        self.cell4_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell4_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell3_title.setText(QCoreApplication.translate("MainWindow", u"Cell 3", None))
        self.cell3_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell3_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell5_title.setText(QCoreApplication.translate("MainWindow", u"Cell 5", None))
        self.cell5_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell5_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell13_title.setText(QCoreApplication.translate("MainWindow", u"Cell 13", None))
        self.cell13_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell13_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell6_title.setText(QCoreApplication.translate("MainWindow", u"Cell 6", None))
        self.cell6_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell6_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell9_title.setText(QCoreApplication.translate("MainWindow", u"Cell 9", None))
        self.cell9_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell9_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell17_title.setText(QCoreApplication.translate("MainWindow", u"Cell 17", None))
        self.cell17_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell17_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        self.cell18_title.setText(QCoreApplication.translate("MainWindow", u"Cell 18", None))
        self.cell18_voltage.setText(QCoreApplication.translate("MainWindow", u"indeterminate mV", None))
        self.cell18_soc.setText(QCoreApplication.translate("MainWindow", u"indeterminate %", None))
        ___qtablewidgetitem = self.diagnostic_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Timestamp", None));
        ___qtablewidgetitem1 = self.diagnostic_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Diagnostic code", None));
        ___qtablewidgetitem2 = self.diagnostic_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Fault class", None));
        ___qtablewidgetitem3 = self.diagnostic_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Cell/NTC number", None));
        self.pause_diagnostic_btn.setText(QCoreApplication.translate("MainWindow", u"Pause Display", None))
        self.clear_diagnostic_btn.setText(QCoreApplication.translate("MainWindow", u"Clear Log", None))
        self.save_diagnostic_btn.setText(QCoreApplication.translate("MainWindow", u"Save Log", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

