import os
import random
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

# Define dataset path
dataset_path = 'shape_texture_dataset/test'
shapes = ['circle', 'square', 'triangle']
images = []

# Load one image per shape and add border
for shape in shapes:
    shape_dir = os.path.join(dataset_path, shape)
    files = [f for f in os.listdir(shape_dir) if f.endswith('.png')]
    selected = random.choice(files)
    img_path = os.path.join(shape_dir, selected)
    img = Image.open(img_path)
    img_with_border = ImageOps.expand(img, border=4, fill='black')
    images.append(img_with_border)

# Display side-by-side
fig, axes = plt.subplots(1, 3, figsize=(9, 3))
for ax, img, shape in zip(axes, images, shapes):
    ax.imshow(img)
    ax.set_title(shape.capitalize())
    ax.axis('off')

plt.tight_layout()
plt.show()
