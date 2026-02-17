from app.domain.entities.card import Card
from app.domain.entities.deck import Deck
from app.domain.interfaces.deck_repository import DeckRepository
from app.infrastructure.repositories.card_repository import cards


decks = [
    Deck(id="0", name="Langs", algorithm="sm2")
]


class DBDeckRepository(DeckRepository):
    """
    Класс для работы с базой данных
    """
    def get_all_decks(self) -> list[Deck]:
        """
        Возвращает все доски.

        Returns:
            list[Deck]: Все доски.
        """
        result: list[Deck] = decks
        return result
    
    def get_deck_by_id(self, deck_id: str) -> Deck | None:
        """
        Возвращает доску по id.

        Args:
            deck_id (str): Уникальный идентификатор.

        Returns:
            Deck: Доска.
        """
        for deck in decks:
            if deck.id != deck_id:
                continue

            result: Deck = deck
            return result
        return None

    
    def get_cards(self, deck_id: str) -> list[Card]:
        """
        Возвращает карточки для доски.

        Args:
            deck_id (str): Уникальный идентификатор.

        Returns:
            list[Card]: Список карт доски.
        """
        result: list[Card] = list(filter(lambda card: card.deck_id == deck_id, cards))
        return result

    def add_deck(self, deck: Deck) -> Deck:
        """
        Добавляет новую доску.

        Args:
            new_deck (Deck): Тело новой доски.

        Returns:
            Deck: Добавленная доска.
        """
        new_deck: Deck = Deck(
            id=str(len(self.get_all_decks())),
            name=deck.name,
            algorithm=deck.algorithm
        )
        decks.append(new_deck)
        return new_deck
    
    def change_deck(self, deck_id: str, new_deck: Deck) -> Deck:
        """
        Заменяет параметры доски.

        Args:
            deck_id (str): Уникальный идентификатор доски, которую необходимо изменить.
            new_deck (Deck): Тело доски с обновленными параметрами.
        
        Returns:
            Deck: Обновленная доска.
        """
        deck: Deck = next(filter(lambda deck: deck.id == deck_id, decks))
        deck.name = new_deck.name
        deck.algorithm = new_deck.algorithm
        return deck   

    def delete_deck(self, deck_id: str) -> Deck:
        """
        Удаляет доску.
        
        Args:
            deck_id (str): Уникальный идентификатор доски, которую необходимо удалить.
        
        Returns:
            Deck: Удаленная доска.
        """
        deck= next(filter(lambda deck: deck.id == deck_id, decks))
        deck_index = decks.index(deck)
        reesult: Deck = decks.pop(deck_index)
        return reesult
    
