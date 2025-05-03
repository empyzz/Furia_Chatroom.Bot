# Furia-ChatRooms

Um sistema de chat para usuários se comunicarem em tempo real e um chat bot para fazerem perguntas relacionadas a Counter Strike. O site é responsivo e funcionara em qualquer dispositivo. O projeto foi desenvolvido utilizando Django, com integração de websockets para mensagens instantâneas.

## Tecnologias Principais usadas

Aqui estão as tecnologias usadas neste projeto:

## Backend
<table>
  <tr>
    <td align="center">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain.svg" width="50" height="50"/>
      <br />Django
    </td>
    <td align="center">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="50" height="50"/>
      <br />Python
    </td>
  </tr>
</table>

## Frontend
<table>
  <tr>
    <td align="center">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="50" height="50"/>
      <br />JavaScript
    </td>
    <td align="center">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="50" height="50"/>
      <br />HTML5
    </td>
    <td align="center">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="50" height="50"/>
      <br />CSS3
    </td>
    <td align="center">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tailwindcss/tailwindcss-original.svg" width="50" height="50"/>
      <br />Tailwind CSS
    </td>
    <td align="center">
      <img src="https://camo.githubusercontent.com/cf6b86ab1d68b2e06eb1312b20d25e5754cf860ece54396611768d7fff034c5e/68747470733a2f2f696d672e646169737975692e636f6d2f696d616765732f646169737975692f646169737975692d6c6f676f2d3139322e706e67" width="50" height="50"/>
      <br />DaisyUI
    </td>
  </tr>
</table>

## Banco de Dados
<table>
  <tr>
    <td align="center">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="50" height="50"/>
      <br />PostgreSQL
    </td>
  </tr>
</table>


## Imagens do Projeto

[![Tela de login](images/paglogin.png)](images/paglogin.png)  
_Tela de login, com criação de conta e restauração de senha._

[![Tela dos cards](images/pagtela1.png)](images/pagtela1.png)  
_Cards com as salas e visualizador de usuários online._

[![Tela do chat](images/pagchat.png)](images/pagchat.png)  
_Página com o chat em tempo real com outros usuários._

[![Tela para Criar os chats](images/pagcriarchat.png)](images/pagcriarchat.png)  
_Criação de cards com nome, descrição e um tema específico para aquela sala._

[![Tela do bot](images/pagbot.png)](images/pagbot.png)  
_Perguntas predefinidas para o usuário selecionar e o bot irá responder._

[![Tela de perfil](images/pagperfil.png)](images/pagperfil.png)
_Pagina para edição de perfil do usuário podendo mudar sua foto de perfil, nome, e alterar sua senha_


## 🚀 Como Rodar o Projeto

### ✅ Pré-requisitos

- 🐍 Python 3.8+
- 🐘 PostgreSQL
- 🚀 Redis (para WebSockets)

### 🛠️ Passos

1. **Clone o repositório**
    ```bash
    git clone https://github.com/empyzz/Furia-ChatRooms.git
    ```

2. **Navegue até o diretório do projeto**
    ```bash
    cd Furia-ChatRooms
    ```

3. **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o banco de dados PostgreSQL** e as variáveis de ambiente (`.env`).

5. **Execute o servidor Django**
    ```bash
    python manage.py runserver
    ```

6. **Inicie os WebSockets**
    ```bash
    python manage.py runchannels
    ```

---

## 🧰 Tecnologias Especificas 

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="50" title="Python"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="50" title="Django"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="50" title="PostgreSQL"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="50" title="JavaScript"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg" width="50" title="Redis"/>
</p>

<p align="center">
  Python • Django • Django Channels • Daphne • PostgreSQL • JavaScript • Redis
</p>

### Considerações Finais

<p>Este foi meu primeiro projeto que trabalhei com o ASGI e funções assíncronas, foi interessante estudar estes conceitos.</p>
<p>Melhorei em muito meu entedimento sobre Javascript, aplicando AJAX e FetchAPI com ele.</p>
<p>E em geral aprendi muitos conceitos novos sobre sistemas webs em geral com esse projeto.</p>
<p>Dei uma chance para o TailwindCSS também e gostei muito de usar, facilitou em muito meu projeto</p>
<p>Junto com o TailwindCSS usei o DaisyUI para componentes mais customizaveis e temas diferentes</p>
<p>Para o chatbot queria ter usado alguma biblioteca como OpenIA para treinar um bot para responder as perguntas mas fiquei com medo de não dar tempo de realizar isso, então fui com um JSON com perguntas e respostas</p>