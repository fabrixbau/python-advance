from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def get_image(image_file):
    try:
        image = Image.open(image_file)
        print(image.size)
        print(image.mode)
        print(image.format)

        # image.show()

        # image_blackwhite = image.convert('L')
        # image_blackwhite.show()
        # image_blackwhite.save('hermanos_bn.jpg')

        font = ImageFont.truetype('fonts/Roboto-Bold.ttf', 120)
        draw = ImageDraw.Draw(image)
        draw.text(
            (500, 0),
            "HERMANOS 2002",
            (255, 255, 255),
            font
        )
        image.show()
        image.save('hermanos_font.jpg')

        # create a Thumbnail ocupa menos espacio de memoria
        image.thumbnail((500, 500))
        image.show()
        image.save('Hermanos_thumbnail.jpg')
    except Exception as e:
        print('no se encontro la foto' + e)


if __name__ == '__main__':
    get_image('hermanos.jpg')
