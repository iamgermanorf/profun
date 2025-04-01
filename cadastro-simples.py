import tkinter as tk
from tkinter import messagebox

# Lista para armazenar os cadastros
cadastros = []

# Função lambda para verificar se o telefone contém apenas números
validar_telefone = lambda telefone: telefone.isdigit()

# Função closure para validar entrada (nome e telefone)
def validar_entrada(nome, telefone):
    def verificar():
        return bool(nome.strip()) and validar_telefone(telefone)
    return verificar

# Função de alta ordem para aplicar qualquer função de validação aos campos
def aplicar_validacao(funcao_validacao, nome, telefone):
    return funcao_validacao(nome, telefone)()

# Função para adicionar um cadastro
def adicionar_cadastro():
    nome = entrada_nome.get()
    telefone = entrada_telefone.get()

    # Aplicando a validação usando a closure e a função de alta ordem
    validar = aplicar_validacao(validar_entrada(nome, telefone), nome, telefone)

    if validar:
        cadastros.append({"nome": nome, "telefone": telefone})
        entrada_nome.delete(0, tk.END)
        entrada_telefone.delete(0, tk.END)
        mostrar_cadastros()
    else:
        messagebox.showerror("Erro", "Nome não pode estar vazio e telefone deve conter apenas números.")

# Função para exibir os cadastros com list comprehension
def mostrar_cadastros():
    lista_cadastros.delete(0, tk.END)
    [lista_cadastros.insert(tk.END, f"{c['nome']} - {c['telefone']}") for c in cadastros]

# Interface gráfica
janela = tk.Tk()
janela.title("Cadastro Simples")

tk.Label(janela, text="Nome:").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Telefone:").pack()
entrada_telefone = tk.Entry(janela)
entrada_telefone.pack()

tk.Button(janela, text="Adicionar", command=adicionar_cadastro).pack()

tk.Label(janela, text="Cadastros:").pack()
lista_cadastros = tk.Listbox(janela)
lista_cadastros.pack()

janela.mainloop()
