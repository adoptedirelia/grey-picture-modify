import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene, QGraphicsPixmapItem,QGraphicsItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import utils
import cv2
import myui
import numpy as np

class AppWindow(QMainWindow,myui.Ui_MainWindow):
    def __init__(self,parent=None):
        super(AppWindow,self).__init__(parent)
        self.setupUi(self)
        
        self.origin_pic = ""
        self.bit = 0
        self.type=""
        self.grey_conv_button.clicked.connect(self.grey_conv)
        self.rgb_conv_button.clicked.connect(self.rgb_conv)
        self.Mean_filter_button.clicked.connect(self.Mean_filter)
        self.Media_filter_button.clicked.connect(self.Media_filter)
        self.pushButton.clicked.connect(self.choose_pic)
        self.Adopted_Irelia.clicked.connect(self.show_me)

    def choose_pic(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self,
                  "选取文件",
                  "./",
                  "bmp picture (*.bmp);;jpg picture (*.jpg)")  
        print(fileName1,filetype)
        self.type = filetype
        if(filetype=="bmp picture (*.bmp)"):
            self.origin_pic,self.bit = utils.readBMP(fileName1)
            self.show_pic(self.origin_pic,0)
        elif(filetype=="jpg picture (*.jpg)"):
            self.origin_pic = cv2.imread(fileName1)
            self.bit = 24
            self.show_pic(self.origin_pic,0)
            

    def show_pic(self,img,position):
        
        img = img.astype(np.uint8)
        if(self.type=="jpg picture (*.jpg)"):
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        y,x = img.shape[:-1]
        frame = QImage(img,x,y,QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
    
        if position==0 :
            self.origin_img.setPixmap(pix)
            self.origin_img.setScaledContents(True)
            self.origin_img.setStyleSheet("border: 2px solid black")
        if position==1 :
            self.processed_img.setPixmap(pix)
            self.processed_img.setScaledContents(True)
            self.processed_img.setStyleSheet("border: 2px solid black")
        if position==2:
            self.AI.setPixmap(pix)
            self.AI.setScaledContents(True)

        if position==3:
            self.AI_2.setPixmap(pix)
            self.AI_2.setScaledContents(True)

    def show_me(self):
        img = cv2.imread('./irelia.jpg')
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img2 = cv2.imread('./irelia_colorful.jpg')
        img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
        self.show_pic(img,2)
        self.show_pic(img2,3)


    def grey_conv(self):
        grey = utils.pic_conv_grey(self.origin_pic,self.bit,'grey_conv')
        self.show_pic(grey,1)

    def rgb_conv(self):
        rgb = utils.pic_conv_rgb(self.origin_pic,'rgb_conv')
        self.show_pic(rgb,1)

    def Media_filter(self):
        Media_f = utils.Media_filter(self.origin_pic,pic_name='Media_filter')
        self.show_pic(Media_f,1)

    def Mean_filter(self):
        Mean_f = utils.Mean_filter(self.origin_pic,pic_name='Mean_filter')
        self.show_pic(Mean_f,1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = AppWindow()
    ui.setWindowTitle("数字图像处理 张登甲")
    ui.show()
    sys.exit(app.exec_())
