# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainFrm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(930, 655)
        icon = QIcon()
        icon.addFile(u":/icons/icon/memory.", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"text-align:left;\n"
"padding:0;\n"
"margin:0;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu_btn = QPushButton(self.header_right_frame)
        self.menu_btn.setObjectName(u"menu_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon1)
        self.menu_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.menu_btn)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignLeft)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.header_center_frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setPixmap(QPixmap(u":/icons/icon/airplay.svg"))

        self.horizontalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.header_center_frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.header_center_frame)

        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_button = QPushButton(self.header_left_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon2)
        self.minimize_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.minimize_button)

        self.restore_button = QPushButton(self.header_left_frame)
        self.restore_button.setObjectName(u"restore_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/cil-window-restore.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon3)
        self.restore_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.restore_button)

        self.close_button = QPushButton(self.header_left_frame)
        self.close_button.setObjectName(u"close_button")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon4)
        self.close_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.close_button)


        self.horizontalLayout.addWidget(self.header_left_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy2)
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.main_left_frame = QFrame(self.main_body_frame)
        self.main_left_frame.setObjectName(u"main_left_frame")
        self.main_left_frame.setFrameShape(QFrame.StyledPanel)
        self.main_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.main_left_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.main_left_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(41, 0))
        self.menu_frame.setMaximumSize(QSize(20, 16777215))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 0, 0, 0)
        self.main_contain_frame_2 = QFrame(self.menu_frame)
        self.main_contain_frame_2.setObjectName(u"main_contain_frame_2")
        self.main_contain_frame_2.setMinimumSize(QSize(170, 0))
        self.main_contain_frame_2.setFrameShape(QFrame.StyledPanel)
        self.main_contain_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_contain_frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 0, -1, 0)
        self.home_page_btn = QPushButton(self.main_contain_frame_2)
        self.home_page_btn.setObjectName(u"home_page_btn")
        self.home_page_btn.setStyleSheet(u"padding:0px 9px;\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_page_btn.setIcon(icon5)
        self.home_page_btn.setIconSize(QSize(40, 32))

        self.verticalLayout_3.addWidget(self.home_page_btn)

        self.cpu_page_btn = QPushButton(self.main_contain_frame_2)
        self.cpu_page_btn.setObjectName(u"cpu_page_btn")
        self.cpu_page_btn.setStyleSheet(u"padding:0px 9px;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icon/cpu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cpu_page_btn.setIcon(icon6)
        self.cpu_page_btn.setIconSize(QSize(40, 32))

        self.verticalLayout_3.addWidget(self.cpu_page_btn)

        self.memory_page_btn = QPushButton(self.main_contain_frame_2)
        self.memory_page_btn.setObjectName(u"memory_page_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icon/ram-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.memory_page_btn.setIcon(icon7)
        self.memory_page_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.memory_page_btn)

        self.swap_page_btn = QPushButton(self.main_contain_frame_2)
        self.swap_page_btn.setObjectName(u"swap_page_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icon/swap.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.swap_page_btn.setIcon(icon8)
        self.swap_page_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.swap_page_btn)

        self.storage_page_btn = QPushButton(self.main_contain_frame_2)
        self.storage_page_btn.setObjectName(u"storage_page_btn")
        self.storage_page_btn.setStyleSheet(u"padding:0px 9px;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icon/disc.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_page_btn.setIcon(icon9)
        self.storage_page_btn.setIconSize(QSize(40, 32))

        self.verticalLayout_3.addWidget(self.storage_page_btn)


        self.verticalLayout_2.addWidget(self.main_contain_frame_2, 0, Qt.AlignTop)


        self.horizontalLayout_9.addWidget(self.menu_frame)


        self.horizontalLayout_8.addWidget(self.main_left_frame, 0, Qt.AlignLeft)

        self.main_contain_frame = QFrame(self.main_body_frame)
        self.main_contain_frame.setObjectName(u"main_contain_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_contain_frame.sizePolicy().hasHeightForWidth())
        self.main_contain_frame.setSizePolicy(sizePolicy3)
        self.main_contain_frame.setFrameShape(QFrame.StyledPanel)
        self.main_contain_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_contain_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.main_contain_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.stackedWidget.addWidget(self.Home)
        self.CPU = QWidget()
        self.CPU.setObjectName(u"CPU")
        self.verticalLayout_7 = QVBoxLayout(self.CPU)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_21 = QFrame(self.CPU)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy2.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy2)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_21)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_25 = QFrame(self.frame_21)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy2.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy2)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_25)

        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_23)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setVerticalSpacing(8)
        self.formLayout_3.setContentsMargins(-1, 20, -1, 21)
        self.label_46 = QLabel(self.frame_23)
        self.label_46.setObjectName(u"label_46")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_46)

        self.lblCPU_Per = QLabel(self.frame_23)
        self.lblCPU_Per.setObjectName(u"lblCPU_Per")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lblCPU_Per)

        self.label_48 = QLabel(self.frame_23)
        self.label_48.setObjectName(u"label_48")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_48)

        self.lblCPU_Idle = QLabel(self.frame_23)
        self.lblCPU_Idle.setObjectName(u"lblCPU_Idle")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lblCPU_Idle)

        self.label_64 = QLabel(self.frame_23)
        self.label_64.setObjectName(u"label_64")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_64)

        self.lblCPU_System = QLabel(self.frame_23)
        self.lblCPU_System.setObjectName(u"lblCPU_System")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lblCPU_System)

        self.lblCPU_User = QLabel(self.frame_23)
        self.lblCPU_User.setObjectName(u"lblCPU_User")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lblCPU_User)

        self.label_66 = QLabel(self.frame_23)
        self.label_66.setObjectName(u"label_66")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_66)

        self.lblCores = QLabel(self.frame_23)
        self.lblCores.setObjectName(u"lblCores")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.lblCores)

        self.label_68 = QLabel(self.frame_23)
        self.label_68.setObjectName(u"label_68")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_68)

        self.lblMainCores = QLabel(self.frame_23)
        self.lblMainCores.setObjectName(u"lblMainCores")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.lblMainCores)

        self.label_69 = QLabel(self.frame_23)
        self.label_69.setObjectName(u"label_69")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_69)


        self.horizontalLayout_13.addWidget(self.frame_23, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy4)
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.cpu_percentage = roundProgressBar(self.frame_24)
        self.cpu_percentage.setObjectName(u"cpu_percentage")
        self.cpu_percentage.setMinimumSize(QSize(200, 200))
        self.cpu_percentage.setMaximumSize(QSize(200, 200))

        self.horizontalLayout_10.addWidget(self.cpu_percentage)


        self.horizontalLayout_13.addWidget(self.frame_24)


        self.verticalLayout_8.addWidget(self.frame_22)


        self.verticalLayout_7.addWidget(self.frame_21)

        self.stackedWidget.addWidget(self.CPU)
        self.Memory = QWidget()
        self.Memory.setObjectName(u"Memory")
        self.verticalLayout_4 = QVBoxLayout(self.Memory)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_26 = QFrame(self.Memory)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy2.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy2)
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_26)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy2.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy2)
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 3, 0, 4)
        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_29)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setVerticalSpacing(8)
        self.formLayout_4.setContentsMargins(-1, 13, -1, 21)
        self.label_50 = QLabel(self.frame_29)
        self.label_50.setObjectName(u"label_50")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_50)

        self.lblTotalRam = QLabel(self.frame_29)
        self.lblTotalRam.setObjectName(u"lblTotalRam")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lblTotalRam)

        self.label_52 = QLabel(self.frame_29)
        self.label_52.setObjectName(u"label_52")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_52)

        self.lblAvailableRam = QLabel(self.frame_29)
        self.lblAvailableRam.setObjectName(u"lblAvailableRam")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.lblAvailableRam)

        self.label_70 = QLabel(self.frame_29)
        self.label_70.setObjectName(u"label_70")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_70)

        self.lblUsedRam = QLabel(self.frame_29)
        self.lblUsedRam.setObjectName(u"lblUsedRam")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.lblUsedRam)

        self.label_72 = QLabel(self.frame_29)
        self.label_72.setObjectName(u"label_72")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_72)

        self.lblFreeRam = QLabel(self.frame_29)
        self.lblFreeRam.setObjectName(u"lblFreeRam")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.lblFreeRam)


        self.horizontalLayout_14.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_28)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy4.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy4)
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.ram_percentage = spiralProgressBar(self.frame_30)
        self.ram_percentage.setObjectName(u"ram_percentage")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(150)
        sizePolicy5.setVerticalStretch(150)
        sizePolicy5.setHeightForWidth(self.ram_percentage.sizePolicy().hasHeightForWidth())
        self.ram_percentage.setSizePolicy(sizePolicy5)
        self.ram_percentage.setMinimumSize(QSize(200, 200))
        self.ram_percentage.setMaximumSize(QSize(200, 200))

        self.horizontalLayout_11.addWidget(self.ram_percentage)


        self.horizontalLayout_14.addWidget(self.frame_30)


        self.verticalLayout_9.addWidget(self.frame_28, 0, Qt.AlignBottom)


        self.verticalLayout_4.addWidget(self.frame_26)

        self.stackedWidget.addWidget(self.Memory)
        self.Swap = QWidget()
        self.Swap.setObjectName(u"Swap")
        self.stackedWidget.addWidget(self.Swap)
        self.Storage = QWidget()
        self.Storage.setObjectName(u"Storage")
        self.verticalLayout_10 = QVBoxLayout(self.Storage)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.Storage)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_4.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_4)

        self.storageTable = QTableWidget(self.Storage)
        if (self.storageTable.columnCount() < 10):
            self.storageTable.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.storageTable.setObjectName(u"storageTable")

        self.verticalLayout_10.addWidget(self.storageTable)

        self.stackedWidget.addWidget(self.Storage)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.main_contain_frame)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame = QFrame(self.footer_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)


        self.horizontalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(self.footer_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Help_btn = QPushButton(self.frame_2)
        self.Help_btn.setObjectName(u"Help_btn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icon/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Help_btn.setIcon(icon10)
        self.Help_btn.setIconSize(QSize(32, 24))

        self.horizontalLayout_7.addWidget(self.Help_btn, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.frame_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"THNJR", None))
        self.minimize_button.setText("")
        self.restore_button.setText("")
        self.close_button.setText("")
        self.home_page_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.cpu_page_btn.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.memory_page_btn.setText(QCoreApplication.translate("MainWindow", u"Memory", None))
        self.swap_page_btn.setText(QCoreApplication.translate("MainWindow", u"Swap", None))
        self.storage_page_btn.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"CPU_Per:", None))
        self.lblCPU_Per.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"CPU_Idle:", None))
        self.lblCPU_Idle.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"CPU_System:", None))
        self.lblCPU_System.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.lblCPU_User.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"cores:", None))
        self.lblCores.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Main cores:", None))
        self.lblMainCores.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"CPU_User", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Total Ram:", None))
        self.lblTotalRam.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Available Ram", None))
        self.lblAvailableRam.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Used Ram:", None))
        self.lblUsedRam.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Free Ram:", None))
        self.lblFreeRam.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Disk Partition", None))
        ___qtablewidgetitem = self.storageTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Device", None));
        ___qtablewidgetitem1 = self.storageTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Mount point", None));
        ___qtablewidgetitem2 = self.storageTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"OPTS", None));
        ___qtablewidgetitem3 = self.storageTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Max", None));
        ___qtablewidgetitem4 = self.storageTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Max file", None));
        ___qtablewidgetitem5 = self.storageTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Max Path", None));
        ___qtablewidgetitem6 = self.storageTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Total Storage", None));
        ___qtablewidgetitem7 = self.storageTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Used Storage", None));
        ___qtablewidgetitem8 = self.storageTable.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Free storage", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | Copyright Njr.", None))
        self.Help_btn.setText("")
    # retranslateUi

