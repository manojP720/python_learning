import tkinter as tk
import colorsys
import math

root = tk.Tk()
root.title("Cursor Tracker")
root.geometry("800x600")
root.configure(bg="#0c0c14")

canvas = tk.Canvas(root, width=800, height=600, bg="#0c0c14", highlightthickness=0)
canvas.pack(fill="both", expand=True)

circle_x, circle_y = 400, 300
mouse_x, mouse_y = 400, 300
size = 60
t = 0

def move_mouse(event):
    global mouse_x, mouse_y
    mouse_x = event.x
    mouse_y = event.y

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

def animate():
    global circle_x, circle_y, t

    canvas.delete("all")

    circle_x += (mouse_x - circle_x) * 0.12
    circle_y += (mouse_y - circle_y) * 0.12
    t += 0.02

    hue = t % 1
    r, g, b = colorsys.hsv_to_rgb(hue, 0.85, 0.95)
    color = rgb_to_hex((int(r * 255), int(g * 255), int(b * 255)))

    # Glow rings
    for i in range(6, 0, -1):
        glow_size = size + i * 20
        alpha_color = colorsys.hsv_to_rgb((hue + 0.15) % 1, 0.7, 0.5)
        gr, gg, gb = [int(c * 255) for c in alpha_color]
        glow = rgb_to_hex((gr // (i + 1), gg // (i + 1), gb // (i + 1)))

        canvas.create_oval(
            circle_x - glow_size / 2,
            circle_y - glow_size / 2,
            circle_x + glow_size / 2,
            circle_y + glow_size / 2,
            outline=glow,
            width=1
        )

    # Main circle
    canvas.create_oval(
        circle_x - size,
        circle_y - size,
        circle_x + size,
        circle_y + size,
        fill=color,
        outline="white",
        width=2
    )

    # Rotating dots around circle
    for angle in range(0, 360, 60):
        rad = math.radians(angle + t * 100)
        dot_x = circle_x + math.cos(rad) * (size + 40)
        dot_y = circle_y + math.sin(rad) * (size + 40)

        dot_hue = (hue + angle / 360) % 1
        dr, dg, db = colorsys.hsv_to_rgb(dot_hue, 0.9, 0.8)
        dot_color = rgb_to_hex((int(dr * 255), int(dg * 255), int(db * 255)))

        canvas.create_oval(
            dot_x - 6, dot_y - 6,
            dot_x + 6, dot_y + 6,
            fill=dot_color, outline=""
        )

    root.after(16, animate)

canvas.bind("<Motion>", move_mouse)
animate()
root.mainloop()