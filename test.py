from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import pandas as pd
import sys
import time

df = pd.read_csv('skillmates.csv')

file = open("fonts/Sanchez-Regular.ttf", "rb")
bytes_font = BytesIO(file.read())
font = ImageFont.truetype(bytes_font, 70)

end_val = len(df.index)

for index, j in df.iterrows():
    # progress bar
    percent = float(index) / end_val
    sys.stdout.write("\r{}%".format(int(round(percent * 100))))
    sys.stdout.flush()

    # image reference
    img = Image.open('skillmate_cert.jpg')
    draw = ImageDraw.Draw(img)

    W = img.size[0] + 17  
    H = img.size[1] - 20
    
    # name query
    # fname = str(j['first_name'])
    # mname = str(j['middle_name'])
    # lname = str(j['last_name'])
    
    # # name format
    # fullname = fname + ' ' + mname + ' ' + lname
    # fullname = fullname.upper()

    fname = str(j['first_name'])

    fullname = fname.upper()

    # w,h = font.getsize(fullname)

    # generating data
    draw.text((W/2, H/2), fullname, fill=(237,182,5), font=font, anchor='mm')
    img.save('pictures/{}.jpg'.format(fname))
    
    time.sleep(.5)
    

