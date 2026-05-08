# Atualizar Autor
## Descricao
Atualiza os dados de um autor existente pelo seu ID.
## Parametros
- **author_id** (int): ID do autor a ser atualizado. Exemplo: 1
- **name** (str): Novo nome do autor. Exemplo: "Carlos Silva"
- **email** (str): Novo email do autor. Exemplo: "carlos@example.com"
## Resposta
- **200 OK**: Retorna o autor atualizado.
- **404 Not Found**: Autor nao encontrado.