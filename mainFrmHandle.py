
import time
from datetime import datetime
import shutil
import psutil
from mainFrm import *
from qt_material import *
from PyQt5 import *
from matplotlib import pyplot as plt

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.figure import Figure

import platform, subprocess, re
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.sip import *




platforms= {
    'linux': 'Linux',
    'linux1': 'Linux',
    'linux2': 'Linux',
    'darwin': 'OS X',
    'win32': 'Windows'
}

class MAINFRMHANDLE(QMainWindow):
    
    uname = platform.uname()
    heightCPU=[]
    n_data = 60
    heightRam=[]
    for i in range(0,n_data):
        heightCPU.append(0)
        heightRam.append(0)
    def __init__(self) :
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.info = str(subprocess.check_output(["inxi", "-Fxz"])).split("\\n")
        self.infoCPU = str(subprocess.check_output(["lscpu"])).split("\\n")
        self.infoRam = str(subprocess.check_output(["sudo","dmidecode","--type","memory"])).split("\\n")
        
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
        global tCPU 
        tCPU = 0
        
        
        #pages
        #Home
        self.ui.home_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.Home))
        #CPU
        self.ui.cpu_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.CPU))
        #RAM
        self.ui.memory_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.Memory))
        #Disk  
        self.ui.storage_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.Storage))
        #Networks  
        self.ui.activiteles_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.Activiteles))
        #Networks  
        self.ui.sensors_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.Sensor))
        #Networks  
        self.ui.networks_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.Networks))
        
        
        self.ui.menu_btn.clicked.connect(lambda:self.slideLeftMenu())
        
        
        self.interval=1000
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.cpu)
        self.timer.timeout.connect(self.ram)
        self.timer.timeout.connect(self.dongHo)
        self.veCPU()
        self.timer.timeout.connect(self.update_CPU)
        self.veRam()
        self.timer.timeout.connect(self.update_Ram)
        self.timer.timeout.connect(self.Pin)
        self.timer.timeout.connect(self.Temperature)
        self.timer.start()
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
        self.system()
        self.machine()
        self.storage()
        self.grapphics()
        self.Hello()
        self.lsCPU()
        self.lsRam()
        self.processes()
        self.sensors()
        self.network()
        time.sleep(1)
        
        for w in self.ui.menu_frame.findChildren(QPushButton):
            w.clicked.connect(self.applyButtonStyle)
        
        self.show()
    
    def network(self):
        for x in psutil.net_if_stats():
            z = psutil.net_if_stats()
            rowPosition = self.ui.twStatus.rowCount()
            self.ui.twStatus.insertRow(rowPosition)

            self.create_table_widget(rowPosition,0, x,"twStatus")
            self.create_table_widget(rowPosition,1, str(z[x].isup),"twStatus")
            self.create_table_widget(rowPosition,2, str(z[x].duplex),"twStatus")
            self.create_table_widget(rowPosition,3, str(z[x].speed),"twStatus")
            self.create_table_widget(rowPosition,4, str(z[x].mtu),"twStatus")
            
        for x in psutil.net_io_counters(pernic=True):
            z = psutil.net_io_counters(pernic=True)
            rowPosition = self.ui.twCounters.rowCount()
            self.ui.twCounters.insertRow(rowPosition)
            
            self.create_table_widget(rowPosition,0, x,"twCounters")
            self.create_table_widget(rowPosition,1, str(z[x].bytes_sent),"twCounters")
            self.create_table_widget(rowPosition,2, str(z[x].bytes_recv),"twCounters")
            self.create_table_widget(rowPosition,3, str(z[x].packets_sent),"twCounters")
            self.create_table_widget(rowPosition,4, str(z[x].packets_recv),"twCounters")
            self.create_table_widget(rowPosition,5, str(z[x].errin),"twCounters")
            self.create_table_widget(rowPosition,6, str(z[x].errout),"twCounters")
            self.create_table_widget(rowPosition,7, str(z[x].dropin),"twCounters")
            self.create_table_widget(rowPosition,8, str(z[x].dropout),"twCounters")
            
            
            
        for x in psutil.net_if_addrs():
            z=psutil.net_if_addrs()
            
            for y in z[x]:
                rowPosition = self.ui.twAddresses.rowCount()
                self.ui.twAddresses.insertRow(rowPosition)
                
                self.create_table_widget(rowPosition,0, str(x),"twAddresses")
                self.create_table_widget(rowPosition,1, str(y.family),"twAddresses")
                self.create_table_widget(rowPosition,2, str(y.address),"twAddresses")
                self.create_table_widget(rowPosition,3, str(y.netmask),"twAddresses")
                self.create_table_widget(rowPosition,4, str(y.broadcast),"twAddresses")
                self.create_table_widget(rowPosition,5, str(y.ptp),"twAddresses")
                
        for x in psutil.net_connections():
            z = psutil.net_connections()
            
            rowPosition = self.ui.twConnections.rowCount()
            self.ui.twConnections.insertRow(rowPosition)
            
            self.create_table_widget(rowPosition,0, str(x.fd),"twConnections")
            self.create_table_widget(rowPosition,1, str(x.family),"twConnections")
            self.create_table_widget(rowPosition,2, str(x.type),"twConnections")
            self.create_table_widget(rowPosition,3, str(x.laddr),"twConnections")
            self.create_table_widget(rowPosition,4, str(x.raddr),"twConnections")
            self.create_table_widget(rowPosition,5, str(x.status),"twConnections")
            self.create_table_widget(rowPosition,6, str(x.pid),"twConnections")
                
                



    def sensors(self):
        
        for x in psutil.sensors_temperatures():
            for y in psutil.sensors_temperatures()[x]:
                rowPosition = self.ui.twSensor.rowCount()
                self.ui.twSensor.insertRow(rowPosition)
                
                self.create_table_widget(rowPosition,0, x,"twSensor")
                self.create_table_widget(rowPosition,1, y.label,"twSensor")
                self.create_table_widget(rowPosition,2, str(y.current),"twSensor")
                self.create_table_widget(rowPosition,3, str(y.high),"twSensor")
                self.create_table_widget(rowPosition,4, str(y.critical),"twSensor")
                
                    
    
    def findName(self):
        name = self.ui.activity_search.text().lower()
        for row in range(self.ui.twActivititese.rowCount()):
            item = self.ui.twActivititese.item(row, 1)
            self.ui.twActivititese.setRowHidden(row, name not in item.text().lower())
    
    def processes(self):
        for x in psutil.pids():
            rowPosition = self.ui.twActivititese.rowCount()
            self.ui.twActivititese.insertRow(rowPosition)
            
            try:
                process = psutil.Process(x)
                
                self.create_table_widget(rowPosition, 0 ,str(process.pid),"twActivititese")
                self.create_table_widget(rowPosition, 1 ,str(process.name()),"twActivititese")
                self.create_table_widget(rowPosition, 2 ,str(process.status()),"twActivititese")
                self.create_table_widget(rowPosition, 3 ,str(datetime.utcfromtimestamp(process.create_time()).strftime('%d/%m/%Y %H:%M:%S')),"twActivititese")
                
                suspend_btn = QPushButton(self.ui.twActivititese)
                suspend_btn.setText("Suspend")
                suspend_btn.setStyleSheet("color: brown")
                self.ui.twActivititese.setCellWidget(rowPosition,4,suspend_btn)
                
                resume_btn = QPushButton(self.ui.twActivititese)
                resume_btn.setText("Resume")
                resume_btn.setStyleSheet("color: green")
                self.ui.twActivititese.setCellWidget(rowPosition,5,resume_btn)
                
                terminate_btn = QPushButton(self.ui.twActivititese)
                terminate_btn.setText("Terminate")
                terminate_btn.setStyleSheet("color: brown")
                self.ui.twActivititese.setCellWidget(rowPosition,6,terminate_btn)
                
                kill_btn = QPushButton(self.ui.twActivititese)
                kill_btn.setText("Kill")
                kill_btn.setStyleSheet("color: brown")
                self.ui.twActivititese.setCellWidget(rowPosition,7,kill_btn)
                
                
            except Exception as e:
                print (e)
        
        self.ui.activity_search.textChanged.connect(self.findName)
            
            
    
    def applyButtonStyle(self):
        for w in self.ui.menu_frame.findChildren(QPushButton):
            if w.objectName() != self.sender().objectName() and self.sender().objectName().__eq__('menu_btn') == False:
                w.setStyleSheet("border-bottom: none;")
        if(self.sender().objectName().__eq__('menu_btn') == False):
            self.sender().setStyleSheet("border-bottom: 2px solid;")
        return
    def grapphics(self):
        gra1 = self.info[18].split(" ")
        gra2 = self.info[20].split(" ")
        gra3 = self.info[22].split(" ")
        gra4 = self.info[24].split(" ")
        gra5 = self.info[25].split(" ")
        gra6 = self.info[26].split(" ")
        gra7 = self.info[27].split(" ")
        
        self.ui.lblDevice1.setText(gra1[3]+" "+gra1[4]+" "+gra1[5])
        self.ui.lblDriverD1.setText(gra1[11])
        self.ui.lblDevice2.setText(gra2[3]+" "+gra2[4])
        self.ui.lblDriverD2.setText(gra1[9])
        self.ui.lblDevice3.setText(gra3[3]+" "+gra3[4])
        self.ui.lblTypeD3.setText(gra3[6])
        self.ui.lblDriverD3.setText(gra3[8])
        
        self.ui.lblDisplay.setText(gra4[3])
        self.ui.lblHomeserver.setText(gra4[5])
        self.ui.lblHomewith.setText(gra4[9])
        self.ui.lblResolution.setText(gra5[10])
        self.ui.lblRenderer.setText(gra6[4]+" "+gra6[5]+" "+gra6[6]+" "+gra6[7])
        self.ui.lblDirectrender.setText(gra7[6])
        
        
        
                
    def machine(self):
        ma = self.info[4].split(" ")
        self.ui.lblType.setText(ma[3])
        self.ui.lblSystem.setText(ma[5])
        self.ui.lblProduct.setText(ma[7]+" "+ma[8])
        
    def system(self):
        sys1 = self.info[1].split(" ")
        sys2 = self.info[2].split(" ")
        self.ui.lblKernel.setText(sys1[3] +" "+sys1[4]) 
        self.ui.lblBits.setText(sys1[6])
        self.ui.lblCompile.setText(sys1[8])
        self.ui.lblVsystem.setText(sys1[10])
        self.ui.lblDesktop.setText(sys2[5])
        self.ui.lblDistro.setText(sys2[7]+" "+sys2[8]+" "+sys2[9])
    
    def Temperature(self):
        tem=str(subprocess.check_output(["inxi", "-s"])).split(" ")
        self.ui.lbltCPU.setText(tem[5] + " C")
        self.ui.lbltPCH.setText(tem[8] + " C")
        
    
    def Pin(self):
        self.ui.Pin.setValue(int(psutil.sensors_battery().percent))
        if psutil.sensors_battery().power_plugged:
            self.ui.lblPin.clear()
            myPixmapForNow = QPixmap() 
            myPixmapForNow.load(":/icons/icon/zap.svg") 
            self.ui.lblPin.setPixmap(myPixmapForNow)
        else:
            self.ui.lblPin.clear()
    
    def Hello(self):
        self.ui.lblHello.setText("Hello " + self.uname.node);
    
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
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
            
            self.create_table_widget(rowPositions, 4, x.maxfile, "storageTable")
            self.create_table_widget(rowPositions, 5, x.maxpath, "storageTable")
            
            disk_usage = shutil.disk_usage(x.mountpoint)
            
            self.create_table_widget(rowPositions,6, str(round((disk_usage.total / (1024*1024*1024)), 2)) + "GB","storageTable")
            self.create_table_widget(rowPositions,7, str(round((disk_usage.used / (1024*1024*1024)), 2)) + "GB","storageTable")
            self.create_table_widget(rowPositions,8, str(round((disk_usage.free / (1024*1024*1024)), 2)) + "GB","storageTable")
            
            full_disk = (disk_usage.used/ disk_usage.total)*100
            progressBar = QProgressBar(self.ui.storageTable)
            progressBar.setObjectName("progressBar")
            progressBar.setValue(int(full_disk))
            self.ui.storageTable.setCellWidget(rowPositions, 9, progressBar)

    def veRam(self):
        
        # self.fig = plt.gcf()
        
            # Create bars and choose color
        self.canvasRam = MplCanvas(self, width=5, height=4, dpi=100)

        
        self.x_data = list(range(self.n_data))
        self.y_data = self.heightRam
        
        
        self.update_Ram()
        layout = QVBoxLayout()
        #self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvasRam)
        self.ui.frame_27.setLayout(layout)
        self.ui.frame_27.setStyleSheet(u"background-color: transparent")
    
    def update_Ram(self):
        # Drop off the first y element, append a new one.
        self.y_data = self.heightRam
        
        self.canvasRam.axes.cla()  # Clear the canvas.
        self.canvasRam.axes.set_title("CPU")
        self.canvasRam.axes.set_ylim(0,100)
        self.canvasRam.axes.set_xlim(0,self.n_data)

        self.canvasRam.axes.plot(self.x_data, self.y_data, color='green')
        # Trigger the canvas to update and redraw.
        self.canvasRam.draw()
    
    def lsRam(self):
        
        self.ui.lblRam1Total.setText(str(self.infoRam[17][15:22]))
        self.ui.lblRam1Data.setText(str(self.infoRam[18][14:21]))
        self.ui.lblRam1Size.setText(str(self.infoRam[19][8:13]))
        self.ui.lblRam1Form.setText(str(self.infoRam[20][15:21]))
        self.ui.lblRam1Locator.setText(str(self.infoRam[22][11:17]))
        self.ui.lblRam1Type.setText(str(self.infoRam[24][8:12]))
        self.ui.lblRam1TypeDetail.setText(str(self.infoRam[25][15:26]))
        self.ui.lblRam1Speed.setText(str(self.infoRam[26][9:18]))

        self.ui.lblRam2Total.setText(str(self.infoRam[52][15:22]))
        self.ui.lblRam2Data.setText(str(self.infoRam[53][14:21]))
        self.ui.lblRam2Size.setText(str(self.infoRam[54][8:12]))
        self.ui.lblRam2Form.setText(str(self.infoRam[55][15:21]))
        self.ui.lblRam2Locator.setText(str(self.infoRam[57][11:17]))
        self.ui.lblRam2Type.setText(str(self.infoRam[59][8:12]))
        self.ui.lblRam2TypeDetail.setText(str(self.infoRam[60][15:26]))
        self.ui.lblRam2Speed.setText(str(self.infoRam[61][9:18]))
    def ram(self):

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
        self.heightRam=self.heightRam[1:]+[ramUesd/totalRam*100]
        
    
        
    def veCPU(self):
        
        # self.fig = plt.gcf()
        
            # Create bars and choose color
        self.canvasCPU = MplCanvas(self, width=5, height=4, dpi=100)

        
        self.x_data = list(range(self.n_data))
        self.y_data = self.heightCPU
        
        
        self.update_CPU()
        layout = QVBoxLayout()
        #self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvasCPU)
        self.ui.frame_25.setLayout(layout)
        self.ui.frame_25.setStyleSheet(u"background-color: transparent")
        
    def update_CPU(self):
        # Drop off the first y element, append a new one.
        self.y_data = self.heightCPU
        
        self.canvasCPU.axes.cla()  # Clear the canvas.
        self.canvasCPU.axes.set_title("CPU")
        self.canvasCPU.axes.set_ylim(0,100)
        self.canvasCPU.axes.set_xlim(0,self.n_data)

        self.canvasCPU.axes.plot(self.x_data, self.y_data, color='green')
        # Trigger the canvas to update and redraw.
        self.canvasCPU.draw()
    
    def lsCPU(self):
        self.ui.lblCPUArchitecture.setText(self.infoCPU[0].split(" ")[20])
        self.ui.lblCPUonmode.setText(self.infoCPU[1][33:47])
        self.ui.lblCPUAddresssize.setText(self.infoCPU[2][33:35]+", "+self.infoCPU[2][51:57])
        self.ui.lblCPUByteorder.setText(self.infoCPU[3][33:46])
        self.ui.lblCPUs.setText(self.infoCPU[4][33])
        self.ui.lblCPUOnlineCPU.setText(self.infoCPU[5][33:37])
        self.ui.lblCPUVendor.setText(self.infoCPU[6][33:45])
        self.ui.lblCPUFamily.setText(self.infoCPU[8][33])
        self.ui.lblCPUmodel.setText(self.infoCPU[9][33:36])
        self.ui.lblCPUTreadpercore.setText(self.infoCPU[10][33])
        self.ui.lblCPUCorepersoket.setText(self.infoCPU[11][33])
        self.ui.lblCPUSoket.setText(self.infoCPU[12][33])
        self.ui.lblCPUStepping.setText(self.infoCPU[13][33])
        self.ui.lblCPUmaxMHZ.setText(self.infoCPU[14][33:37])
        self.ui.lblCPUminMHz.setText(self.infoCPU[15][33:36])
        self.ui.lblCPUBogoMIPS.setText(self.infoCPU[16][33:37])
        
        
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
        
        
        self.heightCPU=self.heightCPU[1:]+[cpuPer]

        
        
        
    def create_table_widget(self,rowPosition,columnPosition,text,tableName):
        qtableWidgetItem = QTableWidgetItem()   
        getattr(self.ui, tableName).setItem(rowPosition, columnPosition, qtableWidgetItem)
        qtableWidgetItem.setText(str(text))
        qtableWidgetItem = getattr(self.ui,tableName).item(rowPosition, columnPosition)

    
    def dongHo(self):

        now = datetime.now()

        s = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second)
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
 

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        
        super(MplCanvas, self).__init__(fig)       