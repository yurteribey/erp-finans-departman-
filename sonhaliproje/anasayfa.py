
from PyQt5.QtWidgets import *
from anasayfa_python import Ui_MainWindow
from gelirtahminiyapma import GelirTahminiYapmaPage
from gidertahminiyapma import GiderTahminiYapmaPage
from gercekgelirihesaplama import GercekGeliriHesaplamaPage
from gercekgiderihesaplama import GercekGideriHesaplamaPage
from tahminigelirtablosu import TahminiGelirTablosuPage
from tahminigidertablosu import GiderTahminiTablosuPage
from gercekgidertablosu import GiderTablosuPage
from gercekgelirtablosu import GelirTablosuPage
from verginumarası import VergiNumarasiPage



class AnasayfaPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.anasayfaform = Ui_MainWindow()
        self.anasayfaform.setupUi(self)
        self.geltahyapform = GelirTahminiYapmaPage()
        self.gidtahyapform = GiderTahminiYapmaPage()
        self.gergelyapform = GercekGeliriHesaplamaPage()
        self.gidgeryapform = GercekGideriHesaplamaPage()
        self.geltahtabyapform = TahminiGelirTablosuPage()
        self.gidtahtabyapform = GiderTahminiTablosuPage()
        self.gidtabyapform = GiderTablosuPage()
        self.geltabyapform = GelirTablosuPage()
        self.vernoform = VergiNumarasiPage()



        self.anasayfaform.actionTahmini_Gelir_Olu_turma.triggered.connect(self.GelirTahminiYapmaFormu)

        self.anasayfaform.actionTahmini_Gider_Olu_turma.triggered.connect(self.GiderTahminiYapmaFormu)

        self.anasayfaform.actionGelirleri_Hesaplama.triggered.connect(self.GercekGeliriHesaplamaFormu)

        self.anasayfaform.actionGiderleri_Hesaplama.triggered.connect(self.GercekGideriHesaplamaFormu)

        self.anasayfaform.actionTahmini_Gelir_Tablolar.triggered.connect(self.TahminiGelirTablosuYapmaFormu)

        self.anasayfaform.actionTahmini_Gider_Tablolar.triggered.connect(self.TahminiGiderTablosuYapmaFormu)

        self.anasayfaform.actionGer_ekle_mi_Gider_Tablolar.triggered.connect(self.GercekGiderTablosuFormu)

        self.anasayfaform.actionGer_ekle_mi_Gelir_Tablolar.triggered.connect(self.GercekGelirTablosuFormu)

        self.anasayfaform.actionVergi_Numaras_ve_Kontrol.triggered.connect(self.VergiNoForm)


    def GelirTahminiYapmaFormu(self):
        self.geltahyapform.show()

    def GiderTahminiYapmaFormu(self):
        self.gidtahyapform.show()

    def GercekGeliriHesaplamaFormu(self):
        self.gergelyapform.show()

    def GercekGideriHesaplamaFormu(self):
        self.gidgeryapform.show()

    def TahminiGelirTablosuYapmaFormu(self):
        self.geltahtabyapform.show()

    def TahminiGiderTablosuYapmaFormu(self):
        self.gidtahtabyapform.show()

    def GercekGiderTablosuFormu(self):
        self.gidtabyapform.show()

    def GercekGelirTablosuFormu(self):
        self.geltabyapform.show()

    def VergiNoForm(self):
        self.vernoform.show()