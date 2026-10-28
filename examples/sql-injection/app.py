"""app.py — login corrigido, consulta parametrizada.

Estudo didático. Banco SQLite em memória, dado fictício, sem servidor.

Uso:
    python app.py autenticar <login> <senha>
    python app.py login <login>

NÃO expõe servidor, NÃO usa dados reais. Use apenas em ambiente local.
"""

import sqlite3
import sys

USUARIO_TESTE = ("alice", "senha-secreta-ficticia")


def criar_banco():
    """Cria um banco SQLite em memória e insere o usuário de teste."""
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
    """Autentica com placeholders, nunca com concatenação.

    Os valores são enviados como parâmetros separados. O SQLite garante
    que a entrada seja tratada como dados e não como parte da query.
    """
    cursor = conexao.execute(
        "SELECT 1 FROM usuario WHERE login = ? AND senha = ?",
        (login, senha),
    )
    return cursor.fetchone() is not None


def main(argv):
    conexao = criar_banco()
    if len(argv) < 3:
        print("Uso: python app.py autenticar <login> <senha>")
        print("   ou: python app.py login <login>")
        return 2

    acao = argv[1]

    if acao == "login":
        if len(argv) != 3:
            print("Uso: python app.py login <login>")
            return 2
        aceito = autenticar(conexao, argv[2], "")
        print("Login aceito" if aceito else "Login recusado")

    elif acao == "autenticar":
        if len(argv) != 4:
            print("Uso: python app.py autenticar <login> <senha>")
            return 2
        aceito = autenticar(conexao, argv[2], argv[3])
        print("Login aceito" if aceito else "Login recusado")

    else:
        print("Ação desconhecida: " + acao)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
