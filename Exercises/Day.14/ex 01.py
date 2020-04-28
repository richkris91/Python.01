import sys
from PyQt5.QtWidgets import QApplication, QWidgetclass App(QWidget):
def __init__(self):
        super().__init__()
        self.initUI()    def initUI(self):
        self.show()app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())