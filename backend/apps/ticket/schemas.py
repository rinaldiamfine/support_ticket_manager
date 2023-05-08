from marshmallow import Schema, ValidationError, fields, validates
from marshmallow_enum import EnumField
from apps import ma
from apps.ticket.models import (
    Tickets,
    TicketLines,
    TicketStatus,
    TicketCategories
)

class UnlimitedApprovalSchema(ma.ModelSchema):
    class Meta:
        model = Tickets