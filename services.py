import json
import datetime
from json import JSONDecodeError

from fastapi import UploadFile, HTTPException
from starlette import status

from models import Rate


async def save_rate(cargo_type: str, date: datetime.date, rate: float) -> None:
    rate = Rate(cargo_type=cargo_type, date=date, rate=rate)
    await rate.save()


async def add_rate_from_request(data: dict) -> None:
    for date, rates in data.items():
        for rate_data in rates:
            await save_rate(rate_data.cargo_type, date, float(rate_data.rate))


async def parse_json_file(file: UploadFile):
    try:
        content = await file.read()
        content_text = content.decode("utf-8")
        data = json.loads(content_text)
    except JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file format")

    for date, rates in data.items():
        for rate_data in rates:
            await save_rate(rate_data["cargo_type"], date, float(rate_data["rate"]))


async def get_actual_price(price: float, cargo_type: str, date: datetime.date) -> float:
    actual_rate = (
        await Rate.filter(cargo_type=cargo_type, date__lte=date)
        .order_by("-date", "-created_at")
        .first()
    )
    if not actual_rate:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No rate found for this type of cargo",
        )
    return price * float(actual_rate.rate)
