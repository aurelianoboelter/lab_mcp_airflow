# O que mudou
Este Pull Request adiciona uma nova etapa à dag `foo.py`, que atualiza a tabela `bar` da refined zone
e realiza a limpeza do bucket de entrada dos dados.

# Porque mudou
A adição dessa etapa aconteceu pois a tabela `bar` estava desatualizada com as novas alterações da trusted zone
e foi necessário adicionar alimpeza do bucket de entrada pois estava acumulando muitos dados e gerando muito custo

# Como mudou
Foi adicionado a task `foo_bar` na dag `foo.py` passando um script localizado na pasta `foor\bar.sql` que executa
o script sql no Bigquery e adicionado o operador de limpeza de diretório na dag.

# Como testar/usar a mudança
Dar o checkout para a branch e fazer os passos:
1. fazer x
2. fazer y
3. fazer z

# Quais os cuidados
Nenhum cuidado em especial para esse processo