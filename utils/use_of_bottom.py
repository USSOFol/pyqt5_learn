"""
本代码将会演示六种button的全部使用方法
"""
from PyQt5.QtCore import QDateTime, QTimer ,Qt
import PyQt5.QtWidgets as Widgets
# 引入基本组件，常用函数
class Button_use(Widgets.QDialog):
    def __init__(self,parent =None):
        super(Button_use,self).__init__(parent)
        # self.originalPalette = Widgets.QApplication.palette()

        # 设置栅格布局，六个按钮使用将会放在栅格里面
        main_layout = Widgets.QGridLayout()



        #添加方法
        self.Use_pushbutton()
        self.Use_toolbutton()
        self.Use_radiobutton()
        self.Use_checkbox()
        self.Use_command_link_button()
        self.Use_dialog_button_box()

        #添加组件
        main_layout.addWidget(self.push_button,0,0)
        main_layout.addWidget(self.tool_button,1,0)
        main_layout.addWidget(self.radio_button,2,0)
        main_layout.addWidget(self.check_box,3,0)
        main_layout.addWidget(self.command_link_button,4,0)
        main_layout.addWidget(self.dial_log_button_box,5,0)

        self.setLayout(main_layout)
        # 设置中心布局
        self.setWindowTitle("六个button")
        # 窗口的名称


    def Use_pushbutton(self):
        """
        pushbutton的使用
        :return:
        """
        self.push_button = Widgets.QGroupBox("pushbuton的使用")

        #pushbotton
        pushbutton1 = Widgets.QPushButton("按钮")

        layout = Widgets.QVBoxLayout()
        layout.addWidget(pushbutton1)

        self.push_button.setLayout(layout)


    def Use_toolbutton(self):
        self.tool_button = Widgets.QGroupBox("toolbuton的使用")

        #pushbotton
        toolbutton1 = Widgets.QToolButton()

        layout = Widgets.QVBoxLayout()
        layout.addWidget(toolbutton1)

        self.tool_button.setLayout(layout)


    def Use_radiobutton(self):
        self.radio_button = Widgets.QGroupBox("radiobuton的使用")

        #pushbotton
        radiobutton1 = Widgets.QRadioButton("单选1")

        layout = Widgets.QVBoxLayout()
        layout.addWidget(radiobutton1)

        self.radio_button.setLayout(layout)


    def Use_checkbox(self):
        self.check_box = Widgets.QGroupBox("checkbox的使用")

        #pushbotton
        checkbox1 = Widgets.QCheckBox("功能")

        layout = Widgets.QVBoxLayout()
        layout.addWidget(checkbox1)

        self.check_box.setLayout(layout)

    def Use_command_link_button(self):
        self.command_link_button = Widgets.QGroupBox("commandlinkbutton的使用")

        #pushbotton
        commandlinkbutton1 = Widgets.QCommandLinkButton("转到")

        layout = Widgets.QVBoxLayout()
        layout.addWidget(commandlinkbutton1)

        self.command_link_button.setLayout(layout)

    def Use_dialog_button_box(self):
        self.dial_log_button_box = Widgets.QGroupBox("dialog_button_box的使用")

        #pushbotton
        dialogbuttonbox1 = Widgets.QDialogButtonBox()

        layout = Widgets.QVBoxLayout()
        layout.addWidget(dialogbuttonbox1)

        self.dial_log_button_box.setLayout(layout)





if __name__ == "__main__":
    import sys
    app = Widgets.QApplication(sys.argv)
    gallery = Button_use()
    gallery.show()
    sys.exit(app.exec_())