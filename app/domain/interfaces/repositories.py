from abc import ABC


class CardRepository(ABC):
    @classmethod
    def get_all_cards(self) -> list[dict]:
        """Получить все карты"""
        pass


    # @classmethod
    # def add_card(self, card: dict) -> dict:
    #     """Добавить карту"""
    #     pass

    # @classmethod
    # def get_card(self, card_id: str) -> dict:
    #     """Получить карту"""
    #     pass

    # @classmethod
    # def change_card(self, card_id) -> dict:
    #     """Изменить карту"""
    #     pass

    # @classmethod
    # def delete_card(self, card_id) -> dict:
    #     """Удалить карту"""
    #     pass


