
import time
import shutil
from SetInterVal import setInterval
import psutil
from mainFrm import *
from qt_material import *
from PyQt5 import *
# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.sip import *
from PySide2extn import *

platforms= {
    'linux': 'Linux',
    'linux1': 'Linux',
    'linux2': 'Linux',
    'darwin': 'OS X',
    'win32': 'Windows'
}

class MAINFRMHANDLE(QMainWindow):
    def __init__(self,app) :
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        # Load Style sheet, this will overide and fonts selected in qt designer
       
        apply_stylesheet(app,theme='dark_blue.xml')
        #remove window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #set main background to trasparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # set main background to transparent
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,550))
        # apply shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        #set window icon and title will not appear on our app maon window because we removed the title bar
        self.setWindowIcon(QtGui.QIcon(":/icons/icon/airplay.svg"))
        #set window title
        self.setWindowTitle("UTIL Manager")
        
       
        #event handler
        self.ui.minimize_button.clicked.connect(lambda:self.showMinimized())
        #Close
        self.ui.close_button.clicked.connect(lambda:self.cancel())
        #Restore/Maximize
        self.ui.restore_button.clicked.connect(lambda:self.restore_or_maximize())   
        
        #pages
        #Home
        self.ui.home_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.Home))
        #CPU
        self.ui.cpu_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.CPU))
        #RAM
        self.ui.memory_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.Memory))
        #Swap
        self.ui.swap_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.Swap))
        #Disk  
        self.ui.storage_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.Storage))
        
        def moveWindow(e):
            if self.isMaximized()==False:
                if e.buttons()==Qt.LeftButton:
                    self.move(self.pos()+e.globalPos() - self.clickPostion)
                    self.clickPostion = e.globalPos()
                    e.accept() 
 
    
        self.ui.header_frame.mouseMoveEvent = moveWindow
        
        self.ui.menu_btn.clicked.connect(lambda:self.slideLeftMenu())
        
        # for w in self.ui.menu_frame.findChildren(QPushButton):
        #     w.clicked.connect(self.applyButtonStyle)
        global intervalCPU,intervalRam
        intervalCPU = setInterval(1, self.cpu)
        intervalRam = setInterval(1, self.ram)
        self.storage()
       
        time.sleep(1)
        
        self.show()
    
    def cancel(self):
        intervalCPU.cancel()
        intervalRam.cancel()
        self.close()
    def storage(self):
        global platforms
        storage_device= psutil.disk_partitions(all=False)
        for x in storage_device:
            rowPositions= self.ui.storageTable.rowCount()
            self.ui.storageTable.insertRow(rowPositions)
            self.create_table_widget(rowPositions, 0, x.device, "storageTable")
            self.create_table_widget(rowPositions, 1, x.mountpoint, "storageTable")
            self.create_table_widget(rowPositions, 2, x.fstype, "storageTable")
            self.create_table_widget(rowPositions, 3, x.opts, "storageTable")
            
            if sys.platform == 'linux' or sys.platform == 'linux1' or sys.platform == 'linux2':
                self.create_table_widget(rowPositions, 4, x.maxfile, "storageTable")
                self.create_table_widget(rowPositions, 5, x.maxpath, "storageTable")
            else:
                self.create_table_widget(rowPositions, 4, "Function not available on " + platforms[sys.platforms],"storageTable" )
                self.create_table_widget(rowPositions, 5, "Function not available on " + platforms[sys.platforms],"storageTable" )
            disk_usage = shutil.disk_usage(x.mountpoint)
            
            self.create_table_widget(rowPositions,6, str(round((disk_usage.total / (1024*1024*1024)), 2)) + "GB","storageTable")
            self.create_table_widget(rowPositions,7, str(round((disk_usage.used / (1024*1024*1024)), 2)) + "GB","storageTable")
            self.create_table_widget(rowPositions,8, str(round((disk_usage.free / (1024*1024*1024)), 2)) + "GB","storageTable")
            
            full_disk = (disk_usage.used/ disk_usage.total)*100
            progressBar = QProgressBar(self.ui.storageTable)
            progressBar.setObjectName("progressBar")
            progressBar.setValue(int(full_disk))
            self.ui.storageTable.setCellWidget(rowPositions, 9, progressBar)
            
            
    def ram(self):
        totalRam = 1.0
        totalRam = psutil.virtual_memory().total * totalRam
        totalRam = totalRam /(1024*1024*1024)
        self.ui.lblTotalRam.setText(str("{:.4f}".format(totalRam) + 'GB'))
        
        availRam = 1.0
        availRam = psutil.virtual_memory().available * availRam
        availRam = availRam /(1024*1024*1024)
        self.ui.lblAvailableRam.setText(str("{:.4f}".format(availRam) + 'GB'))
        self.ui.lblAvailableRam.setStyleSheet("border: 2px  groove rgb(6,233,38);")
        
        ramUesd = 1.0
        ramUesd = psutil.virtual_memory().used * ramUesd
        ramUesd = ramUesd /(1024*1024*1024)
        self.ui.lblUsedRam.setText(str("{:.4f}".format(ramUesd) + 'GB'))
        self.ui.lblUsedRam.setStyleSheet("border: 2px  groove rgb(6,201,233);")
        
        
        ramFree = 1.0
        ramFree = psutil.virtual_memory().free * ramFree
        ramFree = ramFree /(1024*1024*1024)
        self.ui.lblFreeRam.setText(str("{:.4f}".format(ramFree) + 'GB'))
        self.ui.lblFreeRam.setStyleSheet("border: 2px  groove rgb(233,6,201);")
        
        
        self.ui.ram_percentage.spb_setMinimum((0,0,0))
        self.ui.ram_percentage.spb_setMaximum((totalRam,totalRam,totalRam))
        self.ui.ram_percentage.spb_setValue((availRam, ramUesd, ramFree))
        self.ui.ram_percentage.spb_lineColor(((6,233,38), (6,201,233), (233,6,201)))
        self.ui.ram_percentage.spb_setInitialPos(('West','West','West'))
        self.ui.ram_percentage.spb_lineWidth(15)
        self.ui.ram_percentage.spb_lineCap(('RoundCap','RoundCap','RoundCap'))
        self.ui.ram_percentage.spb_setPathHidden(True)        
    
    def cpu(self):
        
        core =psutil.cpu_count()
        self.ui.lblCores.setText(str(core))
        
        mainCores = psutil.cpu_count(False)
        self.ui.lblMainCores.setText(str(mainCores))
        
        cpuPer= psutil.cpu_percent()
        self.ui.lblCPU_Per.setText(str(cpuPer))
        
        cpuIdle=psutil.cpu_times_percent().idle
        self.ui.lblCPU_Idle.setText(str(cpuIdle))
        
        cpuUser=psutil.cpu_times_percent().user
        self.ui.lblCPU_User.setText(str(cpuUser))
        
        cpuSystem=psutil.cpu_times_percent().system
        self.ui.lblCPU_System.setText(str(cpuSystem))
        
        self.ui.cpu_percentage.rpb_setMaximum(100)
        self.ui.cpu_percentage.rpb_setMinimum(0)
        self.ui.cpu_percentage.rpb_setValue(cpuPer)
        self.ui.cpu_percentage.rpb_setBarStyle('Hybrid2')
        self.ui.cpu_percentage.rpb_setLineColor((255,30,99))
        self.ui.cpu_percentage.rpb_setPieColor((45,74,83))
        self.ui.cpu_percentage.rpb_setTextColor((255,255,255))
        self.ui.cpu_percentage.rpb_setInitialPos('West')
        self.ui.cpu_percentage.rpb_setTextFont('Arial')
        self.ui.cpu_percentage.rpb_setLineWidth(15)
        self.ui.cpu_percentage.rpb_setPathWidth(15)
        self.ui.cpu_percentage.rpb_setLineCap('RoundCap')
        
    def create_table_widget(self,rowPosition,columnPosition,text,tableName):
        qtableWidgetItem = QTableWidgetItem()   
        
        getattr(self.ui, tableName).setItem(rowPosition, columnPosition, qtableWidgetItem)
        qtableWidgetItem = getattr(self.ui,tableName).item(rowPosition, columnPosition)
        
        qtableWidgetItem.setText(str(text))

    
    def mousePressEvent(self, event) :
        self.clickPostion = event.globalPos()   
        
    def slideLeftMenu(self):
        width=self.ui.menu_frame.width()
        if width == 41:
            newWidth = 170
        else:
            newWidth =41
        self.animatiion = QPropertyAnimation(self.ui.menu_frame,b"minimumWidth")
        self.animatiion.setDuration(250)
        self.animatiion.setStartValue(width)
        self.animatiion.setEndValue(newWidth)
        self.animatiion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animatiion.start()
        
        
            
    def restore_or_maximize(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_button.setIcon(QtGui.QIcon(":/icons/icon/cil-window-restore.svg"))
        else:
            self.showMaximized()
            self.ui.restore_button.setIcon(QtGui.QIcon(":/icons/icon/square.svg"))    
