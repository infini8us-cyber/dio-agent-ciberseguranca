# Relatório: SQL Injection no login didático
Data da revisão: 28/10/2026. Escopo: somente examples/sql-injection/, laboratório local autorizado.

## 1. Contexto
SQLite em memória, dados fictícios, nenhuma porta aberta ou requisição de rede. Compara app_vulneravel.py e app.py. Objetivo: entender e validar a separação entre comandos SQL e valores.

## 2. Evidências
A função autenticar de app_vulneravel.py concatena login e senha na consulta. A mesma função em app.py usa placeholders e uma tupla de parâmetros.
[testes-sql.txt](evidencias/testes-sql.txt) contém a execução real de quatro testes. O teste da versão vulnerável demonstra autenticação indevida; o da corrigida recusa a mesma entrada no campo login.
A classificação da fraqueza é CWE-89. T1190 só se aplica se a exploração de uma aplicação exposta servir de acesso inicial; essa condição não está demonstrada pelo laboratório local.

## 3. Impacto
No exemplo, a quebra da autenticação permite uma resposta de login aceito sem a senha correta. Em produção, consequências potenciais para confidencialidade e integridade dependem dos dados e privilégios alcançados. Não foram demonstradas extração, alteração de registros ou indisponibilidade.

## 4. Probabilidade
A entrada de teste é reproduzível em condições locais controladas. A probabilidade de ataque externo no laboratório é baixa, pois não existe serviço exposto. Uma implantação real requer avaliação própria.

## 5. Severidade contextual
Impacto baixo sobre dados fictícios e probabilidade baixa de ataque externo resultam em risco local baixo na matriz didática. A facilidade de reprodução da falha é alta e não deve ser confundida com probabilidade de incidente externo. Uma aplicação real exposta pode ter risco maior; faltam dados para classificá-la. Não foi calculado CVSS.

## 6. Correção
app.py fornece os valores separadamente à consulta parametrizada. Isso impede que o conteúdo dos campos altere a estrutura SQL. Validação de entrada e menor privilégio são complementos.
Senha fictícia em texto puro foi mantida para isolar o conceito. Um login de produção exige hash próprio para senhas, controles de sessão, limitação de tentativas e tratamento de erros, entre outros requisitos.

## 7. Validação
Quatro testes executados e aprovados: login válido, senha incorreta, reprodução na vulnerável e recusa na corrigida. Veja a saída real. A revisão do mentor está registrada separadamente em [mentor-analise-sql.txt](evidencias/mentor-analise-sql.txt). A leitura do agente não executa nem substitui os testes.

## 8. Limitações
A suíte cobre uma entrada de injeção no campo login, não todas as formas de SQL Injection nem toda a autenticação. Não houve teste de servidor real, pentest externo ou auditoria completa de dependências. Os resultados não constituem garantia universal de segurança.

## Fontes
- https://cwe.mitre.org/data/definitions/89.html
- https://attack.mitre.org/techniques/T1190/
- https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
