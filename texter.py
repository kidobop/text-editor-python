import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0,minsize=400)
    window.columnconfigure(0,minsize=500)

    text_edit = tk.Text(window, font="Montserrat 18 italic")
    text_edit.grid(row=0,column=1)

    window.mainloop()

main()