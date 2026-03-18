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
