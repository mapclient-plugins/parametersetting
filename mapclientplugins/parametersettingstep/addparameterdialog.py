

from PySide2 import QtWidgets
from mapclientplugins.parametersettingstep.ui_addparameterdialog import Ui_AddParameterDialog


class AddParameterDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_AddParameterDialog()
        self._ui.setupUi(self)

    def getLabel(self):
        return self._ui.lineEditLabel.text()

    def getValue(self):
        return self._ui.lineEditValue.text()
