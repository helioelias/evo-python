# Evo Python 🚀

Este repositório contém um script simples em Python para interação com a **Evolution API**, focado na criação e gerenciamento de instâncias do WhatsApp (utilizando a integração `WHATSAPP-BAILEYS`).

## 📋 Sobre o Projeto

O projeto consiste em um script em Python que realiza requisições HTTP para uma API local ou remota da Evolution API para provisionar novas instâncias de WhatsApp de forma automatizada.

### Estrutura de Arquivos

*   `instance.py`: Script principal que realiza a requisição POST para o endpoint `/instance/create` a fim de criar uma nova instância.
*   `requirements.txt`: Dependências Python necessárias para a execução do script (incluindo `requests` e `python-dotenv`).
*   `.env.example`: Modelo de configuração das variáveis de ambiente.
*   `.env`: Arquivo local de configurações (este arquivo é ignorado pelo Git para segurança dos dados).
*   `.gitignore`: Configuração para evitar o envio de ambientes virtuais (`.venv`) e segredos (`.env`) para o Git.

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

### 4. Configurar as Variáveis de Ambiente
Copie o arquivo de exemplo de variáveis de ambiente e configure seus valores:

```bash
cp .env.example .env
```

Abra o arquivo `.env` e ajuste as variáveis de acordo com o seu ambiente:

*   `EVOLUTION_API_URL`: O endereço base onde a sua Evolution API está rodando (ex: `http://localhost:8080`).
*   `EVOLUTION_API_KEY`: A chave de autenticação (API key) configurada na sua Evolution API.
*   `EVOLUTION_INSTANCE_NAME`: O nome da instância do WhatsApp que você deseja criar (ex: `ebainstance`).
*   `EVOLUTION_INSTANCE_QRCODE`: Define se o QR Code deve ser retornado (`true` ou `false`).
*   `EVOLUTION_INSTANCE_MOBILE`: Configuração do tipo de dispositivo móvel (`true` ou `false`).
*   `EVOLUTION_INSTANCE_INTEGRATION`: Tipo de integração de mensageria (ex: `WHATSAPP-BAILEYS`).

### 5. Executar o Script
Rode o script para enviar a requisição de criação de instância:
```bash
python instance.py
```

Se tudo estiver correto, a Evolution API retornará os dados da nova instância criada, incluindo a chave de pareamento ou dados do QR Code.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
