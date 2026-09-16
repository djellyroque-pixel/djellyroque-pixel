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

           # ================ FRAME DE BOTOẼS ================
    frame botoes = tk.Frame(self.root, bg="#f0f4f8")
    frame botoes.pack(pady=10)

    #Botão inserir
    self.btn_inserir = tk.Button(
      frame_botoes,
      text="🏥inserir",
      font=("Arial", 11, "bold")
      bg="#f0f4f8", fg("white")
      width=12, cursor="hand2",
      relief="flat",
      command=self.inserir
    )
    self.btn_inserir.pack(side="left", padx=5)
   
    # Botão Editar
    self.btn_editar = tk.Button(
      frame_botoes,
      text="- Editar",
      font=("Arial", 11, "bold"),
      bg="#f39c12", fg="White",
      width=12, cursor="hand2"
      relief="flat",
      command=self.editar
    )
    self.btn_editar.pack(side="left", padx=5)
   
    # Botão Deletar
    self.btn_deletar = tk.Button(
      frame_botoes,
      text="🗑️ Deletar",
      font=("Arial", 11, "bold"),
      bg="#e74c3c", fg="White",
      width=12, cursor="hand2",
      relief="flat",
      command=self.Deletar
    )
    self.btn_deletar.pack(side="left", padx=5)

    # Botão limpar campos
    self.btn_inserir = tk.Button(
      frame_botoes,
      text="limpar",
      font=("Arial", 11, "bold")
      bg="#f0f4f8", fg("white")
      width=12, cursor="hand2",
      relief="flat",
      command=self.inserir
    )
    self.btn_limpar.pack
   
   
    # ========== LISTA DE ITENS (TREEVIEW) =========
    frame_lista = tk.Frame(self.root, bg="#f0f4f8")
    frame_lista.pack(pady=10, padx=20, fill="both", expand=True)
   
    # Scrollbar
    scrollbar = tk.Scrollbar(frame_lista)
    scrollbar.pack(side="right", fill="y")
   
    # Treeview
    colunas = ("descricao", "quantidade", "preco", "subtotal")
    self.tree = ttk.Treeview(
        frame_lista,
        show= "headings",
        yscrollcommand=scrollbar.set,
        height=10
    )
    scrollbar.config(command=self.tree.yview)
   
    # Configurar colunas
    self.tree.heading("descricao", text="Descrição")
    self.tree.heading("quantidade", text="0td")
    self.tree.heading("preco", text="Preço Unit. (R$)")
    self.tree.heading("subtotal", text="Subtotal (R$)")
   
    self.tree.column("descricao", widht=250, anchor="W")
    self.tree.column("quantidade", widht=60, anchor="center")
    self.tree.column("preco", widht=120, anchor="e")
    self.tree.column("subtotal", widht=120, anchor="e")
   
    self.treee.pack(fill)
   
    # Evento da seleçao
    self.tree.bind("<<TreeviewSelect>>", self.on_select)
   
    # ========= TOTAL =========
    frame_total = tk.Frame(self.root, bg="#f0f4f8")
    frame_total.pack(pady=10, padx=20, fill="X")
   
    self.lbl_total = tk.Label(
        frame_total,
        text="TOTAL: R$ 0,00",
        font=("Arial", 16, "bold"),
        bg="#f0f4f8",
        fg="#1a5276",
    )
    self.lbl_total.pack(side="right")
   
    # ======== STATUS BAR =========
    self.lbl_status = tk.Label(
        self.root,
        text="pronto. Selecione um item para editar ou deletar.",
        font=("Arial", 9),
        bg="#d5dbdb"
        fg="#2c3e50",
        anchor="W"
    )
    self.lbl_status.pack(fill="X", side="botton")

    # Estilo Treeview
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", font=("Arial", 10), rowheight=25)
style.configure("Treeview.Heading", font=("Arial", 11, "bold"), background="#3498db", foreground="white")
style.map("Treeview", background=[("selected", "#aed6f1")])

def on_select(self, event):
"""Quando um item da lista é selecionado, preenche os campos"""
selecao = self.tree.selection()
if selecao:
item_id = selecao[0]
valores = self.tree.item(item_id, "values")

self.txt_descricao.delete(0, tk.END)
self.txt_descricao.insert(0, valores[0])

self.txt_quantidade.delete(0, tk.END)
self.txt_quantidade.insert(0, valores[1])

self.txt_preco.delete(0, tk.END)
self.txt_preco.insert(0, valores[2].replace("R$ ", "").replace(".", "").replace(",", "."))

self.item_selecionado = item_id
self.lbl_status.config(text=f"Item selecionado: {valores[0]}")

def limpar_campos(self):
"""Limpa todos os campos de entrada"""
self.txt_descricao.delete(0, tk.END)
self.txt_quantidade.delete(0, tk.END)
self.txt_preco.delete(0, tk.END)
self.item_selecionado = None
self.tree.selection_remove(self.tree.selection())
self.lbl_status.config(text="Campos limpos. Pronto para inserir novo item.")
self.txt_descricao.focus()

def validar_entrada(self):
"""Valida os campos de entrada"""
descricao = self.txt_descricao.get().strip()
quantidade = self.txt_quantidade.get().strip()
preco = self.txt_preco.get().strip()

if not descricao:
messagebox.showwarning("Aviso", "Digite a descrição do item!")
return None

try:
qtd = float(quantidade.replace(",", "."))
if qtd <= 0:
messagebox.showwarning("Aviso", "Quantidade deve ser maior que zero!")
return None
except ValueError:
messagebox.showwarning("Aviso", "Quantidade inválida!")
return None

try:
prc = float(preco.replace(",", "."))
if prc < 0:
messagebox.showwarning("Aviso", "Preço não pode ser negativo!")
return None
except ValueError:
messagebox.showwarning("Aviso", "Preço inválido!")
return None

return {"descricao": descricao, "quantidade": qtd, "preco": prc}

def inserir(self):
"""Insere um novo item na lista"""
dados = self.validar_entrada()
if not dados:
return

self.itens.append(dados)
self.salvar_no_arquivo()
self.atualizar_lista()
self.limpar_campos()
self.lbl_status.config(text=f"Item '{dados['descricao']}' inserido com sucesso!")
messagebox.showinfo("Sucesso", f"Item '{dados['descricao']}' inserido!")

def editar(self):
"""Edita o item selecionado"""
if not self.item_selecionado:
messagebox.showwarning("Aviso", "Selecione um item na lista para editar!")
return

dados = self.validar_entrada()
if not dados:
return

# Encontrar o índice do item selecionado
idx = self.tree.index(self.item_selecionado)
self.itens[idx] = dados

self.salvar_no_arquivo()
self.atualizar_lista()
self.limpar_campos()
self.lbl_status.config(text=f"Item '{dados['descricao']}' editado com sucesso!")
messagebox.showinfo("Sucesso", f"Item '{dados['descricao']}' atualizado!")

def deletar(self):
"""Deleta o item selecionado"""
if not self.item_selecionado:
messagebox.showwarning("Aviso", "Selecione um item na lista para deletar!")
return

idx = self.tree.index(self.item_selecionado)
item_nome = self.itens[idx]["descricao"]

if messagebox.askyesno("Confirmar", f"Deseja realmente deletar '{item_nome}'?"):
self.itens.pop(idx)
self.salvar_no_arquivo()
self.atualizar_lista()
self.limpar_campos()
self.lbl_status.config(text=f"Item '{item_nome}' deletado.")
messagebox.showinfo("Sucesso", f"Item '{item_nome}' removido!")

def atualizar_lista(self):
"""Atualiza a Treeview com os dados da lista"""

# Limpar lista
for item in self.tree.get_children():
 self.tree.delete(item)

total = 0.0

for item in self.itens:
 subtotal = item["quantidade"] * item["preco"]
total += subtotal

self.tree.insert("", "end", values=(
item["descricao"],
f"{item['quantidade']:.0f}",
f"R$ {item['preco']:,.2f}",
f"R$ {subtotal:,.2f}"
))

self.lbl_total.config(text=f"TOTAL: R$ {total:,.2f}")

def salvar_no_arquivo(self):
      """Salva a lista no arquivo de texto"""
    try:
    with open(ARQUIVO, "w", encoding="utf-8") as f:
    f.write("=" * 60 + "\n")
    f.write(" LISTA DE COMPRAS\n")
    f.write("=" * 60 + "\n\n")

    total = 0.0
    for i, item in enumerate(self.itens, 1):
    subtotal = item["quantidade"] * item["preco"]
    total += subtotal

f.write(f"{i}. {item['descricao']}\n")
f.write(f" Quantidade: {item['quantidade']:.0f}\n")
f.write(f" Preço Unit.: R$ {item['preco']:,.2f}\n")
f.write(f" Subtotal: R$ {subtotal:,.2f}\n")
f.write("-" * 40 + "\n")

f.write("\n" + "=" * 60 + "\n")
f.write(f" TOTAL DA COMPRA: R$ {total:,.2f}\n")
f.write("=" * 60 + "\n")
except
  Exception as e:
messagebox.showerror("Erro", f"Erro ao salvar arquivo: {e}")

def carregar_do_arquivo(self):
"""Carrega os dados do arquivo (se existir)"""
if not os.path.exists(ARQUIVO):
return

try:
with open(ARQUIVO, "r", encoding="utf-8") as f:
linhas = f.readlines()

# Parser simples do arquivo
i = 0
while i < len(linhas):
linha = linhas[i].strip()
if linha and linha[0].isdigit() and "." in linha:
descricao = linha.split(".", 1)[1].strip()

qtd_str = linhas[i+1].strip().split(":")[1].strip() if i+1 < len(linhas) else "1"
qtd = float(qtd_str)

preco_str = linhas[i+2].strip().split("R$")[1].strip() if i+2 < len(linhas) else "0"
preco = float(preco_str.replace(".", "").replace(",", "."))

self.itens.append({
"descricao": descricao,
"quantidade": qtd,
"preco": preco
})
i += 4
else:
i += 1

except Exception as e:
print(f"Erro ao carregar arquivo: {e}")


# ============================================
# EXECUÇÃO
# ============================================
if __name__ == "__main__":
root = tk.Tk()
app = ListaComprasApp(root)
root.mainloop()