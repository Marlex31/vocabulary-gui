# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(False)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 451))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(400, 10, 341, 451))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(22)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.horizontalLayout_3.addWidget(self.listWidget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 21))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setToolTip("")
        self.menuOpen.setStatusTip("")
        self.menuOpen.setObjectName("menuOpen")
        self.menuOpen_recent = QtWidgets.QMenu(self.menuOpen)
        self.menuOpen_recent.setObjectName("menuOpen_recent")
        self.menuSave = QtWidgets.QMenu(self.menubar)
        self.menuSave.setToolTip("")
        self.menuSave.setObjectName("menuSave")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionRecents = QtWidgets.QAction(MainWindow)
        self.actionRecents.setObjectName("actionRecents")
        self.actiontet = QtWidgets.QAction(MainWindow)
        self.actiontet.setEnabled(True)
        self.actiontet.setObjectName("actiontet")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuOpen_recent.addAction(self.actionRecents)
        self.menuOpen.addAction(self.actiontet)
        self.menuOpen.addAction(self.menuOpen_recent.menuAction())
        self.menuSave.addAction(self.actionSave_2)
        self.menuSave.addAction(self.actionSave_as)
        self.menubar.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menuSave.menuAction())

        self.retranslateUi(MainWindow)
        MainWindow.objectNameChanged['QString'].connect(self.listWidget.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "lorem ipsum"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "New Item"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "vedi vini vici"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("MainWindow", "New Item"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.menuOpen_recent.setTitle(_translate("MainWindow", "Open recent"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSave_2.setText(_translate("MainWindow", "Save"))
        self.actionSave_2.setStatusTip(_translate("MainWindow", "Save current file"))
        self.actionRecents.setText(_translate("MainWindow", "Recents"))
        self.actiontet.setText(_translate("MainWindow", "Open"))
        self.actiontet.setToolTip(_translate("MainWindow", "Open"))
        self.actiontet.setStatusTip(_translate("MainWindow", "Open a file"))
        self.actionSave.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())