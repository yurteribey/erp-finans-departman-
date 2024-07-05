
from PyQt5.QtWidgets import *
from gercekgelirihesaplama_python import Ui_MainWindow
import sqlite3

class GercekGeliriHesaplamaPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.gergelyapform = Ui_MainWindow()
        self.gergelyapform.setupUi(self)

        # Veri tabanı işlemleri
        self.baglanti = sqlite3.connect("gercekgelirihesaplama.db")
        self.islem = self.baglanti.cursor()
        self.baglanti.commit()

        # Tabloyu oluştur veya güncelle
        self.islem.execute("CREATE TABLE IF NOT EXISTS gercekgelir (satisid INTEGER, satılanmiktar INTEGER)")
        self.baglanti.commit()

        # Buton bağlantıları
        self.gergelyapform.btnekler.clicked.connect(self.kayit_ekle1)
        self.gergelyapform.btnkaydt.clicked.connect(self.kayit_listele1)

    def kayit_ekle1(self):
        satisid = int(self.gergelyapform.lineEditsatidi.text())
        satilanmiktar = int(self.gergelyapform.lineEditsatmik.text())

        try:
            ekle = "INSERT INTO gercekgelir (satisid, satılanmiktar) VALUES (?, ?)"
            self.islem.execute(ekle, (satisid, satilanmiktar))
            self.baglanti.commit()
            self.gergelyapform.statusbar.showMessage("Kayıt Ekleme İşlemi Başarılı.")
        except Exception as error:
            self.gergelyapform.statusbar.showMessage("Kayıt Eklenemedi. Hata Çıktı:{}".format(error))

    def kayit_listele1(self):
        self.gergelyapform.tableWidget.clearContents()  # İçeriği temizletir
        sorgu = "SELECT * FROM gercekgelir"
        self.islem.execute(sorgu)

        for indexSatir, satisidi2 in enumerate(self.islem.fetchall()):
            self.gergelyapform.tableWidget.setRowCount(indexSatir + 1)
            for indexSütun, satilanmiktar2 in enumerate(satisidi2):
                item = QTableWidgetItem(str(satilanmiktar2))
                self.gergelyapform.tableWidget.setItem(indexSatir, indexSütun, item)

if __name__ == "__main__":
    app2 = QApplication([])
    window2 = GercekGeliriHesaplamaPage()
    window2.show()
    app2.exec_()