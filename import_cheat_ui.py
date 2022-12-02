import cheat
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow

if __name__ =="__main__":
    app = QApplication(sys.argv)
    MainWindow =QMainWindow()
    ui = cheat.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
