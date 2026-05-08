# Adicionar Livro a Autor
## Descricao
Associa um livro existente a um autor existente pelo ID de ambos.
## Parametros
- **author_id** (int): ID do autor. Exemplo: 1
- **book_id** (int): ID do livro a ser associado. Exemplo: 2
## Resposta
- **200 OK**: Retorna o autor atualizado com o livro na lista.
- **404 Not Found**: Autor ou livro nao encontrado.