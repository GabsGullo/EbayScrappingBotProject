# EbayScrappingBotProject
# 🤖 eBay Universal Scraper

> **Status do Projeto:** 🚀 Finalizado / Em Melhoria

Automação web desenvolvida em **Python** com **Selenium** para extração inteligente de dados do eBay, gerando relatórios automáticos em Excel.

---

## ✨ Funcionalidades

* 🔍 **Busca Dinâmica:** O usuário define o termo de busca em tempo real.
* ⏳ **Espera Inteligente:** Implementação de `WebDriverWait` para evitar erros de carregamento.
* 🧹 **Data Cleaning:** Tratamento de strings para remover sufixos inúteis do eBay.
* 📊 **Exportação Direta:** Geração de planilha `.xlsx` com colunas de Produto, Preço e Link.

---

## 🛠️ Tecnologias e Bibliotecas

| Ferramenta | Descrição |
| :--- | :--- |
| **Python 3.x** | Linguagem base |
| **Selenium** | Automação e Navegação |
| **Pandas** | Estruturação dos dados |
| **Openpyxl** | Motor de escrita para Excel |

---

## 🚀 Como Rodar o Projeto

1. **Prepare o ambiente:**
   ```bash
   pip install selenium pandas openpyxl

2. **Execute o script:**
   ```bash
   python ebayScrappingBot.py

## ⚠️ Aviso Legal (Disclaimer)

Este projeto foi desenvolvido **exclusivamente para fins educacionais** e de demonstração de conhecimentos em Python, Selenium e Automação Web. 

* **Uso Acadêmico:** O código não possui fins comerciais, lucrativos ou de concorrência. Seu único objetivo é compor um portfólio de estudos.
* **Scraping Ético:** O script foi projetado com intervalos de tempo (`time.sleep()`) entre as requisições para evitar qualquer tipo de sobrecarga nos servidores da plataforma, respeitando as diretrizes básicas de responsabilidade na web.
* **Isenção de Responsabilidade:** Não me responsabilizo pelo mau uso, modificação ou execução abusiva deste script por terceiros de forma que viole os Termos de Serviço (ToS) do eBay ou de qualquer outra plataforma.

Recomenda-se fortemente aos usuários que fizerem um *fork* ou clone deste repositório que revisem o arquivo `robots.txt` dos sites alvo e ajam com bom senso ao realizar extração de dados.
