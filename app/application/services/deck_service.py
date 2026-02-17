from app.domain.entities.card import Card
from app.domain.entities.deck import Deck
from app.domain.interfaces.deck_repository import DeckRepository


class DeckService:
    """
    Содержит бизнес-правила. Не знает, откуда берутся данные, знает только ЧТО с ними делать
    """
    def __init__(self, deck_repository: DeckRepository):
        self._deck_repository = deck_repository

    def get_all_decks(self) -> list[Deck]:
        """
        Возвращает все доски.

        Returns:
            list[Deck]: Все доски.
        """
        result: list[Deck] = self._deck_repository.get_all_decks()
        return result
    
    def get_deck_by_id(self, deck_id: str) -> Deck:
        """
        Возвращает доску по id.

        Args:
            deck_id (str): Уникальный идентификатор.

        Returns:
            Deck: Доска.
        """
        result: Deck = self._deck_repository.get_deck_by_id(deck_id)
        return result
    
    def get_cards(self, deck_id: str) -> list[Card]:
        """
        Возвращает карточки для доски.

        Args:
            deck_id (str): Уникальный идентификатор.

        Returns:
            list[Card]: Список карт доски.
        """
        result: list[Card] = self._deck_repository.get_cards(deck_id)
        return result
    
    def add_deck(self, new_deck: Deck) -> Deck:
        """
        Добавляет новую доску.

        Args:
            new_deck (Deck): Тело новой доски.

        Returns:
            Deck: Добавленная доска.
        """
        result: Deck = self._deck_repository.add_deck(new_deck)
        return result

    def change_deck(self, deck_id: str, new_deck: Deck) -> Deck:
        """
        Заменяет параметры доски.

        Args:
            deck_id (str): Уникальный идентификатор доски, которую необходимо изменить.
            new_deck (Deck): Тело доски с обновленными параметрами.
        
        Returns:
            Deck: Обновленная доска.
        """
        result: Deck = self._deck_repository.change_deck(deck_id, new_deck)
        return result
    
    def delete_deck(self, deck_id: str) -> Deck:
        """
        Удаляет доску.
        
        Args:
            deck_id (str): Уникальный идентификатор доски, которую необходимо удалить.
        
        Returns:
            Deck: Удаленная доска.
        """
        result: Deck = self._deck_repository.delete_deck(deck_id)
        return result
    
    
