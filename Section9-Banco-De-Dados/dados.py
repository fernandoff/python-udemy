import sqlite3

# 1- Conectar no BD
def conecta_bd():
    conexao = sqlite3.connect('titulo.db')
    return conexao

# 2- Verificar se o filme já existe
def filme_existe(nome):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM filmes WHERE nome = ?", (nome,))
    count = cursor.fetchone()[0]
    conexao.close()
    return count > 0

# 3- Inserir Dados
def insere_dados(nome, ano, nota):
    if filme_existe(nome):
        return False  # Filme já existe
    
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute( 
    """
        INSERT INTO filmes(nome, ano, nota)
        VALUES (?, ?, ?)
    """, (nome, ano, nota)
    )
    conexao.commit()
    conexao.close()
    return True  # Inserção bem-sucedida
    
# 4 - Listagem de Dados
def obter_dados():
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM filmes ORDER BY id DESC")
    dados = cursor.fetchall()
    cursor.close()
    return dados

# 5 - Excluir Dados
def exclui_dados(id_filme):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute(
    """
        DELETE FROM filmes WHERE id = ?
    """, (id_filme,)
    )
    conexao.commit()
    conexao.close()