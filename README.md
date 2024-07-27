## API de Usuários - Documentação

Visão Geral
Esta API permite criar, listar, buscar e deletar usuários. Foi desenvolvida utilizando Flask, SQLAlchemy, Flask-Migrate e Blueprints, com PostgreSQL como banco de dados.

<details><summary>Endpoints</summary> 

    `GET /users/` - Retorna a lista de todos os usuários.
    `GET /users/<user_id>`- Retorna os detalhes de um usuário específico.
    `POST /users/` - Cria um novo usuário.
    `DELETE /users/<user_id>` - Deleta um usuário específico.

</details>


<details><summary>Estrutura do Projeto</summary>

    ```
    src/
    ├── config/
    │   └── config.py
    ├── models/
    │   └── user_model.py
    ├── repositories/
    │   └── user_repository.py
    ├── routes/
    │   └── user_router.py
    ├── services/
    │   └── user_service.py
    ├── __init__.py
    └── server.py

    ```
</details>

<details><summary>Configuração</summary>

### Variáveis de Ambiente
- `FLASK_APP` - Define o ponto de entrada da aplicação Flask. Deve ser src/server.py.
- `FLASK_ENV` - Define o ambiente de execução. Use development para ambiente de desenvolvimento.
- `DATABASE_URL` - URL de conexão do banco de dados PostgreSQL.

Exemplo de definição das variáveis de ambiente no terminal:

```bash
export FLASK_APP=src/server.py
export FLASK_ENV=development
export DATABASE_URL=postgresql://username:password@localhost/dbname
```
</details>

<details> <summary>Endpoints Detalhados</summary>

`GET /users/`
Retorna a lista de todos os usuários.

#### Request:
```http
GET /users/

```

**Response**:
**Status**: 200 OK
**Body**:

```json
[
    {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com"
    },
    {
        "id": 2,
        "username": "user2",
        "email": "user2@example.com"
    }
]

```

`GET /users/<user_id>`
Retorna os detalhes de um usuário específico.

**Request**:
```http
GET /users/<user_id>

```

**Response**:

**Status**: 200 OK (se o usuário for encontrado)

**Body**:
```json
{
    "id": 1,
    "username": "user1",
    "email": "user1@example.com"
}

```
**Status**: 404 Not Found (se o usuário não for encontrado)
**Body**:
```json
{
    "error": "User not found"
}

```

`POST /users/`
Cria um novo usuário.

**Request:**:

```http
{
    "username": "newuser",
    "email": "newuser@example.com"
}

```


**Response**:

**Status**: 201 Created
**Body**:

```http
{
    "id": 3,
    "username": "newuser",
    "email": "newuser@example.com"
}

```

`DELETE /users/<user_id>`
Deleta um usuário específico.

**Request**:
```http
DELETE /users/<user_id>
```
**Response**:

**Status**: 204 No Content (se o usuário for deletado com sucesso)
**Status**: 404 Not Found (se o usuário não for encontrado)
**Body**:

```json
{
    "error": "User not found"
}

```


</details>