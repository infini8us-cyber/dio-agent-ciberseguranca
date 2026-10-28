# 🤖 DIO Agent

> Seu mentor de Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos, Desafios e muito mais) e ajuda você a estudar com mais clareza, destravar desafios e entender qualquer conceito.

E você não precisa instalar nada complicado. Em **3 passos simples**, o seu mentor de IA estará pronto para usar.

---

## ✨ Antes de começar: dois conceitos rápidos

Para usar o DIO Agent, basta entender duas palavras. As duas estão no [Glossário completo](docs/glossary.md), mas aqui vai a versão rápida:

- 🧠 **Agente de IA:** um chatbot comum responde perguntas, como um buscador mais esperto. Um *agente* de IA vai além: ele lê, planeja e executa passos para te ajudar a alcançar um objetivo. É a diferença entre alguém que te explica o caminho e alguém que caminha junto com você. O DIO Agent é um agente desse tipo: um tutor particular que acompanha a sua evolução.

- 🖥️ **Harness:** é o programa onde a conversa com o agente acontece. Vale a comparação: o agente é o professor, e o harness é a sala de aula. O mesmo professor pode dar aula em salas diferentes. Por isso o DIO Agent funciona em qualquer harness: você escolhe a "sala" no Passo 1, e o seu mentor continua o mesmo.

Pronto. Com isso já dá para começar.

---

## 🎯 O que o DIO Agent faz por você

| Você precisa de... | O DIO Agent... |
|--------------------|----------------|
| Saber por onde começar | Monta um plano de estudos no seu ritmo |
| Destravar um desafio | Te guia até a solução, sem entregar a resposta pronta |
| Entender um conceito | Explica de forma simples, com analogias e exemplos |

Ele conhece os formatos da DIO: Bootcamps, Formações, Acelerações, Cursos, English4Tech, Desafios de Código, Desafios de Projeto, Desafios Criativos, Lives e Mentorias. Assim, as recomendações sempre apontam para algo que você já tem na plataforma.

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um Harness

O harness é o programa que dá vida ao agente. Recomendamos o **Google Antigravity**, que tem limites de uso mais generosos para quem está começando. Mas qualquer harness moderno funciona.

| Harness | Documentação oficial |
|---------|----------------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Claude Code | https://docs.claude.com/en/docs/claude-code |
| Codex | https://developers.openai.com/codex |
| OpenCode | https://opencode.ai/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |

Escolha um e siga o passo a passo da documentação oficial dele. Cada documentação já traz tudo certinho para o seu sistema, então a instalação é tranquila.

### 2️⃣ Configure o DIO Agent

Agora você vai baixar este repositório para o seu computador. Escolha a forma mais simples para você:

**Opção A: com Git** (se você já usa Git)

```bash
git clone https://github.com/infini8us-cyber/dio-agent-ciberseguranca.git
```

**Opção B: baixando o .zip** (se você não usa Git)

Na página do repositório no GitHub, clique no botão verde **Code** e depois em **Download ZIP**. Em seguida, extraia a pasta em um lugar fácil de encontrar.

Com o repositório baixado, abra a pasta `dio-agent` no harness que você instalou. Cada harness tem o seu jeito de abrir uma pasta de projeto, e a documentação dele mostra como fazer isso.

E é só isso! O harness lê automaticamente o arquivo `AGENTS.md` e o agente já sabe quem é: o seu mentor de estudos da DIO.

> 🔄 **Fique de olho nas atualizações.** Não importa se você usou o Git ou o .zip: o repositório do DIO Agent evolui com o tempo. De tempos em tempos, vale voltar aqui e pegar a versão mais recente. Quem usou Git pode rodar `git pull` (ou pedir pro próprio DIO Agent rodar); quem baixou o .zip pode baixar de novo. Assim o seu mentor está sempre com o melhor que a gente tem a oferecer.

### 3️⃣ Hands On!

Agora é só conversar. Você pode falar naturalmente, com as suas palavras. Mas, principalmente nas primeiras vezes, vale usar um modelo de prompt pronto: é só copiar e preencher os campos entre colchetes. Quanto mais contexto você dá, melhor o agente ajuda.

**🗺️ Plano de estudos**

```
Quero montar um plano de estudos (se possível, com materiais complementares).
- Meu objetivo: [ex: aprender mais sobre IA, ser dev back-end, concluir um bootcamp]
- Experiência ou carreira da DIO: [URL ou nome do bootcamp/formação, ou de uma carreira da DIO]
- Meu nível hoje: [iniciante, intermediário, avançado]
- Tempo disponível: [ex: 1 hora por dia, de segunda a sexta]
```

**🔓 Destravar desafio**

```
Estou travado em um Desafio de [Código, Projeto ou Criativo] da DIO.
- O que o desafio pede: [cole o enunciado ou descreva]
- Onde eu travei: [explique o ponto da dificuldade]
- Meu código atual: [cole aqui, se for Desafio de Código]
- Link do repositório base: [cole aqui, se for Desafio de Projeto]
Me ajuda a destravar sem dar a resposta pronta.
```

**💡 Explicar conceito**

```
Me explica o conceito de [ex: API, laço de repetição, herança].
- Meu nível: [nunca vi, já ouvi falar, quero aprofundar]
- Onde apareceu: [ex: no curso X de um bootcamp] (opcional)
```

Não precisa de comando especial nem de formato perfeito: o agente conduz a conversa a partir daí e pede mais detalhes se precisar.

---

## 🧩 As skills do agente

Uma **skill** é uma habilidade do agente, descrita em um guia passo a passo. Além das skills originais, este projeto acrescenta a análise de vulnerabilidades:

| Skill | Para que serve |
|-------|----------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma didática, com analogias e exemplos |
| [Análise de vulnerabilidade](skills/vulnerability-analysis/SKILL.md) | Analisa falhas de segurança, estima riscos e produz relatório padrão |

Você não precisa "chamar" uma skill. O agente percebe o que você precisa e usa a skill certa sozinho.

---

## 🛡️ Especialização em Cibersegurança

A especialização **Análise de Vulnerabilidade** ensina o estudante a
avaliar falhas de segurança (como SQL Injection) com rigor, priorizando
o aprendizado e o raciocínio — nunca a exploração pronta.

O **relatório padrão** foi escolhido como a melhoria central da
especialização. Ele torna a avaliação técnica transparente e revisável:

1. **Contexto** — ambiente, exposição e autorização. Sem essas três,
   nenhuma conclusão de risco pode ser confiável.
2. **Evidências** — o que foi observado, com dados fictícios e sem expor
   nada real.
3. **Impacto** — o que pode acontecer se a falha for explorada.
4. **Probabilidade** — quão provável é que a falha seja aproveitada.
5. **Severidade justificada** — classificação didática de risco que combina impacto e probabilidade
   para o caso específico (baixa, média, alta, crítica), não um valor
   genérico.
6. **Correção** — a correção recomendada, explicada e segura.
7. **Validação** — como confirmar que a correção resolveu o problema.
8. **Limitações** — o que o relatório não cobre ou não testou.

### Como rodar o exemplo de SQL Injection

O exemplo fica em `examples/sql-injection/` e contém:

- `app.py` — versão **corrigida** (consultas parametrizadas);
- `app_vulneravel.py` — versão **vulnerável**, intencionalmente frágil,
  apenas para estudo;
- `test_sql_injection.py` — testes automatizados.

```bash
cd examples/sql-injection
python -m unittest test_sql_injection -v
```

O `README.md` local detalha o que cada teste verifica e os resultados
observados nesta etapa.

### Como a especialização se integra

- **skill** (`skills/vulnerability-analysis/SKILL.md`): passo a passo do
  processo de análise e do relatório padrão;
- **conhecimento** (`agent/knowledge/security-basics.md`): conceitos
  fundamentais (vulnerabilidade, risco, exposição, SQL Injection,
  correções seguras);
- **persona** (`agent/persona.md`): inclui a seção "Especialização em
  Cibersegurança", com o hábito de perguntar ambiente, exposição e
  autorização antes de sugerir comandos;
- **AGENTS.md**: registra a skill no índice de skills, para que o agente
  a use a cada vez que o estudante precisar.

### Limitações

- O exemplo usa SQLite em memória e dados fictícios: nenhum dado real,
  nenhum servidor e nenhuma rede.
- A especialização é um **mentor de análise**, não um gerador de
  exploits. Em ambientes reais, valide sempre com análise profissional.

---

## 🗂️ Estrutura do repositório

```text
dio-agent/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── agent/
│   ├── persona.md
│   └── knowledge/
│       ├── dio-platform.md
│       ├── learning-experiences.md
│       └── security-basics.md
├── skills/
│   ├── README.md
│   ├── study-plan/
│   ├── unblock-challenge/
│   ├── explain-concept/
│   ├── web-search/
│   ├── portfolio-review/
│   └── vulnerability-analysis/
│       ├── SKILL.md
│       └── README.md
├── examples/sql-injection/
│   ├── app.py
│   ├── app_vulneravel.py
│   ├── test_sql_injection.py
│   └── README.md
└── docs/
    ├── glossary.md
    ├── youcom-mcp.md
    ├── ENTREGA.md
    ├── RELATORIO-SQL.md
    └── evidencias/
```
> 🔍 **Por que funciona em qualquer harness?** O coração do projeto é o arquivo `AGENTS.md`, um padrão aberto que harnesses modernos sabem ler. O `CLAUDE.md` apenas aponta para ele, então você pode usar o harness que preferir.

---

## 📖 Glossário rápido

Termos como *agente*, *harness*, *skill* e *prompt* estão explicados com analogias simples no **[Glossário completo](docs/glossary.md)**. Se algum termo soar estranho, comece por lá.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você desde o início dos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀
## Entrega e evidências da especialização

Autoria da adaptação: Antônio Carlos Dias Madeira. Base: [DIO Agent](https://github.com/digitalinnovationone/dio-agent). Adaptação realizada com apoio de IA, revisada com testes locais; nenhum modelo foi treinado.

No Windows, abra um terminal PowerShell na raiz deste projeto e execute `hermes`. Se o comando não estiver no PATH, use `& "$env:LOCALAPPDATA\hermes\bin\hermes.exe"`. Python 3.10+ é suficiente para o exemplo, que usa apenas a biblioteca padrão.

A melhoria escolhida é o relatório padronizado de análise contextual. Consulte [o relatório SQL](docs/RELATORIO-SQL.md), [a validação dos testes](docs/evidencias/testes-sql.txt), [a conversa real do mentor](docs/evidencias/mentor-contexto.txt) e [a conferência da entrega](docs/ENTREGA.md). A resposta de IA é evidência de comportamento observado, não certificação de segurança.

O exemplo usa senha fictícia em texto puro para isolar SQL Injection. A parametrização mitiga a injeção demonstrada; não torna o login um sistema pronto para produção. A classificação de risco é didática e não é CVSS.
### Invocação reproduzível da skill

No Hermes, envie: “Use a skill skills/vulnerability-analysis/SKILL.md deste projeto. Tenho um servidor Ubuntu e quero analisar vulnerabilidades. Por onde começo?”

Na execução registrada, o mentor pediu contexto sem fornecer comandos. A seleção automática da skill falhou nos testes anteriores; não se assume aderência perfeita do modelo. Veja o histórico de validação em docs/ENTREGA.md. As três perguntas da resposta explícita também mostram que a regra de uma pergunta por vez não foi inteiramente seguida.