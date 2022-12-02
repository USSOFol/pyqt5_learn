# pyqt5的基本组件
from PyQt5.QtCore import QDateTime, QTimer ,Qt
from PyQt5.QtWidgets import (QApplication,QGridLayout,
                             QHBoxLayout, QVBoxLayout,

                             QGroupBox,QTabWidget,
                             QLabel,QCheckBox,
                             QRadioButton,QComboBox,
                             QLineEdit,QTextEdit,
                             QDialog,QPushButton,
                             QSlider,QScroller,
                             QScrollBar,QTableWidget,
                             QSpinBox,QTableView,
                             QProgressBar,QDial,
                             QWidget,QStyleFactory,QSizePolicy)
# 引入基本组件，常用函数
class WidgetGallery(QDialog):
    def __init__(self,parent =None):
        """
        设置自定义样式
        :param parent:
        """
        super(WidgetGallery,self).__init__(parent)
        self.originalPalette = QApplication.palette()

        #下拉列表
        style_combobox = QComboBox()
        #创建一个多选列表
        style_combobox.addItems(QStyleFactory.keys())
        #添加选项

        #标签
        style_label = QLabel("样式")
        style_label.setBuddy(style_combobox)

        self.use_stand_checkbox = QCheckBox("使用标准样式")
        self.use_stand_checkbox.setChecked(True)

        disable_wiidget_checkbox= QCheckBox("禁用组件")
        self.createTopLeftGroup()
        # 顶端布局
        top_layout = QHBoxLayout()
        # 水平布局
        top_layout.addWidget(style_label)
        top_layout.addWidget(style_combobox)
        top_layout.addWidget(self.use_stand_checkbox)
        top_layout.addWidget(disable_wiidget_checkbox)

        main_layout = QGridLayout()
        main_layout.addLayout(top_layout,0,0,1,2)
        #
        main_layout.addWidget(self.top_left_group,1,0)
        self.setLayout(main_layout)
        self.setWindowTitle("基本组件")

    # 定义第一组左上角组件
    def createTopLeftGroup(self):
        self.top_left_group =QGroupBox("第一组")
        radioButton0 = QRadioButton("单选1")
        radioButton1 = QRadioButton("单选2")
        radioButton2 = QRadioButton("单选3")

        checkbox = QCheckBox("Tri-state checkbox")
        checkbox.setTristate(True)
        checkbox.setCheckState(Qt.PartiallyChecked)

        # 垂直布局
        layout =QVBoxLayout()
        # 垂直布局
        layout.addWidget(radioButton0)
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(checkbox)
        self.top_left_group.setLayout(layout)


if __name__ =="__main__":
    import sys
    app =QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())












