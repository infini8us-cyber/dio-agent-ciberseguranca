# Exemplo didático: SQL Injection

Estudo de uma vulnerabilidade de segurança **só com dados fictícios**:
sem servidor exposto, sem banco real, sem acesso à rede e sem dados
personais. O objetivo é entender como uma consulta SQL montada com
concatenação de strings abre porta pra **injeção**, e como a **consulta
parametrizada** resolve — ensinando o raciocínio, não entregando exploits.

## Estrutura

- `app.py` — **versão corrigida**: consulta com placeholders (`?`), nunca
  concatena entrada na query.
- `app_vulneravel.py` — **versão vulnerável**, intencionalmente frágil
  (concatenação de strings), **apenas para estudo didático**.
- `test_sql_injection.py` — **testes automatizados** que comparam as duas
  versões.

## Como rodar

1. Entre na pasta do exemplo:

   ```bash
   cd examples/sql-injection
   ```

2. Execute os testes:

   ```bash
   python -m unittest test_sql_injection -v
   ```

3. Para comparar o comportamento ao vivo (ambos usam SQLite em memória):

   ```bash
   # Versão corrigida
   python app.py autenticar alice "senha-secreta-ficticia"

   # Versão vulnerável (apenas para ver o comportamento da frágil)
   python app_vulneravel.py autenticar alice "' OR '1'='1' --"
   ```

   O banco é criado em memória em cada execução; não há servidor e nenhum
   dado sai do exemplo.

## Roteiro de estudo

1. Abra `app_vulneravel.py` e veja como o valor do usuário é jogado direto
   na string da query.
2. Execute a injeção com o login `' OR '1'='1' --`. A versão frágil
   autentica (o `--` desliga o resto da query); a versão corrigida recusa.
3. Abra `app.py` e perceba que a entrada é enviada como **parâmetro**,
   não como parte da query: o SQLite trata a entrada como dados, não como
   comando.

## Resultados esperados dos testes

```
test_injetar_sql_pela_corrigida ... ok
test_injetar_sql_pela_vulneravel ... ok
test_login_valido_aceito ... ok
test_senha_incorreta_recusada ... ok

Ran 4 tests
OK
```

## Limitações

- O banco é em memória: não há persistência, nenhum usuário de verdade e
  nenhum dado real.
- Esta é uma demonstração de **como a falha se comporta**, não um roteiro
  de ataque. Em produção, valide sempre com análise real de segurança.
- Os resultados abaixo são o que o código realmente fez na execução
  registrada nesta etapa.

## Evidências e limites
Consulte [a saída real dos testes](../../docs/evidencias/testes-sql.txt) e [o relatório](../../docs/RELATORIO-SQL.md). A seção acima contém resultados esperados; somente o arquivo de evidências documenta a nova execução. Senhas fictícias em texto puro servem exclusivamente à demonstração e não devem ser adotadas em produção.
