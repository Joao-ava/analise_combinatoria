import tkinter as tk
from tkinter import ttk

from app.plate import Plate
from app.ui.styles import font_title_config


def StateByPlateScreen(master: tk.Widget):
    frame = ttk.Frame(master, padding=10)

    title = ttk.Label(frame, text="Placas", font=font_title_config)
    title.pack()

    # encontrar estado pela placa
    form_frame = ttk.Frame(frame)
    form_frame.pack()

    ttk.Label(form_frame, text="Placa: ").grid(row=0, column=0)
    plate_entry = ttk.Entry(form_frame)
    plate_entry.grid(row=0, column=1)

    result_text = ttk.Label(form_frame, )
    result_text.grid(row=2, column=0)

    def handle_submit():
        state = Plate.find_state(plate_entry.get())
        result_text['text'] = state


    button_submit = ttk.Button(form_frame, text="Encontrar", command=handle_submit)
    button_submit.grid(row=1, column=0)

    # placas por estado
    state_frame = ttk.Frame(frame)
    state_frame.pack()

    ttk.Label(state_frame, text="Placas por estado", font=font_title_config).pack()

    ttk.Label(state_frame, text="Ceará: "+ Plate.count_ce()).pack()
    ttk.Label(state_frame, text="Maranhão: "+ Plate.count_ma()).pack()
    ttk.Label(state_frame, text="Piauí: "+ Plate.count_pi()).pack()

    frame.pack(fill='both', expand=True)
    return frame