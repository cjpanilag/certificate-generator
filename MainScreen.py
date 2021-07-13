import glob
import uuid
import os
import CertificateProcess
from PIL import Image, ImageDraw, ImageFont
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class MainScreen(QWidget):

    def __init__(self):
        super().__init__()
        self.certificate = CertificateProcess.CertificateProcess()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        """
        -- HEADER SECTION --
         header label
        """
        infoLabel = QLabel('CERTIFICATE GENERATOR', self)
        infoLabel.setFont(QFont('Roboto Mono', 12, QFont.Bold))
        infoLabel.setAlignment(QtCore.Qt.AlignCenter)

        guideLabel = QLabel('Make sure to have a fullname \n column in your CSV file', self)
        guideLabel.setFont(QFont('Roboto Mono', 10))
        guideLabel.setAlignment(QtCore.Qt.AlignCenter)

        """
        -- FILE SECTION --
         file label
         file button
        """
        self.imageLineEdit = QLineEdit(self)
        self.imageLineEdit.setEnabled(False)
        self.imageLineEdit.setFont(QFont('Consolas', 8))
        self.imageLineEdit.setText('Image File...')

        self.imageFileSelect = QPushButton('🖼 Image', self)
        self.imageFileSelect.clicked.connect(self.openImage)
        self.imageFileSelect.setFont(QFont('Roboto Mono', 9, QFont.Bold))
        
        """
        -- FILE SECTION --
         file label
         file button
        """
        self.fileLineEdit = QLineEdit(self)
        self.fileLineEdit.setEnabled(False)
        self.fileLineEdit.setFont(QFont('Consolas', 8))
        self.fileLineEdit.setText('CSV File...')

        btnFileSelect = QPushButton('📂 File', self)
        btnFileSelect.clicked.connect(self.openFile)
        btnFileSelect.setFont(QFont('Roboto Mono', 9, QFont.Bold))

        """
        -- FONT SECTION --
         label
         button
        """
        fontFamilyLabel = QLabel('Font-family: ', self)
        fontFamilyLabel.setFont(QFont('Roboto Mono', 9))
        fontFamilyLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.fontFamilyCb = QComboBox()
        self.fontFamilyCb.addItems(self.fileToCBO())

        fontSizeLabel = QLabel('Font-size: ', self)
        fontSizeLabel.setFont(QFont('Roboto Mono', 9))
        fontSizeLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.fontSizeLineEdit = QLineEdit(self)

        """
        -- FONT COLOR SECTION --
         label
         button
        """
        fontColorLabel = QLabel('Font-color: ', self)
        fontColorLabel.setFont(QFont('Roboto Mono', 9))
        fontColorLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.RLineEdit = QLineEdit(self)
        self.RLineEdit.setText('R')
        self.GLineEdit = QLineEdit(self)
        self.GLineEdit.setText('G')
        self.BLineEdit = QLineEdit(self)
        self.BLineEdit.setText('B')

        """
        -- POSITION SECTION --
         file label
         file button
        """
        positionLabel = QLabel('Position: ', self)
        positionLabel.setFont(QFont('Roboto Mono', 9))
        positionLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.xLineEdit = QLineEdit(self)
        self.xLineEdit.setText('X')

        self.yLineEdit = QLineEdit(self)
        self.yLineEdit.setText('Y')

        """
        -- PREVIEW SECTION --
         preview button
        """
        btnPreview = QPushButton('🚩 Preview', self)
        btnPreview.clicked.connect(self.previewImage)
        btnPreview.setFont(QFont('Roboto Mono', 9, QFont.Bold))

        """
        --- FILE SAVE SECTION ---
         file select 
         file button
        """
        self.locationLineEdit = QLineEdit(self)
        self.locationLineEdit.setEnabled(False)
        self.locationLineEdit.setFont(QFont('Consolas', 8))
        self.locationLineEdit.setText('File location...')

        btnLocation = QPushButton('📥 Save File Location', self)
        btnLocation.clicked.connect(self.outputLocation)
        btnLocation.setFont(QFont('Roboto Mono', 9, QFont.Bold))

        """
        -- GENERATE SECTION --
         generate button
        """
        self.btnGenerate = QPushButton('Generate', self)
        self.btnGenerate.clicked.connect(self.generate)
        self.btnGenerate.setFont(QFont('Roboto Mono', 9, QFont.Bold))
        self.btnGenerate.setVisible(False)

        self.progressBar = QProgressBar(self)
        self.progressBar.setVisible(False)

        self.successLabel = QLabel('DONE!', self)
        self.successLabel.setFont(QFont('Roboto Mono', 12))
        self.successLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.successLabel.setVisible(False)

        """
        -- FOOTER SECTION --
         footer label
        """
        footerLabel = QLabel('© cjpanilag@gmail.com ● 2021', self)
        footerLabel.setFont(QFont('Roboto Mono', 8))
        footerLabel.setAlignment(QtCore.Qt.AlignCenter)

        """
        -- LAYOUT GRID --
        """
        self.mainLayout = QGridLayout(self)

        # row 1 
        self.mainLayout.addWidget(infoLabel, 0,0,1,4)

        # row 2
        self.mainLayout.addWidget(guideLabel, 1,0,1,4)

        # row 3
        self.mainLayout.addWidget(self.imageLineEdit, 2, 0, 1, 3)
        self.mainLayout.addWidget(self.imageFileSelect, 2,3)

        # row 4
        self.mainLayout.addWidget(self.fileLineEdit, 3, 0, 1, 3)
        self.mainLayout.addWidget(btnFileSelect, 3,3)
        
        # row 5
        self.mainLayout.addWidget(fontFamilyLabel, 4, 0)
        self.mainLayout.addWidget(self.fontFamilyCb, 4, 1)
        self.mainLayout.addWidget(fontSizeLabel, 4, 2)
        self.mainLayout.addWidget(self.fontSizeLineEdit, 4, 3)

        # row 6
        self.mainLayout.addWidget(fontColorLabel, 5,0)
        self.mainLayout.addWidget(self.RLineEdit, 5,1)
        self.mainLayout.addWidget(self.GLineEdit, 5,2)
        self.mainLayout.addWidget(self.BLineEdit, 5,3)

        # row 7
        self.mainLayout.addWidget(positionLabel, 6,0)
        self.mainLayout.addWidget(self.xLineEdit, 6,1)
        self.mainLayout.addWidget(self.yLineEdit, 6,2)
        self.mainLayout.addWidget(btnPreview, 6,3)
        
        # row 8
        self.mainLayout.addWidget(self.locationLineEdit, 7,0, 1, 3)
        self.mainLayout.addWidget(btnLocation, 7,3)

        # row 9
        self.mainLayout.addWidget(self.btnGenerate, 8,0, 1, 4)
        
        self.mainLayout.addWidget(self.progressBar, 8, 0, 1, 4)

        self.mainLayout.addWidget(self.successLabel, 8, 0, 1, 4)

        # row 10
        ##

        # row 11 / footer
        self.mainLayout.addWidget(footerLabel, 10,0, 1, 4)


        """
        -- MAIN WINDOW --
        """
        self.setWindowTitle('Certificate Generator')
        self.setGeometry(100, 100, 500, 490)
        self.show()


    def openFile(self):
        self.successLabel.setVisible(False)
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        self.fileCSV, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileCSV:
            self.fileLineEdit.setText(self.fileCSV)
            self.fileLineEdit.setToolTip(self.fileCSV)
            self.certificate.setFile(self.fileCSV)

    def openImage(self):
        self.successLabel.setVisible(False)
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        self.fileImage, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileImage:
            self.imageLineEdit.setText(self.fileImage)
            self.imageLineEdit.setToolTip(self.fileImage)
            self.certificate.setImage(self.fileImage)

    def fileToCBO(self):
        mylist = [f for f in glob.glob("fonts/*.ttf")]
        data = []
        for list in mylist:
            x = list.split('\\')
            x = x[1].split('.')
            data.append(x[0])
        return data

    def previewImage(self):
        self.certificate.setFont(str(self.fontFamilyCb.currentText()), int(self.fontSizeLineEdit.text()))
        self.certificate.setFontColor(int(self.RLineEdit.text()), int(self.GLineEdit.text()), int(self.BLineEdit.text()))
        self.certificate.setTextPosition(int(self.xLineEdit.text()), int(self.yLineEdit.text()))
        self.certificate.preview()

    def outputLocation(self):
        self.fileLocation = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if self.fileLocation:
            self.locationLineEdit.setText(self.fileLocation)
            self.btnGenerate.setVisible(True)
            self.successLabel.setVisible(False)

    def generate(self):
        self.progressBar.setVisible(True)
        self.btnGenerate.setVisible(False)
        self.certificate.setFont(str(self.fontFamilyCb.currentText()), int(self.fontSizeLineEdit.text()))
        self.certificate.setFontColor(int(self.RLineEdit.text()), int(self.GLineEdit.text()), int(self.BLineEdit.text()))
        self.certificate.setTextPosition(int(self.xLineEdit.text()), int(self.yLineEdit.text()))

        df = self.certificate.getFile()

        end_val = len(df.index)

        self.directory = uuid.uuid4()

        parent_dir = str(self.locationLineEdit.text())

        self.path = os.path.join(parent_dir, str(self.directory))

        os.mkdir(self.path)

        for index, j in df.iterrows():
            # progress bar
            percent = float(index) / end_val
            indicator = int(round(percent * 100))
            #sys.stdout.write("\r{}%".format(int(round(percent * 100))))
            #sys.stdout.flush()

            img = Image.open(self.certificate.getImage())
            draw = ImageDraw.Draw(img)

            X = img.size[0] + self.certificate.getPosition()[0]
            Y = img.size[1] - self.certificate.getPosition()[1]

            name = str(j['fullname'])

            name = name.upper()

            self.file_name = name

            R = self.certificate.getFontColor()[0]
            G = self.certificate.getFontColor()[1]
            B = self.certificate.getFontColor()[2]

            draw.text((X/2, Y/2), name, fill=(R, G, B), font=self.certificate.getFont(), anchor='mm')
            img.save('{}/{}.jpg'.format(self.path, self.file_name))
            
            self.progressBar.setValue(indicator)
            QApplication.processEvents()

        self.successLabel.setVisible(True)
        # clear file field 
        self.imageLineEdit.clear()
        self.fileLineEdit.clear()
        self.fontSizeLineEdit.clear()
        # clear font size 
        self.RLineEdit.clear()
        self.GLineEdit.clear()
        self.BLineEdit.clear()
        # clear position 
        self.xLineEdit.clear()
        self.yLineEdit.clear()
        # reset the progress bar
        # self.progressBar.value(0)
        self.progressBar.setVisible(False)
        
        
    
    

        

        

           
