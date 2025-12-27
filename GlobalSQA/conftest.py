import os
import time
import pytest
from datetime import datetime
from selenium import webdriver

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run tests (chrome or firefox)"
    )

@pytest.fixture
def browser_setup(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Browser '{browser}' is not supported")

    driver.get("https://www.globalsqa.com/demo-site")
    driver.maximize_window()
    driver.implicitly_wait(4)
    request.cls.driver = driver
    yield
    driver.quit()

def pytest_configure(config):
    # Create reports folder if not exists
    os.makedirs("reports", exist_ok=True)

    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Set report file path dynamically
    report_file = f"reports/report_{timestamp}.html"
    config.option.htmlpath = report_file

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Takes and embeds screenshot in HTML report whenever test fails.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # --- Create screenshots directory if missing ---
            screenshots_dir = "screenshots"
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)

            # ✅ assign file_name first
            test_name = report.nodeid.replace("::", "_").replace("tests/", "")
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

            # --- Full filename ---
            file_name = f"{test_name}_{timestamp}.png"
            file_path = os.path.abspath(os.path.join(screenshots_dir, file_name))

            # ✅ call screenshot function on next line
            _capture_screenshot(file_path)
            if file_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_path
                extra.append(pytest_html.extras.html(html))
        report.extras = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
