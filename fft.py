#!/usr/bin/env python3

import os
import sys
from PySide import QtCore, QtGui

class ImageViewer(QtGui.QMainWindow):
    def __init__(self):
        super(ImageViewer, self).__init__()

        self.printer = QtGui.QPrinter()
        self.scaleFactor = 0.0

        self.imageLabel = QtGui.QLabel()
        self.imageLabel.setBackgroundRole(QtGui.QPalette.Base)
        self.imageLabel.setSizePolicy(QtGui.QSizePolicy.Ignored,
                QtGui.QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        self.scrollArea.setWidget(self.imageLabel)
        self.setCentralWidget(self.scrollArea)

        self.createActions()
        self.createMenus()

        self.setWindowTitle("Unsaac")
        self.resize(660, 506)
        self.videoSize = QtCore.QSize(640, 480)

    def open(self):
        fileName, _ = QtGui.QFileDialog.getOpenFileName(self, "Abrir imagen",
                QtCore.QDir.currentPath(), "Imagenes (*.png *.bmp *.jpg)")
        if fileName:
            pil_image = Image.open(fileName).convert('L')
            fileName = '/tmp/' + str(time.time()) + '.png'
            pil_image.save(fileName)
            image = QtGui.QImage(fileName)

            self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
            self.scaleFactor = 1.0

            self.fitToWindowAct.setEnabled(True)
            self.updateActions()

            if not self.fitToWindowAct.isChecked():
                self.imageLabel.adjustSize()

    def save(self):
        fileName, _ = QtGui.QFileDialog.getSaveFileName(self, "Guardar imagen",
                QtCore.QDir.currentPath())
        if fileName:
            if fileName[-4:] != '.png': fileName += '.png'
            q_img = self.imageLabel.pixmap()
            q_img.save(fileName)

    def zoomIn(self):
        self.scaleImage(1.25)

    def zoomOut(self):
        self.scaleImage(0.8)

    def normalSize(self):
        self.imageLabel.adjustSize()
        self.scaleFactor = 1.0

    def fitToWindow(self):
        fitToWindow = self.fitToWindowAct.isChecked()
        self.scrollArea.setWidgetResizable(fitToWindow)
        if not fitToWindow:
            self.normalSize()

        self.updateActions()

    def createActions(self):
        self.openAct = QtGui.QAction("Abrir...", self,
                triggered=self.open)

        self.fromWebcamAct = QtGui.QAction("Webcam", self,
                triggered=self.runWebcam)

        self.stopWebcamAct = QtGui.QAction("Capturar", self,
                enabled=False, triggered=self.stopWebcam, shortcut="Ctrl+S")

        self.saveAct = QtGui.QAction("Guardar...", self,
                enabled=False, triggered=self.save)

        self.exitAct = QtGui.QAction("Salir", self,
                triggered=self.close)

        self.zoomInAct = QtGui.QAction("Acercar (25%)", self,
                shortcut="Ctrl++", enabled=False, triggered=self.zoomIn)

        self.zoomOutAct = QtGui.QAction("Alejar (25%)", self,
                shortcut="Ctrl+-", enabled=False, triggered=self.zoomOut)

        self.normalSizeAct = QtGui.QAction("Normal", self,
                shortcut="Ctrl+0", enabled=False, triggered=self.normalSize)

        self.fitToWindowAct = QtGui.QAction("Ajustar", self, shortcut="Ctrl+F",
                enabled=False, checkable=True,
                triggered=self.fitToWindow)

        self.ecualizarAct = QtGui.QAction("Ecualizar", self,
                enabled=False, triggered=self.mnuEcualizar)

        self.ecualizarAct = QtGui.QAction("Ecualizar", self,
                enabled=False, triggered=self.mnuEcualizar)

        self.mediaAct = QtGui.QAction("Filtro media", self,
                enabled=False, triggered=self.mnuFiltroMedia)

        self.medianaAct = QtGui.QAction("Filtro mediana", self,
                enabled=False, triggered=self.mnuFiltroMediana)

        self.umbralAct = QtGui.QAction("Filtro umbral", self,
                enabled=False, triggered=self.mnuFiltroUmbral)

        self.realceBordesAct = QtGui.QAction("Realce bordes", self,
                enabled=False, triggered=self.mnuRealceBordes)

        self.reconocimientoLineasAct = QtGui.QAction("Reconocimiento lineas", self,
                enabled=False, triggered=self.mnuReconocimientoLineas)

        self.reconocimientoCircunferenciasAct = QtGui.QAction(
            "Reconocimiento circunferencias", self,
                enabled=False, triggered=self.mnuReconocimientoCircunferencias)

    def createMenus(self):
        self.fileMenu = QtGui.QMenu("Archivo", self)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fromWebcamAct)
        self.fileMenu.addAction(self.stopWebcamAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.saveAct)
        #self.fileMenu.addSeparator()
        #self.fileMenu.addAction(self.exitAct)

        self.viewMenu = QtGui.QMenu("Vista", self)
        self.viewMenu.addAction(self.zoomInAct)
        self.viewMenu.addAction(self.zoomOutAct)
        self.viewMenu.addAction(self.normalSizeAct)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.fitToWindowAct)

        self.operationsMenu = QtGui.QMenu("Operaciones", self)
        self.operationsMenu.addAction(self.ecualizarAct)
        self.operationsMenu.addAction(self.mediaAct)
        self.operationsMenu.addAction(self.medianaAct)
        self.operationsMenu.addAction(self.umbralAct)
        self.operationsMenu.addAction(self.realceBordesAct)
        self.operationsMenu.addAction(self.reconocimientoLineasAct)
        self.operationsMenu.addAction(self.reconocimientoCircunferenciasAct)

        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addMenu(self.viewMenu)
        self.menuBar().addMenu(self.operationsMenu)

    def updateActions(self):
        self.zoomInAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.zoomOutAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())

        self.ecualizarAct.setEnabled(True)
        self.saveAct.setEnabled(True)
        self.mediaAct.setEnabled(True)
        self.medianaAct.setEnabled(True)
        self.umbralAct.setEnabled(True)
        self.realceBordesAct.setEnabled(True)
        self.reconocimientoLineasAct.setEnabled(True)
        self.reconocimientoCircunferenciasAct.setEnabled(True)

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

        self.zoomInAct.setEnabled(self.scaleFactor < 3.0)
        self.zoomOutAct.setEnabled(self.scaleFactor > 0.333)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                                + ((factor - 1) * scrollBar.pageStep()/2)))

    def displayVideoStrean(self):
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.cv.CV_BGR2RGB)
        frame = cv2.flip(frame, 1)
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QtGui.QImage.Format_RGB888)
        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))

        self.scaleFactor = 1.0

        self.fitToWindowAct.setEnabled(True)
        self.updateActions()

        if not self.fitToWindowAct.isChecked():
            self.imageLabel.adjustSize()

    def runWebcam(self):
        self.openAct.setEnabled(False)
        self.fromWebcamAct.setEnabled(False)
        self.stopWebcamAct.setEnabled(True)

        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, self.videoSize.width())
        self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, self.videoSize.height())

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.displayVideoStrean)
        self.timer.start(30)

    def stopWebcam(self):
        self.capture = None
        self.timer = None
        self.openAct.setEnabled(True)
        self.fromWebcamAct.setEnabled(True)
        self.stopWebcamAct.setEnabled(False)
        pil_image = self.getImagen()
        pil_image = pil_image.convert('L')
        fileName = '/tmp/' + str(time.time()) + '.png'
        pil_image.save(fileName)
        self.setImagen(fileName)

    def getImagen(self):
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        q_img = self.imageLabel.pixmap()
        q_img.save(buffer, "PNG")

        strio = cStringIO.StringIO()
        strio.write(buffer.data())
        buffer.close()
        strio.seek(0)
        return Image.open(strio)

    def setImagen(self, fileName):
        image = QtGui.QImage(fileName)
        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))

    def mnuEcualizar(self):
        i = self.getImagen()
        i = rImagen.ecualizar(i)
        fileName = '/tmp/' + str(time.time()) + '.png'
        i.save(fileName)
        self.setImagen(fileName)
        #print "end-ecualizar"

    def mnuFiltroMedia(self):
        i = self.getImagen()
        i = rImagen.filtro_media(i)
        fileName = '/tmp/' + str(time.time()) + '.png'
        i.save(fileName)
        self.setImagen(fileName)
        #print "end-filtro-media"

    def mnuFiltroMediana(self):
        i = self.getImagen()
        i = rImagen.filtro_mediana(i)
        fileName = '/tmp/' + str(time.time()) + '.png'
        i.save(fileName)
        self.setImagen(fileName)
        #print "end-filtro-mediana"

    def mnuFiltroUmbral(self):
        i = self.getImagen()
        i = rImagen.filtro_umbral(i)
        fileName = '/tmp/' + str(time.time()) + '.png'
        i.save(fileName)
        self.setImagen(fileName)
        #print "end-filtro-umbral"

    def mnuRealceBordes(self):
        i = self.getImagen()
        i = rImagen.realce_bordes(i)
        fileName = '/tmp/' + str(time.time()) + '.png'
        i.save(fileName)
        self.setImagen(fileName)
        #print "end-realce-bordes"

    def mnuReconocimientoLineas(self):
        i = self.getImagen()
        i = rImagen.hough(i)
        fileName = '/tmp/' + str(time.time()) + '.png'
        i.save(fileName)
        self.setImagen(fileName)
        #print "end-hough-linea"

    def mnuReconocimientoCircunferencias(self):
        i = self.getImagen()
        i = rImagen.hough(i)
        fileName = '/tmp/' + str(time.time()) + '.png'
        i.save(fileName)
        self.setImagen(fileName)
        #print "end-hough-circunferencia"


def main():
    app = QtGui.QApplication(sys.argv)
    imageViewer = ImageViewer()

    r = imageViewer.geometry()
    r.moveCenter(app.desktop().availableGeometry().center())
    imageViewer.setGeometry(r)

    imageViewer.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
