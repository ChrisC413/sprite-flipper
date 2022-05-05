from PIL import Image
import math

FRAMES = 5
BACKGROUND_COLOR=(13, 72, 7)
BOUNDRY_COLOR=(37, 102, 26)
FRAME_OFFSET=1
FILENAME="bored"

with Image.open(f"{FILENAME}.bmp") as im:
    print(im.format, f"{im.size}x{im.mode}")
    width, height = im.size
    height = 64
    new_width = width / FRAMES
    new_height = height * FRAMES
    if isinstance(new_width, float):
        print("image width is not evenly divisible")
        new_width = math.floor(new_width)
        print(new_width)
    new_image = Image.new(mode='RGB', size=(new_width, new_height))
    for i in range(FRAMES):
        top_left = i * (new_width + FRAME_OFFSET)
        part = im.crop((top_left, 0, top_left+new_width, height))
        new_image.paste(part, (0, i * height))
        print(".")
    new_image.save(f"{FILENAME}_output.bmp", format=im.format)
    pixdata = new_image.load()
# Remove background color
    for y in range(new_image.size[1]):
        for x in range(new_image.size[0]):
            print(pixdata[x, y])
            if pixdata[x, y] in [BACKGROUND_COLOR, BOUNDRY_COLOR]:
                print("found background color")
                pixdata[x, y] = (0, 0, 0)
    new_image.save(f"{FILENAME}_output.bmp", format=im.format)
