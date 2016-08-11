# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\addparameterdialog.ui'
#
# Created: Tue Aug  9 14:25:48 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AddParameterDialog(object):
    def setupUi(self, AddParameterDialog):
        AddParameterDialog.setObjectName("AddParameterDialog")
        AddParameterDialog.resize(452, 189)
        self.verticalLayout = QtGui.QVBoxLayout(AddParameterDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(AddParameterDialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEditLabel = QtGui.QLineEdit(self.groupBox)
        self.lineEditLabel.setObjectName("lineEditLabel")
        self.gridLayout.addWidget(self.lineEditLabel, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEditValue = QtGui.QLineEdit(self.groupBox)
        self.lineEditValue.setObjectName("lineEditValue")
        self.gridLayout.addWidget(self.lineEditValue, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(AddParameterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddParameterDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AddParameterDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AddParameterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddParameterDialog)

    def retranslateUi(self, AddParameterDialog):
        AddParameterDialog.setWindowTitle(QtGui.QApplication.translate("AddParameterDialog", "Add Parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddParameterDialog", "Add a new parameter with the label and value specified here. Note that  a colon will be added to the label automatically:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddParameterDialog", "Parameter label:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddParameterDialog", "Parameter value:", None, QtGui.QApplication.UnicodeUTF8))

