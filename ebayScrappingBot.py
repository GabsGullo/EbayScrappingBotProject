from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os

def save_to_excel(data, nome):
    df = pd.DataFrame(data)
    headers = ['Produto', 'Preço', 'Link']

    # Substitui os espaços por _ para o nome do arquivo
    nome_arquivo = f"{nome.replace(' ', '_')}_Scrapper.xlsx"
    #Garante que a pasta 'Resultados' exista (se não existir, o Python cria)
    os.makedirs("Resultados", exist_ok=True)

    caminho_completo = os.path.join("Resultados", nome_arquivo)
    df.to_excel(caminho_completo, header=headers, index=False)
    print(f"🎉 SUCESSO! Arquivo salvo em: {caminho_completo}")

def clean_data(lista_produtos):
    clean_data = []
    for produto in lista_produtos:
        titulo = produto.find_element(By.CSS_SELECTOR, ".s-card__title").text
        preco = produto.find_element(By.CSS_SELECTOR, ".s-card__price").text
        link = produto.find_element(By.CSS_SELECTOR, "a.s-card__link").get_attribute("href")

        if not preco or not titulo or not link:
            continue
        titulo_limpo = titulo.replace("Abre em janela ou guia separada", "").strip()

        clean_data.append({
            "Console": titulo_limpo,
            "Preço": preco,
            "Link da Oferta": link
        })

    return clean_data


def wait_function(driver, by_type, locator, mode):
    wait = WebDriverWait(driver, 10)
    if mode == 'presence':
        elemento = wait.until(
            EC.presence_of_element_located((by_type, locator))
        )
        return elemento
    elif mode == 'visibility':
        elemento = wait.until(
            EC.visibility_of_element_located((by_type, locator))
        )
        return elemento
    return None


def print_produtos(lista_limpa_produtos):
    print(f"\n✅ Foram processados {len(lista_limpa_produtos)} produtos com sucesso!")
    print("-" * 50)

    for produto in lista_limpa_produtos[:5]:
        try:

            print(f"Produto: {produto['Console']}")
            print(f"Preço: {produto['Preço']}")
            print(f"Link: {produto['Link da Oferta']}")
            print("-" * 50)

        except Exception as e:

            continue


def bot_scrapper(produto):
    options = Options()
    # utilize caso o bot esteja visivel
    #options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    try:
        print("Iniciando bot...")
        driver.get("https://www.ebay.com/")

        print("Site encontrado!")
        print("Procurando barra de busca...")
        barra_busca = wait_function(driver, By.CSS_SELECTOR,"#gh-ac", 'visibility')

        print("Barra de busca encontrada!")
        barra_busca.click()
        barra_busca.clear()
        barra_busca.send_keys(f"{produto_usuario}")
        barra_busca.send_keys(Keys.ENTER)
        print("Pesquisa realizada!\n")

        time.sleep(2)
        #Produtos existem?
        aviso_nao_encontrado = driver.find_elements(By.CSS_SELECTOR, ".srp-save-null-search__heading")
        if len(aviso_nao_encontrado) > 0:
            print(f" Nenhum resultado exato encontrado para '{produto}'.")
            print("Encerrando o bot pacificamente...")
            return  # O 'return' faz o bot encerrar

        print("Produtos encontrados! Continuando o processo...")

        print("Extraindo produtos...")
        lista_produtos = driver.find_elements(By.CSS_SELECTOR, ".s-card")

        print("Produtos extraidos!")
        lista_limpa_produtos = clean_data(lista_produtos)

        print_produtos(lista_limpa_produtos)
        save_to_excel(lista_limpa_produtos, f"{produto}")

    except Exception as erro:
        print(f"Um erro inesperado ocorreu: {erro}")

        os.makedirs('errors', exist_ok=True)
        caminho_foto = os.path.join('errors', 'evidencia_erro.png')
        driver.save_screenshot(caminho_foto)

        print(f"Uma foto da tela no momento do erro foi salva em: {caminho_foto}")

    finally:
        driver.quit()


if __name__ == "__main__":
    print("🤖 Bem-vindo ao Scraper Universal do eBay!")
    produto_usuario = input("👉 Digite o produto que você quer buscar: ")
    bot_scrapper(produto_usuario)