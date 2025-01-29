# 🏛️ Automação de Coleta de Dados do Portal da Transparência

## 📌 Descrição
Este projeto automatiza a coleta de dados de despesas públicas no Portal da Transparência utilizando **Python e Selenium**.  
O script acessa o site, interage com elementos dinâmicos (botões, modais e pop-ups) e faz o download dos relatórios financeiros de **01/2024 a 12/2024**.

---

## 🚀 Tecnologias Utilizadas
- **Python 3.x**  
- **Selenium WebDriver**  
- **WebDriver Manager**  
- **Logging** para monitoramento da execução  

---

## 📂 Funcionalidades
- ✅ Aceita automaticamente os cookies do site  
- ✅ Fecha modais/tutoriais que impedem a navegação  
- ✅ Clica nos botões necessários para acessar os dados  
- ✅ Baixa os arquivos de despesas públicas de 2024  

---

## ⚙️ Como Executar

### 🔹 Pré-requisitos
Antes de rodar o script, certifique-se de ter instalado:  
- **Python 3.x**  
- **Google Chrome** e **ChromeDriver**

### 🔹 Instalando dependências
```bash
pip install -r requirements.txt
```

### 🔹 Executando o Script

```bash
python main.py
```
O Selenium abrirá o navegador, navegará pelo site e iniciará o download dos arquivos.

# 📜 Licença
Este projeto é de código aberto e pode ser usado livremente para fins educacionais ou profissionais.

Desenvolvido por Caio Renato Rodrigues Vicente
