# Form implementation generated from reading ui file '.\form.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1152, 645)
        MainWindow.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1151, 581))
        self.tabWidget.setStyleSheet("background-color: rgb(57, 57, 57);\n"
"color: rgb(0, 255, 0);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_start = QtWidgets.QWidget()
        self.tab_start.setObjectName("tab_start")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.tab_start)
        self.textBrowser.setGeometry(QtCore.QRect(120, 380, 881, 161))
        self.textBrowser.setStyleSheet("QTextBrowser {\n"
"    font-size: 14px; \n"
"    font-family: Arial, sans-serif;\n"
"    color: #333333; /* Dunkelgrauer Text */\n"
"    background-color: #f9f9f9; /* Helles Grau für bessere Lesbarkeit */\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"}\n"
"QTextBrowser {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f0f0f0;\n"
"    width: 10px;\n"
"    margin: 2px 0 2px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #999999;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #666666;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"")
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(parent=self.tab_start)
        self.widget.setGeometry(QtCore.QRect(620, 170, 120, 80))
        self.widget.setObjectName("widget")
        self.tabWidget.addTab(self.tab_start, "")
        self.tab_convert = QtWidgets.QWidget()
        self.tab_convert.setObjectName("tab_convert")
        self.convert_Button = QtWidgets.QPushButton(parent=self.tab_convert)
        self.convert_Button.setGeometry(QtCore.QRect(760, 190, 80, 24))
        self.convert_Button.setObjectName("convert_Button")
        self.listWidget_images_source = QtWidgets.QListWidget(parent=self.tab_convert)
        self.listWidget_images_source.setGeometry(QtCore.QRect(30, 60, 481, 471))
        self.listWidget_images_source.setAcceptDrops(True)
        self.listWidget_images_source.setObjectName("listWidget_images_source")
        self.load_images_Button = QtWidgets.QPushButton(parent=self.tab_convert)
        self.load_images_Button.setGeometry(QtCore.QRect(1040, 60, 80, 24))
        self.load_images_Button.setObjectName("load_images_Button")
        self.load_images_Path = QtWidgets.QLineEdit(parent=self.tab_convert)
        self.load_images_Path.setGeometry(QtCore.QRect(540, 60, 481, 24))
        self.load_images_Path.setObjectName("load_images_Path")
        self.label_load_images = QtWidgets.QLabel(parent=self.tab_convert)
        self.label_load_images.setGeometry(QtCore.QRect(540, 30, 151, 21))
        self.label_load_images.setObjectName("label_load_images")
        self.label_images_loaded = QtWidgets.QLabel(parent=self.tab_convert)
        self.label_images_loaded.setGeometry(QtCore.QRect(30, 30, 151, 21))
        self.label_images_loaded.setObjectName("label_images_loaded")
        self.label_search_in_folder = QtWidgets.QLabel(parent=self.tab_convert)
        self.label_search_in_folder.setGeometry(QtCore.QRect(540, 110, 241, 21))
        self.label_search_in_folder.setObjectName("label_search_in_folder")
        self.load_images_from_folder_Path = QtWidgets.QLineEdit(parent=self.tab_convert)
        self.load_images_from_folder_Path.setGeometry(QtCore.QRect(540, 140, 481, 24))
        self.load_images_from_folder_Path.setObjectName("load_images_from_folder_Path")
        self.load_images_from_folder_Button = QtWidgets.QPushButton(parent=self.tab_convert)
        self.load_images_from_folder_Button.setGeometry(QtCore.QRect(1040, 140, 80, 24))
        self.load_images_from_folder_Button.setObjectName("load_images_from_folder_Button")
        self.listWidget_ico_Output = QtWidgets.QListWidget(parent=self.tab_convert)
        self.listWidget_ico_Output.setGeometry(QtCore.QRect(550, 260, 571, 271))
        self.listWidget_ico_Output.setAcceptDrops(True)
        self.listWidget_ico_Output.setObjectName("listWidget_ico_Output")
        self.label_saved_ico = QtWidgets.QLabel(parent=self.tab_convert)
        self.label_saved_ico.setGeometry(QtCore.QRect(550, 230, 241, 21))
        self.label_saved_ico.setObjectName("label_saved_ico")
        self.tabWidget.addTab(self.tab_convert, "")
        self.tab_settings = QtWidgets.QWidget()
        self.tab_settings.setObjectName("tab_settings")
        self.tabWidget.addTab(self.tab_settings, "")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 580, 1151, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"        border: 2px solid #000;\n"
"        border-radius: 5px;\n"
"        text-align: center;\n"
"        font-size: 16px;  /* Schriftgröße */\n"
"        font-weight: bold; /* Fettgedruckt */\n"
"        color: black;\n"
" }\n"
" QProgressBar::chunk {\n"
"                background-color: rgb(255, 0, 98);  /* Ändert die Farbe des Fortschritts */\n"
"                width: 10px;\n"
" }")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setDocumentTitle(_translate("MainWindow", "README"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><title>README</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Arial\',\'sans-serif\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt;\">This application is written in Python3 and is and remains free. It is based on open source code. So you can be sure that you will not receive any ad goods, malware, or anything with the application that could harm you through hidden costs, viruses in all forms or other. In my opinion, the real work on the code was done by the developers of the module: &quot;Pillow&quot; and the graphical user interface: &quot;PyQt6&quot;. Many online conversion services that are likely to be based on NodeJS can include hidden viruses, bathroom cookies, and more. This does not apply to this application because it is open to view and also does not require any network services. Selling, renting or changing the code by integrating malicious code is strictly prohibited and can be carried out. This code is set under the MIT license and is therefore a very free open source code. To everyone who sees this project not only as a user, but also as a developer, you can simply send me an email or notification to Github and send suggestions for improvement / requests for changes. The same is of course also valid for dear users! &quot; You can simply create an ISSUE in the Github Repository or join the discussion of the project! &quot; </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_start), _translate("MainWindow", "Start"))
        self.convert_Button.setText(_translate("MainWindow", "Convert"))
        self.load_images_Button.setText(_translate("MainWindow", "Load"))
        self.label_load_images.setText(_translate("MainWindow", "Load images to convert:"))
        self.label_images_loaded.setText(_translate("MainWindow", "Images: loaded:"))
        self.label_search_in_folder.setText(_translate("MainWindow", "Search and Select all images from a folder: "))
        self.load_images_from_folder_Button.setText(_translate("MainWindow", "Load"))
        self.label_saved_ico.setText(_translate("MainWindow", "Saved ico to:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_convert), _translate("MainWindow", "Convert"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), _translate("MainWindow", "Settings"))
