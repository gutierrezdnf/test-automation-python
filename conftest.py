"""
Conftest

The plugins defined in this file are located in the fixtures/ package
"""

pytest_plugins = [
    f'fixtures.{module}' for module in [
        'data',
        'hooks',
        'session',
    ]
]
