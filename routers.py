from typing import List, Dict, Optional
import datetime
from fastapi import APIRouter, UploadFile, File
from starlette import status

from schemas import CargoItem
from services import add_rate_from_request, parse_json_file, get_actual_price

router = APIRouter()


@router.post("/rate", status_code=status.HTTP_201_CREATED)
async def load_rate(
    data: Dict[datetime.date, List[CargoItem]],
):
    await add_rate_from_request(data)


@router.post("/rate/file", status_code=status.HTTP_201_CREATED)
async def load_rate_from_file(
    file: UploadFile = File(),
):
    await parse_json_file(file)


@router.get("/rate", status_code=status.HTTP_200_OK)
async def get_price(price: float, cargo_type: str, date: datetime.date):
    actual_price = await get_actual_price(price, cargo_type, date)
    return actual_price
