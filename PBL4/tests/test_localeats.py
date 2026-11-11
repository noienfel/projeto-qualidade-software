"""Teste funcional automatizado do LocalEats com Playwright."""

import re
from uuid import uuid4

from playwright.sync_api import Page, expect

BASE_URL = "https://local-eats-unisenac.vercel.app"
TIMEOUT = 30_000

# O filtro por categoria é assíncrono: ao clicar, a lista é limpa e
# re-renderizada alguns instantes depois. A espera abaixo aguarda a
# condição real (lista preenchida e somente com a categoria escolhida)
# em vez de usar pausas fixas.
AGUARDAR_FILTRO_APLICADO = """
() => {
  const cards = Array.from(document.querySelectorAll('.rest-card'));
  return cards.length > 0 && cards.every((card) => card.innerText.includes('Italiana'));
}
"""


# Responsável: Rafael
def test_filtrar_restaurantes_por_categoria_italiana(page: Page):
    """Cadastra um usuário de teste e verifica o filtro por categoria Italiana."""
    email = f"qa.pbl4.{uuid4().hex[:10]}@example.com"

    page.goto(f"{BASE_URL}/static/login.html", timeout=TIMEOUT)
    page.get_by_role("button", name="Criar Conta").click()
    page.locator("#regName").fill("Rafael QA")
    page.locator("#regEmail").fill(email)
    page.locator("#regPassword").fill("Teste123")
    page.locator('#registerForm button[type="submit"]').click()

    expect(page).to_have_url(re.compile(r".*index\.html"), timeout=TIMEOUT)

    # Aguarda a listagem inicial ser renderizada: garante que o JavaScript
    # da página já está ativo antes de acionar o filtro.
    expect(page.locator(".rest-card").first).to_be_visible(timeout=TIMEOUT)

    page.get_by_role("button", name="Italiana", exact=True).click()

    expect(page.locator(".filter-btn.active")).to_have_text("Italiana", timeout=TIMEOUT)
    page.wait_for_function(AGUARDAR_FILTRO_APLICADO, timeout=TIMEOUT)

    cards = page.locator(".rest-card")
    textos = cards.all_inner_texts()

    assert len(textos) > 0, "O filtro deve retornar pelo menos um restaurante"
    assert all("Italiana" in texto for texto in textos), (
        "Todos os restaurantes exibidos devem ser da categoria Italiana"
    )
