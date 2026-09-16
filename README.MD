
# Gerenciador-Finance

Plataforma desenvolvida com Django para a [i9TMG].

## Instalação

```bash
git clone 
```
---

## Tecnologias utilizadas no projeto

### Back-End

- [Django](https://www.djangoproject.com/): Framework web de alto nível escrito em Python para o desenvolvimento rápido, seguro e escalável.

### Front-End

- [Tailwind CSS](https://tailwindcss.com/): Framework CSS para estilização com classes.

- [Heroicons](https://heroicons.com/) (depende do **Tailwind CSS**): Biblioteca de ícones.

- [Animate.css](https://animate.style/): Biblioteca de animações prontas para projetos web.

## Ferramentas

- [Visual Studio Code](https://code.visualstudio.com/): Editor de código-fonte recomendado para o desenvolvimento do projeto.

### Extensões recomendadas

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python): Suporte completo para a linguagem Python.

- [SQLite3 Editor](https://marketplace.visualstudio.com/items?itemName=yy0931.vscode-sqlite3-editor): Editor e visualizador de banco de dados SQLite.

- [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django): Suporte para sintaxe de templates Django.

---

# Contribuição

Para contribuir com o projeto, siga as instruções abaixo.

## Regras de contribuição

- Não realize commits diretamente no branch `main`.

- Toda nova funcionalidade, correção ou melhoria deve ser desenvolvida em uma branch separada.

- Antes de iniciar uma alteração, certifique-se que seu repositório local esteja atualizado e que outros membros não estejam alterando os mesmos arquivos para evitar conflitos.

- Alterações devem ser revisadas antes da aprovação e merge.

- Commits devem possuir mensagens objetivas e organizadas.

## Padrão de branches

Para as suas branches, utilize o seguinte padrão:

### Funcionalidades

```bash
feature/seu-nome/funcionalidade
```

Exemplo:

```bash
feature/hiagosoares07/login-cadastro-de-usuarios
```

### Correções

```bash
fix/seu-nome/correcao
```

Exemplo:

```bash
fix/hiagosoares07/pagina-login
```

### Melhorias

```bash
improvement/seu-nome/melhoria
```

Exemplo:

```bash
improvement/hiagosoares07/layout-home
```

## Fluxo de contribuição

### 1. Atualizar o projeto

```bash
git pull origin main
```

### 2. Criar uma nova branch

```bash
git checkout -b <nome-do-branch>
```

Exemplo:

```bash
git checkout -b feature/hiagosoares07/login-cadastro-de-usuarios
```

### 3. Realizar alterações e commits

No seu Terminal, consulte suas alterações no seu branch:

```bash
git status
```
Exibe os arquivos alterados no repositório. Em vermelho o que foi alterado e em verde os que você adicionou no `git add`.

Exemplo:

```bash
C:Users\hiagosoares07\Desktop\projeto_django> git status
No ramo feature/hiagosoares07/login-e-registro
Changes not staged for commit:
  (utilize "git add <arquivo>..." para atualizar o que será submetido)
  (use "git restore <file>..." to discard changes in working directory)
        modified: projeto_django/users/templates/login_page.html
        new file: projeto_django/users/templates/register_page

```

Adicione as alterações:

```bash
git add <arquivo>
```

Exemplo:

```bash
git add projeto_django/users/templates/register_page
```

Ou, para adicionar todos os arquivos alterados, excluídos ou adicionados:

```bash
git add .
```

Depois de adicionar as alterações, salve em um commit:

```git bash
git commit -m "descreva suas alteracoes"
```

Exemplo:

```bash
git commit -m "Adicionado tela e funcionalidade de Login e Registro de usuarios"
```

**Atenção:** Evite utilizar acentos no commit.

### 4. Enviar branch para o repositório

Após commitar suas alterações, envie seu branch para o repositório:

```bash
git push origin <seu-branch>
```

Exemplo:

```bash
git push origin feature/hiagosoares07/login-e-registro
```

Após isso, no site do Github, na página do repositório, aparecerá uma opção para abrir um **Pull Request**.

### 5. Abrir Pull Request

No seu Pull Request:

- Descreva claramente as alterações realizadas.

- Caso necessário, adicione imagens ou exemplo.

## Aprovação de Pull Requests

- Pull Requests devem ser aprovados por todos os participantes do projeto e pelo dono do repositório.

- O merge só poderá ser realizado após aprovação.

## Boas práticas

- Manter o código organizado e legível.

- Evitar código duplicado.

- Seguir padrão já utilizado no projeto.

- Testar alterações antes de enviar o Pull Request.

- Documentar funcionalidades quando necessário.