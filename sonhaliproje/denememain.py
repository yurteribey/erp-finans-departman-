    
    
from PyQt5.QtWidgets import QApplication
from girisyapma import GirisYapmaPage

app=QApplication([])
pencere = GirisYapmaPage()
pencere.show()
app.exec_()
