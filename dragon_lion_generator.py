
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def generate_theme(r,g,b):

    width = 400
    height = 700

    image = Image.new("RGB",(width,height),(r,g,b))

    draw = ImageDraw.Draw(image)

    try:
        font1 = ImageFont.truetype("arial.ttf",50)
        font2 = ImageFont.truetype("arial.ttf",40)

    except:
        font1 = ImageFont.load_default()
        font2 = ImageFont.load_default()

    draw.text((80,200),"🐉 DRAGON",fill=(255,0,0),font=font1)

    draw.text((170,320),"+",fill=(255,255,255),font=font1)

    draw.text((100,450),"🦁 LION",fill=(255,215,0),font=font2)

    return image
