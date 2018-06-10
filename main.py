#!/usr/bin/env python

import os
import sys
import numpy as np
from sympy import Symbol,expand
from PySide import QtCore, QtGui
from numpy.linalg import inv
from scipy.interpolate import lagrange as lagrange_interpolation

from complex import complex_matrix
from lagrange import tabular

class fMain(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
    
    def setupUi(self, fMain):
        fMain.setObjectName("fMain")
        fMain.setWindowModality(QtCore.Qt.ApplicationModal)
        fMain.resize(700, 600)
        self.verticalLayout_2 = QtGui.QVBoxLayout(fMain)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblPolyPx = QtGui.QLabel(self.fraInputs)
        self.lblPolyPx.setObjectName("lblPolyPx")
        self.horizontalLayout.addWidget(self.lblPolyPx)
        self.txtPolyPx = QtGui.QLineEdit(self.fraInputs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtPolyPx.sizePolicy().hasHeightForWidth())
        self.txtPolyPx.setSizePolicy(sizePolicy)
        self.txtPolyPx.setObjectName("txtPolyPx")
        self.horizontalLayout.addWidget(self.txtPolyPx)
        self.txtPolyPxFull = QtGui.QLineEdit(self.fraInputs)
        self.txtPolyPxFull.setReadOnly(True)
        self.txtPolyPxFull.setObjectName("txtPolyPxFull")
        self.horizontalLayout.addWidget(self.txtPolyPxFull)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblPolyQx = QtGui.QLabel(self.fraInputs)
        self.lblPolyQx.setObjectName("lblPolyQx")
        self.horizontalLayout_2.addWidget(self.lblPolyQx)
        self.txtPolyQx = QtGui.QLineEdit(self.fraInputs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtPolyQx.sizePolicy().hasHeightForWidth())
        self.txtPolyQx.setSizePolicy(sizePolicy)
        self.txtPolyQx.setObjectName("txtPolyQx")
        self.horizontalLayout_2.addWidget(self.txtPolyQx)
        self.txtPolyQxFull = QtGui.QLineEdit(self.fraInputs)
        self.txtPolyQxFull.setReadOnly(True)
        self.txtPolyQxFull.setObjectName("txtPolyQxFull")
        self.horizontalLayout_2.addWidget(self.txtPolyQxFull)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.lblDetail2 = QtGui.QLabel(self.fraInputs)
        self.lblDetail2.setObjectName("lblDetail2")
        self.verticalLayout_6.addWidget(self.lblDetail2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cmdLagrange = QtGui.QPushButton(self.fraInputs)
        self.cmdLagrange.setEnabled(False)
        self.cmdLagrange.setAutoDefault(False)
        self.cmdLagrange.setObjectName("cmdLagrange")
        self.horizontalLayout_3.addWidget(self.cmdLagrange)
        self.cmdFFT = QtGui.QPushButton(self.fraInputs)
        self.cmdFFT.setEnabled(False)
        self.cmdFFT.setAutoDefault(False)
        self.cmdFFT.setDefault(False)
        self.cmdFFT.setObjectName("cmdFFT")
        self.horizontalLayout_3.addWidget(self.cmdFFT)
        self.cmdFFTi = QtGui.QPushButton(self.fraInputs)
        self.cmdFFTi.setEnabled(False)
        self.cmdFFTi.setAutoDefault(False)
        self.cmdFFTi.setObjectName("cmdFFTi")
        self.horizontalLayout_3.addWidget(self.cmdFFTi)
        self.cmdBitReverso = QtGui.QPushButton(self.fraInputs)
        self.cmdBitReverso.setEnabled(False)
        self.cmdBitReverso.setAutoDefault(False)
        self.cmdBitReverso.setObjectName("cmdBitReverso")
        self.horizontalLayout_3.addWidget(self.cmdBitReverso)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
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
        self.txtProcess = QtGui.QPlainTextEdit(self.fraResults)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.txtProcess.setFont(font)
        self.txtProcess.setReadOnly(True)
        self.txtProcess.setObjectName("txtProcess")
        self.verticalLayout_8.addWidget(self.txtProcess)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout.addWidget(self.fraResults)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(fMain)
        QtCore.QMetaObject.connectSlotsByName(fMain)

    def retranslateUi(self, fMain):
        fMain.setWindowTitle(QtGui.QApplication.translate("fMain", "Multiplication of polynomials", None, QtGui.QApplication.UnicodeUTF8))
        self.fraInputs.setTitle(QtGui.QApplication.translate("fMain", "Inputs", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDetail.setText(QtGui.QApplication.translate("fMain", "Enter two polynomials:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPolyPx.setText(QtGui.QApplication.translate("fMain", "P(x) =", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPolyQx.setText(QtGui.QApplication.translate("fMain", "Q(x) =", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDetail2.setText(QtGui.QApplication.translate("fMain", "Method:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdLagrange.setText(QtGui.QApplication.translate("fMain", "Lagrange", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdFFT.setText(QtGui.QApplication.translate("fMain", "FFT", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdFFTi.setText(QtGui.QApplication.translate("fMain", "FFT(i)", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdBitReverso.setText(QtGui.QApplication.translate("fMain", "Bit reverse", None, QtGui.QApplication.UnicodeUTF8))
        self.fraResults.setTitle(QtGui.QApplication.translate("fMain", "Result", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPolyRx.setText(QtGui.QApplication.translate("fMain", "R(x) =", None, QtGui.QApplication.UnicodeUTF8))

    def methodsEnabled(self, value):
        self.cmdLagrange.setEnabled(value)
        self.cmdFFT.setEnabled(value)
        self.cmdFFTi.setEnabled(value)
        self.cmdBitReverso.setEnabled(value)

    @QtCore.Slot()
    def on_txtPolyPx_textChanged(self):
        try:
            self.px = np.array( map( int, self.txtPolyPx.text().split() ) )
            x=Symbol('x')
            self.txtPolyPxFull.setText( str (expand( np.poly1d(self.px)(x)) ) )
        except:
            pass

        if (self.txtPolyPxFull.text() != "") and (self.txtPolyQxFull.text() != ""):
            self.methodsEnabled(True)
        else:
            self.methodsEnabled(False)

    @QtCore.Slot()
    def on_txtPolyQx_textChanged(self):
        try:
            self.qx = np.array( map( int, self.txtPolyQx.text().split() ) )
            x=Symbol('x')
            self.txtPolyQxFull.setText( str (expand( np.poly1d(self.qx)(x)) ) )
        except:
            pass

        if (self.txtPolyPxFull.text() != "") and (self.txtPolyQxFull.text() != ""):
            self.methodsEnabled(True)
        else:
            self.methodsEnabled(False)

    @QtCore.Slot()
    def on_cmdLagrange_clicked(self):
        out = ""
        np.set_printoptions(precision=4)
        # Tamanio de matriz (n)
        n = 0
        n = len(self.px)
        if n < len(self.qx):
            n = len(self.qx)
        n *= 2
        out += "orden n: " + str(n) + "\n"

        xk = np.array([i for i in range(n)])

        # Polinominios a matriz nx1
        p = self.px
        q = self.qx

        yp = np.array(tabular(p, n))
        yq = np.array(tabular(q, n))

        out += "x:\n"
        out += "%s \n" % str(xk)

        out += "y1:\n"
        out += "%s \n" % str(yp)

        out += "y2:\n"
        out += "%s \n" % str(yq)
        yk = yp * yq

        out += "yk:\n"
        out += "%s \n" % str(yk)

        rx = lagrange_interpolation(xk, yk)

        coeficientes = np.around(rx.coefficients, decimals=2)
        out += "coeficientes:\n"
        out += "%s \n" % str(coeficientes)

        self.rx = rx

        x = Symbol('x')
        self.txtPolyRx.setText(str(expand(np.poly1d(coeficientes)(x))))
        self.txtProcess.setPlainText(out)


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
        out += "coeficientes de a:\n"
        out += str(p) + "\n"
        out += "coeficientes de b:\n"
        out += str(q) + "\n"

        # Matriz vandermode
        vnd = np.matrix(np.vander(range(n), increasing=True))
        out += "Vk: \n"
        out += str(vnd) + "\n"

        # DFT p
        dftp = vnd * p
        out += "dft2n(a):\n"
        out += str(dftp) + "\n"

        # DFT q
        dftq = vnd * q
        out += "dft2n(b):\n"
        out += str(dftq) + "\n"

        # Producto escalar
        yk = np.multiply(dftp, dftq)
        out += "yk:\n"
        out += str(yk) + "\n"

        out += "Vk**-1\n"
        out += str(vnd.I) + "\n"

        a = vnd.I*yk
        out += "c:\n"
        out += str(np.around(a, decimals=2)) + "\n"

        self.rx = np.poly1d(self.px) * np.poly1d(self.qx)
        x=Symbol('x')
        self.txtPolyRx.setText( str(expand(self.rx(x))) )
        self.txtProcess.setPlainText( out )

    @QtCore.Slot()
    def on_cmdFFTi_clicked(self):
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
        out += "coeficientes de a:\n"
        out += str(p) + "\n"
        out += "coeficientes de b:\n"
        out += str(q) + "\n"

        # Matriz vandermode
        vnd = complex_matrix(n)
        out += "Vk(j): \n"
        out += str(vnd) + "\n"

        # DFT p
        dftp = vnd * p
        out += "dft2n(a):\n"
        out += str(dftp) + "\n"

        # DFT q
        dftq = vnd * q
        out += "dft2n(b):\n"
        out += str(dftq) + "\n"

        # Producto escalar
        yk = np.multiply(dftp, dftq)
        out += "yk:\n"
        out += str(yk) + "\n"

        out += "Vk(j)**-1\n"
        out += str(inv(vnd)) + "\n"

        a = inv(vnd)*yk
        out += "c:\n"
        out += str(np.around(a, decimals=2)) + "\n"

        self.rx = np.poly1d(self.px) * np.poly1d(self.qx)

        self.txtPolyRx.setText(str(expand(self.rx(x))))
        self.txtProcess.setPlainText(out)
    
    @QtCore.Slot()
    def on_cmdBitReverso_clicked(self):
        print("Bit reverso")


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
