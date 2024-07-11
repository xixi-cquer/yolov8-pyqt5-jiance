
import sys


from PyQt5 import QtCore, QtGui, QtWidgets

import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ultralytics import YOLO
import qdarkstyle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 771)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox1.setStyleSheet("#groupBox1{\n"
"border: 0px solid #42adff;\n"
"border-radius:9px;\n"
"background:rgba(255, 255, 255, 50);}")
        self.groupBox1.setTitle("")
        self.groupBox1.setObjectName("groupBox1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox2 = QtWidgets.QGroupBox(self.groupBox1)
        self.groupBox2.setStyleSheet("#groupBox2{\n"
"border: 0px solid #42adff;\n"
"border-radius:9px;\n"
"background:rgba(255, 255, 255, 50);}")
        self.groupBox2.setTitle("")
        self.groupBox2.setObjectName("groupBox2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox2)
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 24px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(715, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.minButton = QtWidgets.QPushButton(self.groupBox2)
        self.minButton.setMinimumSize(QtCore.QSize(50, 28))
        self.minButton.setMaximumSize(QtCore.QSize(50, 28))
        self.minButton.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(255, 255, 255, 0);}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(255, 255, 255, 150);}")
        self.minButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/最小化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minButton.setIcon(icon)
        self.minButton.setObjectName("minButton")
        self.horizontalLayout_5.addWidget(self.minButton)
        self.maxButton = QtWidgets.QPushButton(self.groupBox2)
        self.maxButton.setMinimumSize(QtCore.QSize(50, 28))
        self.maxButton.setMaximumSize(QtCore.QSize(50, 28))
        self.maxButton.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(255, 255, 255, 0);}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(255, 255, 255, 150);}")
        self.maxButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/正方形.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("icon/还原.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("icon/还原.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.maxButton.setIcon(icon1)
        self.maxButton.setCheckable(True)
        self.maxButton.setObjectName("maxButton")
        self.horizontalLayout_5.addWidget(self.maxButton)
        self.closeButton = QtWidgets.QPushButton(self.groupBox2)
        self.closeButton.setMinimumSize(QtCore.QSize(50, 28))
        self.closeButton.setMaximumSize(QtCore.QSize(50, 28))
        self.closeButton.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(255, 255, 255, 0);}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(255, 255, 255, 150);}")
        self.closeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_5.addWidget(self.closeButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addWidget(self.groupBox2)
        self.groupBox4 = QtWidgets.QGroupBox(self.groupBox1)
        self.groupBox4.setStyleSheet("#groupBox4{\n"
"border: 0px solid #42adff;\n"
"border-radius:9px;\n"
"background:rgba(255, 255, 255, 50);}")
        self.groupBox4.setTitle("")
        self.groupBox4.setObjectName("groupBox4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox4)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 24px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.groupBox4)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(self.groupBox4)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 24px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.groupBox3 = QtWidgets.QGroupBox(self.groupBox4)
        self.groupBox3.setStyleSheet("#groupBox3{\n"
"border: 0px solid #42adff;\n"
"border-radius:9px;\n"
"background:rgba(255, 255, 255, 50);}")
        self.groupBox3.setTitle("")
        self.groupBox3.setObjectName("groupBox3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox3)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("QTextBrowser\n"
                                   "{\n"
                                   "    font-size: 30px;\n"
                                   "    font-family: \"Microsoft YaHei\";\n"
                                   "    font-weight: bold;\n"
                                   "         border-radius:9px;\n"
                                   "        background:rgba(255, 255, 255, 0);\n"
                                   "color: rgb(0, 0, 0);\n"
                                   "}\n"
                                   "")
        self.horizontalLayout_3.addWidget(self.textBrowser)
        spacerItem1 = QtWidgets.QSpacerItem(428, 298, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox3)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(self.groupBox3)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.label_5 = QtWidgets.QLabel(self.groupBox3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox3)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_2.addWidget(self.horizontalSlider)
        self.label_6 = QtWidgets.QLabel(self.groupBox3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox3)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout_2.addWidget(self.horizontalSlider_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.setStretch(0, 6)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 2)
        self.verticalLayout_5.addWidget(self.groupBox3)
        self.verticalLayout_5.setStretch(0, 15)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.groupBox4)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 15)
        self.verticalLayout.addWidget(self.groupBox1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 点击响应函数
        self.pushButton.clicked.connect(self.select)
        self.pushButton_2.clicked.connect(self.uploadImage)
        self.pushButton_3.clicked.connect(self.uploadMP)
        self.pushButton_4.clicked.connect(self.uploadCamera)
        self.pushButton_5.clicked.connect(self.start)
        self.pushButton_6.clicked.connect(self.stop)
        self.horizontalSlider.valueChanged.connect(self.confchange)
        self.horizontalSlider_2.valueChanged.connect(self.iouchange)

        self.model = YOLO('yolov8s.pt')
        self.conf = 0.7
        self.horizontalSlider.setValue(int(self.conf*100))
        self.iou = 0.4
        self.horizontalSlider_2.setValue(int(self.iou*100))
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.release()
        self.timerca = QTimer()
        self.timerca.timeout.connect(self.showCamera)
        self.timermp = QTimer()
        self.timermp.timeout.connect(self.showvideo)
        self.textBrowser.append('选择你想要的功能然后点击开始吧，若需要选择其他模型，点击选择模型进行选择即可')
        self.leixing = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "智能检测界面"))
        self.label.setText(_translate("MainWindow", "原始图像"))
        self.label_2.setText(_translate("MainWindow", "检测图像"))
        self.label_3.setText(_translate("MainWindow", "功能"))
        self.pushButton.setText(_translate("MainWindow", "选择模型"))
        self.pushButton_2.setText(_translate("MainWindow", "选择图片"))
        self.pushButton_3.setText(_translate("MainWindow", "选择视频"))
        self.pushButton_4.setText(_translate("MainWindow", "选择摄像头"))
        self.pushButton_5.setText(_translate("MainWindow", "开始"))
        self.pushButton_6.setText(_translate("MainWindow", "停止"))
        self.label_5.setText(_translate("MainWindow", "conf"))
        self.label_6.setText(_translate("MainWindow", "iou"))

    def confchange(self):
        self.conf = self.horizontalSlider.value()/100
    def iouchange(self):
        self.iou = self.horizontalSlider_2.value()/100

    def uploadImage(self):
        self.stop()

        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(None, '选择图片', '', 'Images (*.png *.xpm *.jpg *.bmp)')
        self.image_path = image_path
        if image_path:
            self.leixing = 1
            # 在这里添加加载图片的逻辑，例如显示图片到label2
            image = cv2.imread(image_path)
            self.show_image(image, self.label)
            self.textBrowser.append("图片已经打开，点击开始进行检测")
            # pixmap = QtGui.QPixmap(image_path)
            # self.label.setPixmap(pixmap)
            # self.label.setScaledContents(True)

            # results = self.model.predict(self.image_path)
            # annotated_frame = results[0].plot()
            # self.show_image(annotated_frame, self.label_2)


            # annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            # # 将图像数据转换为QImage格式
            # height, width, channel = annotated_frame.shape
            # bytes_per_line = 3 * width
            # qimage = QtGui.QImage(annotated_frame.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
            # # 将QImage转换为QPixmap
            # pixmap = QtGui.QPixmap.fromImage(qimage)
            # # 都执行：
            # self.label_2.setPixmap(pixmap)
            # self.label_2.setScaledContents(False)

    def show_image(self,img_src, label):

        ih, iw, _ = img_src.shape
        w = label.width()
        h = label.height()
        #
        scale=min(w/iw, h/ih)
        nw=int(iw*scale)
        nh=int(scale*ih)
        img_src_ = cv2.resize(img_src, (nw, nh))
        # # 保持纵横比
        # # 找出长边
        # if iw > ih:
        #     scal = w / iw
        #     nw = w
        #     nh = int(scal * ih)
        #     img_src_ = cv2.resize(img_src, (nw, nh))
        #
        # else:
        #     scal = h / ih
        #     nw = int(scal * iw)
        #     nh = h
        #     img_src_ = cv2.resize(img_src, (nw, nh))

        frame = cv2.cvtColor(img_src_, cv2.COLOR_BGR2RGB)
        img = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[2] * frame.shape[1],QImage.Format_RGB888)
        label.setPixmap(QPixmap.fromImage(img) )
        label.setScaledContents(True)

    def uploadMP(self):
        self.stop()

        videoPath, _ = QFileDialog.getOpenFileName(
            None,  # 父窗口对象
            "选择视频文件",  # 标题
            ".",  # 起始目录
            "图片类型 (*.mp4 *.avi)"  # 选择类型过滤项，过滤内容在括号中
        )
        if videoPath:
            self.leixing = 2
        self.image_path = videoPath
        # 参数0代表系统第一个摄像头,第二就用1 以此类推
        self.cap = cv2.VideoCapture(self.image_path)
        # 设置显示分辨率和FPS ,不设置的话会非常卡
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.textBrowser.append("视频已经打开，点击开始进行检测")


    def showvideo(self):
        ret, frame = self.cap.read()
        results=self.model(source=frame,conf=self.conf,iou=self.iou)
        caframe=results[0].plot()
        boxes=results[0].boxes
        names=results[0].names
        labels_num_dict={}
        for box in boxes:
            cls_id=box.cls.cpu().detach().numpy()[0].astype('int')
            for key in names.keys():
                if cls_id==key:
                    if names[key] in labels_num_dict:
                        labels_num_dict[names[key]]+=1
                    else:
                        labels_num_dict[names[key]] = 1
        self.textBrowser.clear()
        self.textBrowser.append(str(labels_num_dict))

        # 视频流置于label中间部分播放
        # 视频色彩转换回RGB，OpenCV images as BGR

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        qImage = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0],QtGui.QImage.Format_RGB888)  # 变成QImage形式
        # 往显示视频的Label里 显示QImage
        self.label.setPixmap(QtGui.QPixmap.fromImage(qImage))
        self.label.setScaledContents(True)

        caframe = cv2.cvtColor(caframe, cv2.COLOR_BGR2RGB)
        caImage = QtGui.QImage(caframe.data, caframe.shape[1], caframe.shape[0], QtGui.QImage.Format_RGB888)  # 变成QImage形式
        # 往显示视频的Label里 显示QImage
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(caImage))
        self.label_2.setScaledContents(True)

    def uploadCamera(self):
        self.stop()

        # 参数0代表系统第一个摄像头,第二就用1 以此类推
        self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        if self.cap.isOpened():
            self.leixing = 3
        # 设置显示分辨率和FPS ,不设置的话会非常卡
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.textBrowser.append("摄像头已经打开，点击开始进行检测")




    def showCamera(self):

        ret, frame = self.cap.read()
        self.image_path = frame
        results=self.model(self.image_path,conf=self.conf,iou=self.iou)
        caframe=results[0].plot()

        boxes = results[0].boxes
        names = results[0].names
        labels_num_dict = {}
        for box in boxes:
            cls_id = box.cls.cpu().detach().numpy()[0].astype('int')
            for key in names.keys():
                if cls_id == key:
                    if names[key] in labels_num_dict:
                        labels_num_dict[names[key]] += 1
                    else:
                        labels_num_dict[names[key]] = 1
        self.textBrowser.append(str(labels_num_dict))

        self.show_image(frame, self.label)
        self.show_image(caframe, self.label_2)


        # 视频流置于label中间部分播放
        # 视频色彩转换回RGB，OpenCV images as BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        qImage = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0],QtGui.QImage.Format_RGB888)  # 变成QImage形式
        # 往显示视频的Label里 显示QImage
        self.label.setPixmap(QtGui.QPixmap.fromImage(qImage))
        self.label.setScaledContents(True)

        caframe = cv2.cvtColor(caframe, cv2.COLOR_BGR2RGB)
        caImage = QtGui.QImage(caframe.data, caframe.shape[1], caframe.shape[0], QtGui.QImage.Format_RGB888)  # 变成QImage形式
        # 往显示视频的Label里 显示QImage
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(caImage))
        self.label_2.setScaledContents(True)
    def start(self):
        if self.leixing == 1:
            results = self.model.predict(self.image_path,conf=self.conf,iou=self.iou)
            annotated_frame = results[0].plot()
            boxes = results[0].boxes
            names = results[0].names
            labels_num_dict = {}
            for box in boxes:
                cls_id = box.cls.cpu().detach().numpy()[0].astype('int')
                for key in names.keys():
                    if cls_id == key:
                        if names[key] in labels_num_dict:
                            labels_num_dict[names[key]] += 1
                        else:
                            labels_num_dict[names[key]] = 1
            self.textBrowser.append(str(labels_num_dict))
            self.show_image(annotated_frame, self.label_2)
        elif self.leixing == 2:
            self.timermp.start(30)
        elif self.leixing == 3:
            self.timerca.start(30)
        else:
            self.stop()
    def select(self):
        self.stop()
        self.leixing=0
        file_dialog = QFileDialog()
        path, _ = file_dialog.getOpenFileName(None, '选择模型', '', 'model(*.pt)')
        if path:
            self.model=YOLO(path)
        self.textBrowser.append("模型已经加载，点击功能开始进行检测")
    def stop(self):
        self.leixing = 0
        self.cap.release()
        self.timerca.stop()
        self.timermp.stop()
        self.label.clear()
        self.label_2.clear()
        self.textBrowser.clear()
        self.textBrowser.append('选择你想要的功能然后点击开始吧，若需要选择其他模型，点击选择模型进行选择即可')
        self.label.setText('原始图像')
        self.label_2.setText('检测图像')

app = QApplication(sys.argv)

app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
main1=QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(main1)
main1.show()
sys.exit(app.exec_())
