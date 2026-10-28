# Fundamentos de segurança
Esta base orienta o mentor; leia-a ao usar a skill vulnerability-analysis.

## Conceitos
- Vulnerabilidade: fraqueza que pode permitir comprometimento de um ativo.
- Ameaça: evento ou agente com potencial de causar dano explorando uma fraqueza.
- Risco: combinação da probabilidade do evento e de suas consequências.
- Exposição: alcance do ponto de entrada e condições necessárias para acessá-lo.
- Confidencialidade: acesso à informação somente por quem está autorizado.
- Integridade: proteção contra alterações indevidas de dados e sistemas.
- Disponibilidade: acesso aos serviços e dados quando necessário.
- Autenticação verifica identidade; autorização de acesso define permissões. Autorização para testar é a permissão do responsável pelo sistema, com escopo e limites definidos.

## Avaliação contextual
Classifique impacto e probabilidade como baixos, médios ou altos e explique as evidências.
Matriz didática (linhas: impacto; colunas: probabilidade baixa, média, alta):
| Impacto | Baixa | Média | Alta |
|---|---|---|---|
| Baixo | Baixa | Baixa | Média |
| Médio | Baixa | Média | Alta |
| Alto | Média | Alta | Crítica |

Esta é uma classificação contextual de risco, não um cálculo CVSS. Se faltarem informações, registre avaliação provisória ou indeterminada. A gravidade potencial da falha não equivale ao risco real de um laboratório local com dados fictícios.

## SQL Injection e correção
Entradas concatenadas em comandos SQL podem mudar a estrutura da consulta. No SQLite, use:
```python
cursor = conexao.execute(
    "SELECT 1 FROM usuario WHERE login = ? AND senha = ?",
    (login, senha),
)
```
Os placeholders separam instrução e valores. A parametrização de valores não torna nomes dinâmicos de tabelas ou colunas seguros; nesses casos use escolhas permitidas previamente definidas.
SQL Injection corresponde à CWE-89. MITRE ATT&CK T1190 descreve exploração de aplicação exposta para acesso inicial; só associe quando o cenário sustentar isso. O exemplo local não comprova uma intrusão real.

## Boas práticas
- Menor privilégio; atualização de dependências e do sistema.
- Validação de entrada no servidor como complemento, sem substituir parâmetros.
- Hash de senha com algoritmo próprio para senhas; nunca texto puro em produção.
- Segredos fora do Git, mensagens de erro sem detalhes internos e logs sem senhas.
- Backups com restauração testada e revisão antes de produção.

O exemplo SQL deste projeto mantém uma senha fictícia em texto puro apenas para isolar a demonstração da injeção. Não é um sistema de autenticação pronto para produção.

## Referências
- https://cwe.mitre.org/data/definitions/89.html
- https://attack.mitre.org/techniques/T1190/
- https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
