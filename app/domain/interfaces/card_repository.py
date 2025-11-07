from abc import ABC

from domain.entities.card import Card


class CardRepository(ABC):
    """
    Интерфейс методов карточки
    """
    @classmethod
    def get_all_cards(self) -> list[Card]:
        """
        Возвращает все карточки.

        Returns:
            list[Card]: Все карточки.
        """
        pass

    @classmethod
    def get_card_by_id(self, card_id: str) -> Card:
        """
        Возвращает карточку по id.

        Args:
            card_id (str): Уникальный идентификатор.

        Returns:
            Card: Карточка.
        """
        pass
    
    @classmethod
    def add_card(self, new_card: Card) -> Card:
        """
        Добавляет новую карточку.

        Args:
            new_card (Card): Тело новой карточки.

        Returns:
            Card: Добавленная карточка.
        """
        pass

    @classmethod
    def change_card(self, card_id: str, new_card: Card) -> Card:
        """
        Заменяет параметры карточки.

        Args:
            card_id (str): Уникальный идентификатор карточки, которую необходимо изменить.
            new_card (Card): Тело карточки с обновленными параметрами.
        
        Returns:
            Card: Обновленная карточка.
        """
        pass
    
    @classmethod
    def delete_card(self, card_id: str) -> Card:
        """
        Удаляет карточку.
        
        Args:
            card_id (str): Уникальный идентификатор карточки, которую необходимо удалить.
        
        Returns:
            Card: Удаленная карточка.
        """
        pass
