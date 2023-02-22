# Form implementation generated from reading ui file 'stock2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import resources
import coinranking
import coinrankcandle as cd

class Ui_Viewer(object):
    def __init__(self) -> None:
        self.candle_widget = QtWebEngineWidgets.QWebEngineView()
        self.cr = cd.CoinRankingOHLC("Qwsogvtv82FCd", "minute","BTC","Bitcoin")
        self.candle_widget.setHtml(self.cr.show_candlestick())
    def setupUi(self, Viewer):
        Viewer.setObjectName("Viewer")
        Viewer.resize(1280, 771)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Viewer.sizePolicy().hasHeightForWidth())
        Viewer.setSizePolicy(sizePolicy)
        Viewer.setAutoFillBackground(False)
        Viewer.setStyleSheet("font-size: 16pt;\n"
"font-family: Lato;\n"
"color: white;\n"
"background-color: #001F2D;\n"
"border: none;")
        self.centralwidget = QtWidgets.QWidget(parent=Viewer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setStyleSheet('''
        QFrame, QComboBox, QPushButton, QWidget{
        background-color: #002234;
        }
        ''')
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(38, 42, 38, 1)
        self.verticalLayout_2.setSpacing(19)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(27, 19))
        self.label_2.setStyleSheet("font-weight: 400;\n"
"font-size: 10pt;\n"
"")
        # if 
        
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/images/stocks.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.checkBox = QtWidgets.QCheckBox(parent=self.frame)
        self.checkBox.setMinimumSize(QtCore.QSize(51, 24))
        self.checkBox.setMaximumSize(QtCore.QSize(45, 24))
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet("QCheckBox::indicator:unchecked {\n"
"    width: 45px;\n"
"    height: 24px;\n"
"    image: url(:/icons/images/off.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    width: 45px;\n"
"    height: 24px;\n"
"    image: url(:/icons/images/on.png);\n"
"}")
        self.checkBox.setText("")
        self.checkBox.setIconSize(QtCore.QSize(45, 24))
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setMaximumSize(QtCore.QSize(24, 24))
        self.label.setStyleSheet("font-weight: 400;\n"
"font-size: 10pt;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/images/crypto.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox = QtWidgets.QComboBox(parent=self.frame)
        self.comboBox.setMinimumSize(QtCore.QSize(70, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(1666666, 1666666))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.comboBox.setStyleSheet("QComboBox{\n"
"    font-weight: 400;\n"
"    font-size: 11pt;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    margin: -1 0 0 -1;\n"
"    image: url(:/icons/images/down.png);\n"
"    height: 13px;\n"
"    width: 13px;\n"
"}")
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setMaximumSize(QtCore.QSize(16666, 48))
        self.label_3.setStyleSheet("font-weight: 600;\n"
"font-size: 26pt;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_2.setMaximumSize(QtCore.QSize(24, 24))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet("font-weight: 100;\n"
"font-size: 20pt;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 31))
        self.lineEdit.setStyleSheet("border: 1px solid #001A27;\n"
"border-radius: 12px;\n"
"background-color:  #001A27;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.listView = QtWidgets.QListWidget(parent=self.frame)
        self.listView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listView.setStyleSheet('''
        QScrollBar {
            width: 6px;
        }
        QScrollBar::handle:vertical {
            background: rgb(22,58,87);
            border-radius: 3px;
        }
        QScrollBar::add-line:vertical {
            height: 0px;
        }
        QScrollBar::sub-line:vertical {
            height: 0px;
        }
        ''')
        self.listView.setObjectName("listView")
        self.listView.setLayout(QtWidgets.QVBoxLayout())
        self.listView.itemClicked.connect(self.selectionChanged)
        global items, cur, past, fake_obj
        past = 0
        cur = 0

        
        self.datacoin()

        fake_obj = [(crypto[0],crypto[1],"$"+crypto[2],crypto[3],"$"+crypto[5]) for crypto in self.crypto]
        items = [listItem(i[0],i[1],i[2],i[3],i[4]) for i in fake_obj]
        widgetlist = []
        #convert to QWidget
        for i in items:
            container = QtWidgets.QWidget()
            i.setupUi(container)
            widgetlist.append(container)
	
            
        containers = []
	#put widget in listwidgetitem
        for j in widgetlist:
            itemcontainer = QtWidgets.QListWidgetItem()
            itemcontainer.setSizeHint(QtCore.QSize(1,77))
            containers.append(itemcontainer)
            self.listView.addItem(itemcontainer)
            self.listView.setItemWidget(itemcontainer,j)
            
        self.listView.setCurrentRow(0)
        self.listView.setItemWidget(containers[0],widgetlist[0])

        

        self.verticalLayout_2.addWidget(self.listView)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame1 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame1.setObjectName("frame1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_3.setContentsMargins(39, 35, 39, 24)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, 5, 5, 5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame1)
        self.label_4.setStyleSheet("font-size: 45pt;\n"
"font-weight: 1000;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(parent=self.frame1)
        self.label_6.setStyleSheet("color: rgba(255,255,255,0.75);\n"
"font-size: 13pt;\n"
"margin: 9 0 0 0;")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.label_5 = QtWidgets.QLabel(parent=self.frame1)
        self.label_5.setStyleSheet("font-size: 21pt;")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 35)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_9 = QtWidgets.QLabel(parent=self.frame1)
        self.label_9.setStyleSheet("font-weight: bold;\n"
"font-size: 21pt;")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTop|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(parent=self.frame1)
        self.label_8.setStyleSheet("font-weight: bold;\n"
"font-size: 13pt;")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTop|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(parent=self.frame1)
        self.label_7.setStyleSheet("font-weight: bold;\n"
"font-size: 13pt;")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTop|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(17 , 17, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.verticalLayout_3.addItem(spacerItem3)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.frame1)
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
"    left: 0;\n"
"    background-color: transparent;\n"
"}\n"
"QTabWidget::pane {\n"
"    top: 18px;\n"
"    left: 0;\n"
"    background-color: transparent;\n"
"}\n"
"QTabWidget{\n"
"\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    font-weight: bold;\n"
"    font-size: 21pt;\n"
"    color: rgba(255,255,255,0.5);\n"
"    background-color: transparent;\n"
"    }\n"
"QTabBar::tab:selected {\n"
"    font-weight: bold;\n"
"    color: rgba(255,255,255,1);\n"
"    background-color: transparent;\n"
"    }")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.tab.setStyleSheet("background-color: rgba(255,255,255,0.3)")        
        graph_layout = QtWidgets.QVBoxLayout()
        graph_layout.addWidget(self.candle_widget)
        self.tab.setLayout(graph_layout)






        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.gridLayout.addWidget(self.frame1, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 362)
        self.gridLayout.setColumnStretch(1, 918)
        Viewer.setCentralWidget(self.centralwidget)

        self.retranslateUi(Viewer)
        self.setSelected(0)
        self.tabWidget.setCurrentIndex(0)
        items[0].setHighlight()
        QtCore.QMetaObject.connectSlotsByName(Viewer)

    def retranslateUi(self, Viewer):
        _translate = QtCore.QCoreApplication.translate
        Viewer.setWindowTitle(_translate("Viewer", "IntelliFi"))
        self.comboBox.setItemText(0, _translate("Viewer", "USD"))
        self.comboBox.setItemText(1, _translate("Viewer", "THB"))
        self.label_3.setText(_translate("Viewer", "Symbol"))
        self.pushButton_2.setText(_translate("Viewer", "+"))
        self.label_4.setText(_translate("Viewer", "SYMB"))
        self.label_6.setText(_translate("Viewer", "Market"))
        self.label_5.setText(_translate("Viewer", "Company Name"))
        self.label_9.setText(_translate("Viewer", "Price"))
        self.label_8.setText(_translate("Viewer", "%change"))
        self.label_7.setText(_translate("Viewer", "Mkt. Cap"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Viewer", "Prices"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Viewer", "News"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Viewer", "Information"))

    def setSelected(self,index):
        _translate = QtCore.QCoreApplication.translate
        symbol,full,price,change,cap = fake_obj[index]
        self.label_4.setText(_translate("Viewer", symbol))
        self.label_6.setText(_translate("Viewer", "NASDAQ"))
        self.label_5.setText(_translate("Viewer", full))
        self.label_9.setText(_translate("Viewer", price))
        self.label_8.setText(_translate("Viewer", change))
        self.label_7.setText(_translate("Viewer", cap))
    
    def selectionChanged(self):
        global past, cur
        past = cur
        current = self.listView.currentRow()
        cur = current
        #print("Selected item: ", current)
        items[past].unsetHightlight()
        items[current].setHighlight()
        self.setSelected(cur)
    

    def datacoin(self):
        data = coinranking.Data()
        data.retrieve_data()
        crypto_sym = data.get_list_symbol()
        crypto_name = data.get_list_name()
        crypto_price = data.get_list_price()
        crypto_change = data.get_list_change()
        crypto_change_color = data.get_list_change_color()
        crypto_marketcap = data.get_list_marketcap()
        crypto_uuid = data.get_list_uuid()

        self.crypto = list(zip(crypto_sym,crypto_name,crypto_price,crypto_change,crypto_change_color,crypto_marketcap,crypto_uuid))
        # print(crypto)
        data.close_connection()

        return self.crypto
    
        


class listItem(object):
    def __init__(self,symbol,comp,price,change,cap):
        self.symbol = symbol
        self.company = comp
        self.price = price
        self.change = change
        self.cap = cap
    def setupUi(self, Form):
        # Form.setObjectName("Form")
        # Form.resize(294, 77)
        # Form.setMinimumSize(QtCore.QSize(0, 77))
        # Form.setMaximumSize(QtCore.QSize(16777215, 77))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(15, 0, 5, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=Form) #symbol
        self.label_2.setStyleSheet('''
        QLabel{
        font-size: 15.6pt;
        font-weight: 800;
        color: rgba(255,255,255,0.3);
        }
'''
)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(parent=Form) #price
        self.label.setStyleSheet("font-size: 13pt;\n"
"color: rgba(255,255,255,1);\n"
)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setStyleSheet("height: 13px;\n"
"    width: 13px;")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_6.setPixmap(QtGui.QPixmap(":/icons/images/pos.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setMaximumSize(15,4)
        self.horizontalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(parent=Form) #name
        self.label_3.setStyleSheet("font-size: 10.4pt;\n"
"font-weight: 300;\n"
"color: rgba(255,255,255,0.8);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=Form) #change
        self.label_4.setStyleSheet("font-size: 7.8pt;\n"
"font-weight: 300;\n"
"color: rgba(255,255,255,0.75);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=Form) #marketCap
        self.label_5.setStyleSheet("font-size: 7.8pt;\n"
"font-weight: 300;\n"
"color: rgba(255,255,255,0.75);")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", self.symbol))
        self.label.setText(_translate("Form", self.price))
        self.label_6.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", self.company))
        self.label_4.setText(_translate("Form", self.change))
        self.label_5.setText(_translate("Form", self.cap))

    def setHighlight(self):
        self.label_2.setStyleSheet('''
        QLabel{
        font-size: 15.6pt;
        font-weight: 800;
        color: rgba(255,255,255,1);
        }
'''
)
        
    def unsetHightlight(self):
        self.label_2.setStyleSheet('''
        QLabel{
        font-size: 15.6pt;
        font-weight: 800;
        color: rgba(255,255,255,0.3);
        }
'''
)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Viewer = QtWidgets.QMainWindow()
    ui = Ui_Viewer()
    ui.setupUi(Viewer)
    Viewer.show()
    sys.exit(app.exec())
