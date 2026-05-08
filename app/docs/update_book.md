# Atualizar Livro
## Descricao
Atualiza os dados de um livro existente pelo seu ID.
## Parametros
- **book_id** (int): ID do livro a ser atualizado. Exemplo: 1
- **title** (str): Novo titulo do livro. Exemplo: "Clean Architecture"
- **isbn** (str): Novo ISBN do livro. Exemplo: "978-0134494166"
## Resposta
- **200 OK**: Retorna o livro atualizado.
- **404 Not Found**: Livro nao encontrado.