from sqlalchemy import create_engine

db = create_engine(
    "postgresql+psycopg2://postgres:password123@localhost:5432/QA"
    )
