# PBL4 — Testes Automatizados do LocalEats

**Integrante:** Rafael — turma da manhã

Entrega da Atividade 4, com a implementação de uma regra de negócio, testes unitários com pytest, aplicação simplificada de TDD e um teste funcional automatizado com Playwright.

## Entrega

- [Documento da atividade](atividade-04-testes-automatizados.md)
- [Relatório da execução](relatorio-pytest.txt)

## Estrutura

```text
PBL4/
├── atividade-04-testes-automatizados.md
├── relatorio-pytest.txt
├── requirements.txt
├── pytest.ini
├── src/
│   ├── __init__.py
│   └── regras_localeats.py
└── tests/
    ├── __init__.py
    ├── test_regras_localeats.py
    └── test_localeats.py
```

## Resumo

- **Regra unitária:** `pedido_atingiu_valor_minimo` (mínimo de R$ 30,00, com `ValueError` para valores negativos).
- **Testes unitários:** 4 testes, incluindo limite e exceção.
- **Teste funcional:** cadastro pela interface e filtro de restaurantes pela categoria “Italiana”, com 5 assertions e sem `time.sleep`.
- **Resultado:** 5 testes aprovados em 2,56 s.

## Como executar

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m playwright install chromium
.\.venv\Scripts\python.exe -m pytest -v
```
