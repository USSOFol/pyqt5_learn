import sys
from utils import learn
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ =="__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    #设置窗口
    ui = learn.Ui_MainWindow()
    #获取UI
    ui.setupUi(MainWindow)
    #UI载入窗口
    MainWindow.show()
    #显示
    sys.exit(app.exec_())