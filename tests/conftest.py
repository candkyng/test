import pytest
from selenium import webdriver

from data.home_data import HomeData

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser name (chrome, firefox or edge)")
    parser.addoption("--url", action="store", default=HomeData.PAGE_URL, help="provide test URL")


@pytest.fixture(scope="class")
def get_driver(request):
    global driver
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        assert False, f"Unsupported browser {browser}"

    driver.implicitly_wait(1)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()


@pytest.fixture(scope="class")
def get_url(request):
    request.cls.test_url = request.config.getoption("--url")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    This method is copied from the course https://www.udemy.com/course/learn-selenium-automation-in-easy-python-language/
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = f'<div><img src="{file_name}" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
