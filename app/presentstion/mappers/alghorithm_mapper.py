
from domain.entities.algorithm import SM2Params
from presentstion.schemas.algorithm_schemas import SM2Response


class SM2Mapper:
    @staticmethod
    def to_response(alghoritm: SM2Params) -> SM2Response:
        """Преобразование доменной сущности в схему ответа"""
        return SM2Response(
            id=alghoritm.id,
            interval=alghoritm.interval,
            ef=alghoritm.ef,
            quality=alghoritm.quality,
            show_dt=alghoritm.show_dt,
        )