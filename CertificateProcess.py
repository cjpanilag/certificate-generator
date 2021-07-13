from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import pandas as pd

class CertificateProcess():

    def setFile(self, file):
        self.file = file

    def setImage(self, image):
        self.image = image

    def setFont(self, font = 'OpenSans-Regular', size = 0):
        self.font = 'fonts/'+str(font)+'.ttf'
        self.size = size

    def setFontColor(self, r, g, b):
        self.R = r
        self.G = g
        self.B = b

    def setTextPosition(self, x = 0, y = 0):
        self.X = x
        self.Y = y

    def getFile(self):
        df = pd.read_csv(self.file)
        return df
    
    def getImage(self):
        return self.image
    
    def getPosition(self):
        return (self.X, self.Y)

    def getFont(self):
        fontFile = open(self.font, "rb")
        bytesFont = BytesIO(fontFile.read())
        font = ImageFont.truetype(bytesFont, self.size)
        return font

    def getFontColor(self):
        return (self.R, self.G, self.B)

    def preview(self):
        df = pd.read_csv(self.file)

        fontFile = open(self.font, "rb")
        bytesFont = BytesIO(fontFile.read())
        font = ImageFont.truetype(bytesFont, self.size)

        img = Image.open(self.image)
        draw = ImageDraw.Draw(img)

        X = img.size[0] + self.X
        Y = img.size[1] - self.Y

        name = str(df['fullname'][0])
            
        name = name.upper()

        draw.text((X/2, Y/2), name, fill=(self.R, self.G, self.B), font=font, anchor='mm')  
        img.show()

