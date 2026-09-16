# Gerenciador-Finance

Plataforma de controle de documentos desenvolvida com Django para a [Finance]

## Instalação

### 1. Clonar o repositório

```bash
git clone git@github.com:hiagosoares07/Gerenciador-Finance.git
cd Gerenciador-Finance
```

### 1.1. Atualizar o projeto

```
git pull origin main
```

### 2. Criar e ativar ambiente virtual

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependências

```
pip install -r requirements.txt
```

Caso o arquivo não exista, ou caso seja necessário atualizar as dependências:

```
pip freeze > requirements.txt
```

### 4. Executando o projeto

```
cd i9tmg
python manage.py runserver
```

### 5. Abrindo o projeto na IDE

Para abrir o projeto no VSCode, execute no seu terminal (na raíz do projeto `/Gerenciador-Finance`):

```
code .
```

## Tecnologias usadas

### Back-end

- [Django](https://www.djangoproject.com/): Framework Web Python completo, com recursos para desenvolvimento rápido e seguro.

### Front-End

- [Tailwindcss](https://tailwindcss.com/): Utilizado para estilização rápida.

- [Heroicons](https://heroicons.com/) (depende do Tailwindcss): Biblioteca de ícones.

- [Animate.css](https://animate.style/): Animações CSS.

## Softwares recomendados

- [Visual Studio Code](https://code.visualstudio.com/): Editor de código-fonte recomendado para o desenvolvimento do projeto.

### Extensões recomendadas

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python): Suporte completo para a linguagem Python.

- [SQLite3 Editor](https://marketplace.visualstudio.com/items?itemName=yy0931.vscode-sqlite3-editor): Editor e visualizador de banco de dados SQLite.

- [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django): Suporte para sintaxe de templates Django.