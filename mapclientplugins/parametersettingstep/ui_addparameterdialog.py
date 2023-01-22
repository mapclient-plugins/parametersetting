# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addparameterdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddParameterDialog(object):
    def setupUi(self, AddParameterDialog):
        if not AddParameterDialog.objectName():
            AddParameterDialog.setObjectName(u"AddParameterDialog")
        AddParameterDialog.resize(452, 189)
        self.verticalLayout = QVBoxLayout(AddParameterDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(AddParameterDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3.setWordWrap(True)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.lineEditLabel = QLineEdit(self.groupBox)
        self.lineEditLabel.setObjectName(u"lineEditLabel")

        self.gridLayout.addWidget(self.lineEditLabel, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEditValue = QLineEdit(self.groupBox)
        self.lineEditValue.setObjectName(u"lineEditValue")

        self.gridLayout.addWidget(self.lineEditValue, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.buttonBox = QDialogButtonBox(AddParameterDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AddParameterDialog)
        self.buttonBox.accepted.connect(AddParameterDialog.accept)
        self.buttonBox.rejected.connect(AddParameterDialog.reject)

        QMetaObject.connectSlotsByName(AddParameterDialog)
    # setupUi

    def retranslateUi(self, AddParameterDialog):
        AddParameterDialog.setWindowTitle(QCoreApplication.translate("AddParameterDialog", u"Add Parameter", None))
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("AddParameterDialog", u"Add a new parameter with the label and value specified here. Note that  a colon will be added to the label automatically for visual effect only:", None))
        self.label.setText(QCoreApplication.translate("AddParameterDialog", u"Parameter label:", None))
        self.label_2.setText(QCoreApplication.translate("AddParameterDialog", u"Parameter value:", None))
    # retranslateUi

