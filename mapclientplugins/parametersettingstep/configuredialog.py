from PySide2 import QtGui, QtWidgets

from mapclientplugins.parametersettingstep.addparameterdialog import AddParameterDialog
from mapclientplugins.parametersettingstep.ui_configuredialog import Ui_ConfigureDialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None
        self._parameters = {}

        self._makeConnections()

    def _makeConnections(self):
        self._ui.lineEdit0.textChanged.connect(self.validate)
        self._ui.pushButtonAdd.clicked.connect(self._addClicked)

    def _addClicked(self):
        dlg = AddParameterDialog(self)
        if dlg.exec_() and dlg.getLabel():
            self._addParameter(dlg.getLabel(), dlg.getValue())

    def _removeClicked(self):
        b = self.sender()
        if b in self._parameters:
            l = self._parameters[b]
            while l.count():
                item = l.takeAt(0)
                w = item.widget()
                if item.widget():
                    w.hide()
                    w.deleteLater()

            del self._parameters[b]
            l.deleteLater()

    def _addParameter(self, label, value=None):
        layout = self._ui.groupBoxParameters.layout()

        l, b = createParameter(label, value, self._ui.groupBoxParameters)
        layout.insertLayout(layout.count() - 1, l)
        b.clicked.connect(self._removeClicked)
        self._parameters[b] = l

    def accept(self):
        """
        Override the accept method so that we can confirm saving an
        invalid configuration.
        """
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(self, 'Invalid Configuration',
                                                   'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        """
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the
        overall validity of the configuration.
        """
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEdit0.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEdit0.text())
        if valid:
            self._ui.lineEdit0.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.lineEdit0.setStyleSheet(INVALID_STYLE_SHEET)

        return valid

    def getConfig(self):
        '''
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = self._ui.lineEdit0.text()
        config = {}
        config['identifier'] = self._ui.lineEdit0.text()
        layout = self._ui.groupBoxParameters.layout()
        kids = layout.children()
        for i, k in enumerate(kids):
            label = k.itemAt(0).widget()
            value = k.itemAt(1).widget()
            label_text = label.text()[:-1]
            config[str(i)] = [label_text, value.text()]

        return config

    def setConfig(self, config):
        """
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = config['identifier']
        self._ui.lineEdit0.setText(config['identifier'])

        parameters = []
        for key in config:
            if key != 'identifier':
                values = config[key]
                try:
                    index = int(key)
                    len_parameters = len(parameters)
                    if index >= len_parameters:
                        parameters.extend([None] * (index - len_parameters + 1))

                    parameters[index] = values

                except ValueError as e:
                    pass

        assert (None not in parameters)
        for p in parameters:
            self._addParameter(p[0], p[1])


def createParameter(label, value, parent):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/parametersettingstep/images/red_cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    pushButton = QtWidgets.QPushButton(parent)
    pushButton.setIcon(icon)
    label = QtWidgets.QLabel(label + ":", parent)
    lineEdit = QtWidgets.QLineEdit(parent)
    if value:
        lineEdit.setText(value)

    layout = QtWidgets.QHBoxLayout()
    layout.addWidget(label)
    layout.addWidget(lineEdit)
    layout.addWidget(pushButton)

    return layout, pushButton


def extractParameters(config):
    """
    Extract only the parameters from the configuration.

    :param config: dict of the complete configuration
    :return: dict of just the parameters.
    """
    parameters = {}
    for key in config:
        if key != 'identifier':
            values = config[key]
            parameters[values[0]] = values[1]

    return parameters
