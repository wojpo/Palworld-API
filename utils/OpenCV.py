from colorthief import ColorThief
import matplotlib.pyplot as plt
import webcolors



def get_dominant_color(image_path):
    ct = ColorThief(image_path)
    dominant_color = ct.get_color(quality=1)
    plt.imshow([[dominant_color]])
    palette = ct.get_palette()
    plt.imshow([palette])
    color = palette[0]
    color = webcolors.rgb_to_hex(color)

    return color


