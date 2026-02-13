from domain.entities.card import Card
from domain.interfaces.card_repository import CardRepository


cards = [
    Card(id="0", deck_id="0", name="hello", description="привет"),
    Card(id="1", deck_id="0", name="world", description="мир")
]


class DBCardRepository(CardRepository):
    """
    Класс для работы с базой данных
    """
    def get_all_cards(self) -> list[Card]:
        """
        Возвращает все карточки.

        Returns:
            list[Card]: Все карточки.
        """
        return cards
    
    def get_card_by_id(self, card_id: str) -> Card | None:
        """
        Возвращает карточку по id.

        Args:
            card_id (str): Уникальный идентификатор.

        Returns:
            Card: Карточка.
        """
        for card in cards:
            if card.id == card_id:
                return card
        return None
    
    def add_card(self, card: Card) -> Card:
        """
        Добавляет новую карточку.

        Args:
            new_card (Card): Тело новой карточки.

        Returns:
            Card: Добавленная карточка.
        """
        new_card = Card(
            id=str(len(self.get_all_cards())),
            deck_id=card.deck_id,
            name=card.name,
            description=card.description
        )
        cards.append(new_card)
        return new_card
    
    def change_card(self, card_id: str, new_card: Card) -> Card:
        """
        Заменяет параметры карточки.

        Args:
            card_id (str): Уникальный идентификатор карточки, которую необходимо изменить.
            new_card (Card): Тело карточки с обновленными параметрами.
        Returns:
            Card: Обновленная карточка.
        """
        card = next(filter(lambda card: card.id == card_id, cards))
        card.deck_id = new_card.deck_id
        card.name = new_card.name
        card.description = new_card.description
        return card   

    def delete_card(self, card_id: str) -> Card:
        """
        Удаляет карточку.
        
        Args:
            card_id (str): Уникальный идентификатор карточки, которую необходимо изменить.
        
        Returns:
            Card: Удаленная картчочка.
        """
        card = next(filter(lambda card: card.id == card_id, cards))
        card_index = cards.index(card)
        return cards.pop(card_index)
    
