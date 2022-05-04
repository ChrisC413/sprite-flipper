from PIL import Image
import math

FRAMES = 8
BACKGROUND_COLOR=(13, 72, 7)

with Image.open("sonic_sprites.bmp") as im:
    print(im.format, f"{im.size}x{im.mode}")
    width, height = im.size
    new_width = width / FRAMES
    new_height = height * FRAMES
    if isinstance(new_width, float):
        print("image width is not evenly divisible")
        new_width = math.floor(new_width)
        print(new_width)
    new_image = Image.new(mode='RGB', size=(new_width, new_height))
    for i in range(FRAMES):
        top_left = i * new_width
        part = im.crop((top_left, 0, top_left+new_width, height))
        new_image.paste(part, (0, i * height))
        print(".")
    new_image.save("output.bmp", format=im.format)
    pixdata = new_image.load()
# Remove background color
    for y in range(new_image.size[1]):
        for x in range(new_image.size[0]):
            print(pixdata[x, y])
            if pixdata[x, y] == BACKGROUND_COLOR:
                print("found background color")
                pixdata[x, y] = (255, 255, 255)
    new_image.save("output.bmp", format='RGB')
