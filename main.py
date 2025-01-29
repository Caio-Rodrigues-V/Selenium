from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def configurar_driver(): 
    options = webdriver.ChromeOptions()
    
    # Configurações para headless
    options.add_argument('--disable-gpu')  # Necessário para compatibilidade em alguns sistemas
    options.add_argument('--no-sandbox')  # Recomendado para ambientes Linux
    options.add_argument('--disable-dev-shm-usage')  # Evitar problemas de memória em containers
    options.add_argument('--window-size=1920,1080')  # Define uma resolução de janela
    options.add_argument('--disable-blink-features=AutomationControlled')  # Evitar detecção de automação

    # Configuração do driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    return driver

def fechar_modal_com_botao(driver):
    try:
        # Aguarda o botão de tutorial estar disponível
        botao_tutorial = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "botao-tutorial"))
        )
        logging.info("Botão do tutorial encontrado. Clicando...")
        
        # Clica no botão para fechar o tutorial/modal
        botao_tutorial.click()
        
        # Aguarda o modal desaparecer
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element((By.ID, "modal-tutorial"))
        )
        logging.info("Modal fechado com sucesso!")
    except Exception as e:
        logging.warning("Erro ao clicar no botão do tutorial:", e)


def coletar_dados(driver, url):
    driver.get(url)
    # Fechar cookies, se existirem
    try:
        cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'accept-all-btn')))
        cookies.click()
        logging.info("Aceitou os cookies!")
    except Exception as e:
        logging.warning("Botão de cookies não encontrado:", e)

    # Fechar modal usando o botão do tutorial
    fechar_modal_com_botao(driver)

    
    try:
        despesas = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.card.card-front')))
        despesas.click()
        logging.info("Elemento clicado!")
    except Exception as e:
        logging.error("Erro ao clicar no elemento de despesas:", e)

    try:
        botao_acessar_painel = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Acessar painel')]")))
        botao_acessar_painel.click()
        logging.info(f"1° Botao clicado")
    except Exception as e:
        logging.error("Erro ao clicar no elemento de despesas:", e)

    try:
        botao_despesas = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "btnDetExDespesasPublicas")))
        botao_despesas.click()
        logging.info("2° Botão clicado!")
    except Exception as e:
        logging.error("Erro ao clicar no botão de despesas", e)

    try:
        download_despesas = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnBaixar")))
        download_despesas.click()
        logging.info("Botão download clicado, verifique sua pasta de downloads (01/2024 - 12/2024)")
        time.sleep(3)
        

    except Exception as e:
        logging.error("Erro ao clicar no botão de despesas", e)
    

  
    
    """try:
        download_despesas = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnDetExDespesasFuncaoSubF")))
        download_despesas.click()
        logging.info("Botão download clicado, verifique sua pasta de downloads (01/2024 - 12/2024)")
        time.sleep(3)
        logging.info("Voltando pagina para continuar automação!")
    except:
        logging.error("Erro ao clicar no botão de despesas", e)"""
            
def main():
    url = "https://portaldatransparencia.gov.br"
    driver = configurar_driver()
    try:
        coletar_dados(driver, url)
    except Exception as e:
        logging.critical("Erro durante a execução: %s", e)
    finally:
        logging.info("Você obteve todas as despesas de 2024 em sua pasta de downloads")
        logging.info("Driver encerrando.")
        driver.quit()
        

if __name__ == "__main__":
    main()
