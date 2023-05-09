from selenium.webdriver import (
    Chrome, ChromeOptions, Firefox, FirefoxOptions, Edge, EdgeOptions,
)
from selenium.webdriver.ie.webdriver import WebDriver

_drivers = {
    'chrome': {
        'driver': Chrome,
        'options': ChromeOptions,
        'arguments': ['headless', '-incognito', '--disable-logging'],
    },
    'firefox': {
        'driver': Firefox,
        'options': FirefoxOptions,
        'arguments': ['-headless', '-private']
    },
    'edge': {
        'driver': Edge,
        'options': EdgeOptions,
        'arguments': ['headless', '-inprivate']
    },
}


def get_driver(browser: str, gui: bool) -> WebDriver:
    """Initializes the Driver for the selected browser"""
    _options = _drivers[browser]['options']()
    for _option in _drivers[browser]['arguments']:
        if 'headless' not in _option or not gui:
            _options.add_argument(_option)
    _driver = _drivers[browser]['driver'](options=_options)
    _driver.set_window_size(1024, 768)
    _driver.implicitly_wait(5)
    return _driver
