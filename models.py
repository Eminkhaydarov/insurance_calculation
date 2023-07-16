from datetime import datetime

from tortoise.models import Model
from tortoise import fields


class Rate(Model):
    id = fields.IntField(pk=True)
    cargo_type = fields.CharField(max_length=255)
    date = fields.DateField()
    rate = fields.DecimalField(max_digits=6, decimal_places=5)
    created_at = fields.DatetimeField(default=datetime.utcnow)
