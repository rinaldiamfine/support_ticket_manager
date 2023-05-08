from flask_restful import Api
from flask import Blueprint

from apps.ticket.api import (
    TicketApi
)

ticket_blueprint = Blueprint(
    'ticket', __name__, url_prefix='/api/v1/tickets'
)
ticket_api = Api(ticket_blueprint)
ticket_api.add_resource(TicketApi, '')
