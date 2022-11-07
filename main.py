import sys

from PyQt5.QtWidgets import QApplication 

from mainFrmHandle import MAINFRMHANDLE



if __name__ == "__main__":
   
    app =QApplication(sys.argv)
    
    Main = MAINFRMHANDLE(app)
   
    sys.exit(app.exec_())