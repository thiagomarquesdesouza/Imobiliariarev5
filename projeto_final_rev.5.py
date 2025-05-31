import sqlite3
import tkinter as tk
from tkinter import messagebox


def conectar_banco(nome_banco):
    return sqlite3.connect(nome_banco)


def criar_tabelas(conexao):
    cursor = conexao.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS USUARIO (
            nome TEXT NOT NULL,
            telefone NUMERIC NOT NULL,
            email TEXT NOT NULL,
            PRIMARY KEY(telefone)
        );''')
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS IMOVEL (
            proprietario TEXT NOT NULL,
            endereco TEXT NOT NULL,
            valor_imovel NUMERIC NOT NULL,
            categoria TEXT NOT NULL,
            PRIMARY KEY(endereco),
            FOREIGN KEY(proprietario) REFERENCES USUARIO(nome)
        );''')
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS TIPO (
            id_tipo INTEGER NOT NULL,
            pavimentos INTEGER NOT NULL,
            quartos INTEGER NOT NULL,
            banheiros INTEGER NOT NULL,
            varanda BOOLEAN NOT NULL,
            PRIMARY KEY(id_tipo)
        );''')
    conexao.commit()
    cursor.close()


def inserir_usuario(conexao, nome, telefone, email):
    cursor = conexao.cursor()
    cursor.execute(
        'INSERT INTO USUARIO (nome, telefone, email) VALUES (?, ?, ?)', (nome, telefone, email))
    conexao.commit()
    cursor.close()
    messagebox.showinfo("Sucesso", "Usuário inserido com sucesso!")


def atualizar_usuario(conexao, nome, telefone, email):
    cursor = conexao.cursor()
    cursor.execute('UPDATE USUARIO SET nome=?, email=? WHERE telefone=?',
                   (nome, email, telefone))
    conexao.commit()
    cursor.close()
    messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")


def deletar_usuario(conexao, telefone):
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM USUARIO WHERE telefone = ?', (telefone,))
    conexao.commit()
    cursor.close()
    messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")


def inserir_tipo(conexao, id_tipo, pavimentos, quartos, banheiros, varanda):
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO TIPO (id_tipo, pavimentos, quartos, banheiros, varanda) VALUES (?, ?, ?, ?, ?)',
                   (id_tipo, pavimentos, quartos, banheiros, varanda))
    conexao.commit()
    cursor.close()
    messagebox.showinfo("Sucesso", "Tipo inserido com sucesso!")


def atualizar_tipo(conexao, id_tipo, pavimentos, quartos, banheiros, varanda):
    cursor = conexao.cursor()
    cursor.execute('UPDATE TIPO SET pavimentos=?, quartos=?, banheiros=?, varanda=? WHERE id_tipo=?',
                   (pavimentos, quartos, banheiros, varanda, id_tipo))
    conexao.commit()
    cursor.close()
    messagebox.showinfo("Sucesso", "Tipo atualizado com sucesso!")


def deletar_tipo(conexao, id_tipo):
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM TIPO WHERE id_tipo = ?', (id_tipo,))
    conexao.commit()
    cursor.close()
    messagebox.showinfo("Sucesso", "Tipo excluído com sucesso!")


def inserir_imovel(conexao, proprietario, endereco, valor_imovel, categoria):
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO IMOVEL (proprietario, endereco, valor_imovel, categoria) VALUES (?, ?, ?, ?)',
                   (proprietario, endereco, valor_imovel, categoria))
    conexao.commit()
    cursor.close()
    messagebox.showinfo("Sucesso", "Imóvel inserido com sucesso!")


def atualizar_imovel(conexao, endereco, valor_imovel, categoria):
    cursor = conexao.cursor()
    cursor.execute('UPDATE IMOVEL SET valor_imovel=?, categoria=? WHERE endereco=?',
                   (valor_imovel, categoria, endereco))
    conexao.commit()
    cursor.close()
    messagebox.showinfo("Sucesso", "Imóvel atualizado com sucesso!")


def deletar_imovel(conexao, endereco):
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM IMOVEL WHERE endereco = ?', (endereco,))
    conexao.commit()
    cursor.close()
    messagebox.showinfo("Sucesso", "Imóvel excluído com sucesso!")


def submit_usuario():
    nome = nome_entry.get()
    telefone = telefone_entry.get()
    email = email_entry.get()

    try:
        if not nome or not telefone or not email:
            raise ValueError("Todos os campos devem ser preenchidos.")
        inserir_usuario(conexao, nome, telefone, email)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))


def update_usuario():
    nome = nome_entry.get()
    telefone = telefone_entry.get()
    email = email_entry.get()
    try:
        if not nome or not telefone or not email:
            raise ValueError("Todos os campos devem ser preenchidos.")
        atualizar_usuario(conexao, nome, telefone, email)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def delete_usuario():
    telefone = telefone_entry.get()
    try:
        if not telefone:
            raise ValueError("Informe o telefone para excluir o usuário.")
        deletar_usuario(conexao, telefone)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def submit_tipo():
    try:
        id_tipo = int(id_tipo_entry.get())
        pavimentos = int(pavimentos_entry.get())
        quartos = int(quartos_entry.get())
        banheiros = int(banheiros_entry.get())
        varanda = int(varanda_var.get())
        inserir_tipo(conexao, id_tipo, pavimentos, quartos, banheiros, varanda)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def update_tipo():
    try:
        id_tipo = int(id_tipo_entry.get())
        pavimentos = int(pavimentos_entry.get())
        quartos = int(quartos_entry.get())
        banheiros = int(banheiros_entry.get())
        varanda = int(varanda_var.get())
        atualizar_tipo(conexao, id_tipo, pavimentos,
                       quartos, banheiros, varanda)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def delete_tipo():
    try:
        id_tipo = int(id_tipo_entry.get())
        deletar_tipo(conexao, id_tipo)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def submit_imovel():
    try:
        proprietario = nome_entry.get()
        endereco = endereco_entry.get()
        valor_imovel = float(valor_imovel_entry.get())
        categoria = categoria_var.get()
        inserir_imovel(conexao, proprietario, endereco,
                       valor_imovel, categoria)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def update_imovel():
    try:
        endereco = endereco_entry.get()
        valor_imovel = float(valor_imovel_entry.get())
        categoria = categoria_var.get()
        atualizar_imovel(conexao, endereco, valor_imovel, categoria)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def delete_imovel():
    try:
        endereco = endereco_entry.get()
        deletar_imovel(conexao, endereco)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


conexao = conectar_banco('IMOBILIARIA.db')
criar_tabelas(conexao)

root = tk.Tk()
root.title("Formulário de Cadastro")
frame = tk.Frame(root)
frame.pack(padx=100, pady=10)


tk.Label(frame, text="Nome e Sobrenome:").grid(row=0, column=0, sticky="e")
nome_entry = tk.Entry(frame)
nome_entry.grid(row=0, column=1)

tk.Label(frame, text="Telefone com ddd:").grid(row=1, column=0, sticky="e")
telefone_entry = tk.Entry(frame)
telefone_entry.grid(row=1, column=1)

tk.Label(frame, text="Email:").grid(row=2, column=0, sticky="e")
email_entry = tk.Entry(frame)
email_entry.grid(row=2, column=1)

tk.Button(frame, text="Inserir Usuário", command=submit_usuario).grid(
    row=3, column=1, pady=10)
tk.Button(frame, text="Atualizar Usuário",
          command=update_usuario).grid(row=4, column=1)
tk.Button(frame, text="Excluir Usuário",
          command=delete_usuario).grid(row=5, column=1)


tk.Label(frame, text="ID Tipo:").grid(row=6, column=0, sticky="e")
id_tipo_entry = tk.Entry(frame)
id_tipo_entry.grid(row=6, column=1)

tk.Label(frame, text="Pavimentos:").grid(row=7, column=0, sticky="e")
pavimentos_entry = tk.Entry(frame)
pavimentos_entry.grid(row=7, column=1)

tk.Label(frame, text="Quartos:").grid(row=8, column=0, sticky="e")
quartos_entry = tk.Entry(frame)
quartos_entry.grid(row=8, column=1)

tk.Label(frame, text="Banheiros:").grid(row=9, column=0, sticky="e")
banheiros_entry = tk.Entry(frame)
banheiros_entry.grid(row=9, column=1)

varanda_var = tk.StringVar(value="0")
tk.Label(frame, text="Varanda:").grid(row=10, column=0, sticky="e")
tk.Radiobutton(frame, text="Sim", variable=varanda_var,
               value="1").grid(row=10, column=1, sticky="w")
tk.Radiobutton(frame, text="Não", variable=varanda_var,
               value="0").grid(row=10, column=1, sticky="e")

tk.Button(frame, text="Inserir Tipo",
          command=submit_tipo).grid(row=11, column=1)
tk.Button(frame, text="Atualizar Tipo",
          command=update_tipo).grid(row=12, column=1)
tk.Button(frame, text="Excluir Tipo",
          command=delete_tipo).grid(row=13, column=1)


tk.Label(frame, text="Endereço:").grid(row=14, column=0, sticky="e")
endereco_entry = tk.Entry(frame)
endereco_entry.grid(row=14, column=1)

tk.Label(frame, text="Valor do Imóvel:").grid(row=15, column=0, sticky="e")
valor_imovel_entry = tk.Entry(frame)
valor_imovel_entry.grid(row=15, column=1)

tk.Label(frame, text="Categoria:").grid(row=16, column=0, sticky="e")
categoria_var = tk.StringVar(value="casa")
tk.Radiobutton(frame, text="Casa", variable=categoria_var,
               value="casa").grid(row=16, column=1, sticky="w")
tk.Radiobutton(frame, text="Apartamento", variable=categoria_var,
               value="apartamento").grid(row=16, column=2, sticky="e")

tk.Button(frame, text="Inserir Imóvel",
          command=submit_imovel).grid(row=17, column=1)
tk.Button(frame, text="Atualizar Imóvel",
          command=update_imovel).grid(row=18, column=1)
tk.Button(frame, text="Excluir Imóvel",
          command=delete_imovel).grid(row=19, column=1)

root.mainloop()
conexao.close()
