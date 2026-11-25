import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap

class Juego(QWidget):

    def __init__(self):
        super().__init__()
        self.anzuelo_lanzado = False
        self.click_izquierdo = False
        self.potencia = 0
        self.direccion = 1
        self.timer = QTimer()
        self.timer.timeout.connect(self.cargar)
        self.barra0 = QPixmap("assets/barra0.png")
        self.barra1 = QPixmap("assets/barra1.png")
        self.barra2 = QPixmap("assets/barra2.png")
        self.barra3 = QPixmap("assets/barra3.png")
        self.barra4 = QPixmap("assets/barra4.png")
        self.barra5 = QPixmap("assets/barra5.png")
        self.barra_final = None

        self.setWindowTitle("La Gran Pesca del DCCongrio")

        self.etiqueta = QLabel("Lanza el anzuelo!")
        self.info_en_pantalla = QLabel("")
        self.info_en_pantalla2 = QLabel()
        self.controles = QLabel("Manten click izquierdo")

        layout_info = QHBoxLayout()
        layout_info.addWidget(self.controles)

        layout_principal = QVBoxLayout()

        layout_principal.addWidget(self.etiqueta)
        layout_principal.addWidget(self.info_en_pantalla)
        layout_principal.addWidget(self.info_en_pantalla2)
        layout_principal.addLayout(layout_info)

        self.setLayout(layout_principal)

    def mousePressEvent(self, event):
        if not self.anzuelo_lanzado:
            if event.button() == Qt.MouseButton.LeftButton:
                self.click_izquierdo = True
                self.etiqueta.setText("Te estas preparando...")
                self.info_en_pantalla.setText(f"Cargando...")
                self.info_en_pantalla2.setPixmap(self.barra0)
                self.timer.start(200)
                    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if not self.anzuelo_lanzado:
                self.etiqueta.setText("Haz lanzado el anzuelo!")
                self.timer.stop()
                self.info_en_pantalla.setText(f"Tu potencia ha sido {self.potencia}!")
                self.info_en_pantalla2.setPixmap(self.barra_final)
                self.anzuelo_lanzado = True
                self.click_izquierdo = False

    def cargar(self):
        #Potencia
        if self.potencia == 5:
            self.direccion = -1
        elif self.potencia == 0:
            self.direccion = 1
        if self.direccion == 1:
            self.potencia += 1
        else:
            self.potencia -= 1
        #Eventos
        if self.potencia == 0:
            self.info_en_pantalla2.setPixmap(self.barra0)
            self.barra_final = self.barra0
        if self.potencia == 1:
            self.info_en_pantalla2.setPixmap(self.barra1)
            self.barra_final = self.barra1
        if self.potencia == 2:
            self.info_en_pantalla2.setPixmap(self.barra2)
            self.barra_final = self.barra2
        if self.potencia == 3:
            self.info_en_pantalla2.setPixmap(self.barra3)
            self.barra_final = self.barra3
        if self.potencia == 4:
            self.info_en_pantalla2.setPixmap(self.barra4)
            self.barra_final = self.barra4
        if self.potencia == 5:
            self.info_en_pantalla2.setPixmap(self.barra5)
            self.barra_final = self.barra5
        


if __name__ == "__main__":
    app = QApplication([])
    ventana = Juego()
    ventana.show()
    app.exec()