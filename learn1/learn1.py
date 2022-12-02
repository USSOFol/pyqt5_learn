import sys
from PyQt5.QtWidgets import QApplication,QWidget
#

if __name__ == "__main__":
    #创建一个QApplication的实例
    app = QApplication(sys.argv)
    #sys.argv用一个列表的形式来收集用户在系统中的输入
    #创建一个窗口
    w = QWidget()
    # 设置窗口尺寸
    w.resize(300,150)
    # 移动窗口,这里定义的是窗口左上角初始位置
    w.move(1000,300)
    #设置窗口标题
    w.setWindowTitle("窗口标题")
    #显示窗口
    w.show()

    #进入程序的主循环，并且通过exit函数保证主循环安全结束
    sys.exit(app.exec_())




