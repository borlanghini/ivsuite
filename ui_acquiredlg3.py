# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acquire3dlg.ui'
#
# Created: Wed Nov 19 17:49:51 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_IVMainWindow(object):
    def setupUi(self, IVMainWindow):
        IVMainWindow.setObjectName(_fromUtf8("IVMainWindow"))
        IVMainWindow.resize(700, 680)
        IVMainWindow.setMinimumSize(QtCore.QSize(700, 680))
        self.centralwidget = QtGui.QWidget(IVMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.IVtabWidget = QtGui.QTabWidget(self.centralwidget)
        self.IVtabWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.IVtabWidget.setObjectName(_fromUtf8("IVtabWidget"))
        self.MeasParamtab = QtGui.QWidget()
        self.MeasParamtab.setObjectName(_fromUtf8("MeasParamtab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.MeasParamtab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.MeasParamtab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_3 = QtGui.QLabel(self.MeasParamtab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_10.addWidget(self.label_3, QtCore.Qt.AlignHCenter)
        self.nameLineEdit = QtGui.QLineEdit(self.MeasParamtab)
        self.nameLineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.nameLineEdit.setObjectName(_fromUtf8("nameLineEdit"))
        self.horizontalLayout_10.addWidget(self.nameLineEdit, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.addDatecheckBox = QtGui.QCheckBox(self.MeasParamtab)
        self.addDatecheckBox.setObjectName(_fromUtf8("addDatecheckBox"))
        self.horizontalLayout_11.addWidget(self.addDatecheckBox, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.horizontalLayout_11, 1, 0, 1, 3)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_4 = QtGui.QLabel(self.MeasParamtab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_9.addWidget(self.label_4, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.areaSpinBox = QtGui.QDoubleSpinBox(self.MeasParamtab)
        self.areaSpinBox.setMinimum(0.01)
        self.areaSpinBox.setObjectName(_fromUtf8("areaSpinBox"))
        self.horizontalLayout_9.addWidget(self.areaSpinBox, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.DetailspushButton = QtGui.QPushButton(self.MeasParamtab)
        self.DetailspushButton.setObjectName(_fromUtf8("DetailspushButton"))
        self.horizontalLayout_9.addWidget(self.DetailspushButton, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 2, 0, 1, 3)
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.label_9 = QtGui.QLabel(self.MeasParamtab)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_25.addWidget(self.label_9, QtCore.Qt.AlignHCenter)
        self.directoriescomboBox = QtGui.QComboBox(self.MeasParamtab)
        self.directoriescomboBox.setMinimumSize(QtCore.QSize(300, 0))
        self.directoriescomboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.directoriescomboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.directoriescomboBox.setObjectName(_fromUtf8("directoriescomboBox"))
        self.horizontalLayout_25.addWidget(self.directoriescomboBox, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.browseButton = QtGui.QPushButton(self.MeasParamtab)
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.horizontalLayout_25.addWidget(self.browseButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_25, 3, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem3)
        self.label_11 = QtGui.QLabel(self.MeasParamtab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setTextFormat(QtCore.Qt.RichText)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_15.addWidget(self.label_11)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.MeasTypelistWidget = QtGui.QListWidget(self.MeasParamtab)
        self.MeasTypelistWidget.setEnabled(True)
        self.MeasTypelistWidget.setMinimumSize(QtCore.QSize(125, 95))
        self.MeasTypelistWidget.setMaximumSize(QtCore.QSize(125, 95))
        self.MeasTypelistWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MeasTypelistWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MeasTypelistWidget.setObjectName(_fromUtf8("MeasTypelistWidget"))
        item = QtGui.QListWidgetItem()
        self.MeasTypelistWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.MeasTypelistWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.MeasTypelistWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.MeasTypelistWidget.addItem(item)
        self.horizontalLayout_12.addWidget(self.MeasTypelistWidget)
        self.MeasTypestackedWidget = QtGui.QStackedWidget(self.MeasParamtab)
        self.MeasTypestackedWidget.setEnabled(True)
        self.MeasTypestackedWidget.setMinimumSize(QtCore.QSize(270, 50))
        self.MeasTypestackedWidget.setMaximumSize(QtCore.QSize(270, 51))
        self.MeasTypestackedWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.MeasTypestackedWidget.setObjectName(_fromUtf8("MeasTypestackedWidget"))
        self.nothing = QtGui.QWidget()
        self.nothing.setObjectName(_fromUtf8("nothing"))
        self.MeasTypestackedWidget.addWidget(self.nothing)
        self.irradiation = QtGui.QWidget()
        self.irradiation.setObjectName(_fromUtf8("irradiation"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout(self.irradiation)
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_2 = QtGui.QLabel(self.irradiation)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_6.addWidget(self.label_2)
        self.IrradspinBox = QtGui.QSpinBox(self.irradiation)
        self.IrradspinBox.setMinimumSize(QtCore.QSize(0, 31))
        self.IrradspinBox.setMaximumSize(QtCore.QSize(16777215, 31))
        self.IrradspinBox.setMaximum(150)
        self.IrradspinBox.setProperty("value", 100)
        self.IrradspinBox.setObjectName(_fromUtf8("IrradspinBox"))
        self.horizontalLayout_6.addWidget(self.IrradspinBox)
        self.horizontalLayout_23.addLayout(self.horizontalLayout_6)
        self.MeasTypestackedWidget.addWidget(self.irradiation)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.VocNPointsspinBox = QtGui.QSpinBox(self.page_3)
        self.VocNPointsspinBox.setGeometry(QtCore.QRect(200, 10, 70, 33))
        self.VocNPointsspinBox.setMinimumSize(QtCore.QSize(70, 0))
        self.VocNPointsspinBox.setMinimum(1)
        self.VocNPointsspinBox.setMaximum(2500)
        self.VocNPointsspinBox.setProperty("value", 1000)
        self.VocNPointsspinBox.setObjectName(_fromUtf8("VocNPointsspinBox"))
        self.label_5 = QtGui.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(10, 16, 191, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.MeasTypestackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.label_6 = QtGui.QLabel(self.page_4)
        self.label_6.setGeometry(QtCore.QRect(20, 16, 161, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.minutesSpinBox = QtGui.QSpinBox(self.page_4)
        self.minutesSpinBox.setGeometry(QtCore.QRect(180, 10, 70, 33))
        self.minutesSpinBox.setMinimumSize(QtCore.QSize(70, 0))
        self.minutesSpinBox.setMinimum(5)
        self.minutesSpinBox.setMaximum(300)
        self.minutesSpinBox.setProperty("value", 30)
        self.minutesSpinBox.setObjectName(_fromUtf8("minutesSpinBox"))
        self.MeasTypestackedWidget.addWidget(self.page_4)
        self.horizontalLayout_12.addWidget(self.MeasTypestackedWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.vmin = QtGui.QLabel(self.MeasParamtab)
        self.vmin.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.vmin.setObjectName(_fromUtf8("vmin"))
        self.horizontalLayout.addWidget(self.vmin, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.VminSpinBox = QtGui.QDoubleSpinBox(self.MeasParamtab)
        self.VminSpinBox.setDecimals(3)
        self.VminSpinBox.setMinimum(-20.0)
        self.VminSpinBox.setMaximum(20.0)
        self.VminSpinBox.setSingleStep(0.001)
        self.VminSpinBox.setProperty("value", -1.0)
        self.VminSpinBox.setObjectName(_fromUtf8("VminSpinBox"))
        self.horizontalLayout.addWidget(self.VminSpinBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label = QtGui.QLabel(self.MeasParamtab)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_8.addWidget(self.label, QtCore.Qt.AlignRight)
        self.currentLimitcomboBox = QtGui.QComboBox(self.MeasParamtab)
        self.currentLimitcomboBox.setObjectName(_fromUtf8("currentLimitcomboBox"))
        self.currentLimitcomboBox.addItem(_fromUtf8(""))
        self.currentLimitcomboBox.addItem(_fromUtf8(""))
        self.currentLimitcomboBox.addItem(_fromUtf8(""))
        self.currentLimitcomboBox.addItem(_fromUtf8(""))
        self.currentLimitcomboBox.addItem(_fromUtf8(""))
        self.currentLimitcomboBox.addItem(_fromUtf8(""))
        self.currentLimitcomboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.currentLimitcomboBox)
        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.vmax = QtGui.QLabel(self.MeasParamtab)
        self.vmax.setObjectName(_fromUtf8("vmax"))
        self.horizontalLayout_2.addWidget(self.vmax, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.VmaxSpinBox = QtGui.QDoubleSpinBox(self.MeasParamtab)
        self.VmaxSpinBox.setDecimals(3)
        self.VmaxSpinBox.setMinimum(-20.0)
        self.VmaxSpinBox.setMaximum(20.0)
        self.VmaxSpinBox.setSingleStep(0.001)
        self.VmaxSpinBox.setProperty("value", 1.0)
        self.VmaxSpinBox.setObjectName(_fromUtf8("VmaxSpinBox"))
        self.horizontalLayout_2.addWidget(self.VmaxSpinBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.sweepstep = QtGui.QLabel(self.MeasParamtab)
        self.sweepstep.setObjectName(_fromUtf8("sweepstep"))
        self.horizontalLayout_4.addWidget(self.sweepstep, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.sweepStepSpinBox = QtGui.QDoubleSpinBox(self.MeasParamtab)
        self.sweepStepSpinBox.setMaximum(21.0)
        self.sweepStepSpinBox.setSingleStep(0.01)
        self.sweepStepSpinBox.setProperty("value", 0.01)
        self.sweepStepSpinBox.setObjectName(_fromUtf8("sweepStepSpinBox"))
        self.horizontalLayout_4.addWidget(self.sweepStepSpinBox)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_27 = QtGui.QHBoxLayout()
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        self.SweepTypelistWidget = QtGui.QListWidget(self.MeasParamtab)
        self.SweepTypelistWidget.setMinimumSize(QtCore.QSize(140, 51))
        self.SweepTypelistWidget.setMaximumSize(QtCore.QSize(140, 51))
        self.SweepTypelistWidget.setObjectName(_fromUtf8("SweepTypelistWidget"))
        item = QtGui.QListWidgetItem()
        self.SweepTypelistWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.SweepTypelistWidget.addItem(item)
        self.horizontalLayout_27.addWidget(self.SweepTypelistWidget)
        self.SweepstackedWidget = QtGui.QStackedWidget(self.MeasParamtab)
        self.SweepstackedWidget.setMinimumSize(QtCore.QSize(271, 111))
        self.SweepstackedWidget.setMaximumSize(QtCore.QSize(271, 111))
        self.SweepstackedWidget.setFrameShape(QtGui.QFrame.Box)
        self.SweepstackedWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.SweepstackedWidget.setObjectName(_fromUtf8("SweepstackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.layoutWidget_3 = QtGui.QWidget(self.page)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 30, 183, 35))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.sweepdel = QtGui.QLabel(self.layoutWidget_3)
        self.sweepdel.setObjectName(_fromUtf8("sweepdel"))
        self.horizontalLayout_3.addWidget(self.sweepdel)
        self.sweepDelSpinBox = QtGui.QDoubleSpinBox(self.layoutWidget_3)
        self.sweepDelSpinBox.setSingleStep(0.01)
        self.sweepDelSpinBox.setProperty("value", 0.01)
        self.sweepDelSpinBox.setObjectName(_fromUtf8("sweepDelSpinBox"))
        self.horizontalLayout_3.addWidget(self.sweepDelSpinBox)
        self.SweepstackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.layoutWidget = QtGui.QWidget(self.page_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 251, 110))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ZerocheckBox = QtGui.QCheckBox(self.layoutWidget)
        self.ZerocheckBox.setObjectName(_fromUtf8("ZerocheckBox"))
        self.verticalLayout.addWidget(self.ZerocheckBox)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.Forwardsweepdel = QtGui.QLabel(self.layoutWidget)
        self.Forwardsweepdel.setObjectName(_fromUtf8("Forwardsweepdel"))
        self.horizontalLayout_5.addWidget(self.Forwardsweepdel)
        self.ForwardsweepDelSpinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.ForwardsweepDelSpinBox.setSingleStep(0.01)
        self.ForwardsweepDelSpinBox.setProperty("value", 0.01)
        self.ForwardsweepDelSpinBox.setObjectName(_fromUtf8("ForwardsweepDelSpinBox"))
        self.horizontalLayout_5.addWidget(self.ForwardsweepDelSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.Backwardsweepdel = QtGui.QLabel(self.layoutWidget)
        self.Backwardsweepdel.setObjectName(_fromUtf8("Backwardsweepdel"))
        self.horizontalLayout_7.addWidget(self.Backwardsweepdel)
        self.BackwardsweepDelSpinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.BackwardsweepDelSpinBox.setSingleStep(0.01)
        self.BackwardsweepDelSpinBox.setProperty("value", 0.01)
        self.BackwardsweepDelSpinBox.setObjectName(_fromUtf8("BackwardsweepDelSpinBox"))
        self.horizontalLayout_7.addWidget(self.BackwardsweepDelSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.SweepstackedWidget.addWidget(self.page_2)
        self.horizontalLayout_27.addWidget(self.SweepstackedWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.closeButton = QtGui.QPushButton(self.MeasParamtab)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout_13.addWidget(self.closeButton)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.measureButton = QtGui.QPushButton(self.MeasParamtab)
        self.measureButton.setObjectName(_fromUtf8("measureButton"))
        self.horizontalLayout_13.addWidget(self.measureButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.line = QtGui.QFrame(self.MeasParamtab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_4.addWidget(self.line)
        self.IVtabWidget.addTab(self.MeasParamtab, _fromUtf8(""))
        self.Resultstab = QtGui.QWidget()
        self.Resultstab.setObjectName(_fromUtf8("Resultstab"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.Resultstab)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.ivplot = QtGui.QVBoxLayout()
        self.ivplot.setObjectName(_fromUtf8("ivplot"))
        self.horizontalLayout_14.addLayout(self.ivplot)
        self.IVtabWidget.addTab(self.Resultstab, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.IVtabWidget)
        IVMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(IVMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuPreferences = QtGui.QMenu(self.menubar)
        self.menuPreferences.setObjectName(_fromUtf8("menuPreferences"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        IVMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(IVMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        IVMainWindow.setStatusBar(self.statusbar)
        self.actionProgram_Help = QtGui.QAction(IVMainWindow)
        self.actionProgram_Help.setObjectName(_fromUtf8("actionProgram_Help"))
        self.actionAbout_I_V = QtGui.QAction(IVMainWindow)
        self.actionAbout_I_V.setObjectName(_fromUtf8("actionAbout_I_V"))
        self.actionConfigure = QtGui.QAction(IVMainWindow)
        self.actionConfigure.setObjectName(_fromUtf8("actionConfigure"))
        self.menuPreferences.addAction(self.actionConfigure)
        self.menuHelp.addAction(self.actionProgram_Help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_I_V)
        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.label_3.setBuddy(self.nameLineEdit)
        self.label_4.setBuddy(self.areaSpinBox)
        self.label_9.setBuddy(self.browseButton)
        self.label_2.setBuddy(self.IrradspinBox)
        self.vmin.setBuddy(self.VminSpinBox)
        self.label.setBuddy(self.currentLimitcomboBox)
        self.vmax.setBuddy(self.VmaxSpinBox)
        self.sweepstep.setBuddy(self.sweepStepSpinBox)
        self.sweepdel.setBuddy(self.sweepDelSpinBox)
        self.Forwardsweepdel.setBuddy(self.sweepDelSpinBox)
        self.Backwardsweepdel.setBuddy(self.sweepDelSpinBox)

        self.retranslateUi(IVMainWindow)
        self.IVtabWidget.setCurrentIndex(0)
        self.MeasTypelistWidget.setCurrentRow(0)
        self.MeasTypestackedWidget.setCurrentIndex(0)
        self.currentLimitcomboBox.setCurrentIndex(4)
        self.SweepTypelistWidget.setCurrentRow(0)
        self.SweepstackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.SweepTypelistWidget, QtCore.SIGNAL(_fromUtf8("currentRowChanged(int)")), self.SweepstackedWidget.setCurrentIndex)
        QtCore.QObject.connect(self.MeasTypelistWidget, QtCore.SIGNAL(_fromUtf8("currentRowChanged(int)")), self.MeasTypestackedWidget.setCurrentIndex)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), IVMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(IVMainWindow)

    def retranslateUi(self, IVMainWindow):
        IVMainWindow.setWindowTitle(_translate("IVMainWindow", "I-V Characterization", None))
        self.label_10.setText(_translate("IVMainWindow", "Sample data", None))
        self.label_3.setText(_translate("IVMainWindow", "Sample name", None))
        self.addDatecheckBox.setText(_translate("IVMainWindow", "Add date and time to filename", None))
        self.label_4.setText(_translate("IVMainWindow", "Sample Area(cm^2)", None))
        self.DetailspushButton.setText(_translate("IVMainWindow", "Add extra sample details", None))
        self.label_9.setText(_translate("IVMainWindow", "Save results in directory...", None))
        self.browseButton.setText(_translate("IVMainWindow", "Browse", None))
        self.label_11.setText(_translate("IVMainWindow", "Measurement  parameters", None))
        __sortingEnabled = self.MeasTypelistWidget.isSortingEnabled()
        self.MeasTypelistWidget.setSortingEnabled(False)
        item = self.MeasTypelistWidget.item(0)
        item.setText(_translate("IVMainWindow", "Dark IV", None))
        item = self.MeasTypelistWidget.item(1)
        item.setText(_translate("IVMainWindow", "Illuminated IV", None))
        item = self.MeasTypelistWidget.item(2)
        item.setText(_translate("IVMainWindow", "Voc photodecay", None))
        item = self.MeasTypelistWidget.item(3)
        item.setText(_translate("IVMainWindow", "Jsc stability", None))
        self.MeasTypelistWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("IVMainWindow", "Irradiation (mW/cm2)", None))
        self.label_5.setText(_translate("IVMainWindow", "Number of points(max 2500)", None))
        self.label_6.setText(_translate("IVMainWindow", "Measurement time(min)", None))
        self.vmin.setText(_translate("IVMainWindow", "Volt Minimum (V)", None))
        self.label.setText(_translate("IVMainWindow", "Current limit", None))
        self.currentLimitcomboBox.setItemText(0, _translate("IVMainWindow", "1.05 uA", None))
        self.currentLimitcomboBox.setItemText(1, _translate("IVMainWindow", "10.5 uA", None))
        self.currentLimitcomboBox.setItemText(2, _translate("IVMainWindow", "105 uA", None))
        self.currentLimitcomboBox.setItemText(3, _translate("IVMainWindow", "1.05 mA", None))
        self.currentLimitcomboBox.setItemText(4, _translate("IVMainWindow", "21 mA", None))
        self.currentLimitcomboBox.setItemText(5, _translate("IVMainWindow", "105 mA", None))
        self.currentLimitcomboBox.setItemText(6, _translate("IVMainWindow", "1.05 A", None))
        self.vmax.setText(_translate("IVMainWindow", "Volt Maximum (V)", None))
        self.sweepstep.setText(_translate("IVMainWindow", "Voltage Step (V)", None))
        __sortingEnabled = self.SweepTypelistWidget.isSortingEnabled()
        self.SweepTypelistWidget.setSortingEnabled(False)
        item = self.SweepTypelistWidget.item(0)
        item.setText(_translate("IVMainWindow", "Simple Sweep", None))
        item = self.SweepTypelistWidget.item(1)
        item.setText(_translate("IVMainWindow", "Hysteresis Sweep", None))
        self.SweepTypelistWidget.setSortingEnabled(__sortingEnabled)
        self.sweepdel.setText(_translate("IVMainWindow", "Sweep Delay (s)", None))
        self.ZerocheckBox.setText(_translate("IVMainWindow", "Start from zero?", None))
        self.Forwardsweepdel.setText(_translate("IVMainWindow", "Forward Sweep Delay (s)", None))
        self.Backwardsweepdel.setText(_translate("IVMainWindow", "Backward Sweep Delay (s)", None))
        self.closeButton.setText(_translate("IVMainWindow", "Close", None))
        self.measureButton.setText(_translate("IVMainWindow", "Measure", None))
        self.IVtabWidget.setTabText(self.IVtabWidget.indexOf(self.MeasParamtab), _translate("IVMainWindow", "Measurement Parameters", None))
        self.IVtabWidget.setTabText(self.IVtabWidget.indexOf(self.Resultstab), _translate("IVMainWindow", "Results", None))
        self.menuPreferences.setTitle(_translate("IVMainWindow", "Tools", None))
        self.menuHelp.setTitle(_translate("IVMainWindow", "Help", None))
        self.actionProgram_Help.setText(_translate("IVMainWindow", "Program Help", None))
        self.actionAbout_I_V.setText(_translate("IVMainWindow", "About this program", None))
        self.actionConfigure.setText(_translate("IVMainWindow", "Preferences", None))

