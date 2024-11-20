import tkinter as tk
from tkinter import ttk

from app.ui.crypto import CryptAnalyzeScreen, EncryptScreen, DecryptScreen


def main():
    # Criação da janela principal
    root = tk.Tk()
    root.title("Análise Combinatória")

    notebook = ttk.Notebook(root)
    # projeto 1
    notebook.add(CryptAnalyzeScreen(notebook), text="CRIPTOANÁLISE")
    notebook.add(EncryptScreen(notebook), text="ENCRIPTAÇÃO")
    notebook.add(DecryptScreen(notebook), text="DECRIPTAÇÃO")

    notebook.grid(row=0, column=0)

    # Início do loop principal do Tkinter
    root.mainloop()
