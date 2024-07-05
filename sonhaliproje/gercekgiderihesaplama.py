
from PyQt5.QtWidgets import *
from gercekgiderihesaplama_pyhton import Ui_MainWindow
import sqlite3

class GercekGideriHesaplamaPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.gidgeryapform = Ui_MainWindow()
        self.gidgeryapform.setupUi(self)

        # Veri tabanı işlemleri
        self.baglanti = sqlite3.connect("gercekgider.db")
        self.islem = self.baglanti.cursor()
        self.baglanti.commit()

        # Tabloyu oluştur
        self.islem.execute("create table if not exists gidertahmini(giderid int , iscilikgideri int, malzemegideri int, genelgiderler int)")
        self.baglanti.commit()

        # Buton bağlantıları
        self.gidgeryapform.pushBtneklers.clicked.connect(self.kayit_ekle)
        self.gidgeryapform.pushBtnkaydt.clicked.connect(self.kayit_listele)

    def kayit_ekle(self):
        giderid = int(self.gidgeryapform.lineEditgid.text())
        iscilikgideri = int(self.gidgeryapform.lineEditiscilikgid.text())
        malzemegideri = int(self.gidgeryapform.lineEditmalzemegid.text())
        genelgiderler = int(self.gidgeryapform.lineEditgenelgid.text())

        try:
            ekle = "insert into gidertahmini(giderid, iscilikgideri, malzemegideri, genelgiderler) values(?, ?, ?, ?)"
            self.islem.execute(ekle, (giderid, iscilikgideri, malzemegideri, genelgiderler))
            self.baglanti.commit()
            self.gidgeryapform.statusbar.showMessage("Kayıt Ekleme İşlemi Başarılı.")

        except Exception as error:
            self.gidgeryapform.statusbar.showMessage("Kayıt Eklenemedi. Hata Çıktı: {}".format(error))

    def kayit_listele(self):
        self.gidgeryapform.tableWidget.clearContents()  # İçeriği temizle
        sorgu = "select * from gidertahmini"
        self.islem.execute(sorgu)

        for indexSatir, gider in enumerate(self.islem.fetchall()):
            self.gidgeryapform.tableWidget.setRowCount(indexSatir + 1)
            for indexSütun, deger in enumerate(gider):
                item = QTableWidgetItem(str(deger))
                self.gidgeryapform.tableWidget.setItem(indexSatir, indexSütun, item)


    

if __name__ == "__main__":
    app = QApplication([])
    window = GercekGideriHesaplamaPage()
    window.show()
    app.exec_()
