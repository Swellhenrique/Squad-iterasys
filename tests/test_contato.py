
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://iterasys.learnworlds.com/"

def test_acessar_linkedin():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Acessar a página inicial
        driver.get(URL)

        # Localizar o botão do LinkedIn no rodapé
        botao_linkedin = wait.until(
            EC.presence_of_element_located(
                (By.ID, "el_1645035537528_322")
            )
        )

        # Rolar até o botão
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            botao_linkedin
        )

        # Aguardar o botão ficar clicável
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "el_1645035537528_322")
            )
        )

        # Registrar as abas abertas antes do clique
        abas_antes = driver.window_handles

        # Clicar no botão
        botao_linkedin.click()

        # Verificar se abriu uma nova aba
        try:
            wait.until(
                EC.new_window_is_opened(abas_antes)
            )
            assert len(driver.window_handles) > len(abas_antes)

        except Exception:
            # Alguns sites abrem o destino na mesma aba.
            # Nesse caso, validar a URL atual.
            assert "linkedin.com" in driver.current_url.lower()

    finally:
        driver.quit()
