import pytest
from selenium.webdriver.ie.webdriver import WebDriver

from helpers.fixtures import get_driver


def pytest_addoption(parser):
    """Command line parameters to be used during the Tests"""
    parser.addoption(
        '--browser',
        help='Browser used to run the Tests: chrome | firefox | edge',
        choices=('chrome', 'firefox', 'edge'),
    )
    parser.addoption(
        '--gui',
        action='store_true',
        default=False,
        help='Browser option to enable the GUI during the Tests: False (default) | True',
    )


@pytest.fixture(scope='session')
def browser(request) -> str:
    """Fixture to specify the Browser during the Tests"""
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def gui(request) -> bool:
    """Fixture to specify if the Browser runs the Tests with GUI"""
    return request.config.getoption('--gui')


@pytest.fixture(scope='function')
def driver(browser: str, gui: bool) -> WebDriver:
    """Fixture to create the driver with the specified Browser and GUI param"""
    _driver = get_driver(browser, gui)
    yield _driver
    _driver.close()
