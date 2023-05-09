import os

import pytest

SCREENSHOTS = False


def pytest_addoption(parser):
    """Command line parameters to be used during the Tests"""
    parser.addoption(
        '--screenshots',
        action='store_true',
        default=False,
        help='Report option to enable screenshots for failed Tests: False (default) | True',
    )


@pytest.fixture(scope='session', autouse=True)
def screenshots(request):
    """Fixture to specify if the Report includes screenshots"""
    global SCREENSHOTS
    SCREENSHOTS = request.config.getoption('--browser')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """Hook to add screenshots on failure in the html report"""
    outcome = yield
    report = outcome.get_result()
    pytest_html = item.config.pluginmanager.getplugin('html')
    extra = getattr(report, 'extra', [])
    if SCREENSHOTS and report.failed and 'driver' in item.funcargs:
        driver = item.funcargs['driver']
        path, file = item.nodeid.split('/')[-1].split('::')
        path = f'{os.getcwd()}/screenshots/{path.split(".")[0]}'
        if not os.path.exists(path):
            os.mkdir(path)
        file = f'{path}/{file}.png'
        driver.save_screenshot(file)
        extra.append(pytest_html.extras.png(file))
    report.extra = extra
