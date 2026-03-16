
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def create_android_theme(r,g,b):

    width = 400
    height = 800

    img = Image.new("RGB",(width,height),(r,g,b))

    draw = ImageDraw.Draw(img)

    try:
        font_big = ImageFont.truetype("arial.ttf",45)
        font_small = ImageFont.truetype("arial.ttf",20)

    except:
        font_big = ImageFont.load_default()
        font_small = ImageFont.load_default()


    # CLOCK
    draw.text((150,40),"12:45",fill=(255,255,255),font=font_big)

    # TITLE
    draw.text((90,120),"🐉 DRAGON",fill=(255,0,0),font=font_big)
    draw.text((110,200),"🦁 LION",fill=(255,215,0),font=font_big)


    # ICON ROW
    draw.rectangle((40,620,90,670),fill=(0,0,0))
    draw.rectangle((120,620,170,670),fill=(0,0,0))
    draw.rectangle((200,620,250,670),fill=(0,0,0))
    draw.rectangle((280,620,330,670),fill=(0,0,0))


    # ICON LABELS
    draw.text((40,690),"Phone",fill=(255,255,255),font=font_small)
    draw.text((120,690),"Camera",fill=(255,255,255),font=font_small)
    draw.text((205,690),"Chat",fill=(255,255,255),font=font_small)
    draw.text((280,690),"Settings",fill=(255,255,255),font=font_small)

    return img
