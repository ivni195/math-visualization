from PIL import Image
import numpy as np
import colorsys

WIDTH = 1024
HEIGHT = 512

def get_color(i):
    color = 255 * np.array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))

def check_convergence(p, n):
    z = 0
    for i in range(n):
        if abs(z) > 2:
            return i
        z = z * z + p
    return -1

def mandelbrot_color(x, y, n=1000):
    p = np.complex(x, y)
    i = check_convergence(p, n)
    if i != -1:
        return get_color(i)
    else:
        return (0, 0, 0)

def rescale(x, in_min, in_max, out_min=-1, out_max=1):
    return float(x - in_min) * float(out_max - out_min) / float(in_max - in_min) + out_min


img = Image.new('RGB', (WIDTH, HEIGHT))
pix = img.load()

for x in range(img.size[0]):
    print(f'{rescale(x+1, 0, img.size[0], 0, 100)}% done')
    for y in range(img.size[1]):
        pix[x, y] = mandelbrot_color(rescale(x, 0, img.size[0], -2, 1), rescale(y, 0, img.size[1], -1, 1), 10000)

img.show()

