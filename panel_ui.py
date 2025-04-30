# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(498, 599)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_2 = QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.tab_1)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit_filePath = QLineEdit(self.groupBox)
        self.lineEdit_filePath.setObjectName(u"lineEdit_filePath")
        self.lineEdit_filePath.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.lineEdit_filePath)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_getFilePath = QPushButton(self.groupBox)
        self.pushButton_getFilePath.setObjectName(u"pushButton_getFilePath")

        self.horizontalLayout_4.addWidget(self.pushButton_getFilePath)

        self.pushButton_generateFromFile = QPushButton(self.groupBox)
        self.pushButton_generateFromFile.setObjectName(u"pushButton_generateFromFile")
        self.pushButton_generateFromFile.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.pushButton_generateFromFile)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab_1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.plainTextEdit_rawInput = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_rawInput.setObjectName(u"plainTextEdit_rawInput")

        self.verticalLayout_4.addWidget(self.plainTextEdit_rawInput)

        self.pushButton_generateFromPlainText = QPushButton(self.groupBox_2)
        self.pushButton_generateFromPlainText.setObjectName(u"pushButton_generateFromPlainText")

        self.verticalLayout_4.addWidget(self.pushButton_generateFromPlainText)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setEnabled(True)
        self.verticalLayout_15 = QVBoxLayout(self.tab_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.groupBox_8 = QGroupBox(self.tab_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_showGraphInText = QPushButton(self.groupBox_8)
        self.pushButton_showGraphInText.setObjectName(u"pushButton_showGraphInText")

        self.horizontalLayout_12.addWidget(self.pushButton_showGraphInText)

        self.pushButton_showGraphInImage = QPushButton(self.groupBox_8)
        self.pushButton_showGraphInImage.setObjectName(u"pushButton_showGraphInImage")

        self.horizontalLayout_12.addWidget(self.pushButton_showGraphInImage)

        self.pushButton_saveGraphAsImage = QPushButton(self.groupBox_8)
        self.pushButton_saveGraphAsImage.setObjectName(u"pushButton_saveGraphAsImage")

        self.horizontalLayout_12.addWidget(self.pushButton_saveGraphAsImage)


        self.verticalLayout_15.addWidget(self.groupBox_8)

        self.plainTextEdit_showGraph = QPlainTextEdit(self.tab_2)
        self.plainTextEdit_showGraph.setObjectName(u"plainTextEdit_showGraph")
        self.plainTextEdit_showGraph.setEnabled(True)
        self.plainTextEdit_showGraph.setReadOnly(True)

        self.verticalLayout_15.addWidget(self.plainTextEdit_showGraph)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_6 = QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_3 = QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_bridgeStart = QLineEdit(self.groupBox_3)
        self.lineEdit_bridgeStart.setObjectName(u"lineEdit_bridgeStart")

        self.horizontalLayout_2.addWidget(self.lineEdit_bridgeStart)

        self.comboBox_bridgeStart = QComboBox(self.groupBox_3)
        self.comboBox_bridgeStart.setObjectName(u"comboBox_bridgeStart")

        self.horizontalLayout_2.addWidget(self.comboBox_bridgeStart)

        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit_bridgeEnd = QLineEdit(self.groupBox_3)
        self.lineEdit_bridgeEnd.setObjectName(u"lineEdit_bridgeEnd")

        self.horizontalLayout.addWidget(self.lineEdit_bridgeEnd)

        self.comboBox_bridgeEnd = QComboBox(self.groupBox_3)
        self.comboBox_bridgeEnd.setObjectName(u"comboBox_bridgeEnd")

        self.horizontalLayout.addWidget(self.comboBox_bridgeEnd)

        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.pushButton_calcBridgeWord = QPushButton(self.groupBox_3)
        self.pushButton_calcBridgeWord.setObjectName(u"pushButton_calcBridgeWord")

        self.verticalLayout_5.addWidget(self.pushButton_calcBridgeWord)


        self.verticalLayout_6.addWidget(self.groupBox_3)

        self.plainTextEdit_outputBridge = QPlainTextEdit(self.tab_3)
        self.plainTextEdit_outputBridge.setObjectName(u"plainTextEdit_outputBridge")
        self.plainTextEdit_outputBridge.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.plainTextEdit_outputBridge)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_8 = QVBoxLayout(self.tab_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_4 = QGroupBox(self.tab_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.plainTextEdit_rawNewInput = QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit_rawNewInput.setObjectName(u"plainTextEdit_rawNewInput")

        self.verticalLayout_7.addWidget(self.plainTextEdit_rawNewInput)

        self.pushButton_generateNewText = QPushButton(self.groupBox_4)
        self.pushButton_generateNewText.setObjectName(u"pushButton_generateNewText")

        self.verticalLayout_7.addWidget(self.pushButton_generateNewText)


        self.verticalLayout_8.addWidget(self.groupBox_4)

        self.plainTextEdit_outputNewText = QPlainTextEdit(self.tab_4)
        self.plainTextEdit_outputNewText.setObjectName(u"plainTextEdit_outputNewText")
        self.plainTextEdit_outputNewText.setReadOnly(True)

        self.verticalLayout_8.addWidget(self.plainTextEdit_outputNewText)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_11 = QVBoxLayout(self.tab_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_5 = QGroupBox(self.tab_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.lineEdit_shortestPathStart = QLineEdit(self.groupBox_5)
        self.lineEdit_shortestPathStart.setObjectName(u"lineEdit_shortestPathStart")

        self.horizontalLayout_6.addWidget(self.lineEdit_shortestPathStart)

        self.comboBox_shortestPathStart = QComboBox(self.groupBox_5)
        self.comboBox_shortestPathStart.setObjectName(u"comboBox_shortestPathStart")

        self.horizontalLayout_6.addWidget(self.comboBox_shortestPathStart)

        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(2, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.lineEdit_shortestPathEnd = QLineEdit(self.groupBox_5)
        self.lineEdit_shortestPathEnd.setObjectName(u"lineEdit_shortestPathEnd")

        self.horizontalLayout_7.addWidget(self.lineEdit_shortestPathEnd)

        self.comboBox_shortestPathEnd = QComboBox(self.groupBox_5)
        self.comboBox_shortestPathEnd.setObjectName(u"comboBox_shortestPathEnd")

        self.horizontalLayout_7.addWidget(self.comboBox_shortestPathEnd)

        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkBox_calcStartToAll = QCheckBox(self.groupBox_5)
        self.checkBox_calcStartToAll.setObjectName(u"checkBox_calcStartToAll")

        self.verticalLayout_9.addWidget(self.checkBox_calcStartToAll)

        self.checkBox_showMultiPath = QCheckBox(self.groupBox_5)
        self.checkBox_showMultiPath.setObjectName(u"checkBox_showMultiPath")
        self.checkBox_showMultiPath.setChecked(True)

        self.verticalLayout_9.addWidget(self.checkBox_showMultiPath)


        self.horizontalLayout_8.addLayout(self.verticalLayout_9)

        self.pushButton_calcShortestPath = QPushButton(self.groupBox_5)
        self.pushButton_calcShortestPath.setObjectName(u"pushButton_calcShortestPath")

        self.horizontalLayout_8.addWidget(self.pushButton_calcShortestPath)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.line = QFrame(self.groupBox_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_shortestPathCount = QLabel(self.groupBox_5)
        self.label_shortestPathCount.setObjectName(u"label_shortestPathCount")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_shortestPathCount.sizePolicy().hasHeightForWidth())
        self.label_shortestPathCount.setSizePolicy(sizePolicy1)

        self.horizontalLayout_13.addWidget(self.label_shortestPathCount)

        self.comboBox_shortestPath = QComboBox(self.groupBox_5)
        self.comboBox_shortestPath.setObjectName(u"comboBox_shortestPath")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_shortestPath.sizePolicy().hasHeightForWidth())
        self.comboBox_shortestPath.setSizePolicy(sizePolicy2)

        self.horizontalLayout_13.addWidget(self.comboBox_shortestPath)

        self.pushButton_showPathInImage = QPushButton(self.groupBox_5)
        self.pushButton_showPathInImage.setObjectName(u"pushButton_showPathInImage")

        self.horizontalLayout_13.addWidget(self.pushButton_showPathInImage)


        self.verticalLayout_10.addLayout(self.horizontalLayout_13)


        self.verticalLayout_11.addWidget(self.groupBox_5)

        self.plainTextEdit_outputShortestPath = QPlainTextEdit(self.tab_5)
        self.plainTextEdit_outputShortestPath.setObjectName(u"plainTextEdit_outputShortestPath")
        self.plainTextEdit_outputShortestPath.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.plainTextEdit_outputShortestPath)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_13 = QVBoxLayout(self.tab_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.groupBox_6 = QGroupBox(self.tab_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.groupBox_6)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.doubleSpinBox_dampingFactor = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_dampingFactor.setObjectName(u"doubleSpinBox_dampingFactor")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_dampingFactor.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_dampingFactor.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_dampingFactor.setMaximum(1.000000000000000)
        self.doubleSpinBox_dampingFactor.setSingleStep(0.010000000000000)
        self.doubleSpinBox_dampingFactor.setValue(0.850000000000000)

        self.horizontalLayout_9.addWidget(self.doubleSpinBox_dampingFactor)


        self.verticalLayout_12.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_14.addWidget(self.label_9)

        self.spinBox_iterationTimes = QSpinBox(self.groupBox_6)
        self.spinBox_iterationTimes.setObjectName(u"spinBox_iterationTimes")
        sizePolicy3.setHeightForWidth(self.spinBox_iterationTimes.sizePolicy().hasHeightForWidth())
        self.spinBox_iterationTimes.setSizePolicy(sizePolicy3)
        self.spinBox_iterationTimes.setMaximum(500)
        self.spinBox_iterationTimes.setSingleStep(10)
        self.spinBox_iterationTimes.setValue(20)

        self.horizontalLayout_14.addWidget(self.spinBox_iterationTimes)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.radioButton_uniformPageRankStrategy = QRadioButton(self.groupBox_6)
        self.radioButton_uniformPageRankStrategy.setObjectName(u"radioButton_uniformPageRankStrategy")
        self.radioButton_uniformPageRankStrategy.setChecked(True)

        self.horizontalLayout_10.addWidget(self.radioButton_uniformPageRankStrategy)

        self.radioButton_inDegreePageRankStrategy = QRadioButton(self.groupBox_6)
        self.radioButton_inDegreePageRankStrategy.setObjectName(u"radioButton_inDegreePageRankStrategy")

        self.horizontalLayout_10.addWidget(self.radioButton_inDegreePageRankStrategy)

        self.radioButton_sumIncomingWeightsPageRankStrategy = QRadioButton(self.groupBox_6)
        self.radioButton_sumIncomingWeightsPageRankStrategy.setObjectName(u"radioButton_sumIncomingWeightsPageRankStrategy")

        self.horizontalLayout_10.addWidget(self.radioButton_sumIncomingWeightsPageRankStrategy)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.pushButton_startPageRank = QPushButton(self.groupBox_6)
        self.pushButton_startPageRank.setObjectName(u"pushButton_startPageRank")

        self.verticalLayout_12.addWidget(self.pushButton_startPageRank)


        self.verticalLayout_13.addWidget(self.groupBox_6)

        self.tableWidget_outputPageRank = QTableWidget(self.tab_6)
        self.tableWidget_outputPageRank.setObjectName(u"tableWidget_outputPageRank")
        self.tableWidget_outputPageRank.setSortingEnabled(True)

        self.verticalLayout_13.addWidget(self.tableWidget_outputPageRank)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_14 = QVBoxLayout(self.tab_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.groupBox_7 = QGroupBox(self.tab_7)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.spinBox_randomWalkSpeed = QSpinBox(self.groupBox_7)
        self.spinBox_randomWalkSpeed.setObjectName(u"spinBox_randomWalkSpeed")
        self.spinBox_randomWalkSpeed.setMinimum(1)
        self.spinBox_randomWalkSpeed.setMaximum(100)
        self.spinBox_randomWalkSpeed.setValue(10)

        self.horizontalLayout_11.addWidget(self.spinBox_randomWalkSpeed)


        self.verticalLayout_16.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_startRandomWalk = QPushButton(self.groupBox_7)
        self.pushButton_startRandomWalk.setObjectName(u"pushButton_startRandomWalk")
        self.pushButton_startRandomWalk.setEnabled(True)
        self.pushButton_startRandomWalk.setCheckable(False)

        self.horizontalLayout_15.addWidget(self.pushButton_startRandomWalk)

        self.pushButton_stopRandomWalk = QPushButton(self.groupBox_7)
        self.pushButton_stopRandomWalk.setObjectName(u"pushButton_stopRandomWalk")
        self.pushButton_stopRandomWalk.setEnabled(False)
        self.pushButton_stopRandomWalk.setAutoExclusive(False)
        self.pushButton_stopRandomWalk.setFlat(False)

        self.horizontalLayout_15.addWidget(self.pushButton_stopRandomWalk)


        self.verticalLayout_16.addLayout(self.horizontalLayout_15)


        self.verticalLayout_14.addWidget(self.groupBox_7)

        self.plainTextEdit_outputRandomWalk = QPlainTextEdit(self.tab_7)
        self.plainTextEdit_outputRandomWalk.setObjectName(u"plainTextEdit_outputRandomWalk")
        self.plainTextEdit_outputRandomWalk.setReadOnly(True)

        self.verticalLayout_14.addWidget(self.plainTextEdit_outputRandomWalk)

        self.tabWidget.addTab(self.tab_7, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton_startRandomWalk.setDefault(False)
        self.pushButton_stopRandomWalk.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u4ece\u6587\u4ef6", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8def\u5f84", None))
        self.pushButton_getFilePath.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.pushButton_generateFromFile.setText(QCoreApplication.translate("Form", u"\u4ece\u8be5\u8def\u5f84\u751f\u6210", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u4ece\u6587\u672c", None))
        self.pushButton_generateFromPlainText.setText(QCoreApplication.translate("Form", u"\u4ece\u8be5\u6587\u672c\u751f\u6210", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("Form", u"\u751f\u6210", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Form", u"\u56fe\u5c55\u793a", None))
        self.pushButton_showGraphInText.setText(QCoreApplication.translate("Form", u"\u5c55\u793a(\u6587\u672c)", None))
        self.pushButton_showGraphInImage.setText(QCoreApplication.translate("Form", u"\u5c55\u793a(\u56fe\u7247)", None))
        self.pushButton_saveGraphAsImage.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u56fe\u7247\u81f3...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u5c55\u793a", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u6865\u63a5\u8bcd", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5355\u8bcd1", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5355\u8bcd2", None))
        self.pushButton_calcBridgeWord.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u6865\u63a5\u8bcd", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u65b0\u6587\u672c\u751f\u6210", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u6587\u672c", None))
        self.pushButton_generateNewText.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u65b0\u6587\u672c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u6587\u672c\u751f\u6210", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"\u6700\u77ed\u8def\u8ba1\u7b97", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u8d77\u70b9", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u7ec8\u70b9", None))
        self.checkBox_calcStartToAll.setText(QCoreApplication.translate("Form", u"\u8d77\u70b9\u81f3\u6240\u6709\u8282\u70b9", None))
        self.checkBox_showMultiPath.setText(QCoreApplication.translate("Form", u"\u591a\u8def\u5f84\u5c55\u793a", None))
        self.pushButton_calcShortestPath.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.label_shortestPathCount.setText(QCoreApplication.translate("Form", u"\u8def\u5f84\u6570\uff1a", None))
        self.pushButton_showPathInImage.setText(QCoreApplication.translate("Form", u"\u5c55\u793a\u56fe\u7247", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\u6700\u77ed\u8def\u5f84", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"PageRank\u7b97\u6cd5", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u963b\u5c3c\u56e0\u5b50", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u8fed\u4ee3\u6b21\u6570", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u521d\u59cb\u503c\u7b56\u7565", None))
        self.radioButton_uniformPageRankStrategy.setText(QCoreApplication.translate("Form", u"\u5e73\u5747\u5206\u914d", None))
        self.radioButton_inDegreePageRankStrategy.setText(QCoreApplication.translate("Form", u"\u6309\u5165\u5ea6\u5206\u914d", None))
        self.radioButton_sumIncomingWeightsPageRankStrategy.setText(QCoreApplication.translate("Form", u"\u6309\u5165\u8fb9\u6743\u91cd\u548c\u5206\u914d", None))
        self.pushButton_startPageRank.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Form", u"PageRank", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", u"\u968f\u673a\u6e38\u8d70", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u6e38\u8d70\u901f\u5ea6\uff08\u6bcf\u79d2\uff0c1-100\uff09", None))
        self.pushButton_startRandomWalk.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.pushButton_stopRandomWalk.setText(QCoreApplication.translate("Form", u"\u505c\u6b62", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("Form", u"\u968f\u673a\u6e38\u8d70", None))
    # retranslateUi

