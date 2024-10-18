# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(925, 739)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 40, 861, 641))
        self.tabWidget.setObjectName("tabWidget")
        self.SIFT = QtWidgets.QWidget()
        self.SIFT.setObjectName("SIFT")
        self.output_ssd = QtWidgets.QLabel(self.SIFT)
        self.output_ssd.setGeometry(QtCore.QRect(20, 320, 441, 221))
        self.output_ssd.setFrameShape(QtWidgets.QFrame.Box)
        self.output_ssd.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.output_ssd.setObjectName("output_ssd")
        self.output_ncc = QtWidgets.QLabel(self.SIFT)
        self.output_ncc.setGeometry(QtCore.QRect(480, 320, 311, 221))
        self.output_ncc.setFrameShape(QtWidgets.QFrame.Box)
        self.output_ncc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.output_ncc.setObjectName("output_ncc")
        self.match_button = QtWidgets.QPushButton(self.SIFT)
        self.match_button.setGeometry(QtCore.QRect(360, 550, 101, 41))
        self.match_button.setObjectName("match_button")
        self.load_original_image = QtWidgets.QPushButton(self.SIFT)
        self.load_original_image.setGeometry(QtCore.QRect(50, 270, 81, 24))
        self.load_original_image.setObjectName("load_original_image")
        self.original_image = QtWidgets.QLabel(self.SIFT)
        self.original_image.setGeometry(QtCore.QRect(50, 20, 321, 241))
        self.original_image.setFrameShape(QtWidgets.QFrame.Box)
        self.original_image.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.original_image.setObjectName("original_image")
        self.load_scaled_image = QtWidgets.QPushButton(self.SIFT)
        self.load_scaled_image.setGeometry(QtCore.QRect(450, 270, 91, 24))
        self.load_scaled_image.setCheckable(False)
        self.load_scaled_image.setObjectName("load_scaled_image")
        self.scaled_image = QtWidgets.QLabel(self.SIFT)
        self.scaled_image.setGeometry(QtCore.QRect(400, 20, 311, 241))
        self.scaled_image.setFrameShape(QtWidgets.QFrame.Box)
        self.scaled_image.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scaled_image.setObjectName("scaled_image")
        self.tabWidget.addTab(self.SIFT, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.output_ssd.setText(_translate("MainWindow", "SSD "))
        self.output_ncc.setText(_translate("MainWindow", "NCC"))
        self.match_button.setText(_translate("MainWindow", "Match Keypoints"))
        self.load_original_image.setText(_translate("MainWindow", "Upload"))
        self.original_image.setText(_translate("MainWindow", "Original Image"))
        self.load_scaled_image.setText(_translate("MainWindow", "Upload"))
        self.scaled_image.setText(_translate("MainWindow", "Scaled Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SIFT), _translate("MainWindow", "SIFT"))
