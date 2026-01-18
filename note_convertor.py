import tkinter as tk
from tkinter import font
from tkinter import messagebox

def create_secondary_window(title, sizex, sizey):
    global root_second, is_open
    is_open = True
    root_second = tk.Toplevel(master=root)
    root_second.grab_set()
    root_second.title(title)
    second_window_width = sizex
    second_window_height = sizey
    screen_width = root_second.winfo_screenwidth()
    screen_height = root_second.winfo_screenheight()
    center_x = int(screen_width/2 - second_window_width / 2)
    center_y = int(screen_height/2 - second_window_height / 2)
    root_second.geometry(f'{second_window_width}x{second_window_height}+{center_x}+{center_y}')
    root_second.resizable(False, False)
    root_second.config(background="#202020")
    root_second.columnconfigure(0, weight=1)
    root_second.columnconfigure(1, weight=1)
    root_second.columnconfigure(2, weight=1)
    if title == "Credits":
        label_name = tk.Label(root_second, text="Note Convertor", background='#202020', foreground='#ffffff', anchor='e', font=base_font)
        label_name.grid(row=0, column=0, sticky='nsew', pady=10)
        label_v = tk.Label(root_second, text="Version 1", background="#202020", foreground="#ffffff", anchor='sw')
        label_v.grid(row=0, column=1, sticky='nsew', pady=10)
        label_dev = tk.Label(root_second, text="Développé par : Marceau", background='#202020', foreground='#ffffff', font=custom_font)
        label_dev.grid(row=1, column=0, columnspan=2, pady=10)
        label_git = tk.Label(root_second, text="Mon Github : MarceauMRS", background='#202020', foreground='#ffffff', font=custom_font)
        label_git.grid(row=2, column=0, columnspan=2, pady=20)
        label_license = tk.Label(root_second, text="Licence : GN GPLv3", background='#202020', foreground='#ffffff', font=custom_font)
        label_license.grid(row=3, column=0, columnspan=2)
        text_link = tk.Text(root_second, background='#202020', foreground='#ffffff', borderwidth=0)
        text_link.grid(row=4, column=0, columnspan=2)
        text_link.tag_configure("center", justify="center")
        text_link.insert("1.0", "https://www.gnu.org/licenses/gpl-3.0.en.html")
        text_link.tag_add("center", "1.0", "end")
        text_link.configure(state=tk.DISABLED)

root = tk.Tk()
root.title("Note Convertor")
window_width = 300
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.config(background="#202020")
root.columnconfigure(0, weight=1)
frame_title = tk.Frame(root, background='#202020')
frame_title.grid(row=0, column=0, pady=10)
frame_base = tk.Frame(root, background='#202020')
frame_base.grid(row=1, column=0, pady=15)
frame_result = tk.Frame(root, background='#202020')
frame_result.grid(row=2, column=0, pady=15)
custom_font = font.Font(size=12)
base_font = font.Font(size=15)
menubar = tk.Menu(root)
menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu", menu=menu)
menu.add_command(label="A propos...", command=lambda: create_secondary_window(title="Credits", sizex=400, sizey=220))
menu.add_separator()
menu.add_command(label="Quitter", command=root.quit)
root.config(menu=menubar)

def verif_virg(entry):
    for a,b in enumerate(entry.get()):
        if b == ',':
            entry.insert(a, '.')
            entry.delete(a+1, a+2)
def on_entry_change(num):
    global label_result
    try:
        verif_virg(entry_base)
        verif_virg(entry_convert)
        verif_virg(entry_max)
        label_result.destroy()
        label_result = tk.Label(frame_result, text=f"{round(float(entry_base.get()) * float(entry_convert.get()) / float(entry_max.get()), 2)} / {entry_convert.get()}", background='#202020', foreground='#ffffff', font=custom_font)
        label_result.grid(row=1, column=0)
    except:
        label_result.destroy()
        label_result = tk.Label(frame_result, text=f"Error", background='#202020', foreground="#AA0909", font=custom_font)
        label_result.grid(row=1, column=0)

label_title = tk.Label(frame_title, text="Convertir la note sur :", background='#202020', foreground='#ffffff', font=custom_font)
label_title.grid(row=0, column=0)
convert_default = tk.StringVar(value='20')
entry_convert = tk.Entry(frame_title, width=4, textvariable=convert_default, font=custom_font)
entry_convert.grid(row=1, column=0, pady=5)
entry_convert.bind("<KeyRelease>", on_entry_change)
label_note = tk.Label(frame_base, text="Note actuelle :", background='#202020', foreground='#ffffff', font=base_font)
label_note.grid(row=0, column=0, pady=10, sticky='e')
base_default = tk.StringVar(value='15')
entry_base = tk.Entry(frame_base, width=4, textvariable=base_default, font=base_font)
entry_base.grid(row=0, column=1, sticky='w')
entry_base.bind("<KeyRelease>", on_entry_change)
label_max = tk.Label(frame_base, text="Note maximale :", background='#202020', foreground='#ffffff', font=custom_font)
label_max.grid(row=1, column=0, sticky='e')
max_default = tk.StringVar(value='25')
entry_max = tk.Entry(frame_base, width=4, textvariable=max_default, font=custom_font)
entry_max.grid(row=1, column=1, sticky='we')
entry_max.bind("<KeyRelease>", on_entry_change)
label_text_result = tk.Label(frame_result, text="Le résultat est :", background='#202020', foreground='#ffffff', font=custom_font)
label_text_result.grid(row=0, column=0)
label_result = tk.Label(frame_result, text=f"{round(float(entry_base.get()) * float(entry_convert.get()) / float(entry_max.get()), 2)} / {entry_convert.get()}", background='#202020', foreground='#ffffff', font=custom_font)
label_result.grid(row=1, column=0)

root.mainloop()