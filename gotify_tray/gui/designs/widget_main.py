# Form implementation generated from reading ui file 'gotify_tray/gui/designs\widget_main.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 647)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.listView_applications = QtWidgets.QListView(self.splitter)
        self.listView_applications.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_applications.setObjectName("listView_applications")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_application = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_application.setObjectName("label_application")
        self.horizontalLayout.addWidget(self.label_application)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pb_refresh = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_refresh.setText("")
        self.pb_refresh.setObjectName("pb_refresh")
        self.horizontalLayout.addWidget(self.pb_refresh)
        self.pb_delete_all = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_delete_all.setText("")
        self.pb_delete_all.setObjectName("pb_delete_all")
        self.horizontalLayout.addWidget(self.pb_delete_all)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.listView_messages = QtWidgets.QListView(self.verticalLayoutWidget)
        self.listView_messages.setAutoScroll(True)
        self.listView_messages.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_messages.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.listView_messages.setObjectName("listView_messages")
        self.verticalLayout_2.addWidget(self.listView_messages)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.listView_applications, self.listView_messages)
        MainWindow.setTabOrder(self.listView_messages, self.pb_refresh)
        MainWindow.setTabOrder(self.pb_refresh, self.pb_delete_all)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.label_application.setText(_translate("MainWindow", "Application"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
