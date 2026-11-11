# Atividade 3 — Estratégia e Projeto de Testes do LocalEats

**Unidade Curricular:** Qualidade de Software  
**Projeto:** LocalEats — <https://local-eats-unisenac.vercel.app/>  
**Integrante:** Rafael Devantier Neuenfeldt — turma da manhã  
**Modalidade:** Individual  
**PBL:** 3

---

## Tarefa 1 — Planejamento dos testes

### 1.1 Objetivo dos testes

Verificar se o estado de favorito de um restaurante é mantido corretamente entre a página do restaurante, a tela “Meus Favoritos”, uma recarga da página e uma nova sessão do mesmo usuário, garantindo que o usuário não perca nem veja informações contraditórias sobre seus favoritos.

### 1.2 Escopo

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| Rafael | Favoritar e desfavoritar restaurantes | A ação de favoritar e desfavoritar, o reflexo em “Meus Favoritos”, a persistência após recarregar a página e iniciar uma nova sessão e a consistência do estado exibido entre as telas. |

| Funcionalidade não incluída | Justificativa |
|---|---|
| Fazer pedido | Envolve carrinho, valores, disponibilidade e checkout. Não é necessário para avaliar favoritos e ampliaria o escopo sem contribuir para os riscos escolhidos. |

### 1.3 Abordagem

| Item | Decisão adotada | Justificativa |
|---|---|---|
| Nível de teste | Sistema | O fluxo será avaliado pela interface, do login até a consulta em “Meus Favoritos”, incluindo a troca de sessão. |
| Tipo de teste | Funcional | O objetivo é verificar o comportamento da funcionalidade de favoritos e suas regras de persistência e consistência. |
| Perspectiva | Caixa-preta | Serão consideradas as entradas e os resultados observáveis na interface, sem acesso ao código ou ao banco de dados. |
| Técnica de teste | Transição de estados | O favorito possui estados bem definidos (não favoritado e favoritado) e transições que podem ocorrer por ação do usuário, recarga ou nova sessão. |

### 1.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | Aplicação disponível em <https://local-eats-unisenac.vercel.app/>; navegador Chromium (execução automatizada) e Chrome/Firefox (verificação manual); resolução desktop de 1280 × 800 e simulação mobile de 390 × 844; conexão com internet; conta de teste autenticada; pelo menos um restaurante disponível; lista de favoritos inicialmente vazia. |
| Responsáveis pelo planejamento | Rafael. |
| Responsáveis pela especificação dos casos | Rafael. |
| Responsáveis pela futura execução | Rafael. |

### 1.5 Critérios

| Critério | Definição adotada |
|---|---|
| Entrada | Aplicação disponível, conta de teste autenticada, restaurante “Restaurante Sabor 0” (id 1) disponível e lista de favoritos vazia. |
| Saída | Os três casos planejados executados, resultados e evidências registrados e nenhuma divergência de estado em aberto. Caso haja falha, o defeito deve ser registrado com identificador e severidade. |
| Suspensão | Aplicação indisponível, login impossível, restaurante ausente ou falha generalizada no carregamento da lista de favoritos. |

---

## Tarefa 2 — Riscos e técnicas de teste

### 2.1 Análise dos riscos

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|---|---|---|---|
| R01 | Rafael | Favoritar e desfavoritar restaurantes | O favorito não persistir após recarregar a página ou iniciar uma nova sessão. | O usuário perde a preferência salva, precisa refazer a busca e passa a desconfiar da capacidade do sistema de guardar seus dados. | Média | Alto | Alta | O valor da funcionalidade depende de o favorito continuar disponível. Uma falha de persistência afeta diretamente a confiança e a retenção do usuário. |
| R02 | Rafael | Favoritar e desfavoritar restaurantes | O estado do favorito divergir entre o botão da página do restaurante e a lista de “Meus Favoritos”. | O usuário vê informações contraditórias, pode favoritar novamente sem necessidade, achar que perdeu o item ou não saber se a ação foi concluída. | Média | Médio | Média | A exploração preliminar mostrou que, em uma nova sessão, o botão exibiu “Favoritar” enquanto o restaurante já estava na lista de favoritos. |

### 2.2 Aplicação da técnica

**Integrante responsável:** Rafael  
**Funcionalidade:** Favoritar e desfavoritar restaurantes  
**Risco relacionado:** R01 e R02  
**Técnica escolhida:** Transição de estados

**Por que a técnica foi escolhida?**

A funcionalidade de favoritos pode ser representada por estados e eventos bem definidos: um restaurante está favoritado ou não, e o usuário pode favoritar, desfavoritar, recarregar a página ou iniciar uma nova sessão. A transição de estados permite verificar tanto as ações permitidas quanto a persistência e a consistência entre telas, que são justamente os riscos identificados. Uma tabela de decisão ou particionamento de equivalência não representaria bem a passagem de estado entre sessões.

#### Estados identificados

| Estado | Descrição |
|---|---|
| S0 | Usuário autenticado e restaurante não favoritado. |
| S1 | Usuário autenticado e restaurante favoritado. |
| S2 | Nova sessão ou recarga da página para o mesmo usuário, com o favorito previamente salvo. |

#### Transições identificadas

| De | Evento | Para | Resultado esperado |
|---|---|---|---|
| S0 | Clicar em “Favoritar” | S1 | O botão muda para “Favoritado!” e o restaurante aparece em “Meus Favoritos”. |
| S1 | Clicar em “Desfavoritar” | S0 | O botão volta para “Favoritar” e o restaurante é removido da lista. |
| S1 | Recarregar a página | S2 | O favorito continua salvo e o botão continua indicando “Favoritado!”. |
| S2 | Iniciar nova sessão e fazer login | S2 | O restaurante continua em “Meus Favoritos” e o botão continua indicando “Favoritado!”. |
| S2 | Clicar em “Desfavoritar” | S0 | O restaurante é removido da lista e o estado volta a “Favoritar”. |

**Transições inválidas a observar:** sair de S0 e chegar a S2 sem uma ação de favoritar; ou estar em S2 com o restaurante na lista e o botão indicar “Favoritar”.

**Casos derivados:** CT01, CT02 e CT03.

---

## Tarefa 3 — Casos de teste e rastreabilidade

### 3.1 Especificação dos casos de teste

#### CT01: Favoritar restaurante autenticado e refletir em “Meus Favoritos”

**Integrante responsável:** Rafael  
**Funcionalidade:** Favoritar e desfavoritar restaurantes  
**Risco ou requisito relacionado:** R02 — estado divergente entre botão e lista  
**Técnica utilizada:** Transição de estados

**Pré-condição:**  
O usuário está autenticado, o “Restaurante Sabor 0” (id 1) está disponível e não está na lista de favoritos.

**Dados de entrada:**  
Restaurante: Restaurante Sabor 0 (id 1).  
Conta: conta de teste criada para a atividade.

**Passos:**  
1. Acessar a página do “Restaurante Sabor 0”.  
2. Verificar que o botão exibe “Favoritar”.  
3. Clicar no botão de favoritar.  
4. Acessar a opção “Meus Favoritos”.

**Resultado esperado:**  
O botão muda para “Favoritado!” e o “Restaurante Sabor 0” aparece uma única vez na lista de favoritos, com o mesmo estado exibido nas duas telas.

---

#### CT02: Desfavoritar restaurante e removê-lo de “Meus Favoritos”

**Integrante responsável:** Rafael  
**Funcionalidade:** Favoritar e desfavoritar restaurantes  
**Risco ou requisito relacionado:** R02 — estado divergente entre botão e lista  
**Técnica utilizada:** Transição de estados

**Pré-condição:**  
O usuário está autenticado e o “Restaurante Sabor 0” está previamente favoritado.

**Dados de entrada:**  
Restaurante: Restaurante Sabor 0 (id 1).  
Conta: a mesma conta de teste utilizada no CT01.

**Passos:**  
1. Acessar a página do “Restaurante Sabor 0”.  
2. Verificar que o botão exibe “Favoritado!”.  
3. Clicar no botão para desfavoritar.  
4. Acessar a opção “Meus Favoritos”.

**Resultado esperado:**  
O botão volta a exibir “Favoritar” e o “Restaurante Sabor 0” não aparece mais na lista de favoritos. A lista não deve conter duplicatas nem manter um estado antigo do restaurante.

---

#### CT03: Manter o favorito após recarregar a página e iniciar uma nova sessão

**Integrante responsável:** Rafael  
**Funcionalidade:** Favoritar e desfavoritar restaurantes  
**Risco ou requisito relacionado:** R01 — favorito não persiste entre sessões  
**Técnica utilizada:** Transição de estados

**Pré-condição:**  
O usuário está autenticado, o “Restaurante Sabor 0” está favoritado e existe a possibilidade de encerrar a sessão e entrar novamente.

**Dados de entrada:**  
Restaurante: Restaurante Sabor 0 (id 1).  
Conta: a mesma conta de teste dos casos anteriores.

**Passos:**  
1. Favoritar o “Restaurante Sabor 0”, caso ele ainda não esteja favoritado.  
2. Recarregar a página do restaurante e verificar o estado do botão.  
3. Encerrar a sessão ou abrir uma nova sessão do navegador.  
4. Entrar novamente com a mesma conta.  
5. Acessar “Meus Favoritos”.  
6. Abrir novamente a página do “Restaurante Sabor 0”.

**Resultado esperado:**  
O restaurante continua presente em “Meus Favoritos” após a recarga e após a nova sessão. O botão da página do restaurante exibe “Favoritado!” de forma consistente com a lista, sem duplicar o item.

---

### 3.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| Rafael | Favoritar e desfavoritar restaurantes | R01 — favorito não persiste entre sessões | Transição de estados | CT03 |
| Rafael | Favoritar e desfavoritar restaurantes | R02 — estado divergente entre botão e lista | Transição de estados | CT01, CT02 e CT03 |

**Conferência da rastreabilidade:** todos os riscos identificados possuem pelo menos um caso de teste. O CT03 cobre os dois riscos porque verifica simultaneamente a persistência e a consistência entre as telas.
