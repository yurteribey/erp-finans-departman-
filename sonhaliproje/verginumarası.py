from PyQt5.QtWidgets import *
from verginumarasi_python import Ui_MainWindow
import sqlite3

class VergiNumarasiPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.vernoform = Ui_MainWindow()
        self.vernoform.setupUi(self)

        # Veri tabanı işlemleri
        self.baglanti = sqlite3.connect("verginumarasi.db")
        self.islem = self.baglanti.cursor()
        self.baglanti.commit()

        # Tabloyu oluştur
        self.islem.execute("create table if not exists vergino(sirketismi text , vergino int)")
        self.baglanti.commit()

        # Buton bağlantıları
        self.vernoform.betnkaydet.clicked.connect(self.kayit_ekle)
        self.vernoform.betnkaydet.clicked.connect(self.kayit_listele)

    def kayit_ekle(self):
        sirketismi = self.vernoform.lineEditsrket.text()
        vergino = int(self.vernoform.lineEditvergi.text())

        try:
            ekle = "insert into vergino(sirketismi, vergino) values(?, ?)"
            self.islem.execute(ekle, (sirketismi, vergino))
            self.baglanti.commit()
            self.vernoform.statusbar.showMessage("Kayıt Ekleme İşlemi Başarılı.")

        except Exception as error:
            self.vernoform.statusbar.showMessage("Kayıt Eklenemedi. Hata Çıktı: {}".format(error))

    def kayit_listele(self):
        self.vernoform.tableWidget.clearContents()  # İçeriği temizle
        sorgu = "select * from vergino"
        self.islem.execute(sorgu)

        for indexSatir, sirket in enumerate(self.islem.fetchall()):
            self.vernoform.tableWidget.setRowCount(indexSatir + 1)
            for indexSütun, verginum in enumerate(sirket):
                self.vernoform.tableWidget.setItem(indexSatir, indexSütun, QTableWidgetItem(str(verginum)))

    

if __name__ == "__main__":
    app = QApplication([])
    window = VergiNumarasiPage()
    window.show()
    app.exec_()
