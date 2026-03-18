from sqlalchemy import MetaData, Table, Column, Integer, String


metadata = MetaData()

cards_table = Table(
    "cards",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("deck_id", Integer, nullable=False),
    Column("name", String(500), nullable=False),
    Column("description", String(500), nullable=False),
)






