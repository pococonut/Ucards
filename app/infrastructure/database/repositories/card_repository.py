from sqlalchemy import insert, select, update, delete
from sqlalchemy.engine import Connection

from domain.entities.card import Card
from domain.interfaces.card_repository import CardRepository
from infrastructure.database.core.tables import cards_table

cards = [
    Card(id="0", deck_id="0", name="hello", description="привет"),
    Card(id="1", deck_id="0", name="world", description="мир")
]


class DBCardRepository(CardRepository):
    """
    Класс для работы с базой данных
    """
    def __init__(self, connection: Connection):
        self.conn = connection

    def get_all_cards(self) -> list[Card]:
        """
        Возвращает все карточки.

        Returns:
            list[Card]: Все карточки.
        """
        stmt = select(cards_table)
        rows = self.conn.execute(stmt).fetchall()
        return [Card(id=row.id, deck_id=row.deck_id, name=row.name, description=row.description) for row in rows]
    
    def get_card_by_id(self, card_id: str) -> Card | None:
        """
        Возвращает карточку по id.

        Args:
            card_id (str): Уникальный идентификатор.

        Returns:
            Card: Карточка.
        """
        stmt = select(cards_table).where(cards_table.c.id==card_id)
        result = self.conn.execute(stmt).first()
        if result:
            return Card(
                id=result.id, 
                deck_id=result.deck_id,
                name=result.name,
                description=result.description)
        return None

    def add_card(self, card: Card) -> Card:
        """
        Добавляет новую карточку.

        Args:
            new_card (Card): Тело новой карточки.

        Returns:
            Card: Добавленная карточка.
        """
        stmt = insert(cards_table).values(
            deck_id=card.deck_id,
            name=card.name,
            description=card.description
        )
        result = self.conn.execute(stmt)
        card_id = result.inserted_primary_key[0]
        return Card(
            id=card_id, 
            deck_id=card.deck_id,
            name=card.name,
            description=card.description)
    
    def change_card(self, card_id: str, new_card: dict) -> Card:
        """
        Заменяет параметры карточки.

        Args:
            card_id (str): Уникальный идентификатор карточки, которую необходимо изменить.
            new_card (Card): Тело карточки с обновленными параметрами.
        Returns:
            Card: Обновленная карточка.
        """
        stmt = (
        update(cards_table)
        .where(cards_table.c.id == card_id)
        .values(**new_card)
        .returning(cards_table)  # возвращает все поля обновлённой строки
    )
        result = self.conn.execute(stmt)
        updated_row = result.first()
        if updated_row:
            # превращаем строку в объект Card
            return Card(
                id=updated_row.id,
                deck_id=updated_row.deck_id,
                name=updated_row.name,
                description=updated_row.description
            )
        return None 

    def delete_card(self, card_id: str) -> bool:
        """
        Удаляет карточку.
        
        Args:
            card_id (str): Уникальный идентификатор карточки, которую необходимо изменить.
        
        Returns:
            Card: Удаленная картчочка.
        """
        stmt = delete(cards_table).where(cards_table.c.id == card_id)
        result = self.conn.execute(stmt)
        return result.rowcount > 0  # rowcount показывает количество затронутых строк
    
