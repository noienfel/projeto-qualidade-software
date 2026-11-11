# Atividade 4 — Testes Automatizados do LocalEats

**Unidade Curricular:** Qualidade de Software  
**Projeto:** LocalEats — <https://local-eats-unisenac.vercel.app/>  
**Integrante:** Rafael — turma da manhã  
**Modalidade:** Individual  
**PBL:** 4

---

## 1. Visão geral da entrega

A entrega é composta por duas partes obrigatórias:

| Parte | Conteúdo | Arquivo |
|---|---|---|
| 1 | Regra de negócio `pedido_atingiu_valor_minimo` e testes unitários com pytest | `src/regras_localeats.py`, `tests/test_regras_localeats.py` |
| 2 | Teste funcional do filtro por categoria com Playwright | `tests/test_localeats.py` |

O relatório completo da execução está em [`relatorio-pytest.txt`](relatorio-pytest.txt).

---

## 2. Parte 1 — Regra unitária e TDD

### 2.1 Regra escolhida

**Regra 1 — verificar valor mínimo do pedido**

```python
pedido_atingiu_valor_minimo(valor_pedido)
```

| Condição | Resultado |
|---|---|
| `valor_pedido >= 30` | `True` |
| `valor_pedido < 30` | `False` |
| `valor_pedido < 0` | `ValueError` |

Implementação em `src/regras_localeats.py`:

```python
def pedido_atingiu_valor_minimo(valor_pedido: float) -> bool:
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")
    return valor_pedido >= 30
```

A função recebeu tipagem, docstring e uma validação explícita para valores negativos.

### 2.2 TDD de Rafael

**Regra escolhida:** Regra 1 — verificar valor mínimo do pedido (`pedido_atingiu_valor_minimo`).

**Primeiro teste escrito:** `test_pedido_com_valor_acima_do_minimo_retorna_true`, verificando que um pedido de R$ 50,00 retorna `True`.

**Por que o teste falhou inicialmente:** a primeira execução terminou com `ModuleNotFoundError: No module named 'src.regras_localeats'`. O teste descrevia o comportamento esperado, mas a função ainda não existia, o que caracteriza a etapa Red do ciclo.

**Implementação mínima realizada:** foi criada a função com o menor código capaz de atender ao teste:

```python
def pedido_atingiu_valor_minimo(valor_pedido):
    return valor_pedido >= 30
```

Com isso, três testes passaram. O teste do valor negativo continuou falhando com `DID NOT RAISE ValueError`.

**Segundo teste escrito:** `test_pedido_com_valor_negativo_gera_value_error`, usando `pytest.raises(ValueError)` para verificar a rejeição de valores negativos.

**Melhoria ou refatoração realizada:** foi adicionada a validação `if valor_pedido < 0: raise ValueError(...)`, além de tipagem, docstring e nomes de testes descritivos. Depois disso, os quatro testes unitários passaram.

> Observação de transparência: os quatro testes foram escritos no mesmo arquivo antes da primeira execução. A execução ocorreu em duas rodadas — primeiro a falha de importação, depois a falha da exceção — e a implementação foi ajustada em cada rodada, como registrado acima.

### 2.3 Testes unitários

| ID | Teste | Verifica |
|---|---|---|
| TU01 | `test_pedido_com_valor_acima_do_minimo_retorna_true` | Pedido de R$ 50,00 retorna `True` |
| TU02 | `test_pedido_no_limite_minimo_retorna_true` | Pedido de exatamente R$ 30,00 retorna `True` (limite) |
| TU03 | `test_pedido_abaixo_do_minimo_retorna_false` | Pedido de R$ 20,00 retorna `False` |
| TU04 | `test_pedido_com_valor_negativo_gera_value_error` | Valor negativo gera `ValueError` com `pytest.raises` |

Os testes são independentes entre si e não compartilham estado.

---

## 3. Parte 2 — Teste funcional com Playwright

### 3.1 Fluxo automatizado

**Fluxo escolhido:** criar uma conta e verificar o filtro de restaurantes por categoria.

1. Acessar a tela de login do LocalEats.
2. Acionar “Criar Conta” e preencher nome, e-mail e senha com dados de teste gerados em tempo de execução.
3. Enviar o cadastro e confirmar o redirecionamento para a página inicial.
4. Aguardar a listagem inicial de restaurantes.
5. Clicar no filtro “Italiana”.
6. Confirmar que o filtro está ativo e que todos os restaurantes exibidos pertencem à categoria Italiana.

O e-mail é único por execução (`uuid4`), evitando conflito com cadastros anteriores.

### 3.2 Elementos reais utilizados

Todos os seletores foram obtidos pela exploração da aplicação real:

| Elemento | Locator |
|---|---|
| Botão de cadastro | `get_by_role("button", name="Criar Conta")` |
| Nome | `#regName` |
| E-mail | `#regEmail` |
| Senha | `#regPassword` |
| Envio do cadastro | `#registerForm button[type="submit"]` |
| Filtro de categoria | `get_by_role("button", name="Italiana", exact=True)` |
| Filtro ativo | `.filter-btn.active` |
| Cartões de restaurante | `.rest-card` |

### 3.3 Assertions

O teste possui mais de duas assertions:

1. `expect(page).to_have_url(...)` — confirma o redirecionamento para `index.html` após o cadastro.
2. `expect(page.locator(".rest-card").first).to_be_visible()` — confirma que a listagem inicial foi renderizada.
3. `expect(page.locator(".filter-btn.active")).to_have_text("Italiana")` — confirma que o filtro clicado ficou ativo.
4. `assert len(textos) > 0` — confirma que o filtro retornou pelo menos um restaurante.
5. `assert all("Italiana" in texto for texto in textos)` — confirma que todos os restaurantes exibidos são da categoria Italiana.

### 3.4 Esperas e falha encontrada durante o desenvolvimento

Não é utilizado `time.sleep`. As esperas são baseadas em condições observáveis:

- `expect(...)` com timeout, que repete a verificação até a condição ser atendida;
- `page.wait_for_function(...)`, que aguarda a lista estar preenchida e somente com restaurantes italianos.

**Falha encontrada e corrigida:** a primeira versão do teste lia a lista logo após o clique e falhava, pois ainda encontrava o “Restaurante Sabor 1” (Japonesa). A investigação com um script de diagnóstico mostrou que o filtro é assíncrono: imediatamente após o clique a lista fica vazia e, cerca de um segundo depois, é re-renderizada apenas com as italianas. A correção foi substituir a leitura imediata por uma espera baseada na condição real do filtro. O teste passou a ser estável em execuções consecutivas.

---

## 4. Identificação das responsabilidades

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
|---|---|---|---|---|
| TU01 | Rafael | Unitário | Pedido acima do valor mínimo retorna `True` | `tests/test_regras_localeats.py::test_pedido_com_valor_acima_do_minimo_retorna_true` |
| TU02 | Rafael | Unitário | Pedido no limite de R$ 30,00 retorna `True` | `tests/test_regras_localeats.py::test_pedido_no_limite_minimo_retorna_true` |
| TU03 | Rafael | Unitário | Pedido abaixo do valor mínimo retorna `False` | `tests/test_regras_localeats.py::test_pedido_abaixo_do_minimo_retorna_false` |
| TU04 | Rafael | Unitário | Valor negativo gera `ValueError` | `tests/test_regras_localeats.py::test_pedido_com_valor_negativo_gera_value_error` |
| TF01 | Rafael | Funcional | Cadastro e filtro de restaurantes por categoria Italiana | `tests/test_localeats.py::test_filtrar_restaurantes_por_categoria_italiana` |

No relatório do pytest, o teste funcional aparece como `test_filtrar_restaurantes_por_categoria_italiana[chromium]` porque o pytest-playwright executa o teste uma vez por navegador configurado.

---

## 5. Explicação individual do teste TF01

O teste funcional TF01 cobre o fluxo de cadastro seguido do filtro por categoria. A escolha desse fluxo se deve ao fato de ele combinar duas interações reais da interface — criação de conta e filtragem — e produzir um resultado observável e verificável: a lista de restaurantes exibida.

O teste começa criando uma conta com e-mail único, o que garante independência entre execuções e evita depender de uma conta fixa que poderia já existir. Em seguida, aguarda a listagem inicial antes de clicar no filtro. Essa espera é importante porque o clique antes da renderização inicial não é processado pela página e o filtro permanece em “Todos” — foi exatamente esse comportamento que a primeira versão do teste revelou.

Depois do clique, o teste verifica duas coisas: que o botão “Italiana” está marcado como filtro ativo e que todos os cartões exibidos contêm a categoria Italiana. A verificação de todos os cartões, e não apenas do primeiro, é o que dá força ao teste: um filtro que apenas reordena a lista passaria se fosse verificado somente o primeiro item. Como a atualização da lista é assíncrona, a espera é feita por condição (`wait_for_function`), sem pausas fixas, o que torna o teste mais rápido e menos sujeito a falhas por tempo.

---

## 6. Relatório da execução

Execução gerada com o comando do escopo, dentro da pasta da atividade:

```powershell
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

Resumo do relatório:

| Item | Resultado |
|---|---|
| Testes coletados | 5 |
| Aprovados | 5 |
| Reprovados | 0 |
| Tempo | 2,56 s |
| Python | 3.12.10 |
| pytest | 9.2.0 |
| Playwright | 1.65.0 |
| pytest-playwright | 0.10.0 |
| Navegador | Chromium |

O relatório apresenta um aviso (`PytestRemovedIn10Warning`) originado da fixture `base_url` do plugin pytest-playwright. O aviso não interfere no resultado dos testes e não é gerado pelo código da atividade.

---

## 7. Como executar

```powershell
# Na pasta PBL4
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m playwright install chromium
.\.venv\Scripts\python.exe -m pytest -v
```

---

## 8. Diferenciais implementados

Itens opcionais do escopo que foram atendidos:

- terceiro e quarto testes unitários para casos de borda (limite de R$ 30,00 e valor negativo);
- uso de `pytest.raises` para verificar a exceção;
- registro de uma falha real encontrada e corrigida no teste funcional (filtro assíncrono).
