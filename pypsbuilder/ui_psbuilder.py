# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'psbuilder.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PSBuilder(object):
    def setupUi(self, PSBuilder):
        PSBuilder.setObjectName("PSBuilder")
        PSBuilder.resize(1106, 726)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PSBuilder.sizePolicy().hasHeightForWidth())
        PSBuilder.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(PSBuilder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter_main = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_main.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_main.setObjectName("splitter_main")
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter_main)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.phaseview = QtWidgets.QListView(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phaseview.sizePolicy().hasHeightForWidth())
        self.phaseview.setSizePolicy(sizePolicy)
        self.phaseview.setObjectName("phaseview")
        self.outview = QtWidgets.QListView(self.splitter_2)
        self.outview.setObjectName("outview")
        self.verticalLayout.addWidget(self.splitter_2)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushCalcTatP = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushCalcTatP.sizePolicy().hasHeightForWidth())
        self.pushCalcTatP.setSizePolicy(sizePolicy)
        self.pushCalcTatP.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushCalcTatP.setObjectName("pushCalcTatP")
        self.horizontalLayout_5.addWidget(self.pushCalcTatP)
        self.pushCalcPatT = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushCalcPatT.sizePolicy().hasHeightForWidth())
        self.pushCalcPatT.setSizePolicy(sizePolicy)
        self.pushCalcPatT.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushCalcPatT.setObjectName("pushCalcPatT")
        self.horizontalLayout_5.addWidget(self.pushCalcPatT)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.splitter = QtWidgets.QSplitter(self.splitter_main)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tabMain = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabMain.sizePolicy().hasHeightForWidth())
        self.tabMain.setSizePolicy(sizePolicy)
        self.tabMain.setMinimumSize(QtCore.QSize(480, 520))
        self.tabMain.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabMain.setObjectName("tabMain")
        self.tabPlot = QtWidgets.QWidget()
        self.tabPlot.setObjectName("tabPlot")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tabPlot)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.mplvl = QtWidgets.QVBoxLayout()
        self.mplvl.setObjectName("mplvl")
        self.horizontalLayout_6.addLayout(self.mplvl)
        self.tabMain.addTab(self.tabPlot, "")
        self.tabSettings = QtWidgets.QWidget()
        self.tabSettings.setObjectName("tabSettings")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabSettings)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tabSettings)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.pminEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pminEdit.sizePolicy().hasHeightForWidth())
        self.pminEdit.setSizePolicy(sizePolicy)
        self.pminEdit.setObjectName("pminEdit")
        self.gridLayout.addWidget(self.pminEdit, 1, 1, 1, 1)
        self.tminEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tminEdit.sizePolicy().hasHeightForWidth())
        self.tminEdit.setSizePolicy(sizePolicy)
        self.tminEdit.setObjectName("tminEdit")
        self.gridLayout.addWidget(self.tminEdit, 0, 1, 1, 1)
        self.tmaxEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tmaxEdit.sizePolicy().hasHeightForWidth())
        self.tmaxEdit.setSizePolicy(sizePolicy)
        self.tmaxEdit.setObjectName("tmaxEdit")
        self.gridLayout.addWidget(self.tmaxEdit, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.pmaxEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pmaxEdit.sizePolicy().hasHeightForWidth())
        self.pmaxEdit.setSizePolicy(sizePolicy)
        self.pmaxEdit.setObjectName("pmaxEdit")
        self.gridLayout.addWidget(self.pmaxEdit, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.pushFromAxes = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushFromAxes.sizePolicy().hasHeightForWidth())
        self.pushFromAxes.setSizePolicy(sizePolicy)
        self.pushFromAxes.setObjectName("pushFromAxes")
        self.gridLayout.addWidget(self.pushFromAxes, 0, 4, 1, 1)
        self.pushResetSettings = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushResetSettings.sizePolicy().hasHeightForWidth())
        self.pushResetSettings.setSizePolicy(sizePolicy)
        self.pushResetSettings.setObjectName("pushResetSettings")
        self.gridLayout.addWidget(self.pushResetSettings, 1, 4, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.checkLabelInv = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkLabelInv.setChecked(True)
        self.checkLabelInv.setObjectName("checkLabelInv")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.checkLabelInv)
        self.checkLabelUni = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkLabelUni.setChecked(True)
        self.checkLabelUni.setObjectName("checkLabelUni")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.checkLabelUni)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.checkLabels = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkLabels.setObjectName("checkLabels")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.checkLabels)
        self.spinPrec = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinPrec.sizePolicy().hasHeightForWidth())
        self.spinPrec.setSizePolicy(sizePolicy)
        self.spinPrec.setMaximum(6)
        self.spinPrec.setProperty("value", 1)
        self.spinPrec.setObjectName("spinPrec")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinPrec)
        self.spinAlpha = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinAlpha.sizePolicy().hasHeightForWidth())
        self.spinAlpha.setSizePolicy(sizePolicy)
        self.spinAlpha.setMaximum(100)
        self.spinAlpha.setSingleStep(10)
        self.spinAlpha.setProperty("value", 50)
        self.spinAlpha.setObjectName("spinAlpha")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.spinAlpha)
        self.spinSteps = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinSteps.sizePolicy().hasHeightForWidth())
        self.spinSteps.setSizePolicy(sizePolicy)
        self.spinSteps.setMinimum(5)
        self.spinSteps.setMaximum(200)
        self.spinSteps.setProperty("value", 50)
        self.spinSteps.setObjectName("spinSteps")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinSteps)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tabSettings)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.drawpdexeEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.drawpdexeEdit.setObjectName("drawpdexeEdit")
        self.gridLayout_2.addWidget(self.drawpdexeEdit, 1, 1, 1, 1)
        self.tcexeEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.tcexeEdit.setObjectName("tcexeEdit")
        self.gridLayout_2.addWidget(self.tcexeEdit, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.pushApplySettings = QtWidgets.QPushButton(self.tabSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushApplySettings.sizePolicy().hasHeightForWidth())
        self.pushApplySettings.setSizePolicy(sizePolicy)
        self.pushApplySettings.setObjectName("pushApplySettings")
        self.horizontalLayout_7.addWidget(self.pushApplySettings)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.setStretch(1, 1)
        self.tabMain.addTab(self.tabSettings, "")
        self.tabScript = QtWidgets.QWidget()
        self.tabScript.setObjectName("tabScript")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tabScript)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.outScript = QtWidgets.QPlainTextEdit(self.tabScript)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outScript.sizePolicy().hasHeightForWidth())
        self.outScript.setSizePolicy(sizePolicy)
        self.outScript.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.outScript.setReadOnly(False)
        self.outScript.setObjectName("outScript")
        self.verticalLayout_8.addWidget(self.outScript)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pushReadScript = QtWidgets.QPushButton(self.tabScript)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushReadScript.sizePolicy().hasHeightForWidth())
        self.pushReadScript.setSizePolicy(sizePolicy)
        self.pushReadScript.setObjectName("pushReadScript")
        self.horizontalLayout_4.addWidget(self.pushReadScript)
        self.pushSaveScript = QtWidgets.QPushButton(self.tabScript)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushSaveScript.sizePolicy().hasHeightForWidth())
        self.pushSaveScript.setSizePolicy(sizePolicy)
        self.pushSaveScript.setObjectName("pushSaveScript")
        self.horizontalLayout_4.addWidget(self.pushSaveScript)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.tabMain.addTab(self.tabScript, "")
        self.tabLog = QtWidgets.QWidget()
        self.tabLog.setObjectName("tabLog")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tabLog)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.logText = QtWidgets.QPlainTextEdit(self.tabLog)
        self.logText.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.logText.setReadOnly(True)
        self.logText.setObjectName("logText")
        self.verticalLayout_9.addWidget(self.logText)
        self.tabMain.addTab(self.tabLog, "")
        self.tabOutput = QtWidgets.QTabWidget(self.splitter)
        self.tabOutput.setObjectName("tabOutput")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textOutput = QtWidgets.QPlainTextEdit(self.tab)
        self.textOutput.setObjectName("textOutput")
        self.horizontalLayout.addWidget(self.textOutput)
        self.tabOutput.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.textFullOutput = QtWidgets.QPlainTextEdit(self.tab_2)
        self.textFullOutput.setObjectName("textFullOutput")
        self.horizontalLayout_8.addWidget(self.textFullOutput)
        self.tabOutput.addTab(self.tab_2, "")
        self.tc_splitter = QtWidgets.QSplitter(self.splitter_main)
        self.tc_splitter.setOrientation(QtCore.Qt.Vertical)
        self.tc_splitter.setChildrenCollapsible(False)
        self.tc_splitter.setObjectName("tc_splitter")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tc_splitter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uniview = QtWidgets.QTableView(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uniview.sizePolicy().hasHeightForWidth())
        self.uniview.setSizePolicy(sizePolicy)
        self.uniview.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.uniview.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.uniview.setObjectName("uniview")
        self.verticalLayout_2.addWidget(self.uniview)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushGuessUni = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushGuessUni.sizePolicy().hasHeightForWidth())
        self.pushGuessUni.setSizePolicy(sizePolicy)
        self.pushGuessUni.setObjectName("pushGuessUni")
        self.horizontalLayout_2.addWidget(self.pushGuessUni)
        self.pushUniRemove = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushUniRemove.sizePolicy().hasHeightForWidth())
        self.pushUniRemove.setSizePolicy(sizePolicy)
        self.pushUniRemove.setObjectName("pushUniRemove")
        self.horizontalLayout_2.addWidget(self.pushUniRemove)
        self.pushUniAdd = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushUniAdd.sizePolicy().hasHeightForWidth())
        self.pushUniAdd.setSizePolicy(sizePolicy)
        self.pushUniAdd.setObjectName("pushUniAdd")
        self.horizontalLayout_2.addWidget(self.pushUniAdd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tc_splitter)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.invview = QtWidgets.QTableView(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invview.sizePolicy().hasHeightForWidth())
        self.invview.setSizePolicy(sizePolicy)
        self.invview.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.invview.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.invview.setObjectName("invview")
        self.verticalLayout_6.addWidget(self.invview)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.pushGuessInv = QtWidgets.QPushButton(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushGuessInv.sizePolicy().hasHeightForWidth())
        self.pushGuessInv.setSizePolicy(sizePolicy)
        self.pushGuessInv.setObjectName("pushGuessInv")
        self.horizontalLayout_3.addWidget(self.pushGuessInv)
        self.pushInvRemove = QtWidgets.QPushButton(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushInvRemove.sizePolicy().hasHeightForWidth())
        self.pushInvRemove.setSizePolicy(sizePolicy)
        self.pushInvRemove.setObjectName("pushInvRemove")
        self.horizontalLayout_3.addWidget(self.pushInvRemove)
        self.pushInvAdd = QtWidgets.QPushButton(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushInvAdd.sizePolicy().hasHeightForWidth())
        self.pushInvAdd.setSizePolicy(sizePolicy)
        self.pushInvAdd.setObjectName("pushInvAdd")
        self.horizontalLayout_3.addWidget(self.pushInvAdd)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.splitter_main)
        PSBuilder.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PSBuilder)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1106, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen_recent = QtWidgets.QMenu(self.menuFile)
        self.menuOpen_recent.setObjectName("menuOpen_recent")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        PSBuilder.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PSBuilder)
        self.statusbar.setObjectName("statusbar")
        PSBuilder.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(PSBuilder)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(PSBuilder)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(PSBuilder)
        self.actionSave.setObjectName("actionSave")
        self.actionExport_Drawpd = QtWidgets.QAction(PSBuilder)
        self.actionExport_Drawpd.setObjectName("actionExport_Drawpd")
        self.actionQuit = QtWidgets.QAction(PSBuilder)
        self.actionQuit.setObjectName("actionQuit")
        self.actionReload = QtWidgets.QAction(PSBuilder)
        self.actionReload.setObjectName("actionReload")
        self.actionAbout = QtWidgets.QAction(PSBuilder)
        self.actionAbout.setObjectName("actionAbout")
        self.actionGenerate = QtWidgets.QAction(PSBuilder)
        self.actionGenerate.setObjectName("actionGenerate")
        self.actionAa = QtWidgets.QAction(PSBuilder)
        self.actionAa.setObjectName("actionAa")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuOpen_recent.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport_Drawpd)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuTools.addAction(self.actionReload)
        self.menuTools.addAction(self.actionGenerate)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(PSBuilder)
        self.tabMain.setCurrentIndex(0)
        self.tabOutput.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PSBuilder)
        PSBuilder.setTabOrder(self.phaseview, self.outview)
        PSBuilder.setTabOrder(self.outview, self.pushCalcTatP)
        PSBuilder.setTabOrder(self.pushCalcTatP, self.pushCalcPatT)
        PSBuilder.setTabOrder(self.pushCalcPatT, self.tabMain)
        PSBuilder.setTabOrder(self.tabMain, self.tabOutput)
        PSBuilder.setTabOrder(self.tabOutput, self.textOutput)
        PSBuilder.setTabOrder(self.textOutput, self.textFullOutput)
        PSBuilder.setTabOrder(self.textFullOutput, self.tminEdit)
        PSBuilder.setTabOrder(self.tminEdit, self.tmaxEdit)
        PSBuilder.setTabOrder(self.tmaxEdit, self.pminEdit)
        PSBuilder.setTabOrder(self.pminEdit, self.pmaxEdit)
        PSBuilder.setTabOrder(self.pmaxEdit, self.pushFromAxes)
        PSBuilder.setTabOrder(self.pushFromAxes, self.pushResetSettings)
        PSBuilder.setTabOrder(self.pushResetSettings, self.spinSteps)
        PSBuilder.setTabOrder(self.spinSteps, self.spinPrec)
        PSBuilder.setTabOrder(self.spinPrec, self.checkLabelInv)
        PSBuilder.setTabOrder(self.checkLabelInv, self.checkLabelUni)
        PSBuilder.setTabOrder(self.checkLabelUni, self.spinAlpha)
        PSBuilder.setTabOrder(self.spinAlpha, self.checkLabels)
        PSBuilder.setTabOrder(self.checkLabels, self.tcexeEdit)
        PSBuilder.setTabOrder(self.tcexeEdit, self.drawpdexeEdit)
        PSBuilder.setTabOrder(self.drawpdexeEdit, self.pushApplySettings)
        PSBuilder.setTabOrder(self.pushApplySettings, self.outScript)
        PSBuilder.setTabOrder(self.outScript, self.pushReadScript)
        PSBuilder.setTabOrder(self.pushReadScript, self.pushSaveScript)
        PSBuilder.setTabOrder(self.pushSaveScript, self.logText)
        PSBuilder.setTabOrder(self.logText, self.uniview)
        PSBuilder.setTabOrder(self.uniview, self.pushGuessUni)
        PSBuilder.setTabOrder(self.pushGuessUni, self.pushUniRemove)
        PSBuilder.setTabOrder(self.pushUniRemove, self.pushUniAdd)
        PSBuilder.setTabOrder(self.pushUniAdd, self.invview)
        PSBuilder.setTabOrder(self.invview, self.pushGuessInv)
        PSBuilder.setTabOrder(self.pushGuessInv, self.pushInvRemove)
        PSBuilder.setTabOrder(self.pushInvRemove, self.pushInvAdd)

    def retranslateUi(self, PSBuilder):
        _translate = QtCore.QCoreApplication.translate
        PSBuilder.setWindowTitle(_translate("PSBuilder", "PS Builder"))
        self.groupBox_3.setTitle(_translate("PSBuilder", "Phases"))
        self.pushCalcTatP.setText(_translate("PSBuilder", "Calc T"))
        self.pushCalcPatT.setText(_translate("PSBuilder", "Calc P"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabPlot), _translate("PSBuilder", "P-T Pseudosection"))
        self.groupBox.setTitle(_translate("PSBuilder", "Default PT range for calculations"))
        self.label_6.setText(_translate("PSBuilder", "T max:"))
        self.label_7.setText(_translate("PSBuilder", "p min:"))
        self.label_8.setText(_translate("PSBuilder", "p max:"))
        self.label_5.setText(_translate("PSBuilder", "T min:"))
        self.pushFromAxes.setText(_translate("PSBuilder", "From axes"))
        self.pushResetSettings.setText(_translate("PSBuilder", "Reset"))
        self.groupBox_2.setTitle(_translate("PSBuilder", "Other settings"))
        self.label.setText(_translate("PSBuilder", "P-T range values precision"))
        self.checkLabelInv.setText(_translate("PSBuilder", "Label invariant points"))
        self.checkLabelUni.setText(_translate("PSBuilder", "Label univariant lines"))
        self.label_2.setText(_translate("PSBuilder", "Labels alpha"))
        self.checkLabels.setText(_translate("PSBuilder", "Use names instead numbers for labels"))
        self.label_9.setText(_translate("PSBuilder", "Number of calculation steps:"))
        self.groupBox_4.setTitle(_translate("PSBuilder", "Programs settings"))
        self.label_4.setText(_translate("PSBuilder", "Drawpd executable:"))
        self.label_3.setText(_translate("PSBuilder", "THERMOCALC executable:"))
        self.pushApplySettings.setText(_translate("PSBuilder", "Apply"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabSettings), _translate("PSBuilder", "Settings"))
        self.pushReadScript.setText(_translate("PSBuilder", "Read"))
        self.pushSaveScript.setText(_translate("PSBuilder", "Save"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabScript), _translate("PSBuilder", "Script file"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabLog), _translate("PSBuilder", "TC-Log"))
        self.tabOutput.setTabText(self.tabOutput.indexOf(self.tab), _translate("PSBuilder", "Modes"))
        self.tabOutput.setTabText(self.tabOutput.indexOf(self.tab_2), _translate("PSBuilder", "Full output"))
        self.groupBox_5.setTitle(_translate("PSBuilder", "Univariant lines"))
        self.pushGuessUni.setText(_translate("PSBuilder", "Copy guess"))
        self.pushUniRemove.setText(_translate("PSBuilder", "Remove"))
        self.pushUniAdd.setText(_translate("PSBuilder", "Add"))
        self.groupBox_6.setTitle(_translate("PSBuilder", "Invariant points"))
        self.pushGuessInv.setText(_translate("PSBuilder", "Copy guess"))
        self.pushInvRemove.setText(_translate("PSBuilder", "Remove"))
        self.pushInvAdd.setText(_translate("PSBuilder", "Add"))
        self.menuFile.setTitle(_translate("PSBuilder", "&File"))
        self.menuOpen_recent.setTitle(_translate("PSBuilder", "Open &recent"))
        self.menuTools.setTitle(_translate("PSBuilder", "&Tools"))
        self.menuHelp.setTitle(_translate("PSBuilder", "&Help"))
        self.actionNew.setText(_translate("PSBuilder", "&New project"))
        self.actionNew.setToolTip(_translate("PSBuilder", "Create new project"))
        self.actionOpen.setText(_translate("PSBuilder", "&Open project"))
        self.actionOpen.setToolTip(_translate("PSBuilder", "Open project"))
        self.actionSave.setText(_translate("PSBuilder", "&Save project"))
        self.actionSave.setToolTip(_translate("PSBuilder", "Save project"))
        self.actionExport_Drawpd.setText(_translate("PSBuilder", "&Export Drawpd file"))
        self.actionExport_Drawpd.setToolTip(_translate("PSBuilder", "Export Drawpd file"))
        self.actionQuit.setText(_translate("PSBuilder", "&Quit"))
        self.actionReload.setText(_translate("PSBuilder", "&Reload scriptfile"))
        self.actionAbout.setText(_translate("PSBuilder", "&About"))
        self.actionGenerate.setText(_translate("PSBuilder", "&Generate from text file"))
        self.actionAa.setText(_translate("PSBuilder", "aa"))

