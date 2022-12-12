## a. qt的基本组件（代码篇）

### 1.APP和窗口显示

```python
from PyQt5.QtWidgets import QApplication,QWidget
```

QApplication：产生一个APP实例，这个实例可以从系统进行数据输入，系统输入的数据以列表形式传入

QWidget：一个窗口类，实例后可以进行各种设置

```python
import sys
from PyQt5.QtWidgets import QApplication,QWidget
#这是对这两个函数的一个简单的使用
if __name__ == "__main__":
    #创建一个QApplication的实例
    app = QApplication(sys.argv)
    #sys.argv用一个列表的形式来收集用户在系统中的输入
    #创建一个窗口
    w = QWidget()
    # 设置窗口尺寸
    w.resize(300,150)
    # 移动窗口
    w.move(300,300)
    #设置窗口标题
    w.setWindowTitle("窗口标题")
    #显示窗口
    w.show()

    #进入程序的主循环，并且通过exit函数保证主循环安全结束
    sys.exit(app.exec_())
```

### 2.四种布局

```python
import PyQt5.QtWidgets as Widgets
# 1.垂直布局
Vertical_Layout = Widgets.QVBoxLayout()
# 2.水平布局
Horizontal_Layout = Widgets.QHBoxLayout()
# 3.栅格布局
Grid_Layout = Widgets.QGridLayout()
# 4.窗体布局
Form_Layout = Widgets.QFormLayout()
```



### 3.六种buttons

```python
import PyQt5.Qtwidgets as widgets
# 1.pushbutton按钮

# 2.toolbutton工具按钮

# 3.radio button单选按钮

# 4.check box

# 5.command link button

# 6.Dialog button Box


```

### 4.两种item views

### 5.三种item widgets

### end.基本组件杂烩

```python
# pyqt5的基本组件
from PyQt5.QtCore import QDateTime, QTimer ,Qt
import PyQt5.QtWidgets as Widgets
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
        #创教标签后设置按键

        self.use_stand_checkbox = QCheckBox("使用标准样式")
        self.use_stand_checkbox.setChecked(True)
        #设置状态为ture

        # 下拉列表选择不同的样式进行更改
        style_combobox.activated[str].connect(self.changeStyle)
        self.use_stand_checkbox.toggled.connect(self.changePalette)

        disable_wiidget_checkbox= QCheckBox("禁用组件")


        #引用大组件，不然里面的self进不来
        self.createTopLeftGroup()
        self.createTopRightGroup()
        self.createBottomLeftTabWidget()
        self.createBottomRightTabWidget()
        self.createProgressbar()


        # 顶端布局
        top_layout = QHBoxLayout()
        # 设置布局
        # 水平布局
        top_layout.addWidget(style_label)
        top_layout.addWidget(style_combobox)
        top_layout.addWidget(self.use_stand_checkbox)
        top_layout.addWidget(disable_wiidget_checkbox)
        # 水平顶端布局添加组件


        # 栅格布局，将布局进行布局
        main_layout = QGridLayout()
        # 栅格布局增加顶端的水平布局
        main_layout.addLayout(top_layout,0,0,1,2)
        # 栅格布局第1行第0个为第一组控件
        main_layout.addWidget(self.top_left_group,1,0)
        # 栅格布局第1行第1个为第二组控件
        main_layout.addWidget(self.top_right_group,1,1)
        # 添加左下角布局
        main_layout.addWidget(self.bottom_left_tabwidget,2,0)
        #添加右下角布局
        main_layout.addWidget(self.bottom_right_group,2,1)
        #添加进度条
        main_layout.addWidget(self.progressbar,3,0,1,2)
        self.setLayout(main_layout)
        # 设置中心布局

        self.setWindowTitle("基本组件")
        # 窗口的名称

    # 定义第一组左上角组件
    def createTopLeftGroup(self):
        self.top_left_group =QGroupBox("第一组")

        #设置组别
        radioButton0 = QRadioButton("单选1")
        radioButton1 = QRadioButton("单选2")
        radioButton2 = QRadioButton("单选3")
        #设置单选按钮radiobutton

        #设置检查按键
        checkbox = QCheckBox("Tri-state checkbox")
        #三态检查框
        checkbox.setTristate(True)
        #设置三态，全选中，半选中，无选中
        checkbox.setCheckState(Qt.PartiallyChecked)

        # 垂直布局
        layout =QVBoxLayout()
        # 垂直布局
        layout.addWidget(radioButton0)
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(checkbox)
        #布局中增加按键
        self.top_left_group.setLayout(layout)

    # 定义第二组的右上角组件
    def createTopRightGroup(self):
        self.top_right_group = QGroupBox("第二组")

        # 设置内容
        default_button = QPushButton("默认button")
        default_button.setDefault(True)

        toggle_button = QPushButton("开关button")
        toggle_button.setCheckable(True)
        toggle_button.setCheckable(True)

        flat_button = QPushButton("FlatButton")
        flat_button.setFlat(True)

        layout = QVBoxLayout()
        layout.addWidget(default_button)
        layout.addWidget(toggle_button)
        layout.addWidget(flat_button)

        self.top_right_group.setLayout(layout)

    # 左下角选项卡布局
    def createBottomLeftTabWidget(self):
        self.bottom_left_tabwidget = QTabWidget()
        # 选择选项卡组件
        self.bottom_left_tabwidget.setSizePolicy(QSizePolicy.Preferred,
                                                 QSizePolicy.Ignored)
        #选项卡中的标签
        tab1 = QWidget()
        tab2 = QWidget()

        tablewidget = QTableWidget(50,2)
        tab1hbox = QHBoxLayout()
        tab1hbox.addWidget(tablewidget)
        tab1.setLayout(tab1hbox)

        textedit = QTextEdit()
        textedit.setPlainText("获取相差\n"
                              "校正相差系数\n"
                              "残余相差")
        tab2hbox = QHBoxLayout()
        tab2hbox.addWidget(textedit)
        tab2.setLayout(tab2hbox)

        self.bottom_left_tabwidget.addTab(tab1,'表格')
        self.bottom_left_tabwidget.addTab(tab2,"文本")

    def createBottomRightTabWidget(self):
        self.bottom_right_group = QGroupBox()

        layout = QGridLayout()
        #设置布局

        lineedit = QLineEdit()
        lineedit.setEchoMode(QLineEdit.Password)
        layout.addWidget(lineedit,0,0,1,2)

        spinbox = QSpinBox(self.bottom_right_group)
        spinbox.setValue(20)
        layout.addWidget(spinbox,1, 0, 1, 2)

        datatime = Widgets.QDateTimeEdit(self.bottom_right_group)
        datatime.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(datatime,2,0,1,2)

        slider = QSlider(Qt.Horizontal) #设置水平和垂直
        slider.setValue(50)
        layout.addWidget(slider,3,0)

        scrollbar = QScrollBar(Qt.Horizontal,self.bottom_right_group)
        scrollbar.setValue(40)
        layout.addWidget(scrollbar,4,0)

        dail = QDial(self.bottom_right_group)
        dail.setValue(20)
        dail.setNotchesVisible(True)
        layout.addWidget(dail,3,1,2,1)

        self.bottom_right_group.setLayout(layout)

    # 构建进度条
    def createProgressbar(self):
        self.progressbar = QProgressBar()
        self.progressbar.setRange(0,1000)
        self.progressbar.setValue(0)

        timer = QTimer(self)
        # qt中事件的处理机制
        timer.timeout.connect(self.advanceProgressBar)
        timer.start(1000)


    def advanceProgressBar(self):
        cur_val = self.progressbar.value()
        max_val = self.progressbar.maximum()

        self.progressbar.setValue(cur_val + (max_val-cur_val)/100)


    # 改变模板
    def changePalette(self):
        if self.use_stand_checkbox.isChecked():
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.originalPalette)

    #改变样式
    def changeStyle(self,style_name):
        QApplication.setStyle(QStyleFactory.create(style_name))
        self.changePalette()

if __name__ =="__main__":
    import sys
    app =QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())
```

## b.qt的基本组件（designer实现篇）

### 1.创建窗口

创建窗口常见的就这四种，一般选择DialogWithoutButtons

![窗口设置1](D:\img\qt学习\窗口设置1.png)

### 2.功能单元说明

进入designer之后左部菜单拥有如下大类

#### Layouts：

四个布局，分别为垂直布局，水平布局，栅格布局，网格布局

#### Spacers：

#### Buttons:

#### Item Views(Model-Based):

列表，树，表格，专栏，

#### Item Widgets(Item-Based):

#### Containers:

容器部件

#### Input Widgets:

各类输入方法

#### Display Widgets:

演示各类信息使用

### 3.编辑和使用designer创建的界面

使用pyuic对界面进行转换，获取界面后，简单引用代码：

```python
import cheat

import sys

from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
#导入相关模块

if __name__ =="__main__":
    #创建一个app从系统接收信息
    app = QApplication(sys.argv)
    #创建一个主窗口
    MainWindow =QMainWindow()
    ui = cheat.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
```



### 3.qt内有四种布局

