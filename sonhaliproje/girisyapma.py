

from PyQt5.QtWidgets import *
from girisyapma_python import Ui_Form
from anasayfa import AnasayfaPage



class GirisYapmaPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.girisform = Ui_Form()
        self.girisform.setupUi(self)
        self.anasayfaac = AnasayfaPage()
        self.girisform.btngiris.clicked.connect(self.GirisYap)


    def GirisYap(self):
        kullanici = self.girisform.lneEditkullanici.text()
        sifre = self.girisform.lneEditsifre.text()

        if kullanici == "ecy" and sifre == "123" :
        
            self.hide()
            self.anasayfaac.show()