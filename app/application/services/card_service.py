from domain.entities.card import Card
from domain.interfaces.card_repository import CardRepository


class CardService:
    """
    Содержит бизнес-правила. Не знает, откуда берутся данные, знает только ЧТО с ними делать
    """
    def __init__(self, card_repository: CardRepository):
        self._card_repository = card_repository

    def get_all_cards(self) -> list[Card]:
        """
        Возвращает все карточки.

        Returns:
            list[Card]: Все карточки.
        """
        result: list[Card] = self._card_repository.get_all_cards()
        return result
    
    def get_card_by_id(self, card_id: str) -> Card:
        """
        Возвращает карточку по id.

        Args:
            card_id (str): Уникальный идентификатор.

        Returns:
            Card: Карточка.
        """
        return self._card_repository.get_card_by_id(card_id)
    
    def add_card(self, new_card: Card) -> Card:
        """
        Добавляет новую карточку.

        Args:
            new_card (Card): Тело новой карточки.

        Returns:
            Card: Добавленная карточка.
        """
        return self._card_repository.add_card(new_card)

    def change_card(self, card_id: str, new_card: Card) -> Card:
        """
        Заменяет параметры карточки.

        Args:
            card_id (str): Уникальный идентификатор карточки, которую необходимо изменить.
            new_card (Card): Тело карточки с обновленными параметрами.
        Returns:
            Card: Обновленная карточка.
        """
        return self._card_repository.change_card(card_id, new_card)
    
    def delete_card(self, card_id: str) -> Card:
        """
        Удаляет карточку.
        
        Args:
            card_id (str): Уникальный идентификатор карточки, которую необходимо удалить.
        
        Returns:
            Card: Удаленная карточка.
        """
        return self._card_repository.delete_card(card_id)
    
    
