"""app_vulneravel.py — versão INTENCIONALMENTE frágil, só para estudo.

Esta versão é escrita para que você veja a falha em ação: o valor do
usuário é concatenado diretamente na string da query SQL.

Como funciona a injeção com o login:
    ' OR '1'='1' --

A query resultante (simplificada) é:
    SELECT 1 FROM usuario WHERE login = '' OR '1'='1' --' AND senha = '...'

O -- transforma o resto da linha em comentário, e '1'='1' deixa a
condição sempre verdadeira. Em um sistema real, isso pode autenticar uma
conta sem a senha correta.

Não use isso em produção. Use app.py (versão corrigida) para ver a
solução com placeholders.
"""

import sqlite3
import sys

USUARIO_TESTE = ("alice", "senha-secreta-ficticia")


def criar_banco():
    conexao = sqlite3.connect(":memory:")
    _criar_tabela(conexao)
    _inserir_usuario(conexao, *USUARIO_TESTE)
    return conexao


def _criar_tabela(conexao):
    conexao.execute(
        "CREATE TABLE IF NOT EXISTS usuario ("
        " login TEXT PRIMARY KEY,"
        " senha TEXT NOT NULL"
        ")"
    )
    conexao.commit()


def _inserir_usuario(conexao, login, senha):
    conexao.execute(
        "INSERT INTO usuario (login, senha) VALUES (?, ?)",
        (login, senha),
    )
    conexao.commit()


def autenticar(conexao, login, senha):
    """VERSÃO FRÁGIL: a entrada é injetada na query por concatenação."""
    query = (
        "SELECT 1 FROM usuario "
        "WHERE login = '" + login + "' "
        "AND senha = '" + senha + "'"
    )
    cursor = conexao.execute(query)
    return cursor.fetchone() is not None


def main(argv):
    conexao = criar_banco()
    if len(argv) < 3:
        print("Uso: python app_vulneravel.py autenticar <login> <senha>")
        print("   ou: python app_vulneravel.py login <login>")
        return 2

    acao = argv[1]

    if acao == "login":
        if len(argv) != 3:
            print("Uso: python app_vulneravel.py login <login>")
            return 2
        aceito = autenticar(conexao, argv[2], "")
        print("Login aceito" if aceito else "Login recusado")

    elif acao == "autenticar":
        if len(argv) != 4:
            print("Uso: python app_vulneravel.py autenticar <login> <senha>")
            return 2
        aceito = autenticar(conexao, argv[2], argv[3])
        print("Login aceito" if aceito else "Login recusado")

    else:
        print("Ação desconhecida: " + acao)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
