# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1232, 992)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setStyleSheet(u"")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.centralwidget.setFont(font)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ln_input_year = QLineEdit(self.centralwidget)
        self.ln_input_year.setObjectName(u"ln_input_year")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ln_input_year.sizePolicy().hasHeightForWidth())
        self.ln_input_year.setSizePolicy(sizePolicy1)
        self.ln_input_year.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.ln_input_year)

        self.ln_race_number = QLineEdit(self.centralwidget)
        self.ln_race_number.setObjectName(u"ln_race_number")
        sizePolicy1.setHeightForWidth(self.ln_race_number.sizePolicy().hasHeightForWidth())
        self.ln_race_number.setSizePolicy(sizePolicy1)
        self.ln_race_number.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.ln_race_number)

        self.ln_pod = QLineEdit(self.centralwidget)
        self.ln_pod.setObjectName(u"ln_pod")
        sizePolicy1.setHeightForWidth(self.ln_pod.sizePolicy().hasHeightForWidth())
        self.ln_pod.setSizePolicy(sizePolicy1)
        self.ln_pod.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.ln_pod)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.sb_session = QScrollBar(self.centralwidget)
        self.sb_session.setObjectName(u"sb_session")
        self.sb_session.setMinimum(1)
        self.sb_session.setMaximum(5)
        self.sb_session.setPageStep(1)
        self.sb_session.setValue(1)
        self.sb_session.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sb_session)

        self.btn_search_for_name_on_position = QPushButton(self.centralwidget)
        self.btn_search_for_name_on_position.setObjectName(u"btn_search_for_name_on_position")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_search_for_name_on_position.sizePolicy().hasHeightForWidth())
        self.btn_search_for_name_on_position.setSizePolicy(sizePolicy2)
        self.btn_search_for_name_on_position.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_2.addWidget(self.btn_search_for_name_on_position)

        self.lb_output_name_position = QLabel(self.centralwidget)
        self.lb_output_name_position.setObjectName(u"lb_output_name_position")
        self.lb_output_name_position.setMaximumSize(QSize(16777215, 200))

        self.verticalLayout_2.addWidget(self.lb_output_name_position)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.ln_input_year.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.ln_race_number.setText(QCoreApplication.translate("MainWindow", u"Race Number", None))
        self.ln_pod.setText(QCoreApplication.translate("MainWindow", u"Position of the Driver", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"FP1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"FP2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"FP3", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Qualifying", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Race", None))
        self.btn_search_for_name_on_position.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.lb_output_name_position.setText(QCoreApplication.translate("MainWindow", u"The driver has finished in this position", None))
    # retranslateUi

