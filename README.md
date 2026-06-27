# Evo Python 🚀

Este repositório contém um script simples em Python para interação com a **Evolution API**, focado na criação e gerenciamento de instâncias do WhatsApp (utilizando a integração `WHATSAPP-BAILEYS`).

## 📋 Sobre o Projeto

O projeto consiste em um script em Python que realiza requisições HTTP para uma API local ou remota da Evolution API para provisionar novas instâncias de WhatsApp de forma automatizada.

### Estrutura de Arquivos

*   `instance.py`: Script principal que realiza a requisição POST para o endpoint `/instance/create` a fim de criar uma nova instância.
*   `requirements.txt`: Dependências Python necessárias para a execução do script (biblioteca `requests` e suas subdependências).
*   `.gitignore`: Configuração para evitar o envio de ambientes virtuais (`.venv`) ou arquivos temporários para o Git.

---

## 🛠️ Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:
*   [Python 3.8+](https://www.python.org/downloads/)
*   [Git](https://git-scm.com/)
*   Uma instância funcional da [Evolution API](https://github.com/Evolution-API/evolution-api) rodando localmente ou em um servidor acessível.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar o ambiente e executar o script:

### 1. Clonar o Repositório
```bash
git clone https://github.com/helioelias/evo-python.git
cd evo-python
```

### 2. Configurar o Ambiente Virtual (Opcional, mas Recomendado)
Crie e ative um ambiente virtual para isolar as dependências do projeto:

**No Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**No Linux/macOS:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as Dependências
Com o ambiente virtual ativo, instale os pacotes necessários:
```bash
pip install -r requirements.txt
```

### 4. Configurar as Variáveis no Script
Abra o arquivo `instance.py` e configure os seguintes parâmetros de acordo com a sua infraestrutura:

*   **URL da API (`url`)**: O endereço onde sua Evolution API está rodando (ex: `http://localhost:8080/instance/create`).
*   **API Key (`apikey`)**: A chave de autenticação configurada na sua Evolution API (passada no cabeçalho `apikey`).
*   **Payload da Instância**:
    *   `instanceName`: Nome que deseja dar à nova instância (ex: `ebainstance`).
    *   `qrcode`: Define se o QR Code deve ser retornado (`True` ou `False`).
    *   `integration`: Tipo de integração (ex: `"WHATSAPP-BAILEYS"`).

### 5. Executar o Script
Rode o script para enviar a requisição de criação de instância:
```bash
python instance.py
```

Se tudo estiver correto, a Evolution API retornará os dados da nova instância criada, incluindo a chave de pareamento ou dados do QR Code.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
