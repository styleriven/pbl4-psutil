
import time
from datetime import datetime
import shutil
from SetInterVal import setInterval
import psutil
from mainFrm import *
from qt_material import *
from PyQt5 import *


from PyQt5.QtChart import QChart, QChartView, QLineSeries
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
    k=0
    uname = platform.uname()
    series =QLineSeries()
    def __init__(self) :
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        # Load Style sheet, this will overide and fonts selected in qt designer
       
        
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
        
       
        
        
        #pages
        #Home
        self.ui.home_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.Home))
        #CPU
        self.ui.cpu_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.CPU))
        #RAM
        self.ui.memory_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.Memory))
        #Disk  
        self.ui.storage_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.Storage))
        
        
        self.ui.menu_btn.clicked.connect(lambda:self.slideLeftMenu())
        
        # for w in self.ui.menu_frame.findChildren(QPushButton):
        #     w.clicked.connect(self.applyButtonStyle)
        global intervalCPU,intervalRam,intervalTime
        intervalCPU = setInterval(1, self.cpu)
        intervalRam = setInterval(1, self.ram)
        intervalTime = setInterval(1, self.dongHo)
        self.storage()
        self.Hello()
        time.sleep(1)
        
        self.show()
    
    
    
    def Hello(self):
        self.ui.lblHello.setText("Hello " + self.uname.node);
    
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        intervalCPU.cancel()
        intervalRam.cancel()
        intervalTime.cancel()
        return super().closeEvent(a0)
    
    
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
        print("ram")
        totalRam = 1.0
        totalRam = psutil.virtual_memory().total * totalRam
        totalRam = totalRam /(1024*1024*1024)
        self.ui.lblTotalRam.setText(str("{:.4f}".format(totalRam) + 'GB'))
        
        availRam = 1.0
        availRam = psutil.virtual_memory().available * availRam
        availRam = availRam /(1024*1024*1024)
        self.ui.lblAvailableRam.setText(str("{:.4f}".format(availRam) + 'GB'))

        
        ramUesd = 1.0
        ramUesd = psutil.virtual_memory().used * ramUesd
        ramUesd = ramUesd /(1024*1024*1024)
        self.ui.lblUsedRam.setText(str("{:.4f}".format(ramUesd) + 'GB'))
        
        
        ramFree = 1.0
        ramFree = psutil.virtual_memory().free * ramFree
        ramFree = ramFree /(1024*1024*1024)
        self.ui.lblFreeRam.setText(str("{:.4f}".format(ramFree) + 'GB'))
        
        
              
    
    def cpu(self):
        print("cpu")
        
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
        
        self.series.append(0, 0)
        

        x = datetime.datetime.now().strftime("%X")
        self.series.append(QPointF(cpuPer, x))
        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("CPU")

        self.chartView = QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chart.setAnimationOptions(QChart.AllAnimations)
        self.chartView.chart().setTheme(QChart.ChartThemeDark)


        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chartView.sizePolicy().hasHeightForWidth())
        self.chartView.setSizePolicy(sizePolicy)
        self.chartView.setMinimumSize(QSize(0, 300))
        layout = QVBoxLayout();
        layout.addWidget(self.chartView)
        self.ui.frame_25.setLayout(layout)
        self.ui.frame_25.setStyleSheet(u"background-color: transparent")
        
    def create_table_widget(self,rowPosition,columnPosition,text,tableName):
        qtableWidgetItem = QTableWidgetItem()   
        
        getattr(self.ui, tableName).setItem(rowPosition, columnPosition, qtableWidgetItem)
        qtableWidgetItem = getattr(self.ui,tableName).item(rowPosition, columnPosition)
        
        qtableWidgetItem.setText(str(text))

    
    def dongHo(self):
        print("Dong Ho")
        now = datetime.now()

        s = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second)
        print(s)
        self.ui.lblTime.setText(str(s))

        
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
        
        