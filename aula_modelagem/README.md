# Aula - Criação de Base de Dados

Utilizamos ORM em python SQLAlchemy e o gerenciador de migrações Alembic.

Passos realizados na aula:

1. pip install alembic sqlalchemy

2. python -m alembic init migration

3. ajustar o caminho da base no arquivo `alembic.ini` a linha de conexão deve ficar:
`sqlalchemy.url = sqlite:///models.db`

4. criar arquivo `data_models/models.py`, ajustar o caminho do objeto `Base` que estabelece a estrutura dos modelos em `migration/env.py`

5.  docker build -t postgres_bi .

6. docker run --name postgres_bi -p 5432:5432 -d postgres_bi