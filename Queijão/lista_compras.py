import tkinter as tk
from tkinter import ttk,messagebox
import 

# ========================================================
# LISTA DE COMPRAS - aplicativo em tkinter 
#=========================================================
ARQUIVO = "lista_compras.txt"

class ListaComprasApp:
    def __init__(self, root):
    self.root = root
    self.root.title( "  Lista de compras")
    self.root.geomtry("750x550")
    self.root.configure(bg= "#f0f4f8")

    # Dados em memória
    self.itens = []
    self.item_selecionado = None

    self.criar_widgets()
    self.carregar_do_arquivo()
    self.atualizar_lista()


    def criar_widgets(self):
        # ======== TÍTULO ========
        lbl_titulo = tk.Label(
            self.root,
            text=" LISTA DE COMPRAS",
            font=("Arial", 20, "bold"),
            bg="#f0f4f8",
            fg="#1a5276"
        )
        lbl_titulo.pack(pady=10)

        # ========== FRAME DE ENTRADA ==========
        frame_entrada = tk.Frame(self.root, bg="#f0f4f8")
        frame_entrada.pack(pady=10, padx=20, fill="x")

        # Descrição
        tk.label(frame_entrada, text="Descrição:", font=("Ariel , 11"), bg="#f0f4f8", fg="#2c3e50").grid(row=0, coluam=0 , padx=5, sticky="e")
        self.txt_deescricao = tl.Entry(frame_entrada, font=("Ariel" ,11), width=30, rellf="solid, bg=1")
        self.txt_descricao.grid(row=0, column=1, padx=5, pady=5)

        # Quantidade 
        tk.label(frame_entrada, text="Quantidade:", font=("Ariel , 11"), bg="#f0f4f8", fg="#2c3e50").grid(row=0, coluam=0 , padx=5, sticky="e")
        self.txt_quantidade = tl.Entry(frame_entrada, font=("Ariel" ,11), width=30, rellf="solid, bg=1")
        self.txt_quantidade.grid(row=0, column=1, padx=5, pady=5)

        #preço
        tk.label(frame_entrada, text="Descrição:", font=("Ariel , 11"), bg="#f0f4f8", fg="#2c3e50").grid(row=0, coluam=0 , padx=5, sticky="e")
        self.txt_preço = tl.Entry(frame_entrada, font=("Ariel" ,11), width=30, rellf="solid, bg=1")
        self.txt_preço.grid(row=0, column=1, padx=5, pady=5)
