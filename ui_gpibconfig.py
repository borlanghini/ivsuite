# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gpib_config.ui'
#
# Created: Thu Oct 30 14:30:07 2014
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

class Ui_GpibConfigDialog(object):
    def setupUi(self, GpibConfigDialog):
        GpibConfigDialog.setObjectName(_fromUtf8("GpibConfigDialog"))
        GpibConfigDialog.resize(378, 263)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(GpibConfigDialog)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(GpibConfigDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.GpibSpinBox = QtGui.QSpinBox(GpibConfigDialog)
        self.GpibSpinBox.setObjectName(_fromUtf8("GpibSpinBox"))
        self.horizontalLayout.addWidget(self.GpibSpinBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.talkGpibPushButton = QtGui.QPushButton(GpibConfigDialog)
        self.talkGpibPushButton.setObjectName(_fromUtf8("talkGpibPushButton"))
        self.horizontalLayout_2.addWidget(self.talkGpibPushButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.ResponseGpibTextEdit = QtGui.QTextEdit(GpibConfigDialog)
        self.ResponseGpibTextEdit.setObjectName(_fromUtf8("ResponseGpibTextEdit"))
        self.gridLayout.addWidget(self.ResponseGpibTextEdit, 2, 0, 1, 1)
        self.GpibButtonBox = QtGui.QDialogButtonBox(GpibConfigDialog)
        self.GpibButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.GpibButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.GpibButtonBox.setObjectName(_fromUtf8("GpibButtonBox"))
        self.gridLayout.addWidget(self.GpibButtonBox, 3, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.retranslateUi(GpibConfigDialog)
        QtCore.QObject.connect(self.GpibButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GpibConfigDialog.accept)
        QtCore.QObject.connect(self.GpibButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GpibConfigDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GpibConfigDialog)

    def retranslateUi(self, GpibConfigDialog):
        GpibConfigDialog.setWindowTitle(_translate("GpibConfigDialog", "Dialog", None))
        self.label.setText(_translate("GpibConfigDialog", "Keithley 2400 GPIB Address", None))
        self.talkGpibPushButton.setText(_translate("GpibConfigDialog", "Talk to the instrument", None))

