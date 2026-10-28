"""test_sql_injection.py — testes automatizados do exemplo de SQL Injection.

Compara a versão corrigida (app.py, consulta parametrizada) com a versão
vulnerável (app_vulneravel.py, concatenação).

Todos os dados são fictícios. O banco é SQLite em memória: sem servidor,
sem dados reais, sem persistência em disco. O objetivo é ver como a
frágil aceita uma injeção e como a segura rejeita.

Uso:
    python -m unittest test_sql_injection -v
"""

import unittest
import sqlite3

from app import autenticar as autenticar_correta
from app_vulneravel import autenticar as autenticar_vulneravel


def criar_banco():
    """Banco SQLite em memória com um único usuário fictício."""
    conexao = sqlite3.connect(":memory:")
    conexao.execute(
        "CREATE TABLE usuario ("
        " login TEXT PRIMARY KEY,"
        " senha TEXT NOT NULL"
        ")"
    )
    conexao.execute(
        "INSERT INTO usuario (login, senha) VALUES (?, ?)",
        ("alice", "senha-secreta-ficticia"),
    )
    conexao.commit()
    return conexao


class TesteSQLInjection(unittest.TestCase):
    def setUp(self):
        self.conexao = criar_banco()
        self.login_valido = "alice"
        self.senha_valida = "senha-secreta-ficticia"
        # Caracteres comuns em uma tentativa de injeção de SQL.
        self.entrada_injecao = "' OR '1'='1' --"

    def tearDown(self):
        self.conexao.close()

    def test_login_valido_aceito(self):
        self.assertTrue(
            autenticar_correta(self.conexao, self.login_valido, self.senha_valida)
        )

    def test_senha_incorreta_recusada(self):
        self.assertFalse(
            autenticar_correta(self.conexao, self.login_valido, "senha-errada")
        )

    def test_injetar_sql_pela_vulneravel(self):
        # A versão frágil interpreta a entrada como SQL e autentica. Esse é o risco.
        self.assertTrue(autenticar_vulneravel(self.conexao, self.entrada_injecao, "qualquer"))

    def test_injetar_sql_pela_corrigida(self):
        # A versão segura trata a entrada como dado: a injeção não
        # altera a intenção da query, e o login não existe.
        self.assertFalse(
            autenticar_correta(self.conexao, self.entrada_injecao, self.senha_valida)
        )


if __name__ == "__main__":
    unittest.main()
