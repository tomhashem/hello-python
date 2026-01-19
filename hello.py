import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Hello World")
    window.geometry("300x150")
    window.configure(bg="blue")

    label = tk.Label(window, text="Hello, World!", font=("Arial", 18), bg="blue", fg="white")
    label.pack(pady=30)

    button = tk.Button(window, text="OK", command=window.destroy, width=10, bg="green", fg="white")
    button.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
