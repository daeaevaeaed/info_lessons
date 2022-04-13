# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hanoiqGSccP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from tower_widget import TowerWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(938, 474)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontal = QWidget(self.centralwidget)
        self.horizontal.setObjectName(u"horizontal")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontal.sizePolicy().hasHeightForWidth())
        self.horizontal.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.horizontal)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalFrame = QFrame(self.horizontal)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setFrameShape(QFrame.StyledPanel)
        self.horizontalFrame.setFrameShadow(QFrame.Sunken)
        self.towerLayout = QHBoxLayout(self.horizontalFrame)
        self.towerLayout.setSpacing(0)
        self.towerLayout.setObjectName(u"towerLayout")
        self.towerLayout.setContentsMargins(0, 0, 0, 0)
        self.tower0 = TowerWidget(self.horizontalFrame)
        self.tower0.setObjectName(u"tower0")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tower0.sizePolicy().hasHeightForWidth())
        self.tower0.setSizePolicy(sizePolicy2)
        self.tower0.setCursor(QCursor(Qt.PointingHandCursor))
        self.tower0.setFocusPolicy(Qt.StrongFocus)
        self.tower0.setAutoFillBackground(True)

        self.towerLayout.addWidget(self.tower0)

        self.tower1 = TowerWidget(self.horizontalFrame)
        self.tower1.setObjectName(u"tower1")
        sizePolicy2.setHeightForWidth(self.tower1.sizePolicy().hasHeightForWidth())
        self.tower1.setSizePolicy(sizePolicy2)
        self.tower1.setCursor(QCursor(Qt.PointingHandCursor))
        self.tower1.setFocusPolicy(Qt.StrongFocus)
        self.tower1.setAutoFillBackground(True)

        self.towerLayout.addWidget(self.tower1)

        self.tower2 = TowerWidget(self.horizontalFrame)
        self.tower2.setObjectName(u"tower2")
        sizePolicy2.setHeightForWidth(self.tower2.sizePolicy().hasHeightForWidth())
        self.tower2.setSizePolicy(sizePolicy2)
        self.tower2.setCursor(QCursor(Qt.PointingHandCursor))
        self.tower2.setFocusPolicy(Qt.StrongFocus)
        self.tower2.setAutoFillBackground(True)

        self.towerLayout.addWidget(self.tower2)


        self.horizontalLayout.addWidget(self.horizontalFrame)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_gameSize = QLabel(self.horizontal)
        self.label_gameSize.setObjectName(u"label_gameSize")

        self.verticalLayout.addWidget(self.label_gameSize)

        self.gameSize = QLineEdit(self.horizontal)
        self.gameSize.setObjectName(u"gameSize")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.gameSize.sizePolicy().hasHeightForWidth())
        self.gameSize.setSizePolicy(sizePolicy3)
        self.gameSize.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.gameSize)

        self.restartGame = QPushButton(self.horizontal)
        self.restartGame.setObjectName(u"restartGame")

        self.verticalLayout.addWidget(self.restartGame)

        self.pushButton = QPushButton(self.horizontal)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_moveCounter = QLabel(self.horizontal)
        self.label_moveCounter.setObjectName(u"label_moveCounter")
        self.label_moveCounter.setTextFormat(Qt.PlainText)
        self.label_moveCounter.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_moveCounter)

        self.moveCounter = QLineEdit(self.horizontal)
        self.moveCounter.setObjectName(u"moveCounter")
        self.moveCounter.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.moveCounter.sizePolicy().hasHeightForWidth())
        self.moveCounter.setSizePolicy(sizePolicy3)
        self.moveCounter.setMouseTracking(False)
        self.moveCounter.setFocusPolicy(Qt.NoFocus)
        self.moveCounter.setAcceptDrops(False)
        self.moveCounter.setAlignment(Qt.AlignCenter)
        self.moveCounter.setReadOnly(True)

        self.verticalLayout.addWidget(self.moveCounter)

        self.resetCount = QPushButton(self.horizontal)
        self.resetCount.setObjectName(u"resetCount")

        self.verticalLayout.addWidget(self.resetCount)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.horizontal, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tower0.clicked.connect(MainWindow.tower0_clicked)
        self.tower1.clicked.connect(MainWindow.tower1_clicked)
        self.tower2.clicked.connect(MainWindow.tower2_clicked)
        self.resetCount.clicked.connect(MainWindow.reset_count)
        self.restartGame.clicked.connect(MainWindow.restart_game)
        self.pushButton.clicked.connect(MainWindow.solve_clicked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Die T\u00fcrme von Hanoi", None))
        self.label_gameSize.setText(QCoreApplication.translate("MainWindow", u"Anzahl Scheiben:", None))
        self.restartGame.setText(QCoreApplication.translate("MainWindow", u"Neues Spiel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"L\u00f6sen", None))
        self.label_moveCounter.setText(QCoreApplication.translate("MainWindow", u"Bisher get\u00e4tigte\n"
"Z\u00fcge:", None))
        self.resetCount.setText(QCoreApplication.translate("MainWindow", u"Z\u00e4hler\n"
"zur\u00fccksetzen", None))
    # retranslateUi

