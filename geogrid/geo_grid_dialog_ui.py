# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geo_grid_dialog_base_en.ui'
#
# Created: Tue Feb 16 14:33:07 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from qgis import gui


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

class Ui_geogridDialogBase(object):
    def setupUi(self, geogridDialogBase):
        geogridDialogBase.setObjectName(_fromUtf8("geogridDialogBase"))
        geogridDialogBase.resize(420, 567)
        geogridDialogBase.setMinimumSize(QtCore.QSize(420, 567))
        geogridDialogBase.setWindowTitle(_fromUtf8("Geo Grid"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geogrid/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        geogridDialogBase.setWindowIcon(icon)
        geogridDialogBase.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout = QtGui.QVBoxLayout(geogridDialogBase)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(geogridDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(402, 180))
        self.frame.setAutoFillBackground(False)
        self.frame.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(3)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.lat_min_d = QtGui.QLineEdit(self.frame)
        self.lat_min_d.setGeometry(QtCore.QRect(70, 125, 61, 19))
        self.lat_min_d.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lat_min_d.setInputMask(_fromUtf8(""))
        self.lat_min_d.setPlaceholderText(_fromUtf8(""))
        self.lat_min_d.setObjectName(_fromUtf8("lat_min_d"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(9, 125, 51, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lat_min_m = QtGui.QLineEdit(self.frame)
        self.lat_min_m.setGeometry(QtCore.QRect(134, 125, 81, 20))
        self.lat_min_m.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lat_min_m.setInputMask(_fromUtf8(""))
        self.lat_min_m.setPlaceholderText(_fromUtf8(""))
        self.lat_min_m.setObjectName(_fromUtf8("lat_min_m"))
        self.lat_max_d = QtGui.QLineEdit(self.frame)
        self.lat_max_d.setGeometry(QtCore.QRect(220, 125, 61, 20))
        self.lat_max_d.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lat_max_d.setInputMask(_fromUtf8(""))
        self.lat_max_d.setPlaceholderText(_fromUtf8(""))
        self.lat_max_d.setObjectName(_fromUtf8("lat_max_d"))
        self.lat_max_m = QtGui.QLineEdit(self.frame)
        self.lat_max_m.setGeometry(QtCore.QRect(286, 125, 91, 20))
        self.lat_max_m.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lat_max_m.setInputMask(_fromUtf8(""))
        self.lat_max_m.setPlaceholderText(_fromUtf8(""))
        self.lat_max_m.setObjectName(_fromUtf8("lat_max_m"))
        self.lon_min_m = QtGui.QLineEdit(self.frame)
        self.lon_min_m.setGeometry(QtCore.QRect(134, 150, 81, 20))
        self.lon_min_m.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lon_min_m.setInputMask(_fromUtf8(""))
        self.lon_min_m.setPlaceholderText(_fromUtf8(""))
        self.lon_min_m.setObjectName(_fromUtf8("lon_min_m"))
        self.lon_min_d = QtGui.QLineEdit(self.frame)
        self.lon_min_d.setGeometry(QtCore.QRect(70, 150, 61, 19))
        self.lon_min_d.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lon_min_d.setInputMask(_fromUtf8(""))
        self.lon_min_d.setPlaceholderText(_fromUtf8(""))
        self.lon_min_d.setObjectName(_fromUtf8("lon_min_d"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(9, 150, 51, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lon_max_d = QtGui.QLineEdit(self.frame)
        self.lon_max_d.setGeometry(QtCore.QRect(221, 150, 61, 19))
        self.lon_max_d.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lon_max_d.setInputMask(_fromUtf8(""))
        self.lon_max_d.setPlaceholderText(_fromUtf8(""))
        self.lon_max_d.setObjectName(_fromUtf8("lon_max_d"))
        self.lon_max_m = QtGui.QLineEdit(self.frame)
        self.lon_max_m.setGeometry(QtCore.QRect(286, 150, 91, 20))
        self.lon_max_m.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lon_max_m.setInputMask(_fromUtf8(""))
        self.lon_max_m.setPlaceholderText(_fromUtf8(""))
        self.lon_max_m.setObjectName(_fromUtf8("lon_max_m"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(69, 81, 40, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(220, 81, 44, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(90, 100, 87, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(240, 100, 91, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_16 = QtGui.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.btn_copy_minmax = QtGui.QPushButton(self.frame)
        self.btn_copy_minmax.setGeometry(QtCore.QRect(220, 40, 161, 31))
        self.btn_copy_minmax.setObjectName(_fromUtf8("btn_copy_minmax"))
        self.mMapLayerComboBox = gui.QgsMapLayerComboBox(self.frame)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(10, 40, 201, 31))
        self.mMapLayerComboBox.setObjectName(_fromUtf8("mMapLayerComboBox"))
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(geogridDialogBase)
        self.frame_2.setMinimumSize(QtCore.QSize(402, 110))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame_2.setFrameShape(QtGui.QFrame.Panel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setLineWidth(3)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.lat_step_d = QtGui.QLineEdit(self.frame_2)
        self.lat_step_d.setGeometry(QtCore.QRect(90, 50, 51, 20))
        self.lat_step_d.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lat_step_d.setInputMask(_fromUtf8(""))
        self.lat_step_d.setPlaceholderText(_fromUtf8(""))
        self.lat_step_d.setObjectName(_fromUtf8("lat_step_d"))
        self.label_7 = QtGui.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(30, 50, 51, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lat_step_m = QtGui.QLineEdit(self.frame_2)
        self.lat_step_m.setGeometry(QtCore.QRect(140, 50, 51, 20))
        self.lat_step_m.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lat_step_m.setInputMask(_fromUtf8(""))
        self.lat_step_m.setPlaceholderText(_fromUtf8(""))
        self.lat_step_m.setObjectName(_fromUtf8("lat_step_m"))
        self.lon_step_m = QtGui.QLineEdit(self.frame_2)
        self.lon_step_m.setGeometry(QtCore.QRect(140, 80, 51, 20))
        self.lon_step_m.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lon_step_m.setInputMask(_fromUtf8(""))
        self.lon_step_m.setPlaceholderText(_fromUtf8(""))
        self.lon_step_m.setObjectName(_fromUtf8("lon_step_m"))
        self.lon_step_d = QtGui.QLineEdit(self.frame_2)
        self.lon_step_d.setGeometry(QtCore.QRect(90, 80, 51, 20))
        self.lon_step_d.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lon_step_d.setInputMask(_fromUtf8(""))
        self.lon_step_d.setPlaceholderText(_fromUtf8(""))
        self.lon_step_d.setObjectName(_fromUtf8("lon_step_d"))
        self.label_8 = QtGui.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(30, 80, 51, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(100, 10, 91, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(240, 30, 141, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(100, 30, 101, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.spin_n_subgrd = QtGui.QSpinBox(self.frame_2)
        self.spin_n_subgrd.setGeometry(QtCore.QRect(270, 60, 41, 31))
        self.spin_n_subgrd.setMinimum(1)
        self.spin_n_subgrd.setMaximum(20)
        self.spin_n_subgrd.setProperty("value", 1)
        self.spin_n_subgrd.setObjectName(_fromUtf8("spin_n_subgrd"))
        self.label_15 = QtGui.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtGui.QFrame(geogridDialogBase)
        self.frame_3.setMinimumSize(QtCore.QSize(402, 110))
        self.frame_3.setFrameShape(QtGui.QFrame.Panel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setLineWidth(3)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.combo_n_brdminuts = QtGui.QComboBox(self.frame_3)
        self.combo_n_brdminuts.setGeometry(QtCore.QRect(300, 10, 69, 22))
        self.combo_n_brdminuts.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.combo_n_brdminuts.setObjectName(_fromUtf8("combo_n_brdminuts"))
        self.combo_n_brdminuts.addItem(_fromUtf8(""))
        self.combo_n_brdminuts.addItem(_fromUtf8(""))
        self.combo_n_brdminuts.addItem(_fromUtf8(""))
        self.combo_n_brdminuts.addItem(_fromUtf8(""))
        self.combo_n_brdminuts.addItem(_fromUtf8(""))
        self.combo_n_brdminuts.addItem(_fromUtf8(""))
        self.combo_n_brdminuts.addItem(_fromUtf8(""))
        self.combo_n_brdminuts.addItem(_fromUtf8(""))
        self.combo_n_brdminuts.addItem(_fromUtf8(""))
        self.combo_n_brdminuts.addItem(_fromUtf8(""))
        self.combo_n_brdminuts.addItem(_fromUtf8(""))
        self.combo_n_brdminuts.addItem(_fromUtf8(""))
        self.combo_n_brdminuts.addItem(_fromUtf8(""))
        self.combo_n_brdminuts.addItem(_fromUtf8(""))
        self.combo_n_brdminuts.addItem(_fromUtf8(""))
        self.combo_n_brdminuts.addItem(_fromUtf8(""))
        self.label_12 = QtGui.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(90, 10, 191, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.combo_n_brdtiks = QtGui.QComboBox(self.frame_3)
        self.combo_n_brdtiks.setGeometry(QtCore.QRect(300, 40, 69, 22))
        self.combo_n_brdtiks.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.combo_n_brdtiks.setObjectName(_fromUtf8("combo_n_brdtiks"))
        self.combo_n_brdtiks.addItem(_fromUtf8(""))
        self.combo_n_brdtiks.addItem(_fromUtf8(""))
        self.combo_n_brdtiks.addItem(_fromUtf8(""))
        self.combo_n_brdtiks.addItem(_fromUtf8(""))
        self.combo_n_brdtiks.addItem(_fromUtf8(""))
        self.combo_n_brdtiks.addItem(_fromUtf8(""))
        self.combo_n_brdtiks.addItem(_fromUtf8(""))
        self.combo_n_brdtiks.addItem(_fromUtf8(""))
        self.combo_n_brdtiks.addItem(_fromUtf8(""))
        self.combo_n_brdtiks.addItem(_fromUtf8(""))
        self.combo_n_brdtiks.addItem(_fromUtf8(""))
        self.combo_n_brdtiks.addItem(_fromUtf8(""))
        self.combo_n_brdtiks.addItem(_fromUtf8(""))
        self.combo_n_brdtiks.addItem(_fromUtf8(""))
        self.label_13 = QtGui.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(90, 40, 171, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.combo_n_lblminuts = QtGui.QComboBox(self.frame_3)
        self.combo_n_lblminuts.setGeometry(QtCore.QRect(300, 70, 69, 22))
        self.combo_n_lblminuts.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.combo_n_lblminuts.setObjectName(_fromUtf8("combo_n_lblminuts"))
        self.combo_n_lblminuts.addItem(_fromUtf8(""))
        self.combo_n_lblminuts.addItem(_fromUtf8(""))
        self.combo_n_lblminuts.addItem(_fromUtf8(""))
        self.combo_n_lblminuts.addItem(_fromUtf8(""))
        self.combo_n_lblminuts.addItem(_fromUtf8(""))
        self.combo_n_lblminuts.addItem(_fromUtf8(""))
        self.combo_n_lblminuts.addItem(_fromUtf8(""))
        self.combo_n_lblminuts.addItem(_fromUtf8(""))
        self.combo_n_lblminuts.addItem(_fromUtf8(""))
        self.combo_n_lblminuts.addItem(_fromUtf8(""))
        self.combo_n_lblminuts.addItem(_fromUtf8(""))
        self.combo_n_lblminuts.addItem(_fromUtf8(""))
        self.combo_n_lblminuts.addItem(_fromUtf8(""))
        self.combo_n_lblminuts.addItem(_fromUtf8(""))
        self.label_14 = QtGui.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(90, 70, 201, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_18 = QtGui.QLabel(self.frame_3)
        self.label_18.setGeometry(QtCore.QRect(10, 10, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout.addWidget(self.frame_3)
        self.Save_btn = QtGui.QToolButton(geogridDialogBase)
        self.Save_btn.setMinimumSize(QtCore.QSize(120, 25))
        self.Save_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.Save_btn.setObjectName(_fromUtf8("Save_btn"))
        self.verticalLayout.addWidget(self.Save_btn)
        self.Fname_lineEdit = QtGui.QLineEdit(geogridDialogBase)
        self.Fname_lineEdit.setObjectName(_fromUtf8("Fname_lineEdit"))
        self.verticalLayout.addWidget(self.Fname_lineEdit)
        self.add_layers = QtGui.QCheckBox(geogridDialogBase)
        self.add_layers.setChecked(True)
        self.add_layers.setObjectName(_fromUtf8("add_layers"))
        self.verticalLayout.addWidget(self.add_layers)
        self.button_box = QtGui.QDialogButtonBox(geogridDialogBase)
        self.button_box.setToolTip(_fromUtf8(""))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(geogridDialogBase)
        self.combo_n_lblminuts.setCurrentIndex(0)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), geogridDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), geogridDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(geogridDialogBase)

    def retranslateUi(self, geogridDialogBase):
        self.lat_min_d.setText(_translate("geogridDialogBase", "-10", None))
        self.label.setText(_translate("geogridDialogBase", "Latitude", None))
        self.lat_min_m.setText(_translate("geogridDialogBase", "0", None))
        self.lat_max_d.setText(_translate("geogridDialogBase", "10", None))
        self.lat_max_m.setText(_translate("geogridDialogBase", "0", None))
        self.lon_min_m.setText(_translate("geogridDialogBase", "0", None))
        self.lon_min_d.setText(_translate("geogridDialogBase", "-10", None))
        self.label_2.setText(_translate("geogridDialogBase", "Longitude", None))
        self.lon_max_d.setText(_translate("geogridDialogBase", "10", None))
        self.lon_max_m.setText(_translate("geogridDialogBase", "0", None))
        self.label_3.setText(_translate("geogridDialogBase", "Minimum", None))
        self.label_4.setText(_translate("geogridDialogBase", "Maximum", None))
        self.label_5.setText(_translate("geogridDialogBase", "degrees minutes", None))
        self.label_6.setText(_translate("geogridDialogBase", "degrees minutes", None))
        self.label_16.setText(_translate("geogridDialogBase", "COVERAGE", None))
        self.btn_copy_minmax.setText(_translate("geogridDialogBase", "Copy coverage", None))
        self.lat_step_d.setText(_translate("geogridDialogBase", "1", None))
        self.label_7.setText(_translate("geogridDialogBase", "Latitude", None))
        self.lat_step_m.setText(_translate("geogridDialogBase", "0", None))
        self.lon_step_m.setText(_translate("geogridDialogBase", "0", None))
        self.lon_step_d.setText(_translate("geogridDialogBase", "1", None))
        self.label_8.setText(_translate("geogridDialogBase", "Longitude", None))
        self.label_9.setText(_translate("geogridDialogBase", "Step grid space", None))
        self.label_10.setText(_translate("geogridDialogBase", "gridlines divided into parts", None))
        self.label_11.setText(_translate("geogridDialogBase", "degrees minutes", None))
        self.label_15.setText(_translate("geogridDialogBase", "GRID", None))
        self.combo_n_brdminuts.setItemText(0, _translate("geogridDialogBase", "1", None))
        self.combo_n_brdminuts.setItemText(1, _translate("geogridDialogBase", "2", None))
        self.combo_n_brdminuts.setItemText(2, _translate("geogridDialogBase", "3", None))
        self.combo_n_brdminuts.setItemText(3, _translate("geogridDialogBase", "4", None))
        self.combo_n_brdminuts.setItemText(4, _translate("geogridDialogBase", "5", None))
        self.combo_n_brdminuts.setItemText(5, _translate("geogridDialogBase", "6", None))
        self.combo_n_brdminuts.setItemText(6, _translate("geogridDialogBase", "10", None))
        self.combo_n_brdminuts.setItemText(7, _translate("geogridDialogBase", "15", None))
        self.combo_n_brdminuts.setItemText(8, _translate("geogridDialogBase", "20", None))
        self.combo_n_brdminuts.setItemText(9, _translate("geogridDialogBase", "30", None))
        self.combo_n_brdminuts.setItemText(10, _translate("geogridDialogBase", "60", None))
        self.combo_n_brdminuts.setItemText(11, _translate("geogridDialogBase", "120", None))
        self.combo_n_brdminuts.setItemText(12, _translate("geogridDialogBase", "180", None))
        self.combo_n_brdminuts.setItemText(13, _translate("geogridDialogBase", "240", None))
        self.combo_n_brdminuts.setItemText(14, _translate("geogridDialogBase", "300", None))
        self.combo_n_brdminuts.setItemText(15, _translate("geogridDialogBase", "600", None))
        self.label_12.setText(_translate("geogridDialogBase", "Border dividing Step (minutes)", None))
        self.combo_n_brdtiks.setItemText(0, _translate("geogridDialogBase", "1", None))
        self.combo_n_brdtiks.setItemText(1, _translate("geogridDialogBase", "2", None))
        self.combo_n_brdtiks.setItemText(2, _translate("geogridDialogBase", "3", None))
        self.combo_n_brdtiks.setItemText(3, _translate("geogridDialogBase", "5", None))
        self.combo_n_brdtiks.setItemText(4, _translate("geogridDialogBase", "6", None))
        self.combo_n_brdtiks.setItemText(5, _translate("geogridDialogBase", "10", None))
        self.combo_n_brdtiks.setItemText(6, _translate("geogridDialogBase", "20", None))
        self.combo_n_brdtiks.setItemText(7, _translate("geogridDialogBase", "30", None))
        self.combo_n_brdtiks.setItemText(8, _translate("geogridDialogBase", "60", None))
        self.combo_n_brdtiks.setItemText(9, _translate("geogridDialogBase", "120", None))
        self.combo_n_brdtiks.setItemText(10, _translate("geogridDialogBase", "180", None))
        self.combo_n_brdtiks.setItemText(11, _translate("geogridDialogBase", "240", None))
        self.combo_n_brdtiks.setItemText(12, _translate("geogridDialogBase", "300", None))
        self.combo_n_brdtiks.setItemText(13, _translate("geogridDialogBase", "600", None))
        self.label_13.setText(_translate("geogridDialogBase", "Step border Ticks (minutes )", None))
        self.combo_n_lblminuts.setItemText(0, _translate("geogridDialogBase", "1", None))
        self.combo_n_lblminuts.setItemText(1, _translate("geogridDialogBase", "2", None))
        self.combo_n_lblminuts.setItemText(2, _translate("geogridDialogBase", "3", None))
        self.combo_n_lblminuts.setItemText(3, _translate("geogridDialogBase", "5", None))
        self.combo_n_lblminuts.setItemText(4, _translate("geogridDialogBase", "6", None))
        self.combo_n_lblminuts.setItemText(5, _translate("geogridDialogBase", "10", None))
        self.combo_n_lblminuts.setItemText(6, _translate("geogridDialogBase", "20", None))
        self.combo_n_lblminuts.setItemText(7, _translate("geogridDialogBase", "30", None))
        self.combo_n_lblminuts.setItemText(8, _translate("geogridDialogBase", "60", None))
        self.combo_n_lblminuts.setItemText(9, _translate("geogridDialogBase", "120", None))
        self.combo_n_lblminuts.setItemText(10, _translate("geogridDialogBase", "180", None))
        self.combo_n_lblminuts.setItemText(11, _translate("geogridDialogBase", "240", None))
        self.combo_n_lblminuts.setItemText(12, _translate("geogridDialogBase", "300", None))
        self.combo_n_lblminuts.setItemText(13, _translate("geogridDialogBase", "600", None))
        self.label_14.setText(_translate("geogridDialogBase", "Step of labels along a border (minute)", None))
        self.label_18.setText(_translate("geogridDialogBase", "BORDER", None))
        self.Save_btn.setText(_translate("geogridDialogBase", "Save As", None))
        self.add_layers.setText(_translate("geogridDialogBase", "Add layers to the current project", None))

#from qgsmaplayercombobox import QgsMapLayerComboBox
import resources
