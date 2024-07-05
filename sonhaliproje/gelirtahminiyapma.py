from PyQt5.QtWidgets import *
from gelirtahminiyapma_python import Ui_MainWindow
import sqlite3

class GelirTahminiYapmaPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.geltahyapform = Ui_MainWindow()
        self.geltahyapform.setupUi(self)

        # Veri tabanı işlemleri
        self.baglanti = sqlite3.connect("gelirtahmini.db")
        self.islem = self.baglanti.cursor()
        self.baglanti.commit()

        # Tabloyu oluştur
        self.islem.execute("create table if not exists gelirtahmini(satisid int , satistahmini int)")
        self.baglanti.commit()

        # Buton bağlantıları
        self.geltahyapform.btnekle.clicked.connect(self.kayit_ekle)
        self.geltahyapform.btnkaydet.clicked.connect(self.kayit_listele)

    def kayit_ekle(self):
        satisid = int(self.geltahyapform.lineEditsatid.text())
        satistahmini = int(self.geltahyapform.lineEditsattah.text())

        try:
            ekle = "insert into gelirtahmini(satisid, satistahmini) values(?, ?)"
            self.islem.execute(ekle, (satisid, satistahmini))
            self.baglanti.commit()
            self.geltahyapform.statusbar.showMessage("Kayıt Ekleme İşlemi Başarılı.")

        except Exception as error:
            self.geltahyapform.statusbar.showMessage("Kayıt Eklenemedi. Hata Çıktı: {}".format(error))

    def kayit_listele(self):
        self.geltahyapform.tableWidget.clearContents()  # İçeriği temizle
        sorgu = "select * from gelirtahmini"
        self.islem.execute(sorgu)

        for indexSatir, satisidi in enumerate(self.islem.fetchall()):
            self.geltahyapform.tableWidget.setRowCount(indexSatir + 1)
            for indexSütun, satistahminii in enumerate(satisidi):
                self.geltahyapform.tableWidget.setItem(indexSatir, indexSütun, QTableWidgetItem(str(satistahminii)))

if __name__ == "__main__":
    app = QApplication([])
    window = GelirTahminiYapmaPage()
    window.show()
    app.exec_()

