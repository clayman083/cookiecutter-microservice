from datetime import datetime
from typing import Dict

import cerberus


class ValidationError(Exception):
    def __init__(self, errors):
        self._errors = errors

    @property
    def errors(self):
        return self._errors


class Validator(cerberus.Validator):
    def _normalize_coerce_bool(self, value):
        if isinstance(value, bool):
            return value
        else:
            return str(value).lower() in ['true', '1', 'yes']

    def _normalize_coerce_datetime(self, value):
        if value:
            if isinstance(value, datetime):
                return value
            else:
                return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')

    def _normalize_default_setter_utcnow(self, document):
        return datetime.utcnow()

    def validate_payload(self, payload: Dict, update: bool=False) -> Dict:
        self.allow_unknown = update
        if not self.validate(payload, update=update):
            raise ValidationError(self.errors)

        return self.document
