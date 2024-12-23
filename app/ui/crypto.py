import pyperclip
import tkinter as tk
from tkinter import ttk

from app.crypto import Crypto
from app.ui.styles import font_title_config


def CryptAnalyzeScreen(master: tk.Widget):
    frame = ttk.Frame(master, padding=10)

    title = ttk.Label(frame, text="Cripto Análise", font=font_title_config)
    title.pack()

    form_frame = ttk.Frame(frame)
    form_frame.pack()

    ttk.Label(form_frame, text="Frase original: ").grid(row=0, column=0)
    original_entry = ttk.Entry(form_frame)
    original_entry.grid(row=0, column=1)

    ttk.Label(form_frame, text="Frase criptografada: ").grid(row=1, column=0)
    crypt_entry = ttk.Entry(form_frame)
    crypt_entry.grid(row=1, column=1)

    result_text = ttk.Label(form_frame, )
    result_text.grid(row=3, column=0)

    def handle_submit():
        key = Crypto.find_key(original_entry.get().upper(), crypt_entry.get().upper())
        print(f'{key=}')
        # if key == -1:
        #     key = 'não encontrada'
        result_text['text'] = f'Chave: {key}'


    button_submit = ttk.Button(form_frame, text="Encontrar", command=handle_submit)
    button_submit.grid(row=2, column=0)

    frame.pack(fill='both', expand=True)
    return frame


def EncryptScreen(master: tk.Widget):
    frame = ttk.Frame(master, padding=10)

    title = ttk.Label(frame, text="Encriptação", font=font_title_config)
    title.pack()

    form_frame = ttk.Frame(frame)
    form_frame.pack()

    ttk.Label(form_frame, text="Chave: ").grid(row=0, column=0)
    key_entry = ttk.Entry(form_frame)
    key_entry.grid(row=0, column=1)

    ttk.Label(form_frame, text="Frase original: ").grid(row=1, column=0)
    text_entry = ttk.Entry(form_frame)
    text_entry.grid(row=1, column=1)

    result_text = ttk.Label(form_frame, )
    result_text.grid(row=3, column=0)

    def handle_submit():
        key = [int(item) for item in key_entry.get()]
        crypt = Crypto.encrypt(key, text_entry.get().upper())
        result_text['text'] = crypt


    button_submit = ttk.Button(form_frame, text="Encriptar", command=handle_submit)
    button_submit.grid(row=2, column=0)

    def handle_copy():
        pyperclip.copy(result_text['text'])


    button_copy = ttk.Button(form_frame, text="Copiar", command=handle_copy)
    button_copy.grid(row=2, column=1)

    frame.pack(fill='both', expand=True)
    return frame


def DecryptScreen(master: tk.Widget):
    frame = ttk.Frame(master, padding=10)

    title = ttk.Label(frame, text="Decriptação", font=font_title_config)
    title.pack()

    form_frame = ttk.Frame(frame)
    form_frame.pack()

    ttk.Label(form_frame, text="Chave: ").grid(row=0, column=0)
    key_entry = ttk.Entry(form_frame)
    key_entry.grid(row=0, column=1)

    ttk.Label(form_frame, text="Frase criptografada: ").grid(row=1, column=0)
    text_entry = ttk.Entry(form_frame)
    text_entry.grid(row=1, column=1)

    result_text = ttk.Label(form_frame, )
    result_text.grid(row=3, column=0)

    def handle_submit():
        key = [int(item) for item in key_entry.get()]
        crypt = Crypto.decrypt(key, text_entry.get().upper())
        result_text['text'] = crypt


    button_submit = ttk.Button(form_frame, text="Decriptar", command=handle_submit)
    button_submit.grid(row=2, column=0)

    frame.pack(fill='both', expand=True)
    return frame
