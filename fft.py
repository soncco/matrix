#!/usr/bin/env python

import os
import sys
import numpy as np
from sympy import Symbol,expand
from PySide import QtCore, QtGui

class fMain(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
    
    def setupUi(self, fMain):
        fMain.setObjectName("fMain")
        fMain.setWindowModality(QtCore.Qt.ApplicationModal)
        fMain.resize(639, 557)
        self.verticalLayout_10 = QtGui.QVBoxLayout(fMain)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.fraInputs = QtGui.QGroupBox(fMain)
        self.fraInputs.setObjectName("fraInputs")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.fraInputs)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lblDetail = QtGui.QLabel(self.fraInputs)
        self.lblDetail.setObjectName("lblDetail")
        self.verticalLayout_6.addWidget(self.lblDetail)
        self.pnlPolyPx = QtGui.QFrame(self.fraInputs)
        self.pnlPolyPx.setFrameShape(QtGui.QFrame.StyledPanel)
        self.pnlPolyPx.setFrameShadow(QtGui.QFrame.Raised)
        self.pnlPolyPx.setObjectName("pnlPolyPx")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.pnlPolyPx)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblPolyPx = QtGui.QLabel(self.pnlPolyPx)
        self.lblPolyPx.setObjectName("lblPolyPx")
        self.horizontalLayout.addWidget(self.lblPolyPx)
        self.txtPolyPx = QtGui.QLineEdit(self.pnlPolyPx)
        self.txtPolyPx.setObjectName("txtPolyPx")
        self.horizontalLayout.addWidget(self.txtPolyPx)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.txtPolyPxFull = QtGui.QLineEdit(self.pnlPolyPx)
        self.txtPolyPxFull.setReadOnly(True)
        self.txtPolyPxFull.setObjectName("txtPolyPxFull")
        self.verticalLayout_2.addWidget(self.txtPolyPxFull)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_6.addWidget(self.pnlPolyPx)
        self.pnlPolyQx = QtGui.QFrame(self.fraInputs)
        self.pnlPolyQx.setFrameShape(QtGui.QFrame.StyledPanel)
        self.pnlPolyQx.setFrameShadow(QtGui.QFrame.Raised)
        self.pnlPolyQx.setObjectName("pnlPolyQx")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.pnlPolyQx)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblPolyQx = QtGui.QLabel(self.pnlPolyQx)
        self.lblPolyQx.setObjectName("lblPolyQx")
        self.horizontalLayout_2.addWidget(self.lblPolyQx)
        self.txtPolyQx = QtGui.QLineEdit(self.pnlPolyQx)
        self.txtPolyQx.setObjectName("txtPolyQx")
        self.horizontalLayout_2.addWidget(self.txtPolyQx)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.txtPolyQxFull = QtGui.QLineEdit(self.pnlPolyQx)
        self.txtPolyQxFull.setReadOnly(True)
        self.txtPolyQxFull.setObjectName("txtPolyQxFull")
        self.verticalLayout_3.addWidget(self.txtPolyQxFull)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addWidget(self.pnlPolyQx)
        self.lblDetail2 = QtGui.QLabel(self.fraInputs)
        self.lblDetail2.setObjectName("lblDetail2")
        self.verticalLayout_6.addWidget(self.lblDetail2)
        self.pnlMethods = QtGui.QFrame(self.fraInputs)
        self.pnlMethods.setFrameShape(QtGui.QFrame.StyledPanel)
        self.pnlMethods.setFrameShadow(QtGui.QFrame.Raised)
        self.pnlMethods.setObjectName("pnlMethods")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.pnlMethods)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cmdFFT = QtGui.QPushButton(self.pnlMethods)
        self.cmdFFT.setEnabled(False)
        self.cmdFFT.setAutoDefault(False)
        self.cmdFFT.setDefault(True)
        self.cmdFFT.setObjectName("cmdFFT")
        self.horizontalLayout_3.addWidget(self.cmdFFT)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6.addWidget(self.pnlMethods)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout.addWidget(self.fraInputs)
        self.fraResults = QtGui.QGroupBox(fMain)
        self.fraResults.setObjectName("fraResults")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.fraResults)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblPolyRx = QtGui.QLabel(self.fraResults)
        self.lblPolyRx.setObjectName("lblPolyRx")
        self.horizontalLayout_5.addWidget(self.lblPolyRx)
        self.txtPolyRx = QtGui.QLineEdit(self.fraResults)
        self.txtPolyRx.setReadOnly(True)
        self.txtPolyRx.setObjectName("txtPolyRx")
        self.horizontalLayout_5.addWidget(self.txtPolyRx)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.txtProcess = QtGui.QPlainTextEdit(self.fraResults)
        self.txtProcess.setFont(font)
        self.txtProcess.setReadOnly(True)
        self.txtProcess.setObjectName("txtProcess")
        self.verticalLayout_8.addWidget(self.txtProcess)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout.addWidget(self.fraResults)
        self.verticalLayout_10.addLayout(self.verticalLayout)

        self.retranslateUi(fMain)
        QtCore.QMetaObject.connectSlotsByName(fMain)

    def retranslateUi(self, fMain):
        fMain.setWindowTitle(QtGui.QApplication.translate("fMain", "Multiplication of polynomials", None, QtGui.QApplication.UnicodeUTF8))
        self.fraInputs.setTitle(QtGui.QApplication.translate("fMain", "Inputs", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDetail.setText(QtGui.QApplication.translate("fMain", "Enter two polynomials:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPolyPx.setText(QtGui.QApplication.translate("fMain", "P(x) =", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPolyQx.setText(QtGui.QApplication.translate("fMain", "Q(x) =", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDetail2.setText(QtGui.QApplication.translate("fMain", "Select method(s):", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdFFT.setText(QtGui.QApplication.translate("fMain", "FFT", None, QtGui.QApplication.UnicodeUTF8))
        self.fraResults.setTitle(QtGui.QApplication.translate("fMain", "Results", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPolyRx.setText(QtGui.QApplication.translate("fMain", "R(x) =", None, QtGui.QApplication.UnicodeUTF8))

    @QtCore.Slot()
    def on_txtPolyPx_textChanged(self):
        try:
            self.px = np.array( map( int, self.txtPolyPx.text().split() ) )
            x=Symbol('x')
            self.txtPolyPxFull.setText( str (expand( np.poly1d(self.px)(x)) ) )
        except:
            pass

        if (self.txtPolyPxFull.text() != "") and (self.txtPolyQxFull.text() != ""):
            self.cmdFFT.setEnabled(True)
        else:
            self.cmdFFT.setEnabled(False)

    @QtCore.Slot()
    def on_txtPolyQx_textChanged(self):
        try:
            self.qx = np.array( map( int, self.txtPolyQx.text().split() ) )
            x=Symbol('x')
            self.txtPolyQxFull.setText( str (expand( np.poly1d(self.qx)(x)) ) )
        except:
            pass

        if (self.txtPolyPxFull.text() != "") and (self.txtPolyQxFull.text() != ""):
            self.cmdFFT.setEnabled(True)
        else:
            self.cmdFFT.setEnabled(False)

    @QtCore.Slot()
    def on_cmdFFT_clicked(self):
        out = ""
        np.set_printoptions(precision=4)
        # Tamanio de matriz (n)        
        n = 0
        n = len(self.px)
        if n < len(self.qx):
            n = len(self.qx)
        n *= 2
        out += "orden n: " + str(n) + "\n"

        # Polinominios a matriz nx1
        p = self.px[::-1]
        q = self.qx[::-1]
        for i in range(n):
                p = np.append(p, [0])
                q = np.append(q, [0])
        p = np.matrix(p[:n]).transpose()
        q = np.matrix(q[:n]).transpose()
        out += "coeficientes p:\n"
        out += str(p) + "\n"
        out += "coeficientes q:\n"
        out += str(q) + "\n"

        # Matriz vandermode
        vnd = np.matrix(np.vander(range(n), increasing=True))
        out += "vandermond: \n"
        out += str(vnd) + "\n"

        # DFT p
        dftp = vnd * p
        out += "dftp:\n"
        out += str(dftp) + "\n"

        # DFT q
        dftq = vnd * q
        out += "dftq:\n"
        out += str(dftq) + "\n"

        # Producto escalar
        yk = np.multiply(dftp, dftq)
        out += "yk:\n"
        out += str(yk) + "\n"

        a = vnd.I*yk
        out += "a:\n"
        out += str(np.around(a, decimals=2)) + "\n"

        self.rx = np.poly1d(self.px) * np.poly1d(self.qx)
        x=Symbol('x')
        self.txtPolyRx.setText( str(expand(self.rx(x))) )
        self.txtProcess.setPlainText( out )


def main():
    app = QtGui.QApplication(sys.argv)
    f = fMain()

    r = f.geometry()
    r.moveCenter(app.desktop().availableGeometry().center())
    f.setGeometry(r)

    f.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
