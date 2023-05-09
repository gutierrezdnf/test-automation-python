from datetime import datetime

import pytest
from faker import Faker

_faker = Faker(['en_US'])


@pytest.fixture(scope='module')
def first_name() -> str:
    """Returns a random First Name"""
    return _faker.first_name()


@pytest.fixture(scope='module')
def last_name() -> str:
    """Returns a random Last Name"""
    return _faker.last_name()


@pytest.fixture(scope='module')
def email() -> str:
    """Returns a random Email"""
    return _faker.email()


@pytest.fixture(scope='module')
def phone_number() -> int:
    """Returns a random Phone Number"""
    return _faker.phone_number()


@pytest.fixture(scope='module')
def address() -> str:
    """Returns a random Address"""
    return _faker.address()


@pytest.fixture(scope='module')
def description() -> str:
    """Returns a random Description"""
    return _faker.text()


@pytest.fixture(scope='module')
def url() -> str:
    """Returns a random Url"""
    return _faker.url()


@pytest.fixture(scope='module')
def country() -> str:
    """Returns a random Country"""
    return _faker.country()


@pytest.fixture(scope='module')
def current_date() -> datetime:
    """Returns the Current Date"""
    return datetime.now()
