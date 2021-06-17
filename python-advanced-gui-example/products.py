import json
import os
import tkinter as tk

from helpers import clear_screen

ROW_SIZE = 4

from PIL import Image, ImageTk


def render_products(screen: tk.Tk):
    clear_screen(screen)

    def on_click_product():
        with open(os.path.join('db', 'products.txt')) as f:
            pass
        pass

    with open(os.path.join('db', 'products.txt')) as f:
        curr_row = curr_col = 0

        for prod_idx, row in enumerate(f):
            product = json.loads(row)

            if prod_idx % ROW_SIZE == 0:
                curr_row += 4
                curr_col = 0

            tk.Label(screen, text=product['name']).grid(row=curr_row, column=curr_col)

            image = Image.open(os.path.join('db', 'images', product['img_path']))
            image = image.resize((100, 100))
            tk_image = ImageTk.PhotoImage(image)
            lbl = tk.Label(screen, image=tk_image)
            lbl.image = tk_image
            lbl.grid(row=curr_row + 1, column=curr_col)

            tk.Label(screen, text=product['count']).grid(row=curr_row + 2, column=curr_col)
            tk.Button(screen, text=f'Buy {product["id"]}', command=on_click_product).grid(row=curr_row + 3, column=curr_col)

            curr_col += 1