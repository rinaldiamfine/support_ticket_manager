from flask_restful import Api, Resource, reqparse
from flask import Blueprint
from apps import app
from flask_apispec import MethodResource, marshal_with, use_kwargs
from apps.ticket.helpers import (
    TicketHelpers
)
from apps.ticket.schemas import (
    TicketSchema,
    TicketListSchema
)
from flask import Response, request
from marshmallow import fields
import http.client
import json
import traceback
import requests

api = Api(app)

class TicketApi(MethodResource):

    @use_kwargs({
        "user_id": fields.Int(),
        "name": fields.Str(),
        "description": fields.Str(),
        "status_id": fields.Int(),
        "category_id": fields.Int(),
    })
    @marshal_with(TicketSchema)
    def post(self, **kwargs):
        try:
            param = dict()
            param['api'] = "/api/v1/tickets"
            param['method'] = "POST"
            result = TicketHelpers(**param).create(kwargs)
            return result
        
        except Exception as e:
            return Response(
                json.dumps(str(e)),
                status=http.client.INTERNAL_SERVER_ERROR,
                mimetype='application/json'
            )

    @use_kwargs({
        "user_id": fields.Int(),
        "offset": fields.Str(),
        "limit": fields.Str(),
        "keywords": fields.Str(),
    }, locations=['query'])
    @marshal_with(TicketListSchema)
    def get(self, **kwargs):
        try:
            param = dict()
            param['api'] = "/api/v1/tickets"
            param['method'] = "GET"
            result = TicketHelpers(**param).get(kwargs)
            return result

        except Exception as e:
            return Response(
                json.dumps(str(e)),
                status=http.client.INTERNAL_SERVER_ERROR,
                mimetype='application/json'
            )
