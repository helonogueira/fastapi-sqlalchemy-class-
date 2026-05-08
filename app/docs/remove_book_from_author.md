# Remover Livro de Autor
## Descricao
Remove a associacao entre um livro e um autor pelo ID de ambos.
## Parametros
- **author_id** (int): ID do autor. Exemplo: 1
- **book_id** (int): ID do livro a ser desassociado. Exemplo: 2
## Resposta
- **200 OK**: Retorna o autor atualizado sem o livro na lista.
- **404 Not Found**: Autor ou livro nao encontrado.