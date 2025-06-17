import os
from PIL import Image, ImageDraw
import random

img_size = 128
shapes = ['circle', 'square', 'triangle']
train_colors = {
    'circle': 'red',
    'square': 'green',
    'triangle': 'blue'
}
test_colors = {
    'circle': ['green', 'blue'],
    'square': ['red', 'blue'],
    'triangle': ['red', 'green']
}

base = 'shape_texture_dataset'
train = os.path.join(base, 'train')
test = os.path.join(base, 'test')

os.makedirs(train, exist_ok=True)
os.makedirs(test, exist_ok=True)

def draw(shape, color):
    bg = Image.new('RGB', (img_size, img_size), 'white')
    fg = Image.new('RGBA', (img_size, img_size))
    d = ImageDraw.Draw(fg)

    s = random.randint(40, 80)
    x = random.randint(10, img_size - s - 10)
    y = random.randint(10, img_size - s - 10)

    if shape == 'circle':
        d.ellipse([x, y, x + s, y + s], fill=color)
    elif shape == 'square':
        d.rectangle([x, y, x + s, y + s], fill=color)
    elif shape == 'triangle':
        p = [(x + s // 2, y), (x, y + s), (x + s, y + s)]
        d.polygon(p, fill=color)

    a = random.randint(0, 360)
    fg = fg.rotate(a)
    bg.paste(Image.alpha_composite(bg.convert('RGBA'), fg).convert('RGB'))
    return bg

for shape in shapes:
    col = train_colors[shape]
    folder = os.path.join(train, shape)
    os.makedirs(folder, exist_ok=True)
    for i in range(200):
        img = draw(shape, col)
        img.save(os.path.join(folder, f'{shape}_{i}.png'))

for shape in shapes:
    folder = os.path.join(test, shape)
    os.makedirs(folder, exist_ok=True)
    for color in test_colors[shape]:
        for i in range(25):
            img = draw(shape, color)
            img.save(os.path.join(folder, f'{shape}_{color}_{i}.png'))
