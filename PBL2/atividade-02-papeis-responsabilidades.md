# Atividade 2 — Organização da Qualidade no LocalEats

**Unidade Curricular:** Qualidade de Software  
**Projeto:** LocalEats — <https://local-eats-unisenac.vercel.app/>  
**Integrante:** Rafael Devantier Neuenfeldt — turma da manhã  
**Modalidade:** Individual  
**PBL:** 2

---

## Tarefa 1 — Diagnóstico da situação

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| Funcionalidades chegam aos usuários com defeitos, como a divergência entre o botão de favorito e a lista de favoritos. | Retrabalho, correções emergenciais e perda de confiança do usuário. O custo de corrigir aumenta depois da entrega. |
| Os critérios para considerar uma funcionalidade pronta não estão claros. | Cada integrante avalia “pronto” de forma diferente; uma entrega pode ser considerada concluída sem testes, revisão ou validação dos critérios de aceitação. |
| Defeitos são identificados, mas nem sempre são registrados ou acompanhados até a correção. | Falhas recorrentes, perda de histórico, correções esquecidas e dificuldade para priorizar o que realmente importa. |

### A qualidade deve ser responsabilidade exclusiva do profissional de QA?

Não. O QA planeja, especifica e verifica os testes, mas não constrói a qualidade sozinho. O Product Owner define valor e critérios de aceitação; o analista esclarece requisitos; o desenvolvedor previne defeitos com código e testes unitários; o líder técnico e o DevOps garantem revisão, integração e entrega segura. A qualidade é responsabilidade compartilhada, com papéis e critérios claros ao longo de todo o processo.

---

## Tarefa 2 — Papéis e competências

A análise é individual, mas os papéis abaixo representam funções organizacionais. Em uma equipe maior, cada papel poderia ser ocupado por uma pessoa diferente.

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| Rafael | Product Owner | Priorizar o backlog, definir valor e critérios de aceitação, decidir a prioridade das correções e aprovar a disponibilização da versão. | Visão de produto, histórias de usuário, métricas, análise de risco e noções de ISO/IEC 25010. | Comunicação, negociação, tomada de decisão, empatia com o usuário e pensamento crítico. |
| Rafael | Analista de Negócio | Levantar e refinar requisitos, documentar regras de negócio e critérios de aceitação, manter a rastreabilidade e apoiar a validação com o usuário. | Modelagem de processos, escrita de requisitos, critérios de aceitação, leitura de APIs e consultas SQL. | Escuta ativa, clareza, organização, colaboração e pensamento crítico. |
| Rafael | Desenvolvedor | Implementar funcionalidades, escrever testes unitários, participar de revisões de código, corrigir defeitos e manter a qualidade do código. | TypeScript/JavaScript ou Python, Git, testes automatizados, APIs, design de código, integração contínua e revisão de código. | Atenção a detalhes, responsabilidade, colaboração, aprendizado contínuo e abertura para feedback. |
| Rafael | QA / Analista de Qualidade | Planejar, especificar e executar testes, analisar riscos, registrar e acompanhar defeitos, validar critérios de aceitação e apoiar a automação. | Técnicas de teste, análise de risco, Playwright, pytest, BDD, testes de API, SQL e gestão de defeitos. | Ceticismo produtivo, comunicação, organização, empatia e capacidade de explicar evidências. |
| Rafael | DevOps | Manter o pipeline de integração e entrega, configurar ambientes, automatizar verificações, monitorar a aplicação e apoiar rollback. | Git, GitHub Actions, containers, cloud, logs, métricas, automação e segurança do pipeline. | Colaboração, prevenção de problemas, resposta a incidentes, documentação e responsabilidade. |
| Rafael | Líder Técnico | Tomar decisões técnicas, definir padrões, revisar código, apoiar a priorização, orientar a equipe e avaliar riscos técnicos. | Arquitetura, revisão de código, testes, segurança, desempenho, débito técnico e integração contínua. | Liderança, comunicação, mentoria, negociação, pensamento crítico e tomada de decisão. |

---

## Tarefa 3 — Matriz de responsabilidades (RACI)

**Legenda:** **R** = Responsável pela execução; **A** = Aprovador, responde pelo resultado final; **C** = Consultado antes da execução ou decisão; **I** = Informado sobre o resultado.

| Atividade de qualidade | Product Owner | Analista de Negócio | Desenvolvedor | QA | DevOps | Líder Técnico |
|---|---|---|---|---|---|---|
| Definir critérios de aceitação | **A** | **R** | C | C | I | C |
| Revisar requisitos | **A** | **R** | C | C | I | C |
| Implementar a funcionalidade | I | C | **R** | C | I | **A** |
| Revisar o código | I | I | **R** | C | I | **A** |
| Criar testes unitários | I | I | **R** | C | I | **A** |
| Planejar e executar testes do sistema | **A** | C | C | **R** | I | C |
| Registrar e acompanhar defeitos | I | I | C | **R** | I | **A** |
| Priorizar a correção dos defeitos | **A** | C | C | C | I | **R** |
| Aprovar a disponibilização da versão | **A** | I | I | **R** | **R** | **R** |

### Lacuna ou conflito encontrado

A atividade **“Aprovar a disponibilização da versão”** tem um único aprovador (Product Owner), mas três papéis responsáveis pela execução da aprovação: QA, DevOps e Líder Técnico. Sem um critério objetivo, cada área pode se considerar com poder de veto, ou a decisão pode ficar ambígua e atrasar a entrega. A proposta é usar um checklist de release com evidências de teste do QA, parecer técnico do Líder Técnico e confirmação de deploy e monitoramento do DevOps; o Product Owner toma a decisão final com base nesses pareceres.

---

## Práticas recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Definition of Done (DoD) acordada antes do desenvolvimento, incluindo critérios de aceitação, revisão de código e evidências de teste. | Critérios de pronto não claros e funcionalidades entregues com defeitos. | Product Owner, Analista de Negócio, Desenvolvedor, QA e Líder Técnico. |
| Registro e triagem de defeitos em uma ferramenta única (por exemplo, GitHub Issues), com responsável, severidade, prioridade e revisão semanal. | Defeitos identificados que não são registrados, acompanhados ou priorizados. | QA, Líder Técnico, Desenvolvedor e Product Owner. |
