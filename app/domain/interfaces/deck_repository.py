from abc import ABC, abstractmethod

from app.domain.entities.card import Card
from app.domain.entities.deck import Deck


class DeckRepository(ABC):
    @abstractmethod
    def get_all_decks(self) -> list[Deck]:
        """
        Возвращает все доски.

        Returns:
            list[Deck]: Все доски.
        """
        pass

    @abstractmethod
    def get_deck_by_id(self) -> Deck:
        """
        Возвращает доску по id.

        Args:
            deck_id (str): Уникальный идентификатор.

        Returns:
            Deck: Доска.
        """
        pass

    @abstractmethod
    def get_cards(self, deck_id: str) -> list[Card]:
        """
        Возвращает карточки для доски.

        Args:
            deck_id (str): Уникальный идентификатор.

        Returns:
            list[Card]: Список карт доски.
        """
        pass
    
    @abstractmethod
    def add_deck(self, new_deck: Deck) -> Deck:
        """
        Добавляет новую доску.

        Args:
            new_deck (Deck): Тело новой доски.

        Returns:
            Deck: Добавленная доска.
        """
        pass

    @abstractmethod
    def change_deck(self, deck_id: str, new_deck: Deck) -> Deck:
        """
        Заменяет параметры доски.

        Args:
            deck_id (str): Уникальный идентификатор доски, которую необходимо изменить.
            new_deck (Deck): Тело доски с обновленными параметрами.
        
        Returns:
            Deck: Обновленная доска.
        """
        pass
    
    @abstractmethod
    def delete_deck(self, deck_id: str) -> Deck:
        """
        Удаляет доску.
        
        Args:
            deck_id (str): Уникальный идентификатор доски, которую необходимо удалить.
        
        Returns:
            Deck: Удаленная доска.
        """
        pass
