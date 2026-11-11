# Atividade 1 — Fundamentos e Características da Qualidade no LocalEats

**Unidade Curricular:** Qualidade de Software  
**Projeto:** LocalEats — <https://local-eats-unisenac.vercel.app/>  
**Integrante:** Rafael Devantier Neuenfeldt — turma da manhã  
**Modalidade:** Individual  
**PBL:** 1

---

## Tarefa 1 — Fundamentos da qualidade

### Necessidades explícitas e implícitas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | O usuário deve conseguir favoritar e desfavoritar restaurantes, mantendo uma lista de preferidos. | Cliente / usuário final | O usuário precisa refazer a busca sempre que quiser acessar um restaurante conhecido, perdendo conveniência e podendo abandonar a plataforma. |
| Explícita | O usuário deve conseguir pesquisar restaurantes por especialidade ou localização. | Cliente / usuário final | O usuário não encontra os restaurantes que atendem ao seu gosto ou à sua região, e a busca deixa de cumprir seu propósito principal. |
| Implícita | Os favoritos devem permanecer salvos e consistentes entre recarregamentos, páginas e novas sessões do mesmo usuário. | Cliente / usuário final e negócio | O usuário interpreta que o sistema perdeu seus dados, perde a confiança no recurso e deixa de utilizá-lo. |
| Implícita | A interface deve informar de forma clara o resultado das ações e das buscas sem resultados, sem deixar o usuário em dúvida sobre o que aconteceu. | Cliente / usuário final e restaurantes parceiros | O usuário não sabe se a ação funcionou ou se realmente não existem opções, aumentando erros, reclamações e abandono. |

### Um sistema com todas as funcionalidades explícitas ainda pode ter baixa qualidade?

Sim. Uma funcionalidade explícita pode existir e ainda assim falhar em necessidades implícitas. No LocalEats, o favorito aparece em “Meus Favoritos”, mas o botão da página do restaurante exibe “Favoritar” em uma nova sessão, gerando informação contraditória. Sem persistência e consistência, o usuário perde a confiança e a qualidade percebida diminui.

---

## Tarefa 2 — Exploração da aplicação

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| Rafael | Favoritar e desfavoritar restaurantes | Entrei com uma conta de teste, favoritei o “Restaurante Sabor 0”, abri “Meus Favoritos”, recarreguei a página, iniciei uma nova sessão e tentei acessar a página do restaurante sem login. | O favorito apareceu em “Meus Favoritos” e permaneceu após a recarga e após uma nova sessão. Porém, na página do restaurante aberta em nova sessão, o botão exibiu “Favoritar” enquanto o restaurante já estava na lista de favoritos. Sem login, o acesso à página do restaurante foi redirecionado para a tela de login. | [Favorito salvo](evidencias/rafael-favorito-salvo.png), [lista de favoritos](evidencias/rafael-favorito-lista.png), [nova sessão](evidencias/rafael-favorito-nova-sessao.png), [divergência do botão](evidencias/rafael-favorito-divergencia.png), [acesso sem login](evidencias/rafael-favoritar-sem-login.png) |

**Observações da exploração:**

- A conta utilizada foi criada exclusivamente para a atividade, com e-mail de teste e senha fictícia; nenhum dado pessoal real foi utilizado.
- O comportamento observado foi registrado como ocorreu, sem afirmar como o código ou o banco de dados foram implementados.
- A evidência “nova sessão” mostra o restaurante na lista de favoritos. A evidência “divergência do botão” mostra a mesma conta, já autenticada, com o botão “Favoritar” na página do restaurante.

---

## Tarefa 3 — Requisitos e características de qualidade

| Integrante | Requisito de qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| Rafael | O estado de favorito de um restaurante deve permanecer salvo e ser o mesmo na página do restaurante, em “Meus Favoritos” e após recarregar a página ou iniciar uma nova sessão. | Confiabilidade (ISO/IEC 25010) | A funcionalidade só entrega valor se o usuário puder confiar que o favorito continua salvo. A exploração mostrou persistência na lista, mas divergência no botão da página do restaurante em nova sessão, o que compromete a confiança nos dados e a coerência da interface. | Executar ciclos de favoritar, recarregar a página, abrir uma nova sessão e comparar o estado do botão com a lista de favoritos. Registrar quantas vezes há divergência e calcular a taxa de consistência (ciclos sem divergência ÷ total de ciclos). Verificar também se o mesmo restaurante aparece duplicado na lista. |

---

## Evidências

As capturas estão em [`evidencias/`](evidencias/) e foram geradas durante a exploração da aplicação em novembro de 2026.
