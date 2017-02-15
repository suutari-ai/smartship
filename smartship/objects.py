# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from jsonschema import validate

from smartship.schemas import (
    ADDRESS_SCHEMA, CUSTOMS_DECLARATION_SCHEMA, EXTRAS_SCHEMA, PARCELS_SCHEMA, PARTNER_SCHEMA, SERVICE_SCHEMA
)


class JSONObject(object):
    schema = {}  # Defined in subclass

    def __init__(self, data=None):
        self._data = data
        if data:
            self.validate()

    def __setitem__(self, key, value):
        self._data[key] = value
        self.validate()

    def __getitem__(self, item):
        return self._data[item]

    def validate(self):
        validate(self._data, self.schema)

    @classmethod
    def from_shipment(cls, shipment):
        data = {}
        return cls(data).get_json()

    def get_json(self):
        return self._data


class Agent(JSONObject):
    schema = ADDRESS_SCHEMA


class CustomsDeclaration(JSONObject):
    schema = CUSTOMS_DECLARATION_SCHEMA


class CustomsPayer(JSONObject):
    schema = ADDRESS_SCHEMA


class Extras(JSONObject):
    schema = EXTRAS_SCHEMA


class FreightPayer(JSONObject):
    schema = ADDRESS_SCHEMA


class Parcels(JSONObject):
    schema = PARCELS_SCHEMA


class Delivery(JSONObject):
    schema = ADDRESS_SCHEMA


class Dispatch(JSONObject):
    schema = ADDRESS_SCHEMA


class Receiver(JSONObject):
    schema = ADDRESS_SCHEMA


class ReceiverPartners(JSONObject):
    schema = PARTNER_SCHEMA


class ReturnPart(JSONObject):
    schema = ADDRESS_SCHEMA


class Sender(JSONObject):
    schema = ADDRESS_SCHEMA


class SenderPartners(JSONObject):
    schema = PARTNER_SCHEMA


class Service(JSONObject):
    schema = SERVICE_SCHEMA


class TaxPayer(JSONObject):
    schema = ADDRESS_SCHEMA