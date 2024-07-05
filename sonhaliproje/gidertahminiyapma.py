
from PyQt5.QtWidgets import *
from gidertahminiyapma_python import Ui_MainWindow
import sqlite3

class GiderTahminiYapmaPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.gidtahyapform = Ui_MainWindow()
        self.gidtahyapform.setupUi(self)

        # Veri tabanı işlemleri
        self.baglanti = sqlite3.connect("gidertahmini.db")
        self.islem = self.baglanti.cursor()
        self.baglanti.commit()

        # Tabloyu oluştur
        self.islem.execute("create table if not exists gidertahmini(giderid int , iscilikgideri int, malzemegideri int, genelgiderler int)")
        self.baglanti.commit()

        # Buton bağlantıları
        self.gidtahyapform.pushBtnekle.clicked.connect(self.kayit_ekle)
        self.gidtahyapform.pushBtnkaydet.clicked.connect(self.kayit_listele)

    def kayit_ekle(self):
        giderid = int(self.gidtahyapform.lineEditgider.text())
        iscilikgideri = int(self.gidtahyapform.lineEditiscilik.text())
        malzemegideri = int(self.gidtahyapform.lineEditmalzeme.text())
        genelgiderler = int(self.gidtahyapform.lineEditgenel.text())

        try:
            ekle = "insert into gidertahmini(giderid, iscilikgideri, malzemegideri, genelgiderler) values(?, ?, ?, ?)"
            self.islem.execute(ekle, (giderid, iscilikgideri, malzemegideri, genelgiderler))
            self.baglanti.commit()
            self.gidtahyapform.statusbar.showMessage("Kayıt Ekleme İşlemi Başarılı.")

        except Exception as error:
            self.gidtahyapform.statusbar.showMessage("Kayıt Eklenemedi. Hata Çıktı: {}".format(error))

    def kayit_listele(self):
        self.gidtahyapform.tableWidget.clearContents()  # İçeriği temizle
        sorgu = "select * from gidertahmini"
        self.islem.execute(sorgu)

        for indexSatir, gider in enumerate(self.islem.fetchall()):
            self.gidtahyapform.tableWidget.setRowCount(indexSatir + 1)
            for indexSütun, deger in enumerate(gider):
                item = QTableWidgetItem(str(deger))
                self.gidtahyapform.tableWidget.setItem(indexSatir, indexSütun, item)


    

if __name__ == "__main__":
    app = QApplication([])
    window = GiderTahminiYapmaPage()
    window.show()
    app.exec_()
