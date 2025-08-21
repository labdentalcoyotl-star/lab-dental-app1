import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QAction, QVBoxLayout, QWidget
from PyQt5.QtGui import QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laboratorio Dental")
        self.setGeometry(100, 100, 700, 400)

        # Tabla principal
        self.table = QTableWidget(5, 3)
        self.table.setHorizontalHeaderLabels(["Doctor", "Trabajo", "Fecha Entrega"])

        # Datos de ejemplo
        data = [
            ("Dr. Pérez", "Corona", "2025-08-25"),
            ("Dr. García", "Prótesis", "2025-08-23"),
            ("Dr. López", "Implante", "2025-08-30"),
            ("Dr. Ramírez", "Incrustación", "2025-08-22"),
            ("Dr. Torres", "Carilla", "2025-08-28")
        ]

        for row, (doctor, trabajo, fecha) in enumerate(data):
            doctor_item = QTableWidgetItem(doctor)
            doctor_item.setForeground(QColor("blue"))
            self.table.setItem(row, 0, doctor_item)
            self.table.setItem(row, 1, QTableWidgetItem(trabajo))
            self.table.setItem(row, 2, QTableWidgetItem(fecha))

        # Menú archivo -> configuración (ejemplo vacío)
        menu = self.menuBar().addMenu("Archivo")
        config_action = QAction("Configuración", self)
        menu.addAction(config_action)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
