import random
import string,io
from PIL import Image,ImageFont,ImageDraw,ImageFilter

class verify1_code(object):
    str1=string.ascii_letters
    width=100
    height=50

    img = Image.new('RGB', (width,height), '#000')
    font =ImageFont.truetype('./day4_统计函数/javatext.ttf',size=30)
    draw=ImageDraw.Draw(img)

    @classmethod
    def create(cls):
        code=''
        for i in range(4):
            code_one=random.choice(cls.str1)
            code+=code_one

            cls.draw.text((10+20*i,0),text=code_one,fill='#fff',font=cls.font)
        return cls.img,code

if __name__ == '__main__':
    img,code=verify1_code.create()

    b=io.BytesIO()
    img.save(b,'png')
    #
    b_v=b.getvalue()

    with open('yitu.png','wb')as f:
        f.write(b_v)
    print(code)


