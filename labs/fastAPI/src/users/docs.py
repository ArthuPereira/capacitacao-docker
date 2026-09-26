from fastapi import status

create_user_docs = {
    "summary": "Criar usuário",
    "description": "Cria um novo usuário no sistema.",
    "responses": {
        status.HTTP_201_CREATED: {
            "description": "Usuário criado com sucesso",
        },
        status.HTTP_409_CONFLICT: {
            "description": "Já existe um usuário com este e-mail",
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Erro de validação dos dados enviados",
        },
    },
}


get_users_docs = {
    "summary": "Listar usuários",
    "description": "Retorna todos os usuários cadastrados.",
    "responses": {
        status.HTTP_200_OK: {
            "description": "Lista de usuários retornada com sucesso",
        },
    },
}


get_user_by_id_docs = {
    "summary": "Buscar usuário por ID",
    "description": "Retorna um usuário pelo identificador.",
    "responses": {
        status.HTTP_200_OK: {
            "description": "Usuário encontrado com sucesso",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Usuário não encontrado",
        },
    },
}


update_user_docs = {
    "summary": "Atualizar usuário",
    "description": "Atualiza os dados de um usuário.",
    "responses": {
        status.HTTP_200_OK: {
            "description": "Usuário atualizado com sucesso",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Usuário não encontrado",
        },
    },
}


delete_user_docs = {
    "summary": "Remover usuário",
    "description": "Remove um usuário do sistema.",
    "responses": {
        status.HTTP_204_NO_CONTENT: {
            "description": "Usuário removido com sucesso",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Usuário não encontrado",
        },
    },
}