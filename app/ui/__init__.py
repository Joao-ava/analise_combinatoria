import tkinter as tk
from tkinter import ttk

from app.ui.crypto import CryptAnalyzeScreen, EncryptScreen, DecryptScreen
from app.ui.plates import StateByPlateScreen


def main():
    # Criação da janela principal
    root = tk.Tk()
    root.title("Análise Combinatória")

    notebook = ttk.Notebook(root)
    # projeto 1
    notebook.add(CryptAnalyzeScreen(notebook), text="CRIPTOANÁLISE")
    notebook.add(EncryptScreen(notebook), text="ENCRIPTAÇÃO")
    notebook.add(DecryptScreen(notebook), text="DECRIPTAÇÃO")

    # projeto 2
    notebook.add(StateByPlateScreen(notebook), text='Placas')

    notebook.grid(row=0, column=0)

    # Início do loop principal do Tkinter
    root.mainloop()
