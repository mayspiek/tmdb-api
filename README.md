# TMDB-API

Este é um projeto Python que combina o poder do framework Svelte para o frontend e o FastAPI para o backend. O projeto oferece funcionalidades completas de CRUD (Create, Read, Update, Delete) e a capacidade de favoritar itens, permitindo aos usuários interagir com a API TMDB (The Movie Database).

## Contribuidores
- Mayara Carvalho 
[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/mayspiek)](https://github.com/mayspiek) [![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/mayara-spieker/)](https://www.linkedin.com/in/mayara-spieker/) [![](https://img.shields.io/badge/Gmail-red?style=flat-square&logo=gmail&logoColor=white)](mailto:maya.spieker@gmail.com)
- Gabriela Marques
[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/gabrielamarqs)](https://github.com/gabrielamarqs) [![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/gabriela-marques-dos-santos-899092161/)](https://www.linkedin.com/in/gabriela-marques-dos-santos-899092161/) [![](https://img.shields.io/badge/Gmail-red?style=flat-square&logo=gmail&logoColor=white)](mailto:margabrielaqs@gmail.com)

![image](https://github.com/mayspiek/tmdb-api/assets/79992764/40e26a55-0fd1-4451-b391-9aad5040a524)
![image](https://github.com/mayspiek/tmdb-api/assets/79992764/884ef7b1-f2d6-44d6-9220-d803e8ea75c7)
![image](https://github.com/mayspiek/tmdb-api/assets/79992764/666ec517-cd36-45fd-a97a-0bfb6b5e880f)
![image](https://github.com/mayspiek/tmdb-api/assets/79992764/1974806b-9767-4468-976d-8e27bdfdec2e)
![image](https://github.com/mayspiek/tmdb-api/assets/79992764/1885940a-123e-4795-9546-24ae5c2b6f10)



## Requisitos
- Python 3.x
- Node.js 20.x (Recomendado)
- NVM (Node Version Manager) instalado (caso a versão do Node.js não seja 20.x)

## Instalação

__Clone este repositório para o seu ambiente local:__

  ```bash
  git clone https://github.com/mayspiek/tmdb-api.git
  cd tmdb-api
  ```


## Configurando o Ambiente
Certifique-se de que você atende a todos os pré-requisitos antes de prosseguir. Para verificar e/ou instalar a versão correta do Node.js com o NVM, siga os passos abaixo:

1. __Verifique a versão atual do Node.js__
  ```bash
  node -v
```

2. __Caso a versão do Node.js não seja 20, use o NVM para trocar__
```bash
  nvm install 20
  nvm use 20
```

3. __Crie um ambiente virtual do Python__
```bash
python -m venv venv

# PARA WINDOWS
venv\Scripts\activate

# PARA macOS E LINUX
source venv/bin/activate
```

4. __Instale as dependências do Python__
```bash
pip install -r requirements.txt
```

5. __Navegue até o diretório front e instale as dependências do Node.js__
```bash
cd front
npm install
```
## Uso
1. __Inicie o servidor FastAPI:__
```bash
cd back
uvicorn pycine:app --reload
```


2. __Inicie o servidor de desenvolvimento Svelte:__
```bash
cd front
npm run dev
```

## Funcionalidades

1. ##### Gerenciamento de Usuários
    - **Criar Usuário**: Permite a criação de novos usuários com informações como nome, e-mail e senha.
    - **Atualizar Usuário**: Oferece a capacidade de atualizar informações de usuários existentes, como nome, e-mail e senha.
    - **Ler Usuário**: Permite a visualização dos detalhes de um usuário, incluindo nome e e-mail.
    - **Deletar Usuário**: Permite a exclusão de usuários do sistema, removendo suas informações.

2. ##### Favoritar Filmes
    - **Favoritar Filmes**: Permite aos usuários favoritar filmes disponíveis através da API TMDb. Os filmes favoritados são associados ao usuário atual.
    - **Deletar Favoritos**: Os usuários podem remover filmes da lista de favoritos.
    - **Acessar Lista de Favoritos**: Os usuários podem acessar a lista de favoritos de determinado usuário

3. ##### Pesquisa de Atores
    - **Pesquisar Atores**: Fornece uma funcionalidade de pesquisa de atores usando a API TMDb. Os usuários podem procurar atores por nome e são mostradas outras informações disponíveis na API como ID do ator, nome, foto e biografia.

4. ##### (Usuário Padrão)
    - **Usuário Padrão**: O projeto inclui um usuário padrão para fins de demonstração e teste. Esse usuário pode ser usado para experimentar as funcionalidades sem a necessidade de criar uma conta separada.


