from datetime import datetime

import pytest  # type: ignore

from {{ cookiecutter.project_slug }}.validation import Validator


@pytest.mark.unit
@pytest.mark.parametrize('payload, expected', (
    ('True', True),
    ('true', True),
    ('1', True),
    ('yes', True),
    (True, True),
    ('0', False),
    ('no', False),
    ('false', False),
    (False, False),
))
def test_validator_coerce_boolean(payload, expected):
    schema = {'enabled': {'type': 'boolean', 'coerce': 'bool'}}

    validator = Validator(schema)
    document = validator.validate_payload({'enabled': payload})

    assert isinstance(document['enabled'], bool)
    assert document['enabled'] == expected


@pytest.mark.unit
def test_validator_coerce_datetime():
    schema = {'created_on': {'type': 'datetime', 'coerce': 'datetime'}}

    validator = Validator(schema)
    document = validator.validate_payload({'created_on': '2017-12-01T23:23:23'})

    assert isinstance(document['created_on'], datetime)


@pytest.mark.unit
@pytest.mark.parametrize('payload', ({}, {'foo': 'bar'}))
def test_validator_utcnow_default_setter(payload):
    validator = Validator({'created_on': {
        'type': 'datetime',
        'coerce': 'datetime',
        'default_setter': 'utcnow',
    }})
    document = validator.validate_payload(payload, update=True)

    assert 'created_on' in document
    assert isinstance(document['created_on'], datetime)
