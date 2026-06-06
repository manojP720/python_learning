import tkinter as tk
import colorsys
import math

root = tk.Tk()
root.title("Aesthetic Cursor Box")
root.geometry("800x500")
root.configure(bg="#0c0c14")

canvas = tk.Canvas(root, width=800, height=500, bg="#0c0c14", highlightthickness=0)
canvas.pack(fill="both", expand=True)

box_x, box_y = 400, 250
mouse_x, mouse_y = 400, 250
size = 70
t = 0

def move_mouse(event):
    global mouse_x, mouse_y
    mouse_x = event.x
    mouse_y = event.y

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

def animate():
    global box_x, box_y, t

    canvas.delete("all")

    box_x += (mouse_x - box_x) * 0.12
    box_y += (mouse_y - box_y) * 0.12
    t += 0.015

    hue = t % 1
    r, g, b = colorsys.hsv_to_rgb(hue, 0.9, 1)
    color = rgb_to_hex((int(r * 255), int(g * 255), int(b * 255)))

    # Glow effect
    for i in range(8, 0, -1):
        glow_size = size + i * 16
        alpha_color = colorsys.hsv_to_rgb((hue + 0.1) % 1, 0.8, 0.7)
        gr, gg, gb = [int(c * 255) for c in alpha_color]
        glow = rgb_to_hex((gr // (i // 2 + 1), gg // (i // 2 + 1), gb // (i // 2 + 1)))

        canvas.create_rectangle(
            box_x - glow_size / 2,
            box_y - glow_size / 2,
            box_x + glow_size / 2,
            box_y + glow_size / 2,
            outline=glow,
            width=2
        )

    # Main colorful box
    canvas.create_rectangle(
        box_x - size / 2,
        box_y - size / 2,
        box_x + size / 2,
        box_y + size / 2,
        fill=color,
        outline="white",
        width=3
    )

    # Sparkle
    sparkle_x = box_x + math.cos(t * 8) * 55
    sparkle_y = box_y + math.sin(t * 8) * 55
    canvas.create_oval(
        sparkle_x - 5,
        sparkle_y - 5,
        sparkle_x + 5,
        sparkle_y + 5,
        fill="white",
        outline=""
    )

    root.after(16, animate)

canvas.bind("<Motion>", move_mouse)
animate()
root.mainloop()