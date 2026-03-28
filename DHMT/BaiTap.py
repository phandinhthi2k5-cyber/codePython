import tkinter as tk

# ================= DDA =================
def draw_dda():
    canvas.delete("all")

    x1, y1 = 50, 50
    x2, y2 = 300, 200

    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1

    for i in range(steps):
        canvas.create_oval(round(x), round(y), round(x)+2, round(y)+2, fill="black")
        x += x_inc
        y += y_inc

# ================= BRESENHAM =================
def draw_bresenham():
    canvas.delete("all")

    x1, y1 = 50, 250
    x2, y2 = 300, 100

    dx = x2 - x1
    dy = y2 - y1

    x, y = x1, y1

    if dx == 0:
        return

    p = 2*abs(dy) - abs(dx)

    for i in range(abs(dx)):
        canvas.create_oval(x, y, x+2, y+2, fill="red")

        if p < 0:
            x += 1
            p += 2*abs(dy)
        else:
            x += 1
            y += -1 if dy < 0 else 1
            p += 2*(abs(dy) - abs(dx))

# ================= CIRCLE =================
def draw_circle():
    canvas.delete("all")

    xc, yc = 200, 150
    r = 80

    x = 0
    y = r
    p = 1 - r

    while x <= y:
        plot_circle_points(xc, yc, x, y)

        x += 1
        if p < 0:
            p += 2*x + 1
        else:
            y -= 1
            p += 2*(x - y) + 1

def plot_circle_points(xc, yc, x, y):
    points = [
        (xc+x, yc+y), (xc-x, yc+y),
        (xc+x, yc-y), (xc-x, yc-y),
        (xc+y, yc+x), (xc-y, yc+x),
        (xc+y, yc-x), (xc-y, yc-x)
    ]
    for px, py in points:
        canvas.create_oval(px, py, px+2, py+2, fill="blue")

# ================= ELLIPSE =================
def draw_ellipse():
    canvas.delete("all")

    xc, yc = 200, 150
    a, b = 120, 60

    x = 0
    y = b

    a2 = a*a
    b2 = b*b

    # Region 1
    p1 = b2 - a2*b + 0.25*a2

    while b2*x < a2*y:
        plot_ellipse_points(xc, yc, x, y)

        x += 1
        if p1 < 0:
            p1 += b2*(2*x + 1)
        else:
            y -= 1
            p1 += b2*(2*x + 1) - 2*a2*y

    # Region 2
    p2 = b2*(x+0.5)**2 + a2*(y-1)**2 - a2*b2

    while y >= 0:
        plot_ellipse_points(xc, yc, x, y)

        y -= 1
        if p2 > 0:
            p2 -= 2*a2*y + a2
        else:
            x += 1
            p2 += 2*b2*x - 2*a2*y + a2

def plot_ellipse_points(xc, yc, x, y):
    points = [
        (xc+x, yc+y), (xc-x, yc+y),
        (xc+x, yc-y), (xc-x, yc-y)
    ]
    for px, py in points:
        canvas.create_oval(px, py, px+2, py+2, fill="green")

# ================= GUI =================
root = tk.Tk()
root.title("Đồ họa máy tính - DDA | Bresenham | Circle | Ellipse")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="DDA", command=draw_dda).pack(side="left")
tk.Button(frame, text="Bresenham", command=draw_bresenham).pack(side="left")
tk.Button(frame, text="Circle", command=draw_circle).pack(side="left")
tk.Button(frame, text="Ellipse", command=draw_ellipse).pack(side="left")

root.mainloop()