# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grey_conv_button = QtWidgets.QPushButton(self.centralwidget)
        self.grey_conv_button.setGeometry(QtCore.QRect(30, 480, 200, 50))
        self.grey_conv_button.setObjectName("grey_conv_button")
        self.rgb_conv_button = QtWidgets.QPushButton(self.centralwidget)
        self.rgb_conv_button.setGeometry(QtCore.QRect(30, 540, 200, 50))
        self.rgb_conv_button.setObjectName("rgb_conv_button")
        self.Media_filter_button = QtWidgets.QPushButton(self.centralwidget)
        self.Media_filter_button.setGeometry(QtCore.QRect(280, 480, 200, 50))
        self.Media_filter_button.setObjectName("Media_filter_button")
        self.Mean_filter_button = QtWidgets.QPushButton(self.centralwidget)
        self.Mean_filter_button.setGeometry(QtCore.QRect(280, 540, 200, 50))
        self.Mean_filter_button.setObjectName("Mean_filter_button")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 600, 200, 50))
        self.pushButton.setObjectName("pushButton")
        self.origin_img = QtWidgets.QLabel(self.centralwidget)
        self.origin_img.setGeometry(QtCore.QRect(20, 10, 450, 450))
        self.origin_img.setAlignment(QtCore.Qt.AlignCenter)
        self.origin_img.setObjectName("origin_img")
        self.processed_img = QtWidgets.QLabel(self.centralwidget)
        self.processed_img.setGeometry(QtCore.QRect(530, 10, 450, 450))
        self.processed_img.setAlignment(QtCore.Qt.AlignCenter)
        self.processed_img.setObjectName("processed_img")
        self.Adopted_Irelia = QtWidgets.QPushButton(self.centralwidget)
        self.Adopted_Irelia.setGeometry(QtCore.QRect(280, 600, 200, 50))
        self.Adopted_Irelia.setObjectName("Adopted_Irelia")
        self.AI = QtWidgets.QLabel(self.centralwidget)
        self.AI.setGeometry(QtCore.QRect(530, 480, 200, 150))
        self.AI.setText("")
        self.AI.setObjectName("AI")
        self.AI_2 = QtWidgets.QLabel(self.centralwidget)
        self.AI_2.setGeometry(QtCore.QRect(770, 480, 200, 150))
        self.AI_2.setText("")
        self.AI_2.setObjectName("AI_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 635, 80, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(830, 635, 80, 20))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 24))
        self.menubar.setObjectName("menubar")
        self.menuAdopted_Irelia = QtWidgets.QMenu(self.menubar)
        self.menuAdopted_Irelia.setObjectName("menuAdopted_Irelia")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menuAdopted_Irelia.addAction(self.action)
        self.menubar.addAction(self.menuAdopted_Irelia.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.grey_conv_button.setText(_translate("MainWindow", "grey_conv"))
        self.rgb_conv_button.setText(_translate("MainWindow", "rgb_conv"))
        self.Media_filter_button.setText(_translate("MainWindow", "Media_filter"))
        self.Mean_filter_button.setText(_translate("MainWindow", "Mean_filter"))
        self.pushButton.setText(_translate("MainWindow", "选择一张图片"))
        self.origin_img.setText(_translate("MainWindow", "原图"))
        self.processed_img.setText(_translate("MainWindow", "修改后"))
        self.Adopted_Irelia.setText(_translate("MainWindow", "直方图"))
        self.label.setText(_translate("MainWindow", "修改前直方图"))
        self.label_2.setText(_translate("MainWindow", "修改后直方图"))
        self.menuAdopted_Irelia.setTitle(_translate("MainWindow", "Adopted Irelia"))
        self.action.setText(_translate("MainWindow", "~~~~~~`"))
