from flask_restful import Api, Resource, reqparse
from flask import Blueprint
from apps import app
from flask_apispec import MethodResource, marshal_with, use_kwargs
from apps.ticket.helpers import (
    TicketHelpers
)
from flask import Response, request
import http.client
import json
import traceback
import requests

api = Api(app)

class TicketApi(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('user_id', type=int)
        super(TicketApi, self).__init__()

    def get(self):
        try:
            filter_options = request.args.to_dict()
            param = dict()

            if filter_options.get('offset'):
                param['offset'] = filter_options.get('offset')

            if filter_options.get('limit'):
                param['limit'] = filter_options.get('limit')

            if filter_options.get('keywords'):
                param['keywords'] = filter_options.get('keywords')

            param['api'] = "/api/v1/tickets"
            param['method'] = "GET"
            status, result = TicketHelpers(**param).get(
                 {}
            )

            if not status:
                return Response(
                    json.dumps(result),
                    status=http.client.BAD_REQUEST,
                    mimetype='application/json'
                )

            return Response(
                json.dumps(result),
                status=http.client.OK,
                mimetype='application/json'
            )

        except Exception as e:
            return Response(
                json.dumps(str(e)),
                status=http.client.INTERNAL_SERVER_ERROR,
                mimetype='application/json'
            )
