import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Hello World")
    window.geometry("300x200")

    bg_color = "#228B22"  # Forest green

    canvas = tk.Canvas(window, width=300, height=200, bg=bg_color, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Pixel banana (each pixel is 8x8)
    pixel = 8
    banana_x, banana_y = 110, 80

    # Banana shape (yellow)
    banana_pixels = [
        (3, 0), (4, 0),
        (2, 1), (3, 1), (4, 1), (5, 1),
        (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2),
        (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
        (2, 4), (3, 4), (4, 4), (5, 4),
        (3, 5), (4, 5),
    ]

    for px, py in banana_pixels:
        canvas.create_rectangle(
            banana_x + px * pixel, banana_y + py * pixel,
            banana_x + (px + 1) * pixel, banana_y + (py + 1) * pixel,
            fill="yellow", outline="gold"
        )

    # Googly eyes (white with black pupils)
    # Left eye
    canvas.create_oval(banana_x + 2*pixel + 2, banana_y + 2*pixel + 2,
                       banana_x + 3*pixel - 2, banana_y + 3*pixel - 2,
                       fill="white", outline="black")
    canvas.create_oval(banana_x + 2*pixel + 4, banana_y + 2*pixel + 4,
                       banana_x + 3*pixel - 4, banana_y + 3*pixel - 4,
                       fill="black")

    # Right eye
    canvas.create_oval(banana_x + 4*pixel + 2, banana_y + 2*pixel + 2,
                       banana_x + 5*pixel - 2, banana_y + 3*pixel - 2,
                       fill="white", outline="black")
    canvas.create_oval(banana_x + 4*pixel + 4, banana_y + 2*pixel + 4,
                       banana_x + 5*pixel - 4, banana_y + 3*pixel - 4,
                       fill="black")

    # Smile
    canvas.create_arc(banana_x + 2*pixel, banana_y + 3*pixel,
                      banana_x + 5*pixel, banana_y + 4*pixel + 4,
                      start=200, extent=140, style="arc", outline="black", width=2)

    # Hello World label
    canvas.create_text(150, 30, text="Hello, World!", font=("Arial", 18, "bold"), fill="white")

    # OK button
    button = tk.Button(window, text="OK", command=window.destroy, width=10, bg="green", fg="white")
    canvas.create_window(150, 170, window=button)

    window.mainloop()

if __name__ == "__main__":
    main()
