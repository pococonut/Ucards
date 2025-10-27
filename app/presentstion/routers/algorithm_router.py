from fastapi import APIRouter, Depends

from domain.entities.algorithm import SM2Params
from presentstion.dependencies import get_sm2_service
from application.services.algorithm_service import SM2Service


router = APIRouter()


@router.post("/initial_variables", tags=['algorithm'])
def post_sm2(card_id: str,
             algorithm_service: SM2Service = Depends(get_sm2_service)):
    params = SM2Params(id=card_id, interval=1, ef=2.5, quality=1)
    return algorithm_service.add_card_params(card_id, params=params)
