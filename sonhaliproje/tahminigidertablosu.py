import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pyqtgraph as pg
from tahminigidertablosu_python import Ui_MainWindow

class GiderTahminiTablosuPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.gidtabtahyapform = Ui_MainWindow()
        self.gidtabtahyapform.setupUi(self)

        # Arayüzü oluştur
        self.setup_ui()

        # Veritabanı bağlantısı
        self.baglanti = sqlite3.connect("gidertahmini.db")
        self.islem = self.baglanti.cursor()

        # Ana pencere özellikleri
        self.setWindowTitle("Gider Tahmini Grafiği")
        self.setGeometry(100, 100, 800, 600)

        # Grafik widget'ını oluştur
        self.plotWidget = pg.PlotWidget()
        self.plotWidget.setBackground('w')
        self.plotWidget.showGrid(x=True, y=True)
        self.plotWidget.setLabel('left', 'Gider', units='TL')
        self.plotWidget.setLabel('bottom', 'Gider ID')

        # Widget'ları düzenle
        layout = QVBoxLayout()
        layout.addWidget(self.plotWidget)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        # Veritabanından verileri çek ve grafikte göster
        self.plot_gider_verileri()

    def setup_ui(self):
        # Arayüzü tasarlayan sınıfı oluştur
        self.gidtahyapform = Ui_MainWindow()
        self.gidtahyapform.setupUi(self)

    def plot_gider_verileri(self):
        try:
            # Veritabanından verileri çek
            self.islem.execute("SELECT * FROM gidertahmini")
            veriler = self.islem.fetchall()

            # Verileri grafikte göster
            x = [veri[0] for veri in veriler]
            y = [veri[1] for veri in veriler]

            # Çizgi grafiği oluştur
            self.plotWidget.plot(x, y, pen=pg.mkPen('b', width=2), symbol='o', symbolSize=5, symbolBrush='r')

        except Exception as e:
            print(f"Hata: {e}")
        finally:
            self.baglanti.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    uygulama = GiderTahminiTablosuPage()
    uygulama.show()
    sys.exit(app.exec_())