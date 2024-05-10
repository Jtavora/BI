# Aula - Criação de Base de Dados SQLITE 

Utilizamos ORM em python SQLAlchemy e o gerenciador de migrações Alembic.

Passos realizados na aula:

1. pip install alembic sqlalchemy

2. python -m alembic init migration

3. ajustar o caminho da base no arquivo `alembic.ini` a linha de conexão deve ficar:
`sqlalchemy.url = sqlite:///models.db`

4. criar arquivo `data_models/models.py`, ajustar o caminho do objeto `Base` que estabelece a estrutura dos modelos em `migration/env.py`