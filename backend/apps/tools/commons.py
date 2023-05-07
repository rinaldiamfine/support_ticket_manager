import datetime
import hashlib
import os
import random
import string
import traceback
from datetime import timedelta
from enum import Enum
from http import HTTPStatus
from logging import getLogger
from typing import Any, Tuple
from flask import current_app, request
from marshmallow import ValidationError
from sqlalchemy import asc, desc

error_logger = getLogger("error")

def descripted_exception_logger(e: Exception) -> None:
    """
    This method used to log an exception with description

    Arguments:
        e {Exception} -- [The raised exception]
    """
    tb_frames = traceback.extract_tb(e.__traceback__)
    message = list()
    pardir_name = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

    for tb in tb_frames:
        if tb.filename.startswith(pardir_name):  # pragma: no cover
            message.append(f"{e} in {tb.filename} line {tb.lineno}")
    error_logger.error(",".join(message))


def get_offset_limit(page: int, per_page: int) -> Tuple[int, int]:
    """
    This method used to convert page per_page to offset limit

    Arguments:
        page {int} -- [The page number]
        per_page {int} -- [Total data per page]

    Returns:
        offset {int} -- [Offset converted from page per_page]
        limit {int} -- [Limit converted from page per_page]
    """
    offset, limit = 0, 10
    if page is not None and per_page is not None:
        offset = (page - 1) * per_page if page > 0 else 0
        limit = per_page
    return offset, limit


def generate_uuid(user_id: int, created: str) -> str:
    token = hashlib.sha256(
        str(user_id).encode("utf-8") + created.encode("utf-8")
    ).hexdigest()

    return token


def camelcase(s):
    parts = iter(s.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


def request_get_json(request: request) -> dict:
    try:
        json_data = request.get_json()
        if not json_data:
            raise
        return json_data
    except Exception:
        raise Exception("JSON not valid")


def bad_request_message(message: str = "Bad request") -> dict:
    return {"code": 400, "message": message}


def created_message(message: str = "Successfully created", data: dict = {}) -> dict:
    return {
        "code": 201,
        "message": message,
        "data": data,
    }


def ok_message(message: str = "Ok", data: dict = {}) -> dict:
    return {
        "code": 200,
        "message": message,
        "data": data,
    }


def remove_field_from_dict(fields: dict, fields_to_pop: list) -> dict:
    """
    used to remove field from dictionary
    """
    for field in fields_to_pop:
        if fields.get(field) or isinstance(fields.get(field), bool):
            fields.pop(field)

    return fields


def compare_object(comparable: Any, value: Any) -> dict:
    try:
        if not comparable:
            raise Exception("comparable cannot be empty")

        if not value:
            raise Exception("value cannot be empty")

        return dict(comparable=comparable, value=value)
    except Exception:
        raise


def mapping_self(self: Any, fields: list, kwargs: dict) -> Any:
    """
    used to auto map self with fields as object and kwargs as value
    """
    for field in fields:
        setattr(self, field, kwargs.get(field))

    return self


def row_to_dict(row: Any) -> dict:
    """
    used to convert base_query result to dictionary
    """
    result = {}
    for data in row._fields:
        result[data] = getattr(row, data)

    return result


def data_exist_in_db(model: Any, filter: dict) -> bool:
    """
    used to check if there data provided with filter exist in the db,
    filter cannot be empty
    """

    # the returned row is not whole (only id) for performance
    # though only 1-2 ms difference compared to select *
    if (
        model.base_query().filter_by(**filter).with_entities(model.id).first()
        is not None
    ):
        return True

    return False


def data_exist_in_db_with_deleted(model: Any, filter: dict) -> bool:
    """
    used to check if there data provided with filter exist in the db,
    filter cannot be empty
    """

    # the returned row is not whole (only id) for performance
    # though only 1-2 ms difference compared to select *
    if model.query.filter_by(**filter).with_entities(model.id).first() is not None:
        return True

    return False


def merge_dict(dict1: dict, dict2: dict) -> dict:
    new_dict = dict()
    new_dict.update(dict1)
    new_dict.update(dict2)
    return new_dict


def convert_str_to_enum(value: Any, enum: Any) -> Any:
    """
    used to convert string to enum
    """
    if isinstance(value, str):
        return enum[value]
    elif isinstance(value, Enum):
        return value

    raise Exception("Invalid type : {}, value : {}".format(type(value), value))


def convert_enum_to_dict(enum: Any) -> dict:
    """
    used to convert enum to dict
    """
    if isinstance(enum, Enum):
        if enum.name and enum.value:
            return {"name": enum.name, "value": enum.value}

        raise Exception("Invalid enum : {}".format(enum))

    raise Exception("Invalid type : {}, value : {}".format(type(enum), enum))


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[
        1
    ].lower() in current_app.config.get("ALLOWED_EXTENSIONS")

def model_to_dict(model: Any, excluded: list = None) -> dict:
    """
    Convert model object to dictionary
    (ex: g.user to dictionary)
    filters used to filter some fields and
    ignore the field that is not in filters but
    exist in the model object
    """
    try:
        result = {}
        columns = model.__table__.columns.keys()

        for column in columns:
            if excluded and column in excluded:
                pass
            else:
                result[column] = getattr(model, column)
                if isinstance(result.get(column), datetime.date):
                    result[column] = result[column].strftime("%Y-%m-%d")

        return result
    except Exception as e:
        raise Exception(e)


def model_to_list(model: Any, excluded: list = None) -> list:
    """
    Convert model object to list
    used for converting one to many objects to list
    """
    try:
        result = []
        for data in model:
            result.append(model_to_dict(data, excluded))
        return result
    except Exception as e:
        raise Exception(e)


def generate_random_alphanumeric_password(length=8) -> str:
    letters_and_digits = string.ascii_letters + string.digits
    result = "".join((random.choice(letters_and_digits) for i in range(length)))

    return result


def sorting_query(model: Any, query: Any, sorting_category: Any):
    if not sorting_category:
        sorting_category = SortingCategory.CREATED_DESC

    sorting_object = {
        SortingCategory.CREATED_ASC: asc(model.created_at),
        SortingCategory.CREATED_DESC: desc(model.created_at),
        SortingCategory.UPDATED_ASC: asc(model.updated_at),
        SortingCategory.UPDATED_DESC: desc(model.updated_at),
    }.get(sorting_category)

    query = query.order_by(sorting_object)

    return query


def sorting_submission_duration_query(model: Any, query: Any, sorting_category: Any):
    if not sorting_category:
        sorting_category = SortingSubmissionDuration.DESC

    sorting_object = {
        SortingSubmissionDuration.ASC: asc(model.deactivation_request_timestamp),
        SortingSubmissionDuration.DESC: desc(model.deactivation_request_timestamp),
    }.get(sorting_category)

    query = query.order_by(sorting_object)

    return query
