from marshmallow import Schema, ValidationError, fields, validates
from marshmallow_enum import EnumField
from apps import ma
from apps.ticket.models import (
    Tickets,
    TicketLines,
    TicketStatus,
    TicketCategories
)

class TicketSchema(ma.ModelSchema):
    class Meta:
        model = Tickets

class TicketListSchema(Schema):
    ticket = fields.Nested(TicketSchema, many=True)
    limit = fields.Int(allow_none=True)
    offset = fields.Int(allow_none=True)
    keywords = fields.Str(allow_none=True)
    total = fields.Int()

    class Meta:
        model = Tickets
