# Conferência da entrega — DIO Agent Cibersegurança
Autor da adaptação: Antônio Carlos Dias Madeira.
Base original: https://github.com/digitalinnovationone/dio-agent
Data: 28/10/2026.

## Requisitos
- Skill com frontmatter name e description: skills/vulnerability-analysis/SKILL.md.
- Documentação humana: skills/vulnerability-analysis/README.md.
- Conhecimento: agent/knowledge/security-basics.md, incluindo tríade, risco e boas práticas.
- Integração: agent/persona.md e AGENTS.md.
- Exemplo: examples/sql-injection/app_vulneravel.py e app.py.
- Validação: quatro testes aprovados, saída real em evidencias/testes-sql.txt.
- Melhoria: relatório padrão de oito partes em RELATORIO-SQL.md.
- Evidências de conversa: evidencias/mentor-contexto.txt e mentor-analise-sql.txt.
- README principal explica contribuição, execução e limitações.

## Avaliação comportamental real
O teste sem indicação explícita da skill não cumpriu o critério: o modelo antecipou comandos/ferramentas. As tentativas estão em mentor-contexto-inicial.txt e mentor-contexto-automatico.txt.
Após reforço das instruções e invocação explícita, o mentor leu a skill e a base e pediu contexto sem oferecer comandos. Fez três perguntas em vez de uma, uma limitação de aderência ao roteiro.
Este resultado demonstra o comportamento observado nessa execução, não confiabilidade absoluta ou conclusão de todas as etapas de uma conversa.

Prompt reproduzível:
> Use a skill skills/vulnerability-analysis/SKILL.md deste projeto. Tenho um servidor Ubuntu e quero analisar vulnerabilidades. Por onde começo?

Para testar as etapas seguintes, informe ambiente e peça ao agente que continue; ele deve levantar exposição e permissão para testes antes de comandos. Não confunda acesso root com autorização do responsável.

## Publicação e submissão
Nome sugerido: dio-agent-ciberseguranca.
Publicar em repositório público na conta do estudante, preservando atribuição ao projeto base. Enviar a URL principal do repositório à DIO.
A publicação depende de autenticação no GitHub e a submissão depende da sessão da DIO. Este documento não afirma que publicação, submissão ou aulas assistidas foram concluídas.

Descrição para entrega:
Especialização do DIO Agent em análise defensiva de vulnerabilidades, com conhecimento de segurança, persona e skill integradas. Inclui laboratório local de SQL Injection com correção parametrizada, testes automatizados e relatório padronizado. Documenta evidências reais e limitações de aderência do modelo.

## O que não publicar
Credenciais, .env, ambientes virtuais, __pycache__, configurações locais do Hermes e o auxiliar temporário fix_readme.py.
